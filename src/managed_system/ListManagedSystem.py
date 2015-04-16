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

CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=ManagedSystem"

class ListManagedSystem(object):

    """"
    lists the details of Managed System
    """
    
    def __init__(self):
        """
        Initializes the content_type
        """
       
        self.content_type = CONTENT_TYPE
       
        
    def list_ManagedSystem(self, ip, session_id):
        """
           collects the xml content of the managed system and
           returns a reference to it
        Args:
            ip : ip address of HMC
            session_id : session to be used
        """
        log_object.log_debug("List of ManagedSystem started")
        listing_object = ListModule.ListModule()
        #call to get the xml content of managed system #
        self.object_list = listing_object.listing("uom", ip,
                                                  "ManagedSystem",
                                                  self.content_type, "ManagedSystem", session_id)
        log_object.log_debug("Returns ManagedSystem objects to"
                                  "the main module")
        return self.object_list

    def print_managedsystem_attributes(self, choice):
        """
           Prints the quick property values from src.the retrieved xml content
           
           Args:
                choice:represents user selected choice of specific
                managed system
        """
        object_list=self.object_list[choice]
        print("\n")
        print("ManagedSystemName".ljust(35), ":",
              object_list.SystemName.value())
        print("ManagedSystem ID".ljust(35), ":",
              object_list.Metadata.Atom.AtomID.value())
        print("MachineType".ljust(35), ":",
              object_list.MachineTypeModelAndSerialNumber.MachineType.value())
        print("Model".ljust(35), ":",
              object_list.MachineTypeModelAndSerialNumber.Model.value())
        print("IPAddress".ljust(35), ":", object_list.PrimaryIPAddress.value())
        print("SystemState".ljust(35), ":", object_list.State.value())
        print("SerialNumber".ljust(35), ":",
              object_list.MachineTypeModelAndSerialNumber.SerialNumber.value())
        print("PhysicalSystemAttentionLEDState".ljust(35), ":",
              object_list.PhysicalSystemAttentionLEDState.value())


       
    
    
    
    

    
    
 
