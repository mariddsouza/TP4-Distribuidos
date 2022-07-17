# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proposta.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eproposta.proto\"|\n\x08Proposta\x12\x18\n\x10idMovelRequerido\x18\x02 \x01(\x03\x12\x17\n\x0fidMovelProposto\x18\x03 \x01(\x03\x12\x1e\n\x16\x63pfUsuarioRequisitante\x18\x04 \x01(\x03\x12\x1d\n\x15\x63pfUsuarioRequisitado\x18\x05 \x01(\x03\"\xba\x01\n\tProposta2\x12\x12\n\nidProposta\x18\x01 \x01(\x03\x12\x1b\n\x0busuarioAlvo\x18\x02 \x01(\x0b\x32\x06.User2\x12#\n\x13usuarioRequisitante\x18\x03 \x01(\x0b\x32\x06.User2\x12\"\n\rmovelProposto\x18\x04 \x01(\x0b\x32\x0b.Furniture2\x12#\n\x0emovelRequerido\x18\x05 \x01(\x0b\x32\x0b.Furniture2\x12\x0e\n\x06status\x18\x06 \x01(\x03\"K\n\nFurniture2\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04nome\x18\x02 \x01(\t\x12\x10\n\x08tempoUso\x18\x03 \x01(\x03\x12\x11\n\tdescricao\x18\x04 \x01(\t\"1\n\x05User2\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\r\n\x05senha\x18\x02 \x01(\t\x12\x0b\n\x03\x63pf\x18\x03 \x01(\x03\"\'\n\x15RespostaFazerProposta\x12\x0e\n\x06status\x18\x01 \x01(\x05\"(\n\x19\x42uscarPropostasRealizadas\x12\x0b\n\x03\x63pf\x18\x01 \x01(\x03\"B\n!RespostaBuscarPropostasRealizadas\x12\x1d\n\tpropostas\x18\x01 \x03(\x0b\x32\n.Proposta2\"\'\n\x18\x42uscarPropostasRecebidas\x12\x0b\n\x03\x63pf\x18\x01 \x01(\x03\"A\n RespostaBuscarPropostasRecebidas\x12\x1d\n\tpropostas\x18\x01 \x03(\x0b\x32\n.Proposta2\"5\n\x0f\x41\x63\x65itarProposta\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x16\n\x0e\x63pfUsuarioAlvo\x18\x02 \x01(\x03\" \n\x0eStatusResposta\x12\x0e\n\x06status\x18\x01 \x01(\x03\"5\n\x0fRecusarProposta\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x16\n\x0e\x63pfUsuarioAlvo\x18\x02 \x01(\x03\x32\xeb\x02\n\x08proposta\x12\x34\n\rfazerProposta\x12\t.Proposta\x1a\x16.RespostaFazerProposta\"\x00\x12]\n\x19\x62uscarPropostasRealizadas\x12\x1a.BuscarPropostasRealizadas\x1a\".RespostaBuscarPropostasRealizadas\"\x00\x12Z\n\x18\x62uscarPropostasRecebidas\x12\x19.BuscarPropostasRecebidas\x1a!.RespostaBuscarPropostasRecebidas\"\x00\x12\x36\n\x0f\x61\x63\x65itarProposta\x12\x10.AceitarProposta\x1a\x0f.StatusResposta\"\x00\x12\x36\n\x0frecusarProposta\x12\x10.RecusarProposta\x1a\x0f.StatusResposta\"\x00\x62\x06proto3')



_PROPOSTA = DESCRIPTOR.message_types_by_name['Proposta']
_PROPOSTA2 = DESCRIPTOR.message_types_by_name['Proposta2']
_FURNITURE2 = DESCRIPTOR.message_types_by_name['Furniture2']
_USER2 = DESCRIPTOR.message_types_by_name['User2']
_RESPOSTAFAZERPROPOSTA = DESCRIPTOR.message_types_by_name['RespostaFazerProposta']
_BUSCARPROPOSTASREALIZADAS = DESCRIPTOR.message_types_by_name['BuscarPropostasRealizadas']
_RESPOSTABUSCARPROPOSTASREALIZADAS = DESCRIPTOR.message_types_by_name['RespostaBuscarPropostasRealizadas']
_BUSCARPROPOSTASRECEBIDAS = DESCRIPTOR.message_types_by_name['BuscarPropostasRecebidas']
_RESPOSTABUSCARPROPOSTASRECEBIDAS = DESCRIPTOR.message_types_by_name['RespostaBuscarPropostasRecebidas']
_ACEITARPROPOSTA = DESCRIPTOR.message_types_by_name['AceitarProposta']
_STATUSRESPOSTA = DESCRIPTOR.message_types_by_name['StatusResposta']
_RECUSARPROPOSTA = DESCRIPTOR.message_types_by_name['RecusarProposta']
Proposta = _reflection.GeneratedProtocolMessageType('Proposta', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSTA,
  '__module__' : 'proposta_pb2'
  # @@protoc_insertion_point(class_scope:Proposta)
  })
_sym_db.RegisterMessage(Proposta)

Proposta2 = _reflection.GeneratedProtocolMessageType('Proposta2', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSTA2,
  '__module__' : 'proposta_pb2'
  # @@protoc_insertion_point(class_scope:Proposta2)
  })
_sym_db.RegisterMessage(Proposta2)

Furniture2 = _reflection.GeneratedProtocolMessageType('Furniture2', (_message.Message,), {
  'DESCRIPTOR' : _FURNITURE2,
  '__module__' : 'proposta_pb2'
  # @@protoc_insertion_point(class_scope:Furniture2)
  })
_sym_db.RegisterMessage(Furniture2)

User2 = _reflection.GeneratedProtocolMessageType('User2', (_message.Message,), {
  'DESCRIPTOR' : _USER2,
  '__module__' : 'proposta_pb2'
  # @@protoc_insertion_point(class_scope:User2)
  })
_sym_db.RegisterMessage(User2)

RespostaFazerProposta = _reflection.GeneratedProtocolMessageType('RespostaFazerProposta', (_message.Message,), {
  'DESCRIPTOR' : _RESPOSTAFAZERPROPOSTA,
  '__module__' : 'proposta_pb2'
  # @@protoc_insertion_point(class_scope:RespostaFazerProposta)
  })
_sym_db.RegisterMessage(RespostaFazerProposta)

BuscarPropostasRealizadas = _reflection.GeneratedProtocolMessageType('BuscarPropostasRealizadas', (_message.Message,), {
  'DESCRIPTOR' : _BUSCARPROPOSTASREALIZADAS,
  '__module__' : 'proposta_pb2'
  # @@protoc_insertion_point(class_scope:BuscarPropostasRealizadas)
  })
_sym_db.RegisterMessage(BuscarPropostasRealizadas)

RespostaBuscarPropostasRealizadas = _reflection.GeneratedProtocolMessageType('RespostaBuscarPropostasRealizadas', (_message.Message,), {
  'DESCRIPTOR' : _RESPOSTABUSCARPROPOSTASREALIZADAS,
  '__module__' : 'proposta_pb2'
  # @@protoc_insertion_point(class_scope:RespostaBuscarPropostasRealizadas)
  })
_sym_db.RegisterMessage(RespostaBuscarPropostasRealizadas)

BuscarPropostasRecebidas = _reflection.GeneratedProtocolMessageType('BuscarPropostasRecebidas', (_message.Message,), {
  'DESCRIPTOR' : _BUSCARPROPOSTASRECEBIDAS,
  '__module__' : 'proposta_pb2'
  # @@protoc_insertion_point(class_scope:BuscarPropostasRecebidas)
  })
_sym_db.RegisterMessage(BuscarPropostasRecebidas)

RespostaBuscarPropostasRecebidas = _reflection.GeneratedProtocolMessageType('RespostaBuscarPropostasRecebidas', (_message.Message,), {
  'DESCRIPTOR' : _RESPOSTABUSCARPROPOSTASRECEBIDAS,
  '__module__' : 'proposta_pb2'
  # @@protoc_insertion_point(class_scope:RespostaBuscarPropostasRecebidas)
  })
_sym_db.RegisterMessage(RespostaBuscarPropostasRecebidas)

AceitarProposta = _reflection.GeneratedProtocolMessageType('AceitarProposta', (_message.Message,), {
  'DESCRIPTOR' : _ACEITARPROPOSTA,
  '__module__' : 'proposta_pb2'
  # @@protoc_insertion_point(class_scope:AceitarProposta)
  })
_sym_db.RegisterMessage(AceitarProposta)

StatusResposta = _reflection.GeneratedProtocolMessageType('StatusResposta', (_message.Message,), {
  'DESCRIPTOR' : _STATUSRESPOSTA,
  '__module__' : 'proposta_pb2'
  # @@protoc_insertion_point(class_scope:StatusResposta)
  })
_sym_db.RegisterMessage(StatusResposta)

RecusarProposta = _reflection.GeneratedProtocolMessageType('RecusarProposta', (_message.Message,), {
  'DESCRIPTOR' : _RECUSARPROPOSTA,
  '__module__' : 'proposta_pb2'
  # @@protoc_insertion_point(class_scope:RecusarProposta)
  })
_sym_db.RegisterMessage(RecusarProposta)

_PROPOSTA = DESCRIPTOR.services_by_name['proposta']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROPOSTA._serialized_start=18
  _PROPOSTA._serialized_end=142
  _PROPOSTA2._serialized_start=145
  _PROPOSTA2._serialized_end=331
  _FURNITURE2._serialized_start=333
  _FURNITURE2._serialized_end=408
  _USER2._serialized_start=410
  _USER2._serialized_end=459
  _RESPOSTAFAZERPROPOSTA._serialized_start=461
  _RESPOSTAFAZERPROPOSTA._serialized_end=500
  _BUSCARPROPOSTASREALIZADAS._serialized_start=502
  _BUSCARPROPOSTASREALIZADAS._serialized_end=542
  _RESPOSTABUSCARPROPOSTASREALIZADAS._serialized_start=544
  _RESPOSTABUSCARPROPOSTASREALIZADAS._serialized_end=610
  _BUSCARPROPOSTASRECEBIDAS._serialized_start=612
  _BUSCARPROPOSTASRECEBIDAS._serialized_end=651
  _RESPOSTABUSCARPROPOSTASRECEBIDAS._serialized_start=653
  _RESPOSTABUSCARPROPOSTASRECEBIDAS._serialized_end=718
  _ACEITARPROPOSTA._serialized_start=720
  _ACEITARPROPOSTA._serialized_end=773
  _STATUSRESPOSTA._serialized_start=775
  _STATUSRESPOSTA._serialized_end=807
  _RECUSARPROPOSTA._serialized_start=809
  _RECUSARPROPOSTA._serialized_end=862
  _PROPOSTA._serialized_start=865
  _PROPOSTA._serialized_end=1228
# @@protoc_insertion_point(module_scope)
