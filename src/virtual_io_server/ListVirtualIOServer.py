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


from src.utility import HTTPClient, HMCClientLogger, HmcHeaders
from src.common import ListModule
import xml.etree.ElementTree as etree
log_object = HMCClientLogger.HMCClientLogger(__name__)

CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; \
                             type=VirtualIOServer"


class ListVirtualIOServer:

    """
    ListVirtualIOServer provides the definitions
    to return the list of
    VirtualIOServer objects available in the
    given ManagedSystem and contains the
    print definition to print the VirtualIOServer
    attribute details.
    """

    def __init__(self):
        self.content_type = CONTENT_TYPE

    def list_VirtualIOServer(self, ip, uuid, session_id):
        """
        Accessed with VirtualIOServer object
        Args:
              ip:ip address of the hmc
              uuid:ManagedSystem uuid
              session_id:session to access the VirtualIOServer
        Returns:
              object_list containing the list of available
              VirtualIOServer Objects
        """
        log_object.log_debug("List of VIOS started")
        listing_object = ListModule.ListModule()
        object_list = listing_object.listing("uom", ip,
                                             "ManagedSystem",
                                             self.content_type,
                                             "VirtualIOServer",
                                             session_id, uuid)
        log_object.log_debug("Returns VirtualIOServer objects" +
                             "to the main module")
        return object_list

    def print_virtualioserver_attributes(self, vios_object):
        """
        Accessed with Listvirtualioserver object
        Arguments:
                object_list:the selected object
                choice from src.the available virtualioserver objects.
        """

        log_object.log_debug("Print VirtualIOServer" +
                             "details that user has selected")
        print("\n")
        print("PartitionName".ljust(35), ":",
              vios_object.PartitionName.value())
        print("PartitionID".ljust(35), ":", vios_object.PartitionID.value())
        print("PartitionType".ljust(35), ":",
              vios_object.PartitionType.value())
        print("PartitionUUID".ljust(35), ":",
              vios_object.PartitionUUID.value())
        print("IsVirtualServiceAttentionLEDOn".ljust(35), ":", vios_object.
              IsVirtualServiceAttentionLEDOn.value())
        print("APICapable".ljust(35), ":", vios_object.APICapable.value())
        print("PartitionState".ljust(35), ":",
              vios_object.PartitionState.value())
        print("AssociatedManagedSystem".ljust(35), ":",
              vios_object.AssociatedManagedSystem.href)
        print("Maximum Memory".ljust(35), ":",
              vios_object.PartitionMemoryConfiguration.MaximumMemory.value())
        print("Desired Memory".ljust(35), ":",
              vios_object.PartitionMemoryConfiguration.DesiredMemory.value())
        print("Minimum Memory".ljust(35), ":",
              vios_object.PartitionMemoryConfiguration.MinimumMemory.value())
        print("HasDedicatedProcessors ".ljust(35), ":",
              vios_object.PartitionProcessorConfiguration.
              HasDedicatedProcessors.value())
        if vios_object.PartitionProcessorConfiguration.\
           HasDedicatedProcessors.value() == True:
            print("Maximum Processors".ljust(35), ":",
                  vios_object.PartitionProcessorConfiguration.
                  DedicatedProcessorConfiguration.MaximumProcessors.value())
            print("Desired Processors".ljust(35), ":",
                  vios_object.PartitionProcessorConfiguration.
                  DedicatedProcessorConfiguration.DesiredProcessors.value())
            print("Minimum Processors".ljust(35), ":",
                  vios_object.PartitionProcessorConfiguration.
                  DedicatedProcessorConfiguration.MinimumProcessors.value())


