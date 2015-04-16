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


from src.utility import HMCClientLogger, HmcHeaders, HTTPClient
from src.common import ListModule
from src.generated_src import UOM
import xml.etree.ElementTree as etree
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "ManagedSystem"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml;type=ManagedSystem"

class ListSRIOVPhysicalPort:

    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE

    def list_sriov_physicalport(self, ip, managedsystem_uuid, x_api_session):
        """
        returns the list of SRIOV Ethernet Physical Port Availble in the system
        Args:
            ip : ip address of HMC
            managedsystem_uuid : UUID of ManagedSystem from which SRIOV physical Ports are listed
            x_api_session : session to be used
        """
        object_list = []  
        header_object = HmcHeaders.HmcHeaders("uom")
        ns = header_object.ns["xmlns"]
        http_object = HTTPClient.HTTPClient("uom", ip, self.root, self.content_type,x_api_session)
        http_object.HTTPGet(append=managedsystem_uuid)
        log.log_debug("List of SRIOV Ethernet Physical Port is returned")
        if http_object.response_b:
            root = etree.fromstring(http_object.response.text)
            entries = root.findall(".//{%s}SRIOVEthernetPhysicalPort"%(ns))
            for entry in entries:
                xmlstring = etree.tostring(entry)
                xml_object = UOM.CreateFromDocument(xmlstring)
                object_list.append(xml_object)
        return object_list

    def print_sriov_physicalport(self, objects):
        print("\n")
        print("MaximumDiagnosticsLogicalPorts".ljust(35),":",objects.MaximumDiagnosticsLogicalPorts.value())
        print("MaximumPromiscuousLogicalPorts".ljust(35),":",objects.MaximumPromiscuousLogicalPorts.value())
        print("PhysicalPortID".ljust(35),":",objects.PhysicalPortID.value())
        print("PortType".ljust(35),":",objects.PortType.value())
        print("PortLogicalPortLimit".ljust(35),":",objects.PortLogicalPortLimit.value())
        print("AllocatedCapacity".ljust(35),":",objects.AllocatedCapacity.value())
        print("ConfiguredMaxEthernetLogicalPorts".ljust(35),":",objects.ConfiguredMaxEthernetLogicalPorts.value())
        print("ConfiguredEthernetLogicalPorts".ljust(35),":",objects.ConfiguredEthernetLogicalPorts.value())
