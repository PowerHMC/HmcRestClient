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
from src.common import ListModule
from src.generated_src import UOM
import pyxb
import xml.etree.ElementTree as etree
log_object = HMCClientLogger.HMCClientLogger(__name__)

CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=%s"
DES_MEMORY = 512
MAX_MEMORY = 512
MIN_MEMORY = 512

class ModifyPartition:
    """
    class provides definitions for Modifying LogicalPartition 
    """
    
    def __init__(self, partition_type):
        """
        initializes the content-type and root
        Args:
            partition_type : type of  object Logical Partition or VirtualIOServer
        """
        
        self.content_type = CONTENT_TYPE%(partition_type)
        self.root = partition_type
        self.headers_obj = HmcHeaders.HmcHeaders("uom")
        
    def modify_Partition(self, ip, logicalpartition_object, session_id):
            """
            Modifies the Memory attributes of provided logicalpartition object
            Args:
               ip : IP address of HMC
               logicalpartition_object : the object of LogicalPartition
                                         to be modified
               session_id : session to be used
            """
            log_object.log_debug("modification of lpar started ")
            logicalpartition_object.PartitionMemoryConfiguration.DesiredMemory = DES_MEMORY
            logicalpartition_object.PartitionMemoryConfiguration.MaximumMemory = MAX_MEMORY
            logicalpartition_object.PartitionMemoryConfiguration.MinimumMemory = MIN_MEMORY
            inputpayload = logicalpartition_object.toxml("utf-8")
            request_object = HTTPClient.HTTPClient("uom",ip,self.root,self.content_type,session_id)
            request_object.HTTPPost(payload=inputpayload,append=str(logicalpartition_object.PartitionUUID.value()))
            log_object.log_debug("response of lpar modification --- %s"%(request_object.response))
            if request_object.response_b:
                log_object.log_debug("updations to partition are made successfully")
                return True
            else:
                return False
