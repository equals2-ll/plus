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
        self._detail = response.success.titleDetailView

    def get_manga_title_detail(self) -> Optional[Manga]:
        return Manga(manga_id=self._detail.title.titleId, manga_name=self._detail.title.name,
                     next_update_time=self._detail.nextTimestamp, is_completed=bool(self._detail.nonAppearanceInfo))


class MangaplusChapter(MangaplusManga):
    def __init__(self, response_proto):
        super().__init__(response_proto)
        self._chapters = list()

    def get_latest_chapter_detail(self) -> List[Chapter]:

        if len(self._detail.lastChapterList) > 0:
            self._chapter_list = self._detail.lastChapterList
        else:
            self._chapter_list = self._detail.firstChapterList

        # Check double chapter
        try:
            newest_chapter_release_date = datetime.fromtimestamp(
                self._chapter_list[-1].startTimeStamp)
            second_newest_chapter_release_date = datetime.fromtimestamp(
                self._chapter_list[-2].startTimeStamp)

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
        if chapter.name == "ex":
            chapter_number = 0  # Remember to convert back to Extra Chapter while creating reddit title
        else:
            chapter_number = int(chapter.name.lstrip('#'))

        self._chapters.append(Chapter(chapter_id=chapter.chapterId,
                              chapter_name=chapter.subTitle, chapter_number=chapter_number,manga_id=self._detail.title.titleId))


class MangaplusService():
    def __init__(self):
        self._base_api_url = "jumpg-webapi.tokyo-cdn.com"
        self._proto_blob = None

    def request_from_api(self, manga_id):
        try:
            conn = http.client.HTTPSConnection(self._base_api_url)
            conn.request("GET", f"/api/title_detail?title_id={manga_id}")

            response = conn.getresponse()
        except:
            error("Request API Error")

        if response.code == 200:
            self._proto_blob = response.read()
            return True
        else:
            return None

    def get_manga_detail(self):

        return MangaplusManga(self._proto_blob).get_manga_title_detail()

    def get_chapter_detail(self):

        return MangaplusChapter(self._proto_blob).get_latest_chapter_detail()
