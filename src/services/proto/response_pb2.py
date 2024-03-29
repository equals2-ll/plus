# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eresponse.proto\"\xa7\x01\n\x05Manga\x12\x10\n\x08manga_id\x18\x01 \x01(\r\x12\x12\n\nmanga_name\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x1a\n\x12portrait_image_url\x18\x04 \x01(\t\x12\x1b\n\x13landscape_image_url\x18\x05 \x01(\t\x12\x12\n\nview_count\x18\x06 \x01(\r\x12\x1b\n\x08language\x18\x07 \x01(\x0e\x32\t.Language\"\xd6\x01\n\x07\x43hapter\x12\x10\n\x08manga_id\x18\x01 \x01(\r\x12\x12\n\nchapter_id\x18\x02 \x01(\r\x12\x16\n\x0e\x63hapter_number\x18\x03 \x01(\t\x12\x14\n\x0c\x63hapter_name\x18\x04 \x01(\t\x12\x15\n\rthumbnail_url\x18\x05 \x01(\t\x12\x17\n\x0fstart_timestamp\x18\x06 \x01(\r\x12\x15\n\rend_timestamp\x18\x07 \x01(\r\x12\x16\n\x0e\x61lready_viewed\x18\x08 \x01(\x08\x12\x18\n\x10is_vertical_only\x18\t \x01(\x08\"C\n\x06\x42\x61nner\x12\x13\n\x0bimageBanner\x18\x01 \x01(\t\x12\x11\n\x03sns\x18\x02 \x01(\x0b\x32\x04.Sns\x12\x11\n\tviewCount\x18\x03 \x01(\x05\" \n\x03Sns\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"\x9c\x05\n\x0bMangaDetail\x12\x15\n\x05manga\x18\x01 \x01(\x0b\x32\x06.Manga\x12\x17\n\x0fmanga_image_url\x18\x02 \x01(\t\x12\x10\n\x08overview\x18\x03 \x01(\t\x12\x1c\n\x14\x62\x61\x63kground_image_url\x18\x04 \x01(\t\x12\x16\n\x0enext_timestamp\x18\x05 \x01(\r\x12/\n\x0cupdateTiming\x18\x06 \x01(\x0e\x32\x19.MangaDetail.UpdateTiming\x12\"\n\x1aviewing_period_description\x18\x07 \x01(\t\x12\x1b\n\x13non_appearance_info\x18\x08 \x01(\t\x12-\n\x0b\x61llLanguage\x18\x1b \x03(\x0b\x32\x18.MangaDetail.AllLanguage\x12\'\n\x08\x63hapters\x18\x1c \x03(\x0b\x32\x15.MangaDetail.Chapters\x1a;\n\x0b\x41llLanguage\x12\x0f\n\x07titleId\x18\x01 \x01(\r\x12\x1b\n\x08language\x18\x02 \x01(\x0e\x32\t.Language\x1a\x84\x01\n\x08\x43hapters\x12\r\n\x05\x63ount\x18\x01 \x01(\r\x12$\n\x12\x66irst_chapter_list\x18\x02 \x03(\x0b\x32\x08.Chapter\x12\x1e\n\x0c\x63hapter_list\x18\x03 \x03(\x0b\x32\x08.Chapter\x12#\n\x11last_chapter_list\x18\x04 \x03(\x0b\x32\x08.Chapter\"\x86\x01\n\x0cUpdateTiming\x12\x11\n\rNOT_REGULARLY\x10\x00\x12\n\n\x06MONDAY\x10\x01\x12\x0b\n\x07TUESDAY\x10\x02\x12\r\n\tWEDNESDAY\x10\x03\x12\x0c\n\x08THURSDAY\x10\x04\x12\n\n\x06\x46RIDAY\x10\x05\x12\x0c\n\x08SATURDAY\x10\x06\x12\n\n\x06SUNDAY\x10\x07\x12\x07\n\x03\x44\x41Y\x10\x08\"\xae\x01\n\x0cUpdatedManga\x12\x10\n\x08manga_id\x18\x01 \x01(\r\x12\x12\n\nmanga_name\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x1a\n\x12portrait_image_url\x18\x04 \x01(\t\x12\x1b\n\x13landscape_image_url\x18\x05 \x01(\t\x12\x12\n\nview_count\x18\x06 \x01(\r\x12\x1b\n\x08language\x18\x07 \x01(\x0e\x32\t.Language\"T\n\x12UpdatedMangaDetail\x12$\n\rupdated_manga\x18\x01 \x01(\x0b\x32\r.UpdatedManga\x12\x18\n\x10upload_timestamp\x18\x02 \x01(\t\"<\n\x07Updated\x12\x31\n\x14updated_manga_detail\x18\x01 \x03(\x0b\x32\x13.UpdatedMangaDetail\"H\n\x08Response\x12\x1f\n\x07success\x18\x01 \x01(\x0b\x32\x0e.SuccessResult\x12\x1b\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x0c.ErrorResult\"\x93\x01\n\x0b\x45rrorResult\x12#\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x13.ErrorResult.Action\x12\x11\n\tdebugInfo\x18\x04 \x01(\t\"L\n\x06\x41\x63tion\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x10\n\x0cUNAUTHORIZED\x10\x01\x12\x0f\n\x0bMAINTENANCE\x10\x02\x12\x12\n\x0eGEOIP_BLOCKING\x10\x03\"N\n\rSuccessResult\x12\"\n\x0cmanga_detail\x18\x08 \x01(\x0b\x32\x0c.MangaDetail\x12\x19\n\x07updated\x18\x14 \x01(\x0b\x32\x08.Updated*g\n\x08Language\x12\x0b\n\x07\x45NGLISH\x10\x00\x12\x0b\n\x07SPANISH\x10\x01\x12\n\n\x06\x46RENCH\x10\x02\x12\x0e\n\nINDONESIAN\x10\x03\x12\x0e\n\nPORTUGUESE\x10\x04\x12\x0b\n\x07RUSSIAN\x10\x05\x12\x08\n\x04THAI\x10\x06\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'response_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LANGUAGE']._serialized_start=1808
  _globals['_LANGUAGE']._serialized_end=1911
  _globals['_MANGA']._serialized_start=19
  _globals['_MANGA']._serialized_end=186
  _globals['_CHAPTER']._serialized_start=189
  _globals['_CHAPTER']._serialized_end=403
  _globals['_BANNER']._serialized_start=405
  _globals['_BANNER']._serialized_end=472
  _globals['_SNS']._serialized_start=474
  _globals['_SNS']._serialized_end=506
  _globals['_MANGADETAIL']._serialized_start=509
  _globals['_MANGADETAIL']._serialized_end=1177
  _globals['_MANGADETAIL_ALLLANGUAGE']._serialized_start=846
  _globals['_MANGADETAIL_ALLLANGUAGE']._serialized_end=905
  _globals['_MANGADETAIL_CHAPTERS']._serialized_start=908
  _globals['_MANGADETAIL_CHAPTERS']._serialized_end=1040
  _globals['_MANGADETAIL_UPDATETIMING']._serialized_start=1043
  _globals['_MANGADETAIL_UPDATETIMING']._serialized_end=1177
  _globals['_UPDATEDMANGA']._serialized_start=1180
  _globals['_UPDATEDMANGA']._serialized_end=1354
  _globals['_UPDATEDMANGADETAIL']._serialized_start=1356
  _globals['_UPDATEDMANGADETAIL']._serialized_end=1440
  _globals['_UPDATED']._serialized_start=1442
  _globals['_UPDATED']._serialized_end=1502
  _globals['_RESPONSE']._serialized_start=1504
  _globals['_RESPONSE']._serialized_end=1576
  _globals['_ERRORRESULT']._serialized_start=1579
  _globals['_ERRORRESULT']._serialized_end=1726
  _globals['_ERRORRESULT_ACTION']._serialized_start=1650
  _globals['_ERRORRESULT_ACTION']._serialized_end=1726
  _globals['_SUCCESSRESULT']._serialized_start=1728
  _globals['_SUCCESSRESULT']._serialized_end=1806
# @@protoc_insertion_point(module_scope)
