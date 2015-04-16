# Copyright 2015, 2016 IBM Corp.
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import xml.etree.ElementTree as etree
from src.utility import *
import sys,pyxb
from src.generated_src import UOM

class ListModule:
    """
    called in Listing operation to get the object list
    of ManagementConsole,ManagedSystem,LogicalPartition,
    LogicalPartitionProfile,VirtualIOServer and other objects.   
    """
    log_object = HMCClientLogger.HMCClientLogger(__name__)
    
    def listing(self, service, ip, root, content_type, Resource, session_id, uuid=None):
        
         """
         Makes an HTTPRequest to get the details of the
         corresponding object and store the response content
         into a python object.
         Args:
             service:uom or web
             ip:ip address of the hmc
             root:root element in rest uri
             content_type:type of object to be extracted
                          (logicalpartition,logicalpartitionprofile,
                           ManagedSystem,VirtualIOServer and other objects)
             session_id:to access the session
             uuid:root unique id
         Returns:
             list of corresponding objects
         """
         #for ManagementConsole the uuid is none and for other types the uri is appended with roots uuid
         obj_list = []
         xml_object = None
         headers_obj = HmcHeaders.HmcHeaders(service)
         ns = headers_obj.ns
         request_obj = HTTPClient.HTTPClient(service, ip, root, content_type, session_id)
         if uuid == None:
             request_obj.HTTPGet()
         else:
             request_obj.HTTPGet(append=str(uuid)+"/"+Resource)
         if request_obj.response_b:
             root = etree.fromstring(request_obj.response.text)
             entries = root.findall(".//%s:%s"%(Resource,Resource),
                                 namespaces={"%s" %(Resource): ns["xmlns"]})
             for entry in entries:
                 if entry.getchildren() != []:
                     xmlstring = etree.tostring(entry)
                     xml_object = UOM.CreateFromDocument(xmlstring)
                     obj_list.append(xml_object)
             return obj_list
