# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x12test_service.proto\x12\x10test_grpc_server"\x1b\n\x0bTestMessage\x12\x0c\n\x04text\x18\x01 \x01(\t2X\n\x0bTestService\x12I\n\tTestServe\x12\x1d.test_grpc_server.TestMessage\x1a\x1d.test_grpc_server.TestMessageb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "test_service_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _TESTMESSAGE._serialized_start = 40
    _TESTMESSAGE._serialized_end = 67
    _TESTSERVICE._serialized_start = 69
    _TESTSERVICE._serialized_end = 157
# @@protoc_insertion_point(module_scope)