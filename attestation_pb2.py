# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: attestation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='attestation.proto',
  package='ethereum.eth.v1alpha1',
  syntax='proto3',
  serialized_options=b'\n\031org.ethereum.eth.v1alpha1B\020AttestationProtoP\001Z6github.com/prysmaticlabs/ethereumapis/eth/v1alpha1;eth\252\002\025Ethereum.Eth.v1alpha1\312\002\025Ethereum\\Eth\\v1alpha1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x61ttestation.proto\x12\x15\x65thereum.eth.v1alpha1\"p\n\x0b\x41ttestation\x12\x18\n\x10\x61ggregation_bits\x18\x01 \x01(\x0c\x12\x34\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32&.ethereum.eth.v1alpha1.AttestationData\x12\x11\n\tsignature\x18\x03 \x01(\x0c\"\x88\x01\n\x1c\x41ggregateAttestationAndProof\x12\x18\n\x10\x61ggregator_index\x18\x01 \x01(\x04\x12\x35\n\taggregate\x18\x03 \x01(\x0b\x32\".ethereum.eth.v1alpha1.Attestation\x12\x17\n\x0fselection_proof\x18\x02 \x01(\x0c\"}\n\"SignedAggregateAttestationAndProof\x12\x44\n\x07message\x18\x01 \x01(\x0b\x32\x33.ethereum.eth.v1alpha1.AggregateAttestationAndProof\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"\xb9\x01\n\x0f\x41ttestationData\x12\x0c\n\x04slot\x18\x01 \x01(\x04\x12\x17\n\x0f\x63ommittee_index\x18\x02 \x01(\x04\x12\x19\n\x11\x62\x65\x61\x63on_block_root\x18\x03 \x01(\x0c\x12\x31\n\x06source\x18\x04 \x01(\x0b\x32!.ethereum.eth.v1alpha1.Checkpoint\x12\x31\n\x06target\x18\x05 \x01(\x0b\x32!.ethereum.eth.v1alpha1.Checkpoint\")\n\nCheckpoint\x12\r\n\x05\x65poch\x18\x01 \x01(\x04\x12\x0c\n\x04root\x18\x02 \x01(\x0c\x42\x97\x01\n\x19org.ethereum.eth.v1alpha1B\x10\x41ttestationProtoP\x01Z6github.com/prysmaticlabs/ethereumapis/eth/v1alpha1;eth\xaa\x02\x15\x45thereum.Eth.v1alpha1\xca\x02\x15\x45thereum\\Eth\\v1alpha1b\x06proto3'
)




_ATTESTATION = _descriptor.Descriptor(
  name='Attestation',
  full_name='ethereum.eth.v1alpha1.Attestation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='aggregation_bits', full_name='ethereum.eth.v1alpha1.Attestation.aggregation_bits', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='ethereum.eth.v1alpha1.Attestation.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='ethereum.eth.v1alpha1.Attestation.signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=44,
  serialized_end=156,
)


_AGGREGATEATTESTATIONANDPROOF = _descriptor.Descriptor(
  name='AggregateAttestationAndProof',
  full_name='ethereum.eth.v1alpha1.AggregateAttestationAndProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='aggregator_index', full_name='ethereum.eth.v1alpha1.AggregateAttestationAndProof.aggregator_index', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aggregate', full_name='ethereum.eth.v1alpha1.AggregateAttestationAndProof.aggregate', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='selection_proof', full_name='ethereum.eth.v1alpha1.AggregateAttestationAndProof.selection_proof', index=2,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=159,
  serialized_end=295,
)


_SIGNEDAGGREGATEATTESTATIONANDPROOF = _descriptor.Descriptor(
  name='SignedAggregateAttestationAndProof',
  full_name='ethereum.eth.v1alpha1.SignedAggregateAttestationAndProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='ethereum.eth.v1alpha1.SignedAggregateAttestationAndProof.message', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='ethereum.eth.v1alpha1.SignedAggregateAttestationAndProof.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=297,
  serialized_end=422,
)


_ATTESTATIONDATA = _descriptor.Descriptor(
  name='AttestationData',
  full_name='ethereum.eth.v1alpha1.AttestationData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='slot', full_name='ethereum.eth.v1alpha1.AttestationData.slot', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='committee_index', full_name='ethereum.eth.v1alpha1.AttestationData.committee_index', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='beacon_block_root', full_name='ethereum.eth.v1alpha1.AttestationData.beacon_block_root', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='ethereum.eth.v1alpha1.AttestationData.source', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='ethereum.eth.v1alpha1.AttestationData.target', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=425,
  serialized_end=610,
)


_CHECKPOINT = _descriptor.Descriptor(
  name='Checkpoint',
  full_name='ethereum.eth.v1alpha1.Checkpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='epoch', full_name='ethereum.eth.v1alpha1.Checkpoint.epoch', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='root', full_name='ethereum.eth.v1alpha1.Checkpoint.root', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=612,
  serialized_end=653,
)

_ATTESTATION.fields_by_name['data'].message_type = _ATTESTATIONDATA
_AGGREGATEATTESTATIONANDPROOF.fields_by_name['aggregate'].message_type = _ATTESTATION
_SIGNEDAGGREGATEATTESTATIONANDPROOF.fields_by_name['message'].message_type = _AGGREGATEATTESTATIONANDPROOF
_ATTESTATIONDATA.fields_by_name['source'].message_type = _CHECKPOINT
_ATTESTATIONDATA.fields_by_name['target'].message_type = _CHECKPOINT
DESCRIPTOR.message_types_by_name['Attestation'] = _ATTESTATION
DESCRIPTOR.message_types_by_name['AggregateAttestationAndProof'] = _AGGREGATEATTESTATIONANDPROOF
DESCRIPTOR.message_types_by_name['SignedAggregateAttestationAndProof'] = _SIGNEDAGGREGATEATTESTATIONANDPROOF
DESCRIPTOR.message_types_by_name['AttestationData'] = _ATTESTATIONDATA
DESCRIPTOR.message_types_by_name['Checkpoint'] = _CHECKPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Attestation = _reflection.GeneratedProtocolMessageType('Attestation', (_message.Message,), {
  'DESCRIPTOR' : _ATTESTATION,
  '__module__' : 'attestation_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.Attestation)
  })
_sym_db.RegisterMessage(Attestation)

AggregateAttestationAndProof = _reflection.GeneratedProtocolMessageType('AggregateAttestationAndProof', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATEATTESTATIONANDPROOF,
  '__module__' : 'attestation_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.AggregateAttestationAndProof)
  })
_sym_db.RegisterMessage(AggregateAttestationAndProof)

SignedAggregateAttestationAndProof = _reflection.GeneratedProtocolMessageType('SignedAggregateAttestationAndProof', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDAGGREGATEATTESTATIONANDPROOF,
  '__module__' : 'attestation_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.SignedAggregateAttestationAndProof)
  })
_sym_db.RegisterMessage(SignedAggregateAttestationAndProof)

AttestationData = _reflection.GeneratedProtocolMessageType('AttestationData', (_message.Message,), {
  'DESCRIPTOR' : _ATTESTATIONDATA,
  '__module__' : 'attestation_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.AttestationData)
  })
_sym_db.RegisterMessage(AttestationData)

Checkpoint = _reflection.GeneratedProtocolMessageType('Checkpoint', (_message.Message,), {
  'DESCRIPTOR' : _CHECKPOINT,
  '__module__' : 'attestation_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.Checkpoint)
  })
_sym_db.RegisterMessage(Checkpoint)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
