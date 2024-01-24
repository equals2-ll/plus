        response.ParseFromString(response_proto)
        self._detail = response.success.manga_detail
        self._chapters = list()

    def get_latest_chapter_detail(self) -> List[Chapter]:
        if len(self._detail.chapters[-1].last_chapter_list) > 0:
            self._chapter_list = self._detail.chapters[-1].last_chapter_list
        else:
            self._chapter_list = self._detail.chapters[-1].first_chapter_list

        # Check double chapter
        try:
            newest_chapter_release_date = datetime.fromtimestamp(
                self._chapter_list[-1].start_timestamp
            )
            for chapter in self._chapter_list:
                second_newest_chapter_release_date = datetime.fromtimestamp(
                    chapter.start_timestamp
                )

                time_difference = (
                    newest_chapter_release_date - second_newest_chapter_release_date
                ).total_seconds()

                if time_difference < 600:
                    self._process_proto_class_to_model_class(chapter)

        except IndexError:
            info("Only one chapter exist, can't check double chapter")

        return self._chapters

    def _process_proto_class_to_model_class(self, chapter):
        if chapter.chapter_number == "ex":
            chapter_number = 0  # Remember to convert back to Extra Chapter while creating reddit title
        elif chapter.chapter_number.lower() == "one-shot":
            chapter_number = 0.1
        else:
            try:
                chapter_number = float(
                    chapter.chapter_number.lstrip("#").replace("-", ".")
                )
            except ValueError:
                chapter_number = 1

        self._chapters.append(
            Chapter(
                chapter_id=chapter.chapter_id,
                chapter_name=chapter.chapter_name,
                chapter_number=chapter_number,
                manga_id=self._detail.manga.manga_id,
            )
        )


class MangaplusUpdated:
    def __init__(self, response_proto):
        response = response_pb.Response()
        response.ParseFromString(response_proto)
        self._updated = response.success.updated
        self._updated_manga_ids = list()

    def get_updated_manga(self, manga_re_edtion_ids) -> List:
        """return new found manga ids"""
        for manga in self._updated.updated_manga_detail:
            if (
                manga.updated_manga.language == 0
                and int(manga.upload_timestamp)
                > datetime.timestamp(datetime.now() - timedelta(minutes=5))
                and manga.updated_manga.manga_id not in manga_re_edtion_ids
            ):
                manga_id = manga.updated_manga.manga_id
                manga_name = manga.updated_manga.manga_name
                info(f"New manga found: {manga_id}   {manga_name}")
                self._updated_manga_ids.append(manga_id)

        return self._updated_manga_ids


class MangaplusService:
    def __init__(self):
        self._base_api_url = "https://jumpg-webapi.tokyo-cdn.com"
        self._proto_blob = b""

    def request_from_api(self, manga_id="", updated=False):
        while True:
            try:
                if manga_id:
                    response = requests.get(
                        self._base_api_url + "/api/title_detailV3",
                        params={"lang": "eng", "title_id": manga_id},
                        stream=True,
                    )
                elif updated:
                    response = requests.get(
                        self._base_api_url + "/api/title_list/updated",
                        params={"lang": "eng"},
                        stream=True,
                    )

                break
            except:
                error("Request API Error")

                time.sleep(3)

        if response.status_code == 200:
            for chunk in response.iter_content(chunk_size=1024):
                self._proto_blob += chunk
            return True
        else:
            return None

    def get_manga_detail(self):
        return MangaplusManga(self._proto_blob).get_manga_title_detail()

    def get_chapter_detail(self):
        return MangaplusChapter(self._proto_blob).get_latest_chapter_detail()

    def get_update_new_manga(self, manga_re_edtion_ids):
        return MangaplusUpdated(self._proto_blob).get_updated_manga(manga_re_edtion_ids)
