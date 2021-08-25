from logging import debug, error, exception, info
import sqlite3
import re
from datetime import datetime, timedelta
from time import time
from functools import wraps
from unidecode import Cache, unidecode
from typing import Optional, List

from .models import Manga, Chapter



def initialize_database(database):
    try:
        db = sqlite3.connect(database)
        db.execute("PRAGMA foreign_keys=ON")
    except sqlite3.OperationalError:
        error(f"Failed to open database {database}")
        return None
    return PlusDatabase(db)


def db_error(f):
    @wraps(f)
    def protected(*args, **kwargs):
        try:
            f(*args, **kwargs)
            return True
        except:
            exception("Database exception thrown")
            return False
    return protected


def db_error_default(default_value):
    value = default_value

    def decorate(f):
        @wraps(f)
        def protected(*args, **kwargs):
            nonlocal value
            try:
                return f(*args, **kwargs)
            except:
                exception("Database exception thrown")
                return value
        return protected
    return decorate


class PlusDatabase:
    def __init__(self, db):
        self._db = db
        self.q = db.cursor()
        self._db.create_collation("alphanum", _collate_alphanum)

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        return getattr(self._db, attr)

    def setup_tables(self):
        self.q.execute("""CREATE TABLE IF NOT EXISTS Manga (
			manga_id			INTEGER NOT NULL PRIMARY KEY,
			manga_name			TEXT NOT NULL,
			subreddit			TEXT NOT NULL,
			next_update_time	INTEGER NOT NULL,
			is_completed		INTEGER NOT NULL DEFAULT 0,
			is_nsfw				INTEGER NOT NULL DEFAULT 0
		)""")
        self.q.execute("""CREATE TABLE IF NOT EXISTS Chapter (
            chapter_id          INTEGER NOT NULL PRIMARY KEY,
            chapter_name        TEXT NOT NULL,
            chapter_number      REAL NOT NULL,
            youpoll_id          INTEGER NOT NULL,
            reddit_post_id      TEXT NOT NULL,
            reddit_comment_id   TEXT NOT NULL,
            manga               INTEGER NOT NULL,
            FOREIGN KEY(manga)  REFERENCES Manga(manga_id) ON DELETE CASCADE
        )""")
        self.q.execute("""CREATE TABLE IF NOT EXISTS Manga_Re_edition (
            manga_id            INTEGER NOT NULL PRIMARY KEY,
            manga_name          TEXT NOT NULL
        )""")

    @db_error_default(None)
    def get_manga(self, manga_id=None) -> Optional[Manga]:
        if manga_id is not None:
            self.q.execute("""SELECT manga_id,manga_name,subreddit,next_update_time,is_completed,is_nsfw 
                FROM Manga WHERE manga_id = ?
            """, (manga_id,))
        else:
            error("manga id required to get manga")
            return None
        manga = self.q.fetchone()
        return Manga(*manga)

    @db_error_default(list())
    def get_mangas(self, completed=False, current_time=None,all=False) -> List[Manga]:
        mangas = list()

        if (current_time is not None):
            self.q.execute("""SELECT manga_id,manga_name,subreddit,next_update_time,is_completed,is_nsfw 
                FROM Manga WHERE next_update_time BETWEEN ? AND ? ORDER BY next_update_time ASC
            """, (datetime.timestamp(current_time-timedelta(minutes=5)),datetime.timestamp(current_time+timedelta(minutes=5))))
            for manga in self.q.fetchall():
                mangas.append(Manga(*manga))

        elif not completed and not all:
            self.q.execute("""SELECT manga_id,manga_name,subreddit,next_update_time,is_completed,is_nsfw 
                FROM Manga WHERE is_completed = 0 ORDER BY next_update_time ASC
            """)
            for manga in self.q.fetchall():
                mangas.append(Manga(*manga))
        elif all:
            self.q.execute("SELECT manga_id,manga_name,subreddit,next_update_time,is_completed,is_nsfw FROM Manga")
            for manga in self.q.fetchall():
                mangas.append(Manga(*manga))
        else:
            info("Getting completed/hiatus manga...")
            self.q.execute("""SELECT manga_id,manga_name,subreddit,next_update_time,is_completed,is_nsfw 
                FROM Manga WHERE is_completed = 1
            """)
            for manga in self.q.fetchall():
                mangas.append(Manga(*manga))

        return mangas
    
    @db_error_default(list())
    def get_manga_ids(self) -> List:
        self.q.execute("SELECT manga_id FROM Manga")
        manga_ids=[manga_id[0] for manga_id in self.q.fetchall()]
        return manga_ids
    
    @db_error_default(list())
    def get_manga_re_edition(self,ids_only=False) -> List:
        if ids_only:
            self.q.execute("SELECT manga_id FROM Manga_Re_edition")
            manga_ids=[manga_id[0] for manga_id in self.q.fetchall()]
            return manga_ids
        else:
            mangas=list()
            self.q.execute("SELECT * FROM Manga_Re_edition")
            for manga in self.q.fetchall():
                mangas.append(manga)
            return mangas

    @db_error_default(None)
    def get_chapter(self, chapter_id=None) -> Optional[Chapter]:
        if chapter_id is not None:
            self.q.execute("""SELECT chapter_id,chapter_name,chapter_number,youpoll_id,reddit_post_id,reddit_comment_id,manga
                FROM Chapter WHERE chapter_id = ?
            """, (chapter_id,))
        else:
            error("chapter id requried to get chapter")
            return None
        chapter = self.q.fetchone()

        return Chapter(*chapter)

    @db_error_default(list())
    def get_chapters(self, manga_id=None) -> List[Chapter]:
        chapters = list()
        
        if manga_id is not None:
            self.q.execute("SELECT * FROM Chapter WHERE manga = ?", (manga_id,))
        else:
            self.q.execute("SELECT * FROM Chapter")

        for chapter in self.q.fetchall():
            chapters.append(Chapter(*chapter))
        return chapters
    
    @db_error_default(list())
    def get_chapter_ids(self) -> List:
        self.q.execute("SELECT chapter_id FROM Chapter")
        chapter_ids=[chapter_id[0] for chapter_id in self.q.fetchall()]
        
        return chapter_ids

    @db_error
    def add_manga(self, manga_id, manga_name, subreddit, next_update_time, is_completed, is_nsfw, commit=True):
        info(f"Adding manga: {manga_name}")
        self.q.execute("INSERT OR IGNORE INTO Manga (manga_id,manga_name,subreddit,next_update_time,is_completed,is_nsfw) VALUES (?,?,?,?,?,?)",
                       (manga_id, manga_name, subreddit, next_update_time, is_completed, is_nsfw))
        if commit:
            self.commit()

    @db_error
    def add_manga_re_edition(self,manga_id,manga_name,commit=True):
        info(f"Adding re-edition manga: {manga_name}")
        self.q.execute("INSERT OR IGNORE INTO Manga_Re_edition (manga_id,manga_name) VALUES (?,?)",(manga_id,manga_name))

        if commit:
            self.commit()

    @db_error
    def add_chapter(self, chapter_id, chapter_name, chapter_number, youpoll_id, reddit_post_id, reddit_comment_id, manga, commit=True):
        info(f"Adding chapter: {chapter_id}")
        self.q.execute("INSERT OR IGNORE INTO Chapter (chapter_id,chapter_name,chapter_number,youpoll_id,reddit_post_id,reddit_comment_id,manga) VALUES (?,?,?,?,?,?,?)",
                       (chapter_id, chapter_name, chapter_number,  youpoll_id, reddit_post_id, reddit_comment_id, manga))
        if commit:
            self.commit()

    @db_error
    def update_manga(self, manga_id, manga_name=None, subreddit=None, next_update_time=None, is_completed=None, is_nsfw=None, commit=True):
        debug(f'Updating manga: {manga_id}')
        if manga_name is not None:
            self.q.execute(
                "UPDATE Manga SET manga_name = ? WHERE manga_id = ?", (manga_name, manga_id))
        if subreddit is not None:
            self.q.execute(
                "UPDATE Manga SET subreddit = ? WHERE manga_id = ?", (subreddit, manga_id))
        if next_update_time is not None:
            self.q.execute(
                "UPDATE Manga SET next_update_time = ? WHERE manga_id = ?", (next_update_time, manga_id))
        if is_completed is not None:
            self.q.execute(
                "UPDATE Manga SET is_completed = ? WHERE manga_id = ?", (is_completed, manga_id))
        if is_nsfw is not None:
            self.q.execute(
                "UPDATE Manga SET is_nsfw = ? WHERE manga_id = ?", (is_nsfw, manga_id))

        if commit:
            self.commit()
    
    @db_error
    def delete_manga(self,manga_id,commit=True):
        info(f"Delete manga {manga_id}")
        self.q.execute("DELETE FROM Manga WHERE manga_id = ?",(manga_id,))
        if commit:
            self.commit()

    @db_error
    def delete_manga_re_edition(self,manga_id,commit=True):
        info(f"Delete manga {manga_id}")
        self.q.execute("DELETE FROM Manga_Re_edition WHERE manga_id = ?",(manga_id,))
        if commit:
            self.commit()
    
    @db_error
    def delete_chapter(self,chapter_id,commit=True):
        info(f"Delete chapter {chapter_id}")
        self.q.execute("DELETE FROM Chapter WHERE chapter_id = ?",(chapter_id,))
        if commit:
            self.commit()



# collation
def _collate_alphanum(str1, str2):

    if str1 == str2:
        return 0
    elif str1 < str2:
        return -1
    else:
        return 1




