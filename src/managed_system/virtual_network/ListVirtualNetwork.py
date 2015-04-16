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

from src.utility import HTTPClient,HMCClientLogger
from src.common import ListModule
HMCClientLogger_object = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "ManagedSystem"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=VirtualNetwork"

class ListVirtualNetwork(object):
    """
    ListVirtualNetwork provides the definitions
    to return the list of
    VirtualNetwork objects available in the
    given LogicalPartition and contains the
    print definition to print the VirtualNetwork
    attribute details.
    """
     
    def __init__(self):
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def list_VirtualNetwork(self,ip,managedsystem_uuid,session_id):
        """
        Accessed with ListVirtualNetwork object
        Args:
              ip:ip address of the hmc
              uuid:LogicalPartition uuid
              session_id:x-api-session id
        Returns:
              object_list containing the list of available virtual network Objects
        """
        
        listing_object = ListModule.ListModule()
        object_list = listing_object.listing("uom", ip,
                                                  self.root, self.content_type,
                                                  "VirtualNetwork",
                                                  session_id, managedsystem_uuid)
        HMCClientLogger_object.log_debug("Returns VirtualNetwork" +
                                  "objects to the main module")
        return object_list
    
    def print_virtualnetwork_attributes(self, virtualnetwork_object):
        """
        Accessed with ListVirtualNetwork object

        Args:
            object_list:the selected object choice from src.the available VirtualNetwork objects.
        """
        
        print("\n")
        print("NetworkName".ljust(35),":",virtualnetwork_object.NetworkName.value())
        print("NetworkVLANID".ljust(35),":",virtualnetwork_object.NetworkVLANID.value())
        print("VswitchID".ljust(35),":",virtualnetwork_object.VswitchID.value())
        print("TaggedNetwork".ljust(35),":",virtualnetwork_object.TaggedNetwork.value())
        
if __name__=="__main__":
    v=ListVirtualNetwork()
    attr=v.list_virtual_network_attributes("9.126.138.108","f8fbeb06-09e9-39a6-91e9-be80b39cae49",sess_id)
    v.print_virtual_network_attributes(attr)
