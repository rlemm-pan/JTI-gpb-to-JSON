This script was created to translate JUNOS Telemetry Info from Google Protocol Buffer into JSON Format.  
Below is a JUNOS Configuration example needed to stream telemetry info in GPB format via UDP.  The script receives GPB data on UDP port 30000, reformats the data into JSON for sending streaming JSON to AppFormix via REST API on tcp port 8090.

services {

    analytics {
    
        streaming-server telemetry-server {
        
            remote-address 10.3.3.2;
            
            remote-port 30000;
            
        }
        
        export-profile appformix {
        
            local-address 10.255.1.2;
            
            local-port 21112;
            
            reporting-rate 1;
            
            format gpb;
            
            transport udp;
            
        }
        
        sensor linecard-interface-logical-usage {
        
            server-name telemetry-server;
            
            export-name appformix;
            
            resource /junos/system/linecard/interface/logical/usage/;
            
            resource-filter ge-*;
            
        }
        
    }
    
}

interfaces {

    ge-0/0/0 {
    
        unit 0 {
        
            family inet {
            
                address 10.3.3.1/24;
                
            }
            
        }
        
    }
    
    ge-0/0/2 {
    
        unit 0 {
        
            family inet {
            
                address 10.255.1.2/24;
                
            }
            
        }
        
    }
    
}


## Requirements needed by Python:
http_client

httplib

http

google.protobuf

protobuf_to_dict

urllib

requests

json

socket

## Requirements needed for PIP:

pip install protobuf

pip install protobuf_to_dict

## Requirements needed for Linux Host:

apt-get install netcat

apt-get install protobuf-compiler

apt-get install libprotobuf-dev

