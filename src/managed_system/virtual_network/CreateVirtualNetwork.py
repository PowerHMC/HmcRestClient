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
from src.utility import HTTPClient, HmcHeaders, HMCClientLogger
import pyxb
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "ManagedSystem"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=VirtualNetwork"
SCHEMA_VER = "V1_3_0"
NETWORK_VLAN_ID = 7
TAGGED_NETWORK = "false"

class CreateVirtualNetwork:
    
    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def create_virtualnetwork(self, ip, managedsystem_uuid, x_api_session, virtualswitch_object):
        """
        create a virtual network in a given managed system
        Args:
            ip:ip address of hmc
            managedsystem_uuid:UUID of managedsystem
            x_api_session:session to be used
            virtualswitch_object:Virtual switch object to be used for virtual network
        Returns:
            boolean value
        """
        log.log_debug("virtual network creation started")
        pyxb.RequireValidWhenGenerating(True)
        virtual_network_object = UOM.VirtualNetwork()
        virtual_network_object.schemaVersion = SCHEMA_VER
        virtual_network_object.AssociatedSwitch = pyxb.BIND()
        virtual_network_object.AssociatedSwitch.href = "https://%s:12443/rest/api/uom/ManagedSystem/%s/VirtualSwitch/%s"\
                                                       %(ip,managedsystem_uuid,virtualswitch_object.Metadata.Atom.AtomID.value())
        virtual_network_object.AssociatedSwitch.rel = "related"
        virtual_network_object.NetworkVLANID = NETWORK_VLAN_ID 
        virtual_network_object.NetworkName = "VLAN%s-%s"%(virtual_network_object.NetworkVLANID.value(),virtualswitch_object.SwitchName.value())
        virtual_network_object.VswitchID = virtualswitch_object.SwitchID.value()
        virtual_network_object.TaggedNetwork = TAGGED_NETWORK
        xml = virtual_network_object.toxml()
        http_object = HTTPClient.HTTPClient("uom",ip,self.root,self.content_type,x_api_session)
        http_object.HTTPPut(xml,append=managedsystem_uuid+"/VirtualNetwork")
        log.log_debug("virtualnetwork creation response -- %s"%(http_object.response))
        if http_object.response_b:
            return True
        else :
            return False
            
