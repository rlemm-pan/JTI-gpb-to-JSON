#!/usr/bin/python
import requests
import argparse
import json
import os
import logging
import socket
from telemetry_top_pb2 import *
from cpu_memory_utilization_pb2 import *
from firewall_pb2 import *
from inline_jflow_pb2 import *
from logical_port_pb2 import *
from lsp_mon_pb2 import *
from lsp_stats_pb2 import *
from npu_memory_utilization_pb2 import *
from npu_utilization_pb2 import *
from optics_pb2 import *
from packet_stats_pb2 import *
from port_pb2 import *
from google.protobuf.json_format import *
from protobuf_to_dict import protobuf_to_dict, TYPE_CALLABLE_MAP

#Telemetry
Telemetry_Stream = TelemetryStream()
IETF_Sensors = IETFSensors()
Enterprise_Sensors = EnterpriseSensors()
Juniper_Networks_Sensors = JuniperNetworksSensors()

#Packet Stats
Packet_Statistics = PacketStatistics()
Packet_Stats_Packet_ForwardingEngine = PacketStatsPacketForwardingEngine()
Packet_Stats_Class = PacketStatsClass()
Packet_Stats_Counter = PacketStatsCounter()

#Port
Port = Port()
Interface_Infos = InterfaceInfos()
Queue_Stats = QueueStats()
Interface_Stats = InterfaceStats()
Ingress_Interface_Errors = IngressInterfaceErrors()

#Optics
Optics = Optics()
Optics_Infos = OpticsInfos()
Optics_Diag_Stats = OpticsDiagStats()
Optics_DiagLane_Stats = OpticsDiagLaneStats()

#Network Processor Utilization
Network_Processor_Utilization = NetworkProcessorUtilization()
Utilization = Utilization()
Memory_Load = MemoryLoad()
Packet_Load = PacketLoad()

#Network Processor Memory Utilization
Network_Processor_Memory_Utilization = NetworkProcessorMemoryUtilization()
Npu_Memory = NpuMemory()
Npu_Memory_Summary = NpuMemorySummary()
Npu_Memory_Partition = NpuMemoryPartition()

#LSP Stats
Lsp_Stats = LspStats()
Lsp_Stats_Record = LspStatsRecord()

#LSP Monitoring
key = key()
lsp_monitor_data_event = lsp_monitor_data_event()
ero_type_entry = ero_type_entry()
ero_ipv4_type = ero_ipv4_type()
rro_type_entry = rro_type_entry()
rro_ipv4_type = rro_ipv4_type()
lsp_monitor_data_property = lsp_monitor_data_property()
lsp_mon = lsp_mon()

#Inline JFlow Monitoring
Inline_Jflow = InlineJflow()
Inline_Jflow_Npu_Stats = InlineJflowNpuStats()

#Firewall
Firewall = Firewall()
Firewall_Stats = FirewallStats()
Memory_Usage = MemoryUsage()
Counter_Stats = CounterStats()
Policer_Stats = PolicerStats()
Extended_Policer_Stats = ExtendedPolicerStats()
Hierarchical_Policer_Stats = HierarchicalPolicerStats()

#CPU Memory
Cpu_Memory_Utilization = CpuMemoryUtilization()
Cpu_Memory_Utilization_Summary = CpuMemoryUtilizationSummary()
Cpu_Memory_Utilization_Per_Application = CpuMemoryUtilizationPerApplication()

ip = '0.0.0.0'
udp_port = 30000
rest_ip = '127.0.0.1'
rest_port = '8090'
buffer_size = 65535

parser = argparse.ArgumentParser(add_help=True)

parser.add_argument("-l", action="store_false",
                    help="log JSON Stream to Screen")

parser.add_argument("-r", action="store_false",
                    help="Log HTTP Requests to Screen")

parser.add_argument("-i", action="store",
                    help="Host to post JSON Stream via REST.  Default is 127.0.0.1")

parser.add_argument("-p", action="store",
                    help="Port to post JSON Stream via REST.  Default is 8090")

parser.add_argument("-u", action="store",
                    help="UDP Port to listen for protobuf Stream.  Default is 30000")

parser.add_argument("-b", action="store",
                    help="Size of packet being sent by protobuf.  Default is 65535.  Leave it alone if you're not having problems")

parser.add_argument("-j", action="store",
                    help="IP to listen for protobuf Stream.  This is usually the local IP of the Host this script runs on.  Default is 0.0.0.0.")

args = parser.parse_args()

if args.l is False:
    print_json = 1
elif args.l is True:
    print_json = 0
if args.r is False:
    http_log_enabled = 1
elif args.r is True:
    http_log_enabled = 0
if args.j:
    ip = args.j
if args.u:
    udp_port = int(args.u)
if args.i:
    rest_ip = args.i
if args.p:
    rest_port = args.p
if args.b:
    buffer_size = int(args.b)

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((ip, udp_port))
roomKey = ''
collection_name = ''
json_header = {'content-type': 'application/json'}

url = 'http://'+rest_ip+':'+rest_port+'/version/2.0/post_event'

def log_http():
    try:
        import http.client as http_client
    except ImportError:
        import httplib as http_client

    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

def post_url(json_data):
    global print_json, http_log_enabled, rest_ip, rest_port, url, json_header
    if print_json == 1 and http_log_enabled == 0:
        print json_data
        requests.post(url=url, data=json_data, headers=json_header)
    elif http_log_enabled == 1 and print_json == 0:
        log_http()
        requests.post(url=url, data=json_data, headers=json_header)
    elif print_json == 1 and http_log_enabled == 1:
        log_http()
        print json_data
        requests.post(url=url, data=json_data, headers=json_header)
    else:
        requests.post(url=url, data=json_data, headers=json_header)

def stream_gpb_to_json():
    global buffer_size
    while True:
        junos_telemetry_info_stream, addr = socket.recvfrom(buffer_size)
        try:
            for gpb_data in [Telemetry_Stream]:
                gpb_data.ParseFromString(junos_telemetry_info_stream)
                json_data = json.dumps(protobuf_to_dict(gpb_data, type_callable_map=TYPE_CALLABLE_MAP, use_enum_labels=True))
                json_data = json.loads(json_data)
                roomKey = json_data['system_id']
                timestamp = json_data['timestamp']
                data = {'collection_name': 'jdi_usage_collection', 'data': {'Timestamp': timestamp, \
                        'roomKey': roomKey, 'jti_info': json_data}, 'tailwind_manager': {}}
                json_data = json.dumps(data).replace("u'", "'")
                post_url(json_data)
        except:
            pass

stream_gpb_to_json()
