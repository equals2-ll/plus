from datetime import datetime, timedelta
import enum
from dataclasses import dataclass, field
@dataclass(order=True)
class Manga:
    manga_id:int
    manga_name:str
    subreddit:str = field(default='-')
    next_update_time:int = field(default=datetime.now()+timedelta(days=7))
    is_completed:bool = field(default=False)
    is_nsfw:bool = field(default=False)

    def __str__(self) -> str:
        return f"""
        Manga ID:           {self.manga_id}
        Manga Name:         {self.manga_name}
        Subreddit:          {self.subreddit}
        Next Update Time:   {datetime.fromtimestamp(self.next_update_time).strftime("%y-%m-%d %H:%M")}
        Is Completed:       {self.is_completed}
        Is NSFW:            {self.is_nsfw}
        """
    
    

@dataclass()
class Chapter:
    chapter_id:int
    chapter_name:str
    chapter_number:int
    youpoll_id:str = field(default='')
    reddit_post_id:str = field(default='')
    reddit_comment_id:str = field(default='')
    manga_id:int = field(default=None)
    
