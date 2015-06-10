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

from src.utility import HTTPClient,HMCClientLogger,HmcHeaders
from src.generated_src.UOM import *
import pyxb
import time
import xml.etree.ElementTree as etree
log_object = HMCClientLogger.HMCClientLogger(__name__)

CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=%s"
ROOT = "ManagedSystem"
SCHEMA_VER = "V1_3_0"
DEDICATED_PROCESSORS = False
PARTITION_NAME = "%s-"
MAX_MEMORY = 256
MIN_MEMORY = 256
DES_MEMORY = 256
DES_PROC_UNITS = 0.5
MIN_PROC_UNITS = 0.5
MAX_PROC_UNITS = 0.5
DES_VIRTUAL_PROCESSORS = 1
MIN_VIRTUAL_PROCESSORS = 1
MAX_VIRTUAL_PROCESSORS = 1
SHARING_MODE = "capped"

class CreatePartition:
    """
    class provides definitions for LogicalPartition Creation
    """
    
    def __init__(self, partition_type):
        """
        initializes the content-type and root
        Args:
            partition_type : type of  object Logical Partition or VirtualIOServer
        """
        self.type = partition_type
        self.content_type = CONTENT_TYPE%(partition_type)
        self.root = ROOT
        self.headers_obj = HmcHeaders.HmcHeaders("uom")
        
    def create_Partition(self,ip,uuid,session_id):
            """
            Args:
              ip:ip address of HMC
              uuid:ManagedSystemUUID
              session_id:to access the session
            Returns:
              Returns the created LogicalPartition object
            """
            log_object.log_debug("creation of logical partition started")
            obj = eval(self.type)()
            ns = self.headers_obj.ns
            obj.schemaVersion = SCHEMA_VER
            pyxb.RequireValidWhenGenerating(True)
            obj.PartitionMemoryConfiguration = pyxb.BIND()
            obj.PartitionMemoryConfiguration.schemaVersion = SCHEMA_VER
            obj.PartitionMemoryConfiguration.DesiredMemory = DES_MEMORY
            obj.PartitionMemoryConfiguration.MaximumMemory = MAX_MEMORY
            obj.PartitionMemoryConfiguration.MinimumMemory = MIN_MEMORY
            obj.PartitionProcessorConfiguration = pyxb.BIND()
            obj.PartitionProcessorConfiguration.schemaVersion = SCHEMA_VER
            obj.PartitionProcessorConfiguration.HasDedicatedProcessors = DEDICATED_PROCESSORS
            obj.PartitionProcessorConfiguration.SharedProcessorConfiguration = pyxb.BIND()
            obj.PartitionProcessorConfiguration.SharedProcessorConfiguration.schemaVersion = SCHEMA_VER
            obj.PartitionProcessorConfiguration.SharedProcessorConfiguration.DesiredProcessingUnits = DES_PROC_UNITS
            obj.PartitionProcessorConfiguration.SharedProcessorConfiguration.DesiredVirtualProcessors = DES_VIRTUAL_PROCESSORS
            obj.PartitionProcessorConfiguration.SharedProcessorConfiguration.MaximumProcessingUnits = MAX_PROC_UNITS
            obj.PartitionProcessorConfiguration.SharedProcessorConfiguration.MaximumVirtualProcessors = MAX_VIRTUAL_PROCESSORS
            obj.PartitionProcessorConfiguration.SharedProcessorConfiguration.MinimumProcessingUnits = MIN_PROC_UNITS
            obj.PartitionProcessorConfiguration.SharedProcessorConfiguration.MinimumVirtualProcessors = MIN_VIRTUAL_PROCESSORS
            obj.PartitionProcessorConfiguration.SharingMode = SHARING_MODE
            if self.type == "VirtualIOServer":
                obj.PartitionType = "Virtual IO Server"
                partition_name = PARTITION_NAME%("VIOS")+""+time.strftime("%d%m%y-%X")
            else:
                obj.PartitionType = "AIX/Linux"
                partition_name = PARTITION_NAME%("LPAR")+""+time.strftime("%d%m%y-%X")
            obj.PartitionName = partition_name
            xmlobject = obj.toDOM()
            xmlobject.documentElement.setAttribute("xmlns",ns["xmlns"])
            xmlpayload = xmlobject.toxml("utf-8")
            request_obj = HTTPClient.HTTPClient("uom",ip,self.root,self.content_type,session_id)
            request_obj.HTTPPut(xmlpayload,append=str(uuid)+"/"+self.type)
            log_object.log_debug("response of lpar creation -- %s"%(request_obj.response))
            if request_obj.response_b:
                root = etree.fromstring(request_obj.response.content)
                entry = root.findall(".//%s:%s"%(self.type,self.type),
                                     namespaces={self.type: ns["xmlns"]})
                xmlstring = etree.tostring(entry[0])
                xml_object = CreateFromDocument(xmlstring)
                log_object.log_debug("partition created successfully")
                return xml_object
            
