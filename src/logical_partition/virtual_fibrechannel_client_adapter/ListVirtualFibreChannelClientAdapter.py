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

from src.common import ListModule
from src.utility import HMCClientLogger
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "LogicalPartition"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml;type=VirtualFibreChannelClientAdapter"

class ListVirtualFibreChannelClientAdapter:
    """
    List the details of the virtual fibre channel adapter
    for a given logical partition
    """
    def __init__(self):
        """
        assign the root and content_type for request
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def list_virtualfibrechannel_clientadapter(self, ip, logicalpartition_id, x_api_session):
        """
        returns the list of virtual fibre channel adapter available in the
        client partition
        Args:
           ip : ip address of HMC
           logicalpartition_id : UUID of the Logical Partition
           x_api_session : session to be used
        """
        log.log_debug("fc adarpter object list is started")
        list_object = ListModule.ListModule()
        object_list = list_object.listing("uom", ip, self.root, self.content_type,
                            "VirtualFibreChannelClientAdapter", x_api_session,
                            logicalpartition_id)
        log.log_debug("fc adarpter object list is returned")
        return object_list
    
    def print_virtualfibrechannel_attributes(self,objects):
        """
        print the details of the given virtual fibre channel adapter
        """
        print("\n")
        print("LocalPartitionID".ljust(35),":",objects.LocalPartitionID.value())
        print("VirtualSlotNumber".ljust(35),":",objects.VirtualSlotNumber.value())
        print("RequiredAdapter".ljust(35),":",objects.RequiredAdapter.value())
        print("ConnectingPartitionID".ljust(35),":",objects.ConnectingPartitionID.value())
        print("ConnectingVirtualSlotNumber".ljust(35),":",objects.ConnectingVirtualSlotNumber.value())
        print("WWPNs".ljust(35),":",objects.WWPNs.value())
