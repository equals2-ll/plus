from logging import debug, info, warning, error
from datetime import datetime, timedelta
import time


from services import mangaplus, youpoll
import reddit

import schedule

ignore_chapter_id = False # for debugging purposes, normally should always be False

reddit_post_title_format = ''
reddit_post_link_format = "https://mangaplus.shueisha.co.jp/viewer/{chapter_id}"
reddit_comment_body_format = ''
reddit_search_url_format = 'https://www.reddit.com/r/manga/search/?q=title%3A"{manga_name}" flair%3A"DISC"&restrict_sr=1&sort=new'


def main(config, db, **kwargs):
    global reddit_post_title_format,reddit_comment_body_format
    reddit_post_title_format=config.post_title
    reddit_comment_body_format=config.comment_body

    if kwargs['debug']:
        info("Debug mode not available")
        # debug_chapter = input("Update chapters to database? (Y/N): ").lower()
        # if debug_chapter == 'y':
        #     pass
    else:
        schedule.every().hour.at(":00").do(_find_mangaplus_chapters,config,db)
        schedule.every().day.at("23:30").do(_update_mangaplus_hiatus_manga,config,db)
        schedule.every().friday.at("22:00").do(_update_mangaplus_manga,config,db)
        # _find_mangaplus_chapters(config,db)
        # test(config,db)
        while True:
            schedule.run_pending()
            time.sleep(1)
            
# def test(config,db):
#     chapters = db.get_chapters()
#     chapter_ids = [chapter.chapter_id for chapter in chapters]
#     m = mangaplus.MangaplusService()

#     resp=m.request_from_api(manga_id=100171)
#     if resp:
#         Manga = m.get_manga_detail()
#         Chapters = m.get_chapter_detail()

#         if Chapters[0].chapter_id not in chapter_ids or ignore_chapter_id:
#             reddit_post_title,reddit_post_link=_process_into_reddit_post(config,db,Manga,Chapters)
#             info(f"Reddit Post Title: {reddit_post_title}")
#             info(f"Reddit Post Link: {reddit_post_link}")


def _find_mangaplus_chapters(config, db):
    reddit.init_reddit(config)
    time.sleep(1)
    mangas = db.get_mangas(current_time=datetime.now())

    chapters = db.get_chapters()
    chapter_ids = [chapter.chapter_id for chapter in chapters]

    m = mangaplus.MangaplusService()
    y = youpoll.YouPoll()

    for manga in mangas:
        resp=m.request_from_api(manga_id=manga.manga_id)
        if resp:
            Manga = m.get_manga_detail()
            Chapters = m.get_chapter_detail()

            if Chapters[0].chapter_id not in chapter_ids or ignore_chapter_id:
                reddit_post_title,reddit_post_link=_process_into_reddit_post(config,db,Manga,Chapters)
                info(f"Reddit Post Title: {reddit_post_title}")
                info(f"Reddit Post Link: {reddit_post_link}")
                submission=reddit.submit_link_post(reddit_post_title,reddit_post_link,config.subreddit,manga.is_nsfw)


                reddit_comment_body,youpoll_id=_process_into_reddit_comment(config,db,y,reddit_post_title,manga)
                comment=reddit.comment_post(submission,reddit_comment_body)

                for Chapter in Chapters:
                    Chapter.youpoll_id=youpoll_id
                    Chapter.reddit_post_id=submission.id
                    Chapter.reddit_comment_id=comment.id
                    db.add_chapter(Chapter.chapter_id,Chapter.chapter_name,Chapter.chapter_number,Chapter.youpoll_id,Chapter.reddit_post_id,Chapter.reddit_comment_id,manga.manga_id)

            db.update_manga(manga_id=manga.manga_id,next_update_time=Manga.next_update_time,is_completed=Manga.is_completed)



def _process_into_reddit_post(config,db,Manga,Chapters):
    chapter_number ="Extra Chapter" if Chapters[0].chapter_number == 0 else f"{Chapters[0].chapter_number:g}" #Revert back to Extra Chapter due to data class constraint

    reddit_post_title=reddit_post_title_format.format(manga_name=Manga.manga_name,chapter_number=chapter_number)
    reddit_post_link=reddit_post_link_format.format(chapter_id=Chapters[0].chapter_id)

    if len(Chapters)>1:
        reddit_post_title+=f" & {'Extra Chapter' if Chapters[1].chapter_number == 0 else f'{Chapters[1].chapter_number:g}' }"

    return reddit_post_title,reddit_post_link

def _process_into_reddit_comment(config,db,youpoll,reddit_post_title,manga):
    poll_url, poll_id = youpoll.create_poll(reddit_post_title[7:])
    if poll_id is not None:
        reddit_search_url = reddit_search_url_format.format(
            manga_name=manga.manga_name.replace('#',''))

        reddit_comment_body = reddit_comment_body_format.format(
            poll_url=poll_url, manga_title=reddit_post_title[7:], reddit_search_url=reddit_search_url, subreddit_name=manga.subreddit)

    return reddit_comment_body,poll_id


def _update_mangaplus_hiatus_manga(config,db):
    info(f"Hiatus manga info update")
    mangas=db.get_mangas(completed=True)
    _update_next_update_time(config,db,mangas)

def _update_mangaplus_manga(config,db):
    info(f"Weekly manga info update")
    mangas=db.get_mangas(completed=False)
    _update_next_update_time(config,db,mangas)

def _update_next_update_time(config,db,mangas):
    m = mangaplus.MangaplusService()
    for manga in mangas:
        resp=m.request_from_api(manga_id=manga.manga_id)
        if resp:
            Manga = m.get_manga_detail()
            if Manga.next_update_time != manga.next_update_time:
                info(f"Updating {Manga.manga_name}  Next Update Time:{datetime.fromtimestamp(Manga.next_update_time)}")
                db.update_manga(next_update_time=Manga.next_update_time)
        time.sleep(3)



