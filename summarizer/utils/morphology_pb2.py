# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: morphology.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="morphology.proto",
    package="zemberek.morphology",
    syntax="proto3",
    serialized_options=_b("\n\031zemberek.proto.morphologyP\001"),
    serialized_pb=_b(
        '\n\x10morphology.proto\x12\x13zemberek.morphology"$\n\x13WordAnalysisRequest\x12\r\n\x05input\x18\x01 \x01(\t"N\n\x13\x44ictionaryItemProto\x12\r\n\x05lemma\x18\x01 \x01(\t\x12\x12\n\nprimaryPos\x18\x02 \x01(\t\x12\x14\n\x0csecondaryPos\x18\x03 \x01(\t"\xe4\x01\n\x13SingleAnalysisProto\x12\x0b\n\x03pos\x18\x01 \x01(\t\x12@\n\x0e\x64ictionaryItem\x18\x02 \x01(\x0b\x32(.zemberek.morphology.DictionaryItemProto\x12\x10\n\x08\x61nalysis\x18\x03 \x01(\t\x12\x10\n\x08informal\x18\x04 \x01(\x08\x12\x0f\n\x07runtime\x18\x05 \x01(\x08\x12\x0e\n\x06lemmas\x18\x06 \x03(\t\x12\x39\n\tmorphemes\x18\x07 \x03(\x0b\x32&.zemberek.morphology.MorphemeDataProto"6\n\x11MorphemeDataProto\x12\x0f\n\x07surface\x18\x01 \x01(\t\x12\x10\n\x08morpheme\x18\x02 \x01(\t"^\n\x11WordAnalysisProto\x12\r\n\x05input\x18\x01 \x01(\t\x12:\n\x08\x61nalyses\x18\x02 \x03(\x0b\x32(.zemberek.morphology.SingleAnalysisProto"D\n\x17SentenceAnalysisRequest\x12\r\n\x05input\x18\x01 \x01(\t\x12\x1a\n\x12\x63ontainAllAnalyses\x18\x02 \x01(\x08"g\n\x15SentenceAnalysisProto\x12\r\n\x05input\x18\x01 \x01(\t\x12?\n\x07results\x18\x02 \x03(\x0b\x32..zemberek.morphology.SentenceWordAnalysisProto"\x97\x01\n\x19SentenceWordAnalysisProto\x12\r\n\x05token\x18\x01 \x01(\t\x12\x36\n\x04\x62\x65st\x18\x02 \x01(\x0b\x32(.zemberek.morphology.SingleAnalysisProto\x12\x33\n\x03\x61ll\x18\x03 \x01(\x0b\x32&.zemberek.morphology.WordAnalysisProto2\xe1\x01\n\x11MorphologyService\x12k\n\x0f\x41nalyzeSentence\x12,.zemberek.morphology.SentenceAnalysisRequest\x1a*.zemberek.morphology.SentenceAnalysisProto\x12_\n\x0b\x41nalyzeWord\x12(.zemberek.morphology.WordAnalysisRequest\x1a&.zemberek.morphology.WordAnalysisProtoB\x1d\n\x19zemberek.proto.morphologyP\x01\x62\x06proto3'
    ),
)


_WORDANALYSISREQUEST = _descriptor.Descriptor(
    name="WordAnalysisRequest",
    full_name="zemberek.morphology.WordAnalysisRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="input",
            full_name="zemberek.morphology.WordAnalysisRequest.input",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=41,
    serialized_end=77,
)


_DICTIONARYITEMPROTO = _descriptor.Descriptor(
    name="DictionaryItemProto",
    full_name="zemberek.morphology.DictionaryItemProto",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="lemma",
            full_name="zemberek.morphology.DictionaryItemProto.lemma",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="primaryPos",
            full_name="zemberek.morphology.DictionaryItemProto.primaryPos",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="secondaryPos",
            full_name="zemberek.morphology.DictionaryItemProto.secondaryPos",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=79,
    serialized_end=157,
)


_SINGLEANALYSISPROTO = _descriptor.Descriptor(
    name="SingleAnalysisProto",
    full_name="zemberek.morphology.SingleAnalysisProto",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="pos",
            full_name="zemberek.morphology.SingleAnalysisProto.pos",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dictionaryItem",
            full_name="zemberek.morphology.SingleAnalysisProto.dictionaryItem",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="analysis",
            full_name="zemberek.morphology.SingleAnalysisProto.analysis",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="informal",
            full_name="zemberek.morphology.SingleAnalysisProto.informal",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="runtime",
            full_name="zemberek.morphology.SingleAnalysisProto.runtime",
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="lemmas",
            full_name="zemberek.morphology.SingleAnalysisProto.lemmas",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="morphemes",
            full_name="zemberek.morphology.SingleAnalysisProto.morphemes",
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=160,
    serialized_end=388,
)


_MORPHEMEDATAPROTO = _descriptor.Descriptor(
    name="MorphemeDataProto",
    full_name="zemberek.morphology.MorphemeDataProto",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="surface",
            full_name="zemberek.morphology.MorphemeDataProto.surface",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="morpheme",
            full_name="zemberek.morphology.MorphemeDataProto.morpheme",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=390,
    serialized_end=444,
)


_WORDANALYSISPROTO = _descriptor.Descriptor(
    name="WordAnalysisProto",
    full_name="zemberek.morphology.WordAnalysisProto",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="input",
            full_name="zemberek.morphology.WordAnalysisProto.input",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="analyses",
            full_name="zemberek.morphology.WordAnalysisProto.analyses",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=446,
    serialized_end=540,
)


_SENTENCEANALYSISREQUEST = _descriptor.Descriptor(
    name="SentenceAnalysisRequest",
    full_name="zemberek.morphology.SentenceAnalysisRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="input",
            full_name="zemberek.morphology.SentenceAnalysisRequest.input",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="containAllAnalyses",
            full_name="zemberek.morphology.SentenceAnalysisRequest.containAllAnalyses",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=542,
    serialized_end=610,
)


_SENTENCEANALYSISPROTO = _descriptor.Descriptor(
    name="SentenceAnalysisProto",
    full_name="zemberek.morphology.SentenceAnalysisProto",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="input",
            full_name="zemberek.morphology.SentenceAnalysisProto.input",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="results",
            full_name="zemberek.morphology.SentenceAnalysisProto.results",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=612,
    serialized_end=715,
)


_SENTENCEWORDANALYSISPROTO = _descriptor.Descriptor(
    name="SentenceWordAnalysisProto",
    full_name="zemberek.morphology.SentenceWordAnalysisProto",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="token",
            full_name="zemberek.morphology.SentenceWordAnalysisProto.token",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="best",
            full_name="zemberek.morphology.SentenceWordAnalysisProto.best",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="all",
            full_name="zemberek.morphology.SentenceWordAnalysisProto.all",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=718,
    serialized_end=869,
)

_SINGLEANALYSISPROTO.fields_by_name[
    "dictionaryItem"
].message_type = _DICTIONARYITEMPROTO
_SINGLEANALYSISPROTO.fields_by_name["morphemes"].message_type = _MORPHEMEDATAPROTO
_WORDANALYSISPROTO.fields_by_name["analyses"].message_type = _SINGLEANALYSISPROTO
_SENTENCEANALYSISPROTO.fields_by_name[
    "results"
].message_type = _SENTENCEWORDANALYSISPROTO
_SENTENCEWORDANALYSISPROTO.fields_by_name["best"].message_type = _SINGLEANALYSISPROTO
_SENTENCEWORDANALYSISPROTO.fields_by_name["all"].message_type = _WORDANALYSISPROTO
DESCRIPTOR.message_types_by_name["WordAnalysisRequest"] = _WORDANALYSISREQUEST
DESCRIPTOR.message_types_by_name["DictionaryItemProto"] = _DICTIONARYITEMPROTO
DESCRIPTOR.message_types_by_name["SingleAnalysisProto"] = _SINGLEANALYSISPROTO
DESCRIPTOR.message_types_by_name["MorphemeDataProto"] = _MORPHEMEDATAPROTO
DESCRIPTOR.message_types_by_name["WordAnalysisProto"] = _WORDANALYSISPROTO
DESCRIPTOR.message_types_by_name["SentenceAnalysisRequest"] = _SENTENCEANALYSISREQUEST
DESCRIPTOR.message_types_by_name["SentenceAnalysisProto"] = _SENTENCEANALYSISPROTO
DESCRIPTOR.message_types_by_name[
    "SentenceWordAnalysisProto"
] = _SENTENCEWORDANALYSISPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WordAnalysisRequest = _reflection.GeneratedProtocolMessageType(
    "WordAnalysisRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_WORDANALYSISREQUEST,
        __module__="morphology_pb2"
        # @@protoc_insertion_point(class_scope:zemberek.morphology.WordAnalysisRequest)
    ),
)
_sym_db.RegisterMessage(WordAnalysisRequest)

DictionaryItemProto = _reflection.GeneratedProtocolMessageType(
    "DictionaryItemProto",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DICTIONARYITEMPROTO,
        __module__="morphology_pb2"
        # @@protoc_insertion_point(class_scope:zemberek.morphology.DictionaryItemProto)
    ),
)
_sym_db.RegisterMessage(DictionaryItemProto)

SingleAnalysisProto = _reflection.GeneratedProtocolMessageType(
    "SingleAnalysisProto",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SINGLEANALYSISPROTO,
        __module__="morphology_pb2"
        # @@protoc_insertion_point(class_scope:zemberek.morphology.SingleAnalysisProto)
    ),
)
_sym_db.RegisterMessage(SingleAnalysisProto)

MorphemeDataProto = _reflection.GeneratedProtocolMessageType(
    "MorphemeDataProto",
    (_message.Message,),
    dict(
        DESCRIPTOR=_MORPHEMEDATAPROTO,
        __module__="morphology_pb2"
        # @@protoc_insertion_point(class_scope:zemberek.morphology.MorphemeDataProto)
    ),
)
_sym_db.RegisterMessage(MorphemeDataProto)

WordAnalysisProto = _reflection.GeneratedProtocolMessageType(
    "WordAnalysisProto",
    (_message.Message,),
    dict(
        DESCRIPTOR=_WORDANALYSISPROTO,
        __module__="morphology_pb2"
        # @@protoc_insertion_point(class_scope:zemberek.morphology.WordAnalysisProto)
    ),
)
_sym_db.RegisterMessage(WordAnalysisProto)

SentenceAnalysisRequest = _reflection.GeneratedProtocolMessageType(
    "SentenceAnalysisRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SENTENCEANALYSISREQUEST,
        __module__="morphology_pb2"
        # @@protoc_insertion_point(class_scope:zemberek.morphology.SentenceAnalysisRequest)
    ),
)
_sym_db.RegisterMessage(SentenceAnalysisRequest)

SentenceAnalysisProto = _reflection.GeneratedProtocolMessageType(
    "SentenceAnalysisProto",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SENTENCEANALYSISPROTO,
        __module__="morphology_pb2"
        # @@protoc_insertion_point(class_scope:zemberek.morphology.SentenceAnalysisProto)
    ),
)
_sym_db.RegisterMessage(SentenceAnalysisProto)

SentenceWordAnalysisProto = _reflection.GeneratedProtocolMessageType(
    "SentenceWordAnalysisProto",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SENTENCEWORDANALYSISPROTO,
        __module__="morphology_pb2"
        # @@protoc_insertion_point(class_scope:zemberek.morphology.SentenceWordAnalysisProto)
    ),
)
_sym_db.RegisterMessage(SentenceWordAnalysisProto)


DESCRIPTOR._options = None

_MORPHOLOGYSERVICE = _descriptor.ServiceDescriptor(
    name="MorphologyService",
    full_name="zemberek.morphology.MorphologyService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=872,
    serialized_end=1097,
    methods=[
        _descriptor.MethodDescriptor(
            name="AnalyzeSentence",
            full_name="zemberek.morphology.MorphologyService.AnalyzeSentence",
            index=0,
            containing_service=None,
            input_type=_SENTENCEANALYSISREQUEST,
            output_type=_SENTENCEANALYSISPROTO,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="AnalyzeWord",
            full_name="zemberek.morphology.MorphologyService.AnalyzeWord",
            index=1,
            containing_service=None,
            input_type=_WORDANALYSISREQUEST,
            output_type=_WORDANALYSISPROTO,
            serialized_options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_MORPHOLOGYSERVICE)

DESCRIPTOR.services_by_name["MorphologyService"] = _MORPHOLOGYSERVICE

# @@protoc_insertion_point(module_scope)
