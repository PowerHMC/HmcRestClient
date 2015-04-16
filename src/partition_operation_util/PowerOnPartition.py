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
from src.common.JobStatus import *
from src.logical_partition_profile import ListLogicalPartitionProfile
import pyxb
import time
import os
import xml.etree.ElementTree as etree
from src.generated_src import UOM
log_object = HMCClientLogger.HMCClientLogger(__name__)

CONTENT_TYPE = "application/vnd.ibm.powervm.web+xml; type=JobRequest"


class PowerOnPartition(JobStatus):
    
    def __init__(self, partition_type):
        """
        initializes root and content_type
        Args:
            partition_type : type of  object Logical Partition or VirtualIOServer
        """
        self.content_type = CONTENT_TYPE
        self.root = partition_type
        self.headers_obj = HmcHeaders.HmcHeaders("web")
        directory_path=os.path.dirname(__file__)
        self.input = open(directory_path+"/data/poweron_lpar.xml","r").read()
        
    def poweron_Partition(self, ip, logicalpartition_object, session_id):
        """
        performs poweron operation for the provided LogicalPartition object
        Args:
           ip : ip address of HMC
           logicalpartition_object : object of the logical partition to be activated
           session_id : session to be used
        """
        super().__init__(ip, self.root, self.content_type, session_id)
        log_object.log_debug("Power on of lpar started")
        namespace = self.headers_obj.ns["xmlns"]
        logicalpartitionprofile_object = ListLogicalPartitionProfile.ListLogicalPartitionProfile(self.root)
        object_list = logicalpartitionprofile_object.list_LogicalPartitionProfile(ip,logicalpartition_object.PartitionUUID.value(),session_id)
        ProfileUUID = object_list[0].Metadata.Atom.AtomID.value()
        inputpayload = self.input.format(self.root, ProfileUUID)
        logicalpartition_uuid = logicalpartition_object.PartitionUUID.value()
        request_object = HTTPClient.HTTPClient("uom", ip, self.root, self.content_type, session_id)
        request_object.HTTPPut(payload=inputpayload, append=str(logicalpartition_uuid)+"/do/PowerOn")
        log_object.log_debug("response of lpar poweron --- %s"%(request_object.response))
        if request_object.response_b:
            self.get_job_status(request_object)
            
