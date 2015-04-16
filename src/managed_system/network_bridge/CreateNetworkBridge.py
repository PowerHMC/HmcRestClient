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

from src.generated_src import UOM
from src.utility import HTTPClient,HmcHeaders,HMCClientLogger
import xml.etree.ElementTree as etree
import pyxb
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "ManagedSystem"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml;type=NetworkBridge"
SCHEMA_VER = "V1_3_0"
FAILOVER_ENABLED = "false"
LOADBALANCING_ENABLED = "false"
LOADGROUP_PORT_VLAN_ID = 2
BACKINGDEVICE_ADAPTER_ID = 1
BACKINGDEVICE_NAME = "ent1"
SEA_PORT_VLAN_ID = 2
SEA_IS_PRIMARY = "true"
NETWORK_BRIDGE_PVLANID = 2

class CreateNetworkBridge:
    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        self.headers_obj = HmcHeaders.HmcHeaders("uom")

    def create_network_bridge(self, ip, managedsystem_uuid, session_id, vios_uuid, virtual_network_uuid):
        """
        creates a network bridge in a given managed system.
        Args:
            ip:ip address of hmc
            managedsystem_uuid:UUID of managed system
            session_id:session to be used
            vios_uuid:UUID of vios to create trunk and shared ethernet adapter
            virtual_network_uuid:UUID of virtual network on which network bridge is to be created
        """
        log.log_debug("creation of network bridge started")
        link = "https://%s:12443/rest/api/uom/ManagedSystem/%s/%s"
        vios_link=link%(ip,managedsystem_uuid,"VirtualIOServer/"+vios_uuid)
        virtual_network_link=link%(ip,managedsystem_uuid,"VirtualNetwork/"+virtual_network_uuid)
        ns = self.headers_obj.ns
        pyxb.RequireValidWhenGenerating(True)
        network_bridge_object = UOM.NetworkBridge()
        network_bridge_object.schemaVersion = SCHEMA_VER
        network_bridge_object.FailoverEnabled = FAILOVER_ENABLED
        network_bridge_object.LoadBalancingEnabled = LOADBALANCING_ENABLED
        network_bridge_object.LoadGroups = pyxb.BIND()
        virtual_network = UOM.VirtualNetwork_Links_Type()
        virtual_network.link.append(UOM.AtomLink_Type(rel="related",href=virtual_network_link))

        load_groups_obj = UOM.LoadGroup()
        load_groups_obj.PortVLANID = LOADGROUP_PORT_VLAN_ID
        load_groups_obj.schemaVersion = SCHEMA_VER
        load_groups_obj.VirtualNetworks=pyxb.BIND()
        load_groups_obj.VirtualNetworks.link = virtual_network.link
        network_bridge_object.LoadGroups = pyxb.BIND(load_groups_obj,schemaVersion = "V1_3_0")
        
        network_bridge_object.SharedEthernetAdapters = pyxb.BIND()
        sea_obj = UOM.SharedEthernetAdapter()
        sea_obj.schemaVersion = SCHEMA_VER
        sea_obj.AssignedVirtualIOServer = pyxb.BIND()
        sea_obj.AssignedVirtualIOServer.href = vios_link
        sea_obj.AssignedVirtualIOServer.rel = "related"
        sea_obj.BackingDeviceChoice = pyxb.BIND()
        sea_obj.BackingDeviceChoice.EthernetBackingDevice =  pyxb.BIND()
        sea_obj.BackingDeviceChoice.EthernetBackingDevice.schemaVersion = SCHEMA_VER
        sea_obj.BackingDeviceChoice.EthernetBackingDevice.AdapterID = BACKINGDEVICE_ADAPTER_ID
        sea_obj.BackingDeviceChoice.EthernetBackingDevice.DeviceName = BACKINGDEVICE_NAME
        sea_obj.PortVLANID = SEA_PORT_VLAN_ID
        sea_obj.IsPrimary = SEA_IS_PRIMARY
        network_bridge_object.SharedEthernetAdapters = pyxb.BIND(sea_obj,schemaVersion = "V1_3_0")

        network_bridge_object.PortVLANID = NETWOR_BRIDGE_PVLANID
        network_bridge_object.VirtualNetworks = pyxb.BIND()
        virtual_network = UOM.VirtualNetwork_Links_Type()
        virtual_network.link.append(UOM.AtomLink_Type(rel="related",href=virtual_network_link))
        network_bridge_object.VirtualNetworks.link = virtual_network.link

        xmlobject = network_bridge_object.toDOM()
        xmlobject.documentElement.setAttribute("xmlns",ns["xmlns"])
        xmlpayload = xmlobject.toxml("utf-8")
        request_obj = HTTPClient.HTTPClient("uom",ip,self.root,self.content_type,session_id)
        request_obj.HTTPPut(xmlpayload,append=str(managedsystem_uuid)+"/NetworkBridge")
        log.log_debug("response of network bridge creation -- %s"%(request_obj.response))
        if request_obj.response_b:
            root = etree.fromstring(request_obj.response.content)
            entry = root.findall(".//NetworkBridge:NetworkBridge",
                                     namespaces={"NetworkBridge": ns["xmlns"]})
            xmlstring = etree.tostring(entry[0])
            xml_object = UOM.CreateFromDocument(xmlstring)
            return xml_object
        
        

