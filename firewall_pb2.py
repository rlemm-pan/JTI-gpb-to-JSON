# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: firewall.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import telemetry_top_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='firewall.proto',
  package='',
  serialized_pb='\n\x0e\x66irewall.proto\x1a\x13telemetry_top.proto\"2\n\x08\x46irewall\x12&\n\x0e\x66irewall_stats\x18\x01 \x03(\x0b\x32\x0e.FirewallStats\"\xf4\x01\n\rFirewallStats\x12\x1a\n\x0b\x66ilter_name\x18\x01 \x02(\tB\x05\x82@\x02\x08\x01\x12\x18\n\ttimestamp\x18\x02 \x01(\x04\x42\x05\x82@\x02\x10\x01\x12\"\n\x0cmemory_usage\x18\x03 \x03(\x0b\x32\x0c.MemoryUsage\x12$\n\rcounter_stats\x18\x04 \x03(\x0b\x32\r.CounterStats\x12$\n\rpolicer_stats\x18\x05 \x03(\x0b\x32\r.PolicerStats\x12=\n\x1ahierarchical_policer_stats\x18\x06 \x03(\x0b\x32\x19.HierarchicalPolicerStats\"<\n\x0bMemoryUsage\x12\x13\n\x04name\x18\x01 \x02(\tB\x05\x82@\x02\x08\x01\x12\x18\n\tallocated\x18\x02 \x01(\x04\x42\x05\x82@\x02 \x01\"Q\n\x0c\x43ounterStats\x12\x13\n\x04name\x18\x01 \x02(\tB\x05\x82@\x02\x08\x01\x12\x16\n\x07packets\x18\x02 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x14\n\x05\x62ytes\x18\x03 \x01(\x04\x42\x05\x82@\x02\x18\x01\"\xa0\x01\n\x0cPolicerStats\x12\x13\n\x04name\x18\x01 \x02(\tB\x05\x82@\x02\x08\x01\x12\"\n\x13out_of_spec_packets\x18\x02 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12 \n\x11out_of_spec_bytes\x18\x03 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x35\n\x16\x65xtended_policer_stats\x18\x04 \x01(\x0b\x32\x15.ExtendedPolicerStats\"\x9a\x01\n\x14\x45xtendedPolicerStats\x12\x1e\n\x0foffered_packets\x18\x01 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1c\n\roffered_bytes\x18\x02 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\"\n\x13transmitted_packets\x18\x03 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12 \n\x11transmitted_bytes\x18\x04 \x01(\x04\x42\x05\x82@\x02\x18\x01\"\xaf\x01\n\x18HierarchicalPolicerStats\x12\x13\n\x04name\x18\x01 \x02(\tB\x05\x82@\x02\x08\x01\x12\x1e\n\x0fpremium_packets\x18\x02 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1c\n\rpremium_bytes\x18\x03 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12 \n\x11\x61ggregate_packets\x18\x04 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1e\n\x0f\x61ggregate_bytes\x18\x05 \x01(\x04\x42\x05\x82@\x02\x18\x01:=\n\x11jnpr_firewall_ext\x12\x17.JuniperNetworksSensors\x18\x06 \x01(\x0b\x32\t.Firewall')


JNPR_FIREWALL_EXT_FIELD_NUMBER = 6
jnpr_firewall_ext = _descriptor.FieldDescriptor(
  name='jnpr_firewall_ext', full_name='jnpr_firewall_ext', index=0,
  number=6, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_FIREWALL = _descriptor.Descriptor(
  name='Firewall',
  full_name='Firewall',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='firewall_stats', full_name='Firewall.firewall_stats', index=0,
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
  serialized_start=39,
  serialized_end=89,
)


_FIREWALLSTATS = _descriptor.Descriptor(
  name='FirewallStats',
  full_name='FirewallStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter_name', full_name='FirewallStats.filter_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='FirewallStats.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\020\001')),
    _descriptor.FieldDescriptor(
      name='memory_usage', full_name='FirewallStats.memory_usage', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='counter_stats', full_name='FirewallStats.counter_stats', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policer_stats', full_name='FirewallStats.policer_stats', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hierarchical_policer_stats', full_name='FirewallStats.hierarchical_policer_stats', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=92,
  serialized_end=336,
)


_MEMORYUSAGE = _descriptor.Descriptor(
  name='MemoryUsage',
  full_name='MemoryUsage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='MemoryUsage.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')),
    _descriptor.FieldDescriptor(
      name='allocated', full_name='MemoryUsage.allocated', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=338,
  serialized_end=398,
)


_COUNTERSTATS = _descriptor.Descriptor(
  name='CounterStats',
  full_name='CounterStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CounterStats.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')),
    _descriptor.FieldDescriptor(
      name='packets', full_name='CounterStats.packets', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='CounterStats.bytes', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=400,
  serialized_end=481,
)


_POLICERSTATS = _descriptor.Descriptor(
  name='PolicerStats',
  full_name='PolicerStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PolicerStats.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')),
    _descriptor.FieldDescriptor(
      name='out_of_spec_packets', full_name='PolicerStats.out_of_spec_packets', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='out_of_spec_bytes', full_name='PolicerStats.out_of_spec_bytes', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='extended_policer_stats', full_name='PolicerStats.extended_policer_stats', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=484,
  serialized_end=644,
)


_EXTENDEDPOLICERSTATS = _descriptor.Descriptor(
  name='ExtendedPolicerStats',
  full_name='ExtendedPolicerStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offered_packets', full_name='ExtendedPolicerStats.offered_packets', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='offered_bytes', full_name='ExtendedPolicerStats.offered_bytes', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='transmitted_packets', full_name='ExtendedPolicerStats.transmitted_packets', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='transmitted_bytes', full_name='ExtendedPolicerStats.transmitted_bytes', index=3,
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
  serialized_start=647,
  serialized_end=801,
)


_HIERARCHICALPOLICERSTATS = _descriptor.Descriptor(
  name='HierarchicalPolicerStats',
  full_name='HierarchicalPolicerStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='HierarchicalPolicerStats.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')),
    _descriptor.FieldDescriptor(
      name='premium_packets', full_name='HierarchicalPolicerStats.premium_packets', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='premium_bytes', full_name='HierarchicalPolicerStats.premium_bytes', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='aggregate_packets', full_name='HierarchicalPolicerStats.aggregate_packets', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')),
    _descriptor.FieldDescriptor(
      name='aggregate_bytes', full_name='HierarchicalPolicerStats.aggregate_bytes', index=4,
      number=5, type=4, cpp_type=4, label=1,
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
  serialized_start=804,
  serialized_end=979,
)

_FIREWALL.fields_by_name['firewall_stats'].message_type = _FIREWALLSTATS
_FIREWALLSTATS.fields_by_name['memory_usage'].message_type = _MEMORYUSAGE
_FIREWALLSTATS.fields_by_name['counter_stats'].message_type = _COUNTERSTATS
_FIREWALLSTATS.fields_by_name['policer_stats'].message_type = _POLICERSTATS
_FIREWALLSTATS.fields_by_name['hierarchical_policer_stats'].message_type = _HIERARCHICALPOLICERSTATS
_POLICERSTATS.fields_by_name['extended_policer_stats'].message_type = _EXTENDEDPOLICERSTATS
DESCRIPTOR.message_types_by_name['Firewall'] = _FIREWALL
DESCRIPTOR.message_types_by_name['FirewallStats'] = _FIREWALLSTATS
DESCRIPTOR.message_types_by_name['MemoryUsage'] = _MEMORYUSAGE
DESCRIPTOR.message_types_by_name['CounterStats'] = _COUNTERSTATS
DESCRIPTOR.message_types_by_name['PolicerStats'] = _POLICERSTATS
DESCRIPTOR.message_types_by_name['ExtendedPolicerStats'] = _EXTENDEDPOLICERSTATS
DESCRIPTOR.message_types_by_name['HierarchicalPolicerStats'] = _HIERARCHICALPOLICERSTATS

class Firewall(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FIREWALL

  # @@protoc_insertion_point(class_scope:Firewall)

class FirewallStats(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FIREWALLSTATS

  # @@protoc_insertion_point(class_scope:FirewallStats)

class MemoryUsage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MEMORYUSAGE

  # @@protoc_insertion_point(class_scope:MemoryUsage)

class CounterStats(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COUNTERSTATS

  # @@protoc_insertion_point(class_scope:CounterStats)

class PolicerStats(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _POLICERSTATS

  # @@protoc_insertion_point(class_scope:PolicerStats)

class ExtendedPolicerStats(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXTENDEDPOLICERSTATS

  # @@protoc_insertion_point(class_scope:ExtendedPolicerStats)

class HierarchicalPolicerStats(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HIERARCHICALPOLICERSTATS

  # @@protoc_insertion_point(class_scope:HierarchicalPolicerStats)

jnpr_firewall_ext.message_type = _FIREWALL
telemetry_top_pb2.JuniperNetworksSensors.RegisterExtension(jnpr_firewall_ext)

_FIREWALLSTATS.fields_by_name['filter_name'].has_options = True
_FIREWALLSTATS.fields_by_name['filter_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')
_FIREWALLSTATS.fields_by_name['timestamp'].has_options = True
_FIREWALLSTATS.fields_by_name['timestamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\020\001')
_MEMORYUSAGE.fields_by_name['name'].has_options = True
_MEMORYUSAGE.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')
_MEMORYUSAGE.fields_by_name['allocated'].has_options = True
_MEMORYUSAGE.fields_by_name['allocated']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002 \001')
_COUNTERSTATS.fields_by_name['name'].has_options = True
_COUNTERSTATS.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')
_COUNTERSTATS.fields_by_name['packets'].has_options = True
_COUNTERSTATS.fields_by_name['packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_COUNTERSTATS.fields_by_name['bytes'].has_options = True
_COUNTERSTATS.fields_by_name['bytes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_POLICERSTATS.fields_by_name['name'].has_options = True
_POLICERSTATS.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')
_POLICERSTATS.fields_by_name['out_of_spec_packets'].has_options = True
_POLICERSTATS.fields_by_name['out_of_spec_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_POLICERSTATS.fields_by_name['out_of_spec_bytes'].has_options = True
_POLICERSTATS.fields_by_name['out_of_spec_bytes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_EXTENDEDPOLICERSTATS.fields_by_name['offered_packets'].has_options = True
_EXTENDEDPOLICERSTATS.fields_by_name['offered_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_EXTENDEDPOLICERSTATS.fields_by_name['offered_bytes'].has_options = True
_EXTENDEDPOLICERSTATS.fields_by_name['offered_bytes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_EXTENDEDPOLICERSTATS.fields_by_name['transmitted_packets'].has_options = True
_EXTENDEDPOLICERSTATS.fields_by_name['transmitted_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_EXTENDEDPOLICERSTATS.fields_by_name['transmitted_bytes'].has_options = True
_EXTENDEDPOLICERSTATS.fields_by_name['transmitted_bytes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_HIERARCHICALPOLICERSTATS.fields_by_name['name'].has_options = True
_HIERARCHICALPOLICERSTATS.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\010\001')
_HIERARCHICALPOLICERSTATS.fields_by_name['premium_packets'].has_options = True
_HIERARCHICALPOLICERSTATS.fields_by_name['premium_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_HIERARCHICALPOLICERSTATS.fields_by_name['premium_bytes'].has_options = True
_HIERARCHICALPOLICERSTATS.fields_by_name['premium_bytes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_HIERARCHICALPOLICERSTATS.fields_by_name['aggregate_packets'].has_options = True
_HIERARCHICALPOLICERSTATS.fields_by_name['aggregate_packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
_HIERARCHICALPOLICERSTATS.fields_by_name['aggregate_bytes'].has_options = True
_HIERARCHICALPOLICERSTATS.fields_by_name['aggregate_bytes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202@\002\030\001')
# @@protoc_insertion_point(module_scope)
