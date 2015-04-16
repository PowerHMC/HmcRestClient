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

from src.utility import HTTPClient, HMCClientLogger
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "ManagedSystem"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=VirtualNetwork"

class ModifyVirtualNetwork:
    
    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def modify_virtualnetwork(self, ip, managedsystem_uuid, session_id, virtualnetwork_object):
        """
        Modifies the name of the selected Virtual Network
        Args:
            ip:ip address of hmc
            managedsystem_uuid:UUID of managedsystem
            x_api_session:session to be used
            virtualnetwork_object:virtual network object to be modified
        Returns:
            boolean value
        """
        log.log_debug("virtual network modification started")
        virtualnetwork_object.NetworkName = "VLAN%s-%s"%(virtualnetwork_object.NetworkVLANID.value(),virtualnetwork_object.VswitchID.value())
        virtualnetwork_id = virtualnetwork_object.Metadata.Atom.AtomID.value()
        xml = virtualnetwork_object.toxml()
        http_object = HTTPClient.HTTPClient("uom",ip,self.root,self.content_type,session_id)
        http_object.HTTPPost(xml,append=managedsystem_uuid+"/VirtualNetwork/"+virtualnetwork_id)
        log.log_debug("response of virtual network modification -- %s"%(http_object.response))
        if http_object.response_b:
            return True
        else:
            return False
