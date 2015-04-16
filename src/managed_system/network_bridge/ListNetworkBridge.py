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
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=NetworkBridge"

class ListNetworkBridge:
    """
    ListNetworkBridge provides the definitions
    to return the list of
    NetworkBridge objects available in the
    given HMCClientLoggericalPartition and contains the
    print definition to print the NetworkBridge
    attribute details.
    """
     
    def __init__(self):

        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def list_networkbridge_attributes(self,ip,managedsystem_uuid,session_id):
        """
        Accessed with NetworkBridge object
        Args:
              ip:ip address of the hmc
              uuid:HMCClientLoggericalPartition uuid
              session_id:session to access the HMCClientLoggericalPartition
        Returns:
              object_list containing the list of available HMCClientLoggericalPartition Objects
        """
        
        listing_object = ListModule.ListModule()
        object_list = listing_object.listing("uom", ip,
                                                  self.root, self.content_type,
                                                  "NetworkBridge",session_id, managedsystem_uuid)
        
        return object_list
    
    def print_networkbridge_attributes(self, objects):
        """
        Accessed with NetworkBridge object

        Args:
            object_list:the selected object choice from src.the available NetworkBridge objects.
        """
        
        print("\n")
        print("FailoverEnabled".ljust(35),":",objects.FailoverEnabled.value())
        print("LoadBalancingEnabled".ljust(35),":",objects.LoadBalancingEnabled.value())
        print("PortVLANID".ljust(35),":",objects.PortVLANID.value())
        print("\nAvailable LoadGroups:")
        for loadgroup in objects.LoadGroups.LoadGroup:
            print("LoadGroup PortVLANID".ljust(35),":",loadgroup.PortVLANID.value())
            print("Available TrunkAdapters in LoadGroup :")
            for trunkadapter in loadgroup.TrunkAdapters.TrunkAdapter:
                print("TrunkAdapter PortVLANID".ljust(35),":",trunkadapter.PortVLANID.value())
                print("DeviceName".ljust(35),":",trunkadapter.DeviceName.value())
                print("TrunkPriority".ljust(35),":",trunkadapter.TrunkPriority.value())
                print("\n")
        print("SharedEthernetAdapter :")
        for sharedethernetadapter in objects.SharedEthernetAdapters.SharedEthernetAdapter:
            print("Backing device type".ljust(35),":",
                  sharedethernetadapter.BackingDeviceChoice.EthernetBackingDevice.DeviceType.value())
            print("Backing device name".ljust(35),":",
                  sharedethernetadapter.BackingDeviceChoice.EthernetBackingDevice.DeviceName.value())
            print("\n")
