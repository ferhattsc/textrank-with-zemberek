# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: normalization.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="normalization.proto",
    package="zemberek.normalization",
    syntax="proto3",
    serialized_options=_b("\n\016zemberek.protoP\001"),
    serialized_pb=_b(
        '\n\x13normalization.proto\x12\x16zemberek.normalization"%\n\x14NormalizationRequest\x12\r\n\x05input\x18\x01 \x01(\t"@\n\x15NormalizationResponse\x12\x18\n\x10normalized_input\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t2\x80\x01\n\x14NormalizationService\x12h\n\tNormalize\x12,.zemberek.normalization.NormalizationRequest\x1a-.zemberek.normalization.NormalizationResponseB\x12\n\x0ezemberek.protoP\x01\x62\x06proto3'
    ),
)


_NORMALIZATIONREQUEST = _descriptor.Descriptor(
    name="NormalizationRequest",
    full_name="zemberek.normalization.NormalizationRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="input",
            full_name="zemberek.normalization.NormalizationRequest.input",
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
    serialized_start=47,
    serialized_end=84,
)


_NORMALIZATIONRESPONSE = _descriptor.Descriptor(
    name="NormalizationResponse",
    full_name="zemberek.normalization.NormalizationResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="normalized_input",
            full_name="zemberek.normalization.NormalizationResponse.normalized_input",
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
            name="error",
            full_name="zemberek.normalization.NormalizationResponse.error",
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
    serialized_start=86,
    serialized_end=150,
)

DESCRIPTOR.message_types_by_name["NormalizationRequest"] = _NORMALIZATIONREQUEST
DESCRIPTOR.message_types_by_name["NormalizationResponse"] = _NORMALIZATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NormalizationRequest = _reflection.GeneratedProtocolMessageType(
    "NormalizationRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_NORMALIZATIONREQUEST,
        __module__="normalization_pb2"
        # @@protoc_insertion_point(class_scope:zemberek.normalization.NormalizationRequest)
    ),
)
_sym_db.RegisterMessage(NormalizationRequest)

NormalizationResponse = _reflection.GeneratedProtocolMessageType(
    "NormalizationResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_NORMALIZATIONRESPONSE,
        __module__="normalization_pb2"
        # @@protoc_insertion_point(class_scope:zemberek.normalization.NormalizationResponse)
    ),
)
_sym_db.RegisterMessage(NormalizationResponse)


DESCRIPTOR._options = None

_NORMALIZATIONSERVICE = _descriptor.ServiceDescriptor(
    name="NormalizationService",
    full_name="zemberek.normalization.NormalizationService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=153,
    serialized_end=281,
    methods=[
        _descriptor.MethodDescriptor(
            name="Normalize",
            full_name="zemberek.normalization.NormalizationService.Normalize",
            index=0,
            containing_service=None,
            input_type=_NORMALIZATIONREQUEST,
            output_type=_NORMALIZATIONRESPONSE,
            serialized_options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_NORMALIZATIONSERVICE)

DESCRIPTOR.services_by_name["NormalizationService"] = _NORMALIZATIONSERVICE

# @@protoc_insertion_point(module_scope)