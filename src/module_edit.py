from logging import debug, info, warning, error
from datetime import datetime, timedelta
import sys
import os

from services import mangaplus
from data.models import Manga

from ruamel.yaml import YAML

'''
Add new mangas to database easily

Limitations:
Can't update manga in database. (Lazy to do that yet ==ll)
To update database, use "-m update update" instead
'''


def main(config, db, *args):
    if len(args) == 2 and args[1].lower() == 'dump':
        warning(
            "Dumping will overwrite manga file with database data, mainly used when transferring machines")
        _dump_to_yaml_file_from_db(db, args[0])

    elif len(args) ==2 and args[1].lower() == 'migrate':
        info(f"Migrating {args[0]} to database.sqlite")
        _migrate_chapters(db,args[0])

    elif len(args) == 1 or (len(args) == 2 and args[1].lower() == 'load'):
        if _edit_with_file(db, args[0]):
            info("Edit successful; saving")
            db.commit()
        else:
            error("Edit failed; reverting")
            db.rollback()
    else:
        warning("Not enough arguments, please input edit file name")


def _edit_with_file(db, edit_file):
    yaml = YAML()
    info(f"Parsing manga edit file: {edit_file}")
    edit_file_path = os.path.join("manga_config", edit_file)
    with open(edit_file_path) as fp:
        parsed = yaml.load(fp)
    manga_ids = [manga.manga_id for manga in db.get_mangas(all=True)]
    for manga_id in parsed:
        if manga_id not in manga_ids:
            info(
                f"Adding new manga '{parsed[manga_id]['manga_name']} to database")
            m = mangaplus.MangaplusService()
            resp = m.request_from_api(manga_id=manga_id)
            if resp:
                manga = m.get_manga_detail()
                manga.subreddit = parsed[manga_id]['subreddit']
                manga.is_completed = parsed[manga_id]['is_completed']
                manga.is_nsfw = parsed[manga_id]['is_nsfw']
                db.add_manga(manga.manga_id, manga.manga_name, manga.subreddit,
                             manga.next_update_time, manga.is_completed, manga.is_nsfw, commit=False)
            else:
                return False
    return True


def _dump_to_yaml_file_from_db(db, edit_file):
    yaml = YAML()
    info(f"Dump database Manga table to: {edit_file}")
    edit_file_path = os.path.join("manga_config", edit_file)
    try:
        with open(edit_file_path) as fp:
            data = yaml.load(fp)
    except Exception:
        warning(Exception)
        data = {}
    mangas = db.get_mangas(all=True)
    for manga in mangas:
        data[manga.manga_id] = {"manga_name": manga.manga_name, "subreddit": manga.subreddit, "is_nsfw": bool(
            manga.is_nsfw), "is_completed": bool(manga.is_completed)}

    with open(edit_file_path, 'w') as fp:
        yaml.dump(data, fp)

def _migrate_chapters(db,old_db_name):
    from data import database
    old_db=database.initialize_database(old_db_name)
    manga_ids=db.get_manga_ids()

    for manga_id in manga_ids:
        chapter_ids=db.get_chapter_ids(manga_id=manga_id) 
        old_chapter_ids=old_db.get_chapter_ids(manga_id=manga_id)

        different_chapter_ids=list(set(old_chapter_ids) - set(chapter_ids))

        for chapter_id in different_chapter_ids:
            chapter=old_db.get_chapter(chapter_id=chapter_id)

            info(chapter)
            
            db.add_chapter(chapter.chapter_id,chapter.chapter_name,chapter.chapter_number,chapter.youpoll_id,chapter.reddit_post_id,chapter.reddit_comment_id,chapter.manga_id)
            