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
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; Type=ClientNetworkAdapter"

class ListClientNetworkAdapter:
    """
    List the details of existing client network adapter
    """
    
    def __init__(self):
        """
        assign the root and content_type for request
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def list_clientnetwork_adapter(self, ip, logicalpartition_id, x_api_session):
        """
        returns a list client network adapters available in the given logical partition
        Args:
          ip : ip address of HMC
          logicalpartition_object : object of Logical Partition in which client Network Adapter
                                    is to be created
          x_api_session : session to be used
        """
        log.log_debug("client network adapter object list is started")
        list_object_list = ListModule.ListModule()
        object_list = list_object_list.listing("uom", ip,
                                 self.root, self.content_type,
                                 "ClientNetworkAdapter", x_api_session,
                                 logicalpartition_id)
        log.log_debug("client network adapter object list is returned")
        
        return object_list
    
    def print_clientnetwork_adapter_attributes(self,objects):
        """
        prints the details of the given client network adapter given
        """
        print("\n")
        print("VirtualSlotNumber".ljust(35),":",objects.VirtualSlotNumber.value())
        print("VirtualSwitchID".ljust(35),":",objects.VirtualSwitchID.value())
        print("PortVLANID".ljust(35),":",objects.PortVLANID.value())
        print("RequiredAdapter".ljust(35),":",objects.RequiredAdapter.value())                                
