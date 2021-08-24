from logging import debug, info, warning, error, exception
import re
from datetime import datetime, timedelta
from typing import Optional, List
import requests
import http.client

import services.proto.title_detail_pb2 as title_detail_pb
from data.models import Manga, Chapter



class MangaplusManga:
    def __init__(self, response_proto):
        response = title_detail_pb.Response()
        response.ParseFromString(response_proto)
        self._detail = response.success.manga_detail

    def get_manga_title_detail(self) -> Optional[Manga]:
        return Manga(manga_id=self._detail.manga.manga_id, manga_name=self._detail.manga.manga_name,
                     next_update_time=self._detail.next_timestamp, is_completed=bool(self._detail.non_appearance_info))


class MangaplusChapter(MangaplusManga):
    def __init__(self, response_proto):
        super().__init__(response_proto)
        self._chapters = list()

    def get_latest_chapter_detail(self) -> List[Chapter]:

        if len(self._detail.last_chapter_list) > 0:
            self._chapter_list = self._detail.last_chapter_list
        else:
            self._chapter_list = self._detail.first_chapter_list

        # Check double chapter
        try:
            newest_chapter_release_date = datetime.fromtimestamp(
                self._chapter_list[-1].start_timestamp)
            second_newest_chapter_release_date = datetime.fromtimestamp(
                self._chapter_list[-2].start_timestamp)

            time_difference = (
                newest_chapter_release_date-second_newest_chapter_release_date).total_seconds()

            if time_difference < 600:
                chapter = self._chapter_list[-2]
                self._process_proto_class_to_model_class(chapter)

        except IndexError:
            info("Only one chapter exist, can't check double chapter")

        chapter = self._chapter_list[-1]
        self._process_proto_class_to_model_class(chapter)

        return self._chapters

    def _process_proto_class_to_model_class(self, chapter):
        if chapter.chapter_number == "ex":
            chapter_number = 0  # Remember to convert back to Extra Chapter while creating reddit title
        else:
            chapter_number = float(chapter.chapter_number.lstrip('#'))

        self._chapters.append(Chapter(chapter_id=chapter.chapter_id,
                              chapter_name=chapter.chapter_name, chapter_number=chapter_number,manga_id=self._detail.manga.manga_id))


class MangaplusService():
    def __init__(self):
        self._base_api_url = "https://jumpg-webapi.tokyo-cdn.com"
        self._proto_blob = b""

    def request_from_api(self, manga_id='',updated=False):
        try:
            if manga_id:
                response= requests.get(self._base_api_url+"/api/title_detail",params={'lang':'eng','title_id':manga_id},stream=True)
            elif updated:
                response= requests.get(self._base_api_url+"/api/title_list/updated",params={'lang':'eng'},stream=True)
        except:
            error("Request API Error")

        if response.status_code == 200:
            for chunk in response.iter_content(chunk_size=1024):
                self._proto_blob+=chunk
            return True
        else:
            return None

    def get_manga_detail(self):

        return MangaplusManga(self._proto_blob).get_manga_title_detail()

    def get_chapter_detail(self):

        return MangaplusChapter(self._proto_blob).get_latest_chapter_detail()
