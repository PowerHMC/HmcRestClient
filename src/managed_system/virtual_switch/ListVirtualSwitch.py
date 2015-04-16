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
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=VirtualSwitch"

class ListVirtualSwitch(object):
    """
    ListVirtualSwitch provides the definitions
    to return the list of
    VirtualSwitch objects available in the
    given ManagedSystem and contains the
    print definition to print the VirtualSwitch
    attribute details.
    """
     
    def __init__(self):        
        """
        initializes content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def list_virtualswitch_attributes(self,ip,managedsystem_uuid,session_id):
        """
        Accessed with ListVirtualSwitch object
        Args:
              ip:ip address of the hmc
              managedsystem_uuid: ManagedSystem uuid
              session_id:X-api-session id of the current session
        Returns:
              object_list containing the list of available virtual switch Objects
        """
        
        listing_object = ListModule.ListModule()
        object_list = listing_object.listing("uom", ip,
                                                  self.root, self.content_type,
                                                  "VirtualSwitch",
                                                  session_id, managedsystem_uuid)
        HMCClientLogger_object.log_debug("Returns VirtualSwitch" +
                                  "objects to the main module")
        return object_list
    
    def print_virtualswitch_attributes(self, virtualswitch_object):
        """
        Accessed with ListVirtualSwitch object

        Args:
            object_list:the selected object choice from src.the available VirtualSwitch objects.
        """
        
        print("\n")
        print("SwitchID".ljust(35),":",virtualswitch_object.SwitchID.value())
        print("SwitchName".ljust(35),":",virtualswitch_object.SwitchName.value())

