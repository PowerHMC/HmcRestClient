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
import pyxb
import xml.etree.ElementTree as etree
log_object = HMCClientLogger.HMCClientLogger(__name__)

ROOT =  "ManagedSystem"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=LogicalPartition"

class DeleteLogicalPartition:
    
    def __init__(self):
        """
        initializes root ans content-type
        """
        self.content_type = CONTENT_TYPE
        self.root = ROOT
        
    def delete_LogicalPartition(self,ip,uuid,logicalpartition_object,session_id):
        """
        Deletes the provided LogicalPartition
        Args:
           ip : ip Address of HMC
           uuid : ManagedSystemUUID
           logicalpartition_object : object of LogicalPartition to be deleted
           session_id : to access the session
        """
        log_object.log_debug("lpar state --- %s"%(logicalpartition_object.PartitionState.value()))
        if logicalpartition_object.PartitionState.value() == "not activated":
            request_obj = HTTPClient.HTTPClient("uom",ip,self.root,self.content_type,session_id)
            request_obj.HTTPDelete(append=str(uuid)+"/LogicalPartition/"+str(logicalpartition_object.PartitionUUID.value()))
            if request_obj.response_b:
                log_object.log_debug("Partition Deleted Successfully")
                print("\nPartition Deleted Successfully")
        else :
            log_object.log_warn("LogicalPartition is in Running State...Shutdown the partition before deleting.")
            
        
    
