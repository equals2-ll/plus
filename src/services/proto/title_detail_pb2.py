import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='title_detail.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12title_detail.proto\"H\n\x08Response\x12\x1f\n\x07success\x18\x01 \x01(\x0b\x32\x0e.SuccessResult\x12\x1b\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x0c.ErrorResult\"\x93\x01\n\x0b\x45rrorResult\x12#\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x13.ErrorResult.Action\x12\x11\n\tdebugInfo\x18\x04 \x01(\t\"L\n\x06\x41\x63tion\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x10\n\x0cUNAUTHORIZED\x10\x01\x12\x0f\n\x0bMAINTENANCE\x10\x02\x12\x12\n\x0eGEOIP_BLOCKING\x10\x03\":\n\rSuccessResult\x12)\n\x0ftitleDetailView\x18\x08 \x01(\x0b\x32\x10.TitleDetailView\"\xba\x02\n\x0fTitleDetailView\x12\x15\n\x05title\x18\x01 \x01(\x0b\x32\x06.Title\x12\x15\n\rtitleImageUrl\x18\x02 \x01(\t\x12\x10\n\x08overview\x18\x03 \x01(\t\x12\x1a\n\x12\x62\x61\x63kgroundImageUrl\x18\x04 \x01(\t\x12\x15\n\rnextTimestamp\x18\x05 \x01(\r\x12\x14\n\x0cupdateTiming\x18\x06 \x01(\r\x12 \n\x18viewingPeriodDescription\x18\x07 \x01(\t\x12\x19\n\x11nonAppearanceInfo\x18\x08 \x01(\t\x12\"\n\x10\x66irstChapterList\x18\t \x03(\x0b\x32\x08.Chapter\x12!\n\x0flastChapterList\x18\n \x03(\x0b\x32\x08.Chapter\x12\x1a\n\x12\x63haptersDescending\x18\x11 \x01(\x08\"\xc7\x01\n\x05Title\x12\x0f\n\x07titleId\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x18\n\x10portraitImageUrl\x18\x04 \x01(\t\x12\x19\n\x11landscapeImageUrl\x18\x05 \x01(\t\x12\x11\n\tviewCount\x18\x06 \x01(\r\x12!\n\x08language\x18\x07 \x01(\x0e\x32\x0f.Title.Language\"$\n\x08Language\x12\x0b\n\x07\x45NGLISH\x10\x00\x12\x0b\n\x07SPANISH\x10\x01\"\xc0\x01\n\x07\x43hapter\x12\x0f\n\x07titleId\x18\x01 \x01(\r\x12\x11\n\tchapterId\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08subTitle\x18\x04 \x01(\t\x12\x14\n\x0cthumbnailUrl\x18\x05 \x01(\t\x12\x16\n\x0estartTimeStamp\x18\x06 \x01(\r\x12\x14\n\x0c\x65ndTimeStamp\x18\x07 \x01(\r\x12\x15\n\ralreadyViewed\x18\x08 \x01(\x08\x12\x16\n\x0eisVerticalOnly\x18\t \x01(\x08\x62\x06proto3')
)



_ERRORRESULT_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='ErrorResult.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNAUTHORIZED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAINTENANCE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEOIP_BLOCKING', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=168,
  serialized_end=244,
)
_sym_db.RegisterEnumDescriptor(_ERRORRESULT_ACTION)

_TITLE_LANGUAGE = _descriptor.EnumDescriptor(
  name='Language',
  full_name='Title.Language',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENGLISH', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPANISH', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=787,
  serialized_end=823,
)
_sym_db.RegisterEnumDescriptor(_TITLE_LANGUAGE)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='Response.success', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='Response.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=94,
)


_ERRORRESULT = _descriptor.Descriptor(
  name='ErrorResult',
  full_name='ErrorResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='ErrorResult.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='debugInfo', full_name='ErrorResult.debugInfo', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ERRORRESULT_ACTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=244,
)


_SUCCESSRESULT = _descriptor.Descriptor(
  name='SuccessResult',
  full_name='SuccessResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='titleDetailView', full_name='SuccessResult.titleDetailView', index=0,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=304,
)


_TITLEDETAILVIEW = _descriptor.Descriptor(
  name='TitleDetailView',
  full_name='TitleDetailView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='TitleDetailView.title', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='titleImageUrl', full_name='TitleDetailView.titleImageUrl', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overview', full_name='TitleDetailView.overview', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backgroundImageUrl', full_name='TitleDetailView.backgroundImageUrl', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nextTimestamp', full_name='TitleDetailView.nextTimestamp', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateTiming', full_name='TitleDetailView.updateTiming', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='viewingPeriodDescription', full_name='TitleDetailView.viewingPeriodDescription', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonAppearanceInfo', full_name='TitleDetailView.nonAppearanceInfo', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='firstChapterList', full_name='TitleDetailView.firstChapterList', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastChapterList', full_name='TitleDetailView.lastChapterList', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chaptersDescending', full_name='TitleDetailView.chaptersDescending', index=10,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=621,
)


_TITLE = _descriptor.Descriptor(
  name='Title',
  full_name='Title',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='titleId', full_name='Title.titleId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Title.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='Title.author', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portraitImageUrl', full_name='Title.portraitImageUrl', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landscapeImageUrl', full_name='Title.landscapeImageUrl', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='viewCount', full_name='Title.viewCount', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='Title.language', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TITLE_LANGUAGE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=624,
  serialized_end=823,
)


_CHAPTER = _descriptor.Descriptor(
  name='Chapter',
  full_name='Chapter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='titleId', full_name='Chapter.titleId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chapterId', full_name='Chapter.chapterId', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Chapter.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subTitle', full_name='Chapter.subTitle', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thumbnailUrl', full_name='Chapter.thumbnailUrl', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTimeStamp', full_name='Chapter.startTimeStamp', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTimeStamp', full_name='Chapter.endTimeStamp', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alreadyViewed', full_name='Chapter.alreadyViewed', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isVerticalOnly', full_name='Chapter.isVerticalOnly', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=826,
  serialized_end=1018,
)

_RESPONSE.fields_by_name['success'].message_type = _SUCCESSRESULT
_RESPONSE.fields_by_name['error'].message_type = _ERRORRESULT
_ERRORRESULT.fields_by_name['action'].enum_type = _ERRORRESULT_ACTION
_ERRORRESULT_ACTION.containing_type = _ERRORRESULT
_SUCCESSRESULT.fields_by_name['titleDetailView'].message_type = _TITLEDETAILVIEW
_TITLEDETAILVIEW.fields_by_name['title'].message_type = _TITLE
_TITLEDETAILVIEW.fields_by_name['firstChapterList'].message_type = _CHAPTER
_TITLEDETAILVIEW.fields_by_name['lastChapterList'].message_type = _CHAPTER
_TITLE.fields_by_name['language'].enum_type = _TITLE_LANGUAGE
_TITLE_LANGUAGE.containing_type = _TITLE
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['ErrorResult'] = _ERRORRESULT
DESCRIPTOR.message_types_by_name['SuccessResult'] = _SUCCESSRESULT
DESCRIPTOR.message_types_by_name['TitleDetailView'] = _TITLEDETAILVIEW
DESCRIPTOR.message_types_by_name['Title'] = _TITLE
DESCRIPTOR.message_types_by_name['Chapter'] = _CHAPTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'title_detail_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)

ErrorResult = _reflection.GeneratedProtocolMessageType('ErrorResult', (_message.Message,), dict(
  DESCRIPTOR = _ERRORRESULT,
  __module__ = 'title_detail_pb2'
  # @@protoc_insertion_point(class_scope:ErrorResult)
  ))
_sym_db.RegisterMessage(ErrorResult)

SuccessResult = _reflection.GeneratedProtocolMessageType('SuccessResult', (_message.Message,), dict(
  DESCRIPTOR = _SUCCESSRESULT,
  __module__ = 'title_detail_pb2'
  # @@protoc_insertion_point(class_scope:SuccessResult)
  ))
_sym_db.RegisterMessage(SuccessResult)

TitleDetailView = _reflection.GeneratedProtocolMessageType('TitleDetailView', (_message.Message,), dict(
  DESCRIPTOR = _TITLEDETAILVIEW,
  __module__ = 'title_detail_pb2'
  # @@protoc_insertion_point(class_scope:TitleDetailView)
  ))
_sym_db.RegisterMessage(TitleDetailView)

Title = _reflection.GeneratedProtocolMessageType('Title', (_message.Message,), dict(
  DESCRIPTOR = _TITLE,
  __module__ = 'title_detail_pb2'
  # @@protoc_insertion_point(class_scope:Title)
  ))
_sym_db.RegisterMessage(Title)

Chapter = _reflection.GeneratedProtocolMessageType('Chapter', (_message.Message,), dict(
  DESCRIPTOR = _CHAPTER,
  __module__ = 'title_detail_pb2'
  # @@protoc_insertion_point(class_scope:Chapter)
  ))
_sym_db.RegisterMessage(Chapter)

