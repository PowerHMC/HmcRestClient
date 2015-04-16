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
log_object = HMCClientLogger.HMCClientLogger(__name__)

CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=LogicalPartitionProfile"

class ListLogicalPartitionProfile:
    """
    ListLogicalPartitionProfile provides the definitions
    to return the list of
    LogicalPartitionProfile objects available in the
    given vios and contains the
    print definition to print the LogicalPartitionProfile
    attribute details.
    """
     
    def __init__(self,root):        
        
        self.content_type = CONTENT_TYPE
        self.root=root
        
    def list_LogicalPartitionProfile(self,ip,uuid,session_id):
        """
        Accessed with ListLogicalPartitionProfile object
        Args:
              ip:ip address of the hmc
              uuid:vios uuid
              session_id:session to access the vios
        Returns:
              object_list containing the list of available LogicalPartitionProfile Objects
        """
        log_object.log_debug("List of Logical Partition Profile Started")
        listing_object = ListModule.ListModule()
        object_list = listing_object.listing("uom", ip,
                                                  self.root,
                                                  self.content_type, "LogicalPartitionProfile",
                                                  session_id, uuid)
        log_object.log_debug("Returns Logical Partition Profile" +
                                  "objects to the main module")
        return object_list
    
    def print_logicalpartitionprofile_attributes(self, profile_object):
        """
        Accessed with ListLogicalPartitionProfile object

        Args:
            object_list:the selected object choice from src.the available LogicalPartitionProfile objects.
        """
        
        print("\n")
        print("ProfileName".ljust(35),":",profile_object.ProfileName.value())
        print("ProfileType".ljust(35),":",profile_object.ProfileType.value())
        print("Maximum Memory".ljust(35),":",profile_object.ProfileMemory.MaximumMemory.value())
        print("Desired Memory".ljust(35),":",profile_object.ProfileMemory.DesiredMemory.value())
        print("Minimum Memory".ljust(35),":",profile_object.ProfileMemory.MinimumMemory.value())
        print("HasDedicatedProcessors".ljust(35),":",
              profile_object.ProcessorAttributes.HasDedicatedProcessors.value())
        if profile_object.ProcessorAttributes.HasDedicatedProcessors.value():
            print("Maximum Processors".ljust(35),":",profile_object.ProcessorAttributes.\
                                  DedicatedProcessorConfiguration.MaximumProcessors.value())
            print("Desired Processors".ljust(35),":",profile_object.ProcessorAttributes.\
                                  DedicatedProcessorConfiguration.DesiredProcessors.value())
            print("Minimum Processors".ljust(35),":",profile_object.ProcessorAttributes.\
                                  DedicatedProcessorConfiguration.MinimumProcessors.value())
        else:
            print("Maximum ProcessingUnits".ljust(35),":",profile_object.ProcessorAttributes.\
                                  SharedProcessorConfiguration.MaximumProcessingUnits.value())
            print("Desired ProcessingUnits".ljust(35),":",profile_object.ProcessorAttributes.\
                                  SharedProcessorConfiguration.DesiredProcessingUnits.value())
            print("Minimum ProcessingUnits".ljust(35),":",profile_object.ProcessorAttributes.\
                                  SharedProcessorConfiguration.MinimumProcessingUnits.value())
