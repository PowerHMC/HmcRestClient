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

ROOT = "ManagedSystem"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=LogicalPartition"

class ListLogicalPartition:
    
    def __init__(self):
        """
        initializes root and content-type
        """
        self.content_type = CONTENT_TYPE
        self.root = ROOT
        self.headers_obj = HmcHeaders.HmcHeaders("uom")
        
    def list_LogicalPartition(self, ip, uuid, session_id):
        """
        returns the list of available logicalpartition objects
         Args:
           ip : ip address of HMC
           uuid : UUID of the Logical Partition
           session_id : session to be used
        """
        log_object.log_debug("list of Lpar started")
        listing_object = ListModule.ListModule()
        object_list = listing_object.listing("uom",ip,self.root,self.content_type,"LogicalPartition",session_id,uuid)
        log_object.log_debug("Returns Logical Partition objects to the main module")
        return object_list
    
    def print_logicalpartition_attributes(self,logicalpartition_object):
        """
        prints the details of the given LogicalPartition object to the console
        """
        try:
            print("\n")
            print("PartitionName".ljust(35),":",logicalpartition_object.PartitionName.value())
            print("PartitionID".ljust(35),":",logicalpartition_object.PartitionID.value())
            print("PartitionType".ljust(35),":",logicalpartition_object.PartitionType.value())
            print("PartitionState".ljust(35),":",logicalpartition_object.PartitionState.value())
            print("MigrationState".ljust(35),":",logicalpartition_object.MigrationState.value())
            print("PartitionUUID".ljust(35),":",logicalpartition_object.PartitionUUID.value())
            print("AssociatedManagedSystem".ljust(35),":",logicalpartition_object.AssociatedManagedSystem.href)
            print("IsVirtualServiceAttentionLEDOn".ljust(35),":",logicalpartition_object.IsVirtualServiceAttentionLEDOn.value())
            print("Maximum Memory".ljust(35),":",logicalpartition_object.PartitionMemoryConfiguration.MaximumMemory.value())
            print("Desired Memory".ljust(35),":",logicalpartition_object.PartitionMemoryConfiguration.DesiredMemory.value())
            print("Minimum Memory".ljust(35),":",logicalpartition_object.PartitionMemoryConfiguration.MinimumMemory.value())
            print("HasDedicatedProcessors".ljust(35),":",logicalpartition_object.PartitionProcessorConfiguration.HasDedicatedProcessors.value())
            if logicalpartition_object.PartitionProcessorConfiguration.HasDedicatedProcessors.value():
                print("Maximum Processors".ljust(35),":",logicalpartition_object.PartitionProcessorConfiguration.\
                                      DedicatedProcessorConfiguration.MaximumProcessors.value())
                print("Desired Processors".ljust(35),":",logicalpartition_object.PartitionProcessorConfiguration.\
                                      DedicatedProcessorConfiguration.DesiredProcessors.value())
                print("Minimum Processors".ljust(35),":",logicalpartition_object.PartitionProcessorConfiguration.\
                                      DedicatedProcessorConfiguration.MinimumProcessors.value())
            else:
                print("Maximum ProcessingUnits".ljust(35),":",logicalpartition_object.PartitionProcessorConfiguration.\
                                      SharedProcessorConfiguration.MaximumProcessingUnits.value())
                print("Desired ProcessingUnits".ljust(35),":",logicalpartition_object.PartitionProcessorConfiguration.\
                                      SharedProcessorConfiguration.DesiredProcessingUnits.value())
                print("Minimum ProcessingUnits".ljust(35),":",logicalpartition_object.PartitionProcessorConfiguration.\
                                      SharedProcessorConfiguration.MinimumProcessingUnits.value())
        except Exception as e:
            self.log_object.log_info("Nonetype object found")




