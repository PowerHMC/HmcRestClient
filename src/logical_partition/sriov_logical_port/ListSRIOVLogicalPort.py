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


from src.utility import HMCClientLogger,HTTPClient,HmcHeaders
from src.common import ListModule
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "LogicalPartition"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml;type=SRIOVEthernetLogicalPort"

class ListSRIOVLogicalPort(object):

    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE

    def list_sriov_logical_port(self, ip, logicalpartition_uuid, x_api_session):
        """
        returns a list of SRIOV Ethernet Logical Ports
        Args:
            ip : ip address of HMC
            logicalpartition_uuid : UUID of the Logical Partition
            x_api_session : session to be used
        """
        log.log_debug("list of SRIOVLogical Ports started")
        list_object = ListModule.ListModule()
        object_list = list_object.listing("uom", ip , self.root,
                            self.content_type, "SRIOVEthernetLogicalPort",
                            x_api_session, logicalpartition_uuid)
        log.log_debug("list of SRIOVLogical Ports returned")
        return object_list
    
    def print_sriov_logical_port(self,objects):
        """
        Prints the details of the SRIOV Logical Port to the screen
        """
        print("\n")
        print("AdapterID".ljust(35),":",objects.AdapterID.value())
        print("Capacity".ljust(35),":",objects.ConfiguredCapacity.value())
        print("AllowedVLANs".ljust(35),":",objects.AllowedVLANs.value())
        print("ConfigurationID".ljust(35),":",objects.ConfigurationID.value())
        print("PortVLANID".ljust(35),":",objects.PortVLANID.value())
