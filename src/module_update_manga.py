from logging import debug, info, warning, error
from datetime import date, datetime, timedelta

from services import mangaplus
from data.models import Manga, Chapter

from tabulate import tabulate


def main(config, db, *args, **kwargs):
    if len(args)==1:
        if args[0].lower()=='add':
            _add_new_manga(config,db)
        elif args[0].lower()=='update':
            _update_existing_manga(config,db)
        elif args[0].lower()=='view_manga':
            _view_manga_in_database(config,db)
        elif args[0].lower()=='view_chapter':
            _view_chapters_in_database(config,db)
    else:
        print(f"""
        Mangaplus Bot Database
        {'-'*20}
        1. Add new manga
        2. Update existing manga
        3. View manga in database
        4. View chapters in database
        5. Add new manga re-edition (ignore)
        6. View manga re-edition in database
        {'-'*20}
        """)
        while True:
            choice = int(input("Input (1-6): "))
            if choice in range(1, 7):
                break
            else:
                print("Invalid input")
        if choice == 1:
            _add_new_manga(config, db)
        elif choice == 2:
            _update_existing_manga(config, db)
        elif choice == 3:
            _view_manga_in_database(config, db)
        elif choice == 4:
            _view_chapters_in_database(config,db)
        elif choice == 5:
            _add_new_manga_re_edition(config,db)
        elif choice == 6:
            _view_manga_re_edition_in_database(config,db)
        

def _add_new_manga(config, db):
    while True:
        manual = input(
            "Manual input or auto load from Mangaplus (M/A): ").lower()

        manga_id = int(input("Manga ID: "))
        if manual == 'm':
            manga = _manual_input(
                manga_id)
        else:
            manga = _load_from_mangaplus(
                manga_id)

        manga.is_nsfw = bool(int(input("Is NSFW: ")))
        manga.subreddit = input("Subreddit name: ")

        print(manga)

        confirm = input("Add to database? (Y/N): ").lower()
        if confirm == 'y':
            db.add_manga(manga.manga_id,manga.manga_name,manga.subreddit,manga.next_update_time,manga.is_completed,manga.is_nsfw)
            # db.add_manga(manga_id, manga_name, subreddit,
            #              next_update_time, is_completed, is_nsfw)

        continued = input("Continue? (Y/N): ").lower()
        if continued == 'n':
            break


def _manual_input(manga_id):
    manga_name = input("Manga Name: ")
    next_update_time = int(input("Next Update Time (Epoch Timestamp): "))
    is_completed = bool(int(input("Is completed: ")))

    return Manga(manga_id=manga_id,manga_name=manga_name,next_update_time=next_update_time,is_completed=is_completed)


def _load_from_mangaplus(manga_id):
    m = mangaplus.MangaplusService()
    resp = m.request_from_api(manga_id=manga_id)
    if resp:
        return m.get_manga_detail()


def _update_existing_manga(config, db):
    manga_id = int(input("Manga ID: "))
    m = db.get_manga(manga_id=manga_id)
    print(m)
    print(f"""
    {'-'*20}
    Which data to update
    1. manga name       2. next update time     3. is completed     4. is nsfw      5. subreddit
    """)
    choice = int(input("input: "))
    if choice == 1:
        manga_name = input("Manga name: ")
        confirm = input("Confirm (Y/N): ").lower()
        if confirm == 'y':
            db.update_manga(manga_id=manga_id, manga_name=manga_name)
    elif choice == 2:
        next_udpate_time = int(input("Next update time: "))
        confirm = input("Confirm (Y/N): ").lower()
        if confirm == 'y':
            db.update_manga(manga_id=manga_id,
                            next_update_time=next_udpate_time)
    elif choice == 3:
        is_completed = bool(int(input("Is completed: ")))
        confirm = input("Confirm (Y/N): ").lower()
        if confirm == 'y':
            db.update_manga(manga_id=manga_id, is_completed=is_completed)
    elif choice == 4:
        is_nsfw = bool(int(input("Is nsfw: ")))
        confirm = input("Confirm (Y/N): ").lower()
        if confirm == 'y':
            db.update_manga(manga_id=manga_id, is_nsfw=is_nsfw)
    elif choice == 5:
        is_completed = input("Is completed: ")
        confirm = input("Confirm (Y/N): ").lower()
        if confirm == 'y':
            db.update_manga(manga_id=manga_id, is_completed=is_completed)


def _view_manga_in_database(config, db):
    hiatus=input("Hiatus (Y/N): ").lower()
    if hiatus == 'y':
        mangas = db.get_mangas(completed=True)
    else:
        mangas = db.get_mangas(completed=False)
    headers = ['Manga ID', 'Manga Name', 'Subreddit',
               'Next Update Time', 'Completed', 'NSFW']
    table = []
    for manga in mangas:
        table.append([manga.manga_id, manga.manga_name, manga.subreddit,
                     datetime.fromtimestamp(manga.next_update_time).strftime("%y-%m-%d %H:%M"), bool(manga.is_completed), bool(manga.is_nsfw)])
    print(tabulate(table, headers=headers))
    
    # delete manga from database not available, forgot to set up on delete cascade on Chapter table
    delete_manga=input("\nDelete manga from database? (Y/N): ").lower()
    if delete_manga == 'y':
        manga_id=int(input("Manga ID: "))
        db.delete_manga(manga_id)

def _view_chapters_in_database(config,db):
    manga_id= int(input("Manga ID (0 for all chapters): "))
    if manga_id==0:
        chapters=db.get_chapters()
    else:
        chapters=db.get_chapters(manga_id=manga_id)
    headers=["Chapter ID","Chapter Number","Youpoll ID","Reddit Post ID","Reddit Comment ID","Manga ID"]
    table=[]
    for chapter in chapters:
        table.append([chapter.chapter_id,chapter.chapter_number,chapter.youpoll_id,chapter.reddit_post_id,chapter.reddit_comment_id,chapter.manga_id])
    print(tabulate(table,headers=headers))
    delete_chapter=input("\nDelete chapter from database? (Y/N): ").lower()
    if delete_chapter == 'y':
        chapter_id=int(input("Chapter ID: "))
        db.delete_chapter(chapter_id)

def _add_new_manga_re_edition(config,db):
    while True:

        manga_id = int(input("Manga Re-edition ID: "))
        manga_name= input("Manga Re-edition name: ")

        print(f"{manga_id}  {manga_name}")

        confirm = input("Add to database? (Y/N): ").lower()
        if confirm == 'y':
            db.add_manga_re_edition(manga_id,manga_name)
            

        continued = input("Continue? (Y/N): ").lower()
        if continued == 'n':
            break

def _view_manga_re_edition_in_database(config,db):
    mangas=db.get_manga_re_edition()
    print(tabulate(mangas,headers=["Manga ID","Manga Name"]))
    delete_manga=input("\nDelete manga re-edtion from database? (Y/N): ").lower()
    if delete_manga == 'y':
        manga_id=int(input("Manga Re-edition ID: "))
        db.delete_manga_re_edtion(manga_id)