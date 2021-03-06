# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logical_port.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import telemetry_top_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='logical_port.proto',
  package='',
  serialized_pb='\n\x12logical_port.proto\x1a\x13telemetry_top.proto\"<\n\x0bLogicalPort\x12-\n\x0einterface_info\x18\x01 \x03(\x0b\x32\x15.LogicalInterfaceInfo\"\xd5\x03\n\x14LogicalInterfaceInfo\x12\x16\n\x07if_name\x18\x01 \x02(\tB\x05\x82@\x02\x08\x01\x12\x18\n\tinit_time\x18\x02 \x02(\x04\x42\x05\x82@\x02\x10\x01\x12\x1c\n\rsnmp_if_index\x18\x03 \x01(\rB\x05\x82@\x02\x08\x01\x12\x1d\n\x0eparent_ae_name\x18\x04 \x01(\tB\x05\x82@\x02\x08\x01\x12-\n\ringress_stats\x18\x05 \x01(\x0b\x32\x16.IngressInterfaceStats\x12+\n\x0c\x65gress_stats\x18\x06 \x01(\x0b\x32\x15.EgressInterfaceStats\x12#\n\x08op_state\x18\x07 \x01(\x0b\x32\x11.OperationalState\x12\x1e\n\x16\x61\x64ministractive_status\x18\x08 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\t\x12\x13\n\x0blast_change\x18\n \x01(\r\x12\x12\n\nhigh_speed\x18\x0b \x01(\r\x12\x37\n\x12ingress_queue_info\x18\x0c \x03(\x0b\x32\x1b.logicalInterfaceQueueStats\x12\x36\n\x11\x65gress_queue_info\x18\r \x03(\x0b\x32\x1b.logicalInterfaceQueueStats\"\xbf\x01\n\x15IngressInterfaceStats\x12\x19\n\nif_packets\x18\x01 \x02(\x04\x42\x05\x82@\x02\x18\x01\x12\x18\n\tif_octets\x18\x02 \x02(\x04\x42\x05\x82@\x02\x18\x01\x12\x1f\n\x10if_ucast_packets\x18\x03 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1f\n\x10if_mcast_packets\x18\x04 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12/\n\x0bif_fc_stats\x18\x05 \x03(\x0b\x32\x1a.ForwardingClassAccounting\"\x8d\x01\n\x14\x45gressInterfaceStats\x12\x19\n\nif_packets\x18\x01 \x02(\x04\x42\x05\x82@\x02\x18\x01\x12\x18\n\tif_octets\x18\x02 \x02(\x04\x42\x05\x82@\x02\x18\x01\x12\x1f\n\x10if_ucast_packets\x18\x03 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1f\n\x10if_mcast_packets\x18\x04 \x01(\x04\x42\x05\x82@\x02\x18\x01\".\n\x10OperationalState\x12\x1a\n\x12operational_status\x18\x01 \x01(\t\"\x84\x01\n\x19\x46orwardingClassAccounting\x12\x18\n\tif_family\x18\x01 \x01(\tB\x05\x82@\x02\x08\x01\x12\x18\n\tfc_number\x18\x02 \x01(\rB\x05\x82@\x02\x08\x01\x12\x19\n\nif_packets\x18\x03 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x18\n\tif_octets\x18\x04 \x01(\x04\x42\x05\x82@\x02\x18\x01\"\xb5\x03\n\x1alogicalInterfaceQueueStats\x12\x1b\n\x0cqueue_number\x18\x01 \x01(\rB\x05\x82@\x02\x08\x01\x12\x16\n\x07packets\x18\x02 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x14\n\x05\x62ytes\x18\x03 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12 \n\x11tail_drop_packets\x18\x04 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12&\n\x17rate_limit_drop_packets\x18\x05 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12$\n\x15rate_limit_drop_bytes\x18\x06 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1f\n\x10red_drop_packets\x18\x07 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1d\n\x0ered_drop_bytes\x18\x08 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\'\n\x18\x61verage_buffer_occupancy\x18\t \x01(\x04\x42\x05\x82@\x02 \x01\x12\'\n\x18\x63urrent_buffer_occupancy\x18\n \x01(\x04\x42\x05\x82@\x02 \x01\x12$\n\x15peak_buffer_occupancy\x18\x0b \x01(\x04\x42\x05\x82@\x02 \x01\x12$\n\x15\x61llocated_buffer_size\x18\x0c \x01(\x04\x42\x05\x82@\x02 \x01:F\n\x17jnprLogicalInterfaceExt\x12\x17.JuniperNetworksSensors\x18\x07 \x01(\x0b\x32\x0c.LogicalPort')


JNPRLOGICALINTERFACEEXT_FIELD_NUMBER = 7
jnprLogicalInterfaceExt = _descriptor.FieldDescriptor(
  name='jnprLogicalInterfaceExt', full_name='jnprLogicalInterfaceExt', index=0,
  number=7, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_LOGICALPORT = _descriptor.Descriptor(
  name='LogicalPort',
  full_name='LogicalPort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='interface_info', full_name='LogicalPort.interface_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=43,
  serialized_end=103,
)


_LOGICALINTERFACEINFO = _descriptor.Descriptor(
  name='LogicalInterfaceInfo',
  full_name='LogicalInterfaceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='if_name', full_name='LogicalInterfaceInfo.if_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')),
    _descriptor.FieldDescriptor(
      name='init_time', full_name='LogicalInterfaceInfo.init_time', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\020\001')),
    _descriptor.FieldDescriptor(
      name='snmp_if_index', full_name='LogicalInterfaceInfo.snmp_if_index', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')),
    _descriptor.FieldDescriptor(
      name='parent_ae_name', full_name='LogicalInterfaceInfo.parent_ae_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')),
    _descriptor.FieldDescriptor(
      name='ingress_stats', full_name='LogicalInterfaceInfo.ingress_stats', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egress_stats', full_name='LogicalInterfaceInfo.egress_stats', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='op_state', full_name='LogicalInterfaceInfo.op_state', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='administractive_status', full_name='LogicalInterfaceInfo.administractive_status', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='LogicalInterfaceInfo.description', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_change', full_name='LogicalInterfaceInfo.last_change', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high_speed', full_name='LogicalInterfaceInfo.high_speed', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ingress_queue_info', full_name='LogicalInterfaceInfo.ingress_queue_info', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egress_queue_info', full_name='LogicalInterfaceInfo.egress_queue_info', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=106,
  serialized_end=575,
)


_INGRESSINTERFACESTATS = _descriptor.Descriptor(
  name='IngressInterfaceStats',
  full_name='IngressInterfaceStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='if_packets', full_name='IngressInterfaceStats.if_packets', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='if_octets', full_name='IngressInterfaceStats.if_octets', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='if_ucast_packets', full_name='IngressInterfaceStats.if_ucast_packets', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='if_mcast_packets', full_name='IngressInterfaceStats.if_mcast_packets', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='if_fc_stats', full_name='IngressInterfaceStats.if_fc_stats', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=578,
  serialized_end=769,
)


_EGRESSINTERFACESTATS = _descriptor.Descriptor(
  name='EgressInterfaceStats',
  full_name='EgressInterfaceStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='if_packets', full_name='EgressInterfaceStats.if_packets', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='if_octets', full_name='EgressInterfaceStats.if_octets', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='if_ucast_packets', full_name='EgressInterfaceStats.if_ucast_packets', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='if_mcast_packets', full_name='EgressInterfaceStats.if_mcast_packets', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=772,
  serialized_end=913,
)


_OPERATIONALSTATE = _descriptor.Descriptor(
  name='OperationalState',
  full_name='OperationalState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operational_status', full_name='OperationalState.operational_status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=915,
  serialized_end=961,
)


_FORWARDINGCLASSACCOUNTING = _descriptor.Descriptor(
  name='ForwardingClassAccounting',
  full_name='ForwardingClassAccounting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='if_family', full_name='ForwardingClassAccounting.if_family', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')),
    _descriptor.FieldDescriptor(
      name='fc_number', full_name='ForwardingClassAccounting.fc_number', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')),
    _descriptor.FieldDescriptor(
      name='if_packets', full_name='ForwardingClassAccounting.if_packets', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='if_octets', full_name='ForwardingClassAccounting.if_octets', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=964,
  serialized_end=1096,
)


_LOGICALINTERFACEQUEUESTATS = _descriptor.Descriptor(
  name='logicalInterfaceQueueStats',
  full_name='logicalInterfaceQueueStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queue_number', full_name='logicalInterfaceQueueStats.queue_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')),
    _descriptor.FieldDescriptor(
      name='packets', full_name='logicalInterfaceQueueStats.packets', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='logicalInterfaceQueueStats.bytes', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='tail_drop_packets', full_name='logicalInterfaceQueueStats.tail_drop_packets', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='rate_limit_drop_packets', full_name='logicalInterfaceQueueStats.rate_limit_drop_packets', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='rate_limit_drop_bytes', full_name='logicalInterfaceQueueStats.rate_limit_drop_bytes', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='red_drop_packets', full_name='logicalInterfaceQueueStats.red_drop_packets', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='red_drop_bytes', full_name='logicalInterfaceQueueStats.red_drop_bytes', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='average_buffer_occupancy', full_name='logicalInterfaceQueueStats.average_buffer_occupancy', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002 \001')),
    _descriptor.FieldDescriptor(
      name='current_buffer_occupancy', full_name='logicalInterfaceQueueStats.current_buffer_occupancy', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002 \001')),
    _descriptor.FieldDescriptor(
      name='peak_buffer_occupancy', full_name='logicalInterfaceQueueStats.peak_buffer_occupancy', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002 \001')),
    _descriptor.FieldDescriptor(
      name='allocated_buffer_size', full_name='logicalInterfaceQueueStats.allocated_buffer_size', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002 \001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1099,
  serialized_end=1536,
)

_LOGICALPORT.fields_by_name['interface_info'].message_type = _LOGICALINTERFACEINFO
_LOGICALINTERFACEINFO.fields_by_name['ingress_stats'].message_type = _INGRESSINTERFACESTATS
_LOGICALINTERFACEINFO.fields_by_name['egress_stats'].message_type = _EGRESSINTERFACESTATS
_LOGICALINTERFACEINFO.fields_by_name['op_state'].message_type = _OPERATIONALSTATE
_LOGICALINTERFACEINFO.fields_by_name['ingress_queue_info'].message_type = _LOGICALINTERFACEQUEUESTATS
_LOGICALINTERFACEINFO.fields_by_name['egress_queue_info'].message_type = _LOGICALINTERFACEQUEUESTATS
_INGRESSINTERFACESTATS.fields_by_name['if_fc_stats'].message_type = _FORWARDINGCLASSACCOUNTING
DESCRIPTOR.message_types_by_name['LogicalPort'] = _LOGICALPORT
DESCRIPTOR.message_types_by_name['LogicalInterfaceInfo'] = _LOGICALINTERFACEINFO
DESCRIPTOR.message_types_by_name['IngressInterfaceStats'] = _INGRESSINTERFACESTATS
DESCRIPTOR.message_types_by_name['EgressInterfaceStats'] = _EGRESSINTERFACESTATS
DESCRIPTOR.message_types_by_name['OperationalState'] = _OPERATIONALSTATE
DESCRIPTOR.message_types_by_name['ForwardingClassAccounting'] = _FORWARDINGCLASSACCOUNTING
DESCRIPTOR.message_types_by_name['logicalInterfaceQueueStats'] = _LOGICALINTERFACEQUEUESTATS

class LogicalPort(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGICALPORT

  # @@protoc_insertion_point(class_scope:LogicalPort)

class LogicalInterfaceInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGICALINTERFACEINFO

  # @@protoc_insertion_point(class_scope:LogicalInterfaceInfo)

class IngressInterfaceStats(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INGRESSINTERFACESTATS

  # @@protoc_insertion_point(class_scope:IngressInterfaceStats)

class EgressInterfaceStats(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EGRESSINTERFACESTATS

  # @@protoc_insertion_point(class_scope:EgressInterfaceStats)

class OperationalState(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPERATIONALSTATE

  # @@protoc_insertion_point(class_scope:OperationalState)

class ForwardingClassAccounting(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FORWARDINGCLASSACCOUNTING

  # @@protoc_insertion_point(class_scope:ForwardingClassAccounting)

class logicalInterfaceQueueStats(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGICALINTERFACEQUEUESTATS

  # @@protoc_insertion_point(class_scope:logicalInterfaceQueueStats)

jnprLogicalInterfaceExt.message_type = _LOGICALPORT
telemetry_top_pb2.JuniperNetworksSensors.RegisterExtension(jnprLogicalInterfaceExt)

_LOGICALINTERFACEINFO.fields_by_name['if_name'].has_options = True
_LOGICALINTERFACEINFO.fields_by_name['if_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')
_LOGICALINTERFACEINFO.fields_by_name['init_time'].has_options = True
_LOGICALINTERFACEINFO.fields_by_name['init_time']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\020\001')
_LOGICALINTERFACEINFO.fields_by_name['snmp_if_index'].has_options = True
_LOGICALINTERFACEINFO.fields_by_name['snmp_if_index']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')
_LOGICALINTERFACEINFO.fields_by_name['parent_ae_name'].has_options = True
_LOGICALINTERFACEINFO.fields_by_name['parent_ae_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')
_INGRESSINTERFACESTATS.fields_by_name['if_packets'].has_options = True
_INGRESSINTERFACESTATS.fields_by_name['if_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_INGRESSINTERFACESTATS.fields_by_name['if_octets'].has_options = True
_INGRESSINTERFACESTATS.fields_by_name['if_octets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_INGRESSINTERFACESTATS.fields_by_name['if_ucast_packets'].has_options = True
_INGRESSINTERFACESTATS.fields_by_name['if_ucast_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_INGRESSINTERFACESTATS.fields_by_name['if_mcast_packets'].has_options = True
_INGRESSINTERFACESTATS.fields_by_name['if_mcast_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_EGRESSINTERFACESTATS.fields_by_name['if_packets'].has_options = True
_EGRESSINTERFACESTATS.fields_by_name['if_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_EGRESSINTERFACESTATS.fields_by_name['if_octets'].has_options = True
_EGRESSINTERFACESTATS.fields_by_name['if_octets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_EGRESSINTERFACESTATS.fields_by_name['if_ucast_packets'].has_options = True
_EGRESSINTERFACESTATS.fields_by_name['if_ucast_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_EGRESSINTERFACESTATS.fields_by_name['if_mcast_packets'].has_options = True
_EGRESSINTERFACESTATS.fields_by_name['if_mcast_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_FORWARDINGCLASSACCOUNTING.fields_by_name['if_family'].has_options = True
_FORWARDINGCLASSACCOUNTING.fields_by_name['if_family']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')
_FORWARDINGCLASSACCOUNTING.fields_by_name['fc_number'].has_options = True
_FORWARDINGCLASSACCOUNTING.fields_by_name['fc_number']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')
_FORWARDINGCLASSACCOUNTING.fields_by_name['if_packets'].has_options = True
_FORWARDINGCLASSACCOUNTING.fields_by_name['if_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_FORWARDINGCLASSACCOUNTING.fields_by_name['if_octets'].has_options = True
_FORWARDINGCLASSACCOUNTING.fields_by_name['if_octets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_LOGICALINTERFACEQUEUESTATS.fields_by_name['queue_number'].has_options = True
_LOGICALINTERFACEQUEUESTATS.fields_by_name['queue_number']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')
_LOGICALINTERFACEQUEUESTATS.fields_by_name['packets'].has_options = True
_LOGICALINTERFACEQUEUESTATS.fields_by_name['packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_LOGICALINTERFACEQUEUESTATS.fields_by_name['bytes'].has_options = True
_LOGICALINTERFACEQUEUESTATS.fields_by_name['bytes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_LOGICALINTERFACEQUEUESTATS.fields_by_name['tail_drop_packets'].has_options = True
_LOGICALINTERFACEQUEUESTATS.fields_by_name['tail_drop_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_LOGICALINTERFACEQUEUESTATS.fields_by_name['rate_limit_drop_packets'].has_options = True
_LOGICALINTERFACEQUEUESTATS.fields_by_name['rate_limit_drop_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_LOGICALINTERFACEQUEUESTATS.fields_by_name['rate_limit_drop_bytes'].has_options = True
_LOGICALINTERFACEQUEUESTATS.fields_by_name['rate_limit_drop_bytes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_LOGICALINTERFACEQUEUESTATS.fields_by_name['red_drop_packets'].has_options = True
_LOGICALINTERFACEQUEUESTATS.fields_by_name['red_drop_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_LOGICALINTERFACEQUEUESTATS.fields_by_name['red_drop_bytes'].has_options = True
_LOGICALINTERFACEQUEUESTATS.fields_by_name['red_drop_bytes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_LOGICALINTERFACEQUEUESTATS.fields_by_name['average_buffer_occupancy'].has_options = True
_LOGICALINTERFACEQUEUESTATS.fields_by_name['average_buffer_occupancy']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002 \001')
_LOGICALINTERFACEQUEUESTATS.fields_by_name['current_buffer_occupancy'].has_options = True
_LOGICALINTERFACEQUEUESTATS.fields_by_name['current_buffer_occupancy']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002 \001')
_LOGICALINTERFACEQUEUESTATS.fields_by_name['peak_buffer_occupancy'].has_options = True
_LOGICALINTERFACEQUEUESTATS.fields_by_name['peak_buffer_occupancy']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002 \001')
_LOGICALINTERFACEQUEUESTATS.fields_by_name['allocated_buffer_size'].has_options = True
_LOGICALINTERFACEQUEUESTATS.fields_by_name['allocated_buffer_size']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002 \001')
# @@protoc_insertion_point(module_scope)
