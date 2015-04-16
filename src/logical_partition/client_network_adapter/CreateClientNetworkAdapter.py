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
from src.utility import HTTPClient,HMCClientLogger
import pyxb
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "LogicalPartition"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; Type=ClientNetworkAdapter"
SCHEMA_VER = "V1_3_0"
PORT_VLAN_ID = 1

class CreateClientNetworkAdapter:
    """
    creates a client network adapter with next adapter id
    This will update the LPAR and put a new CNA on it.  If the LPAR is active
    can only perform and if there is an active RMC connection.  If the LPAR is
    powered off, then it will update it offline.
    """
    
    def __init__(self):
        """
        assign the root and content_type for request
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def create_clientnetwork_adapter(self, ip, logicalpartition_id, x_api_session):
        """
        Args:
           ip:ip address of the hmc
           logicalpartition_id:the uuid of the logical partition on which network adapter
           is to be created
           x_api_session:session used to create network adapter
        """
        log.log_debug("create client network adapter starting")
        pyxb.RequireValidWhenGenerating(True)
        clientnetwork_adapter_object = UOM.ClientNetworkAdapter()
        clientnetwork_adapter_object.PortVLANID = PORT_VLAN_ID
        clientnetwork_adapter_object.schemaVersion = SCHEMA_VER
        xml = clientnetwork_adapter_object.toxml()
        http_object = HTTPClient.HTTPClient("uom", ip, self.root, self.content_type, x_api_session)
        http_object.HTTPPut(xml,append= logicalpartition_id+"/ClientNetworkAdapter")
        log.log_debug("response of create client network adapter --- %s"%(http_object.response))
        if http_object.response_b:
            print("ClientNetworkAdapter Created successfully")
            log.log_debug("ClientNetworkAdapter Created successfully")
        else :
            log.log_error("Error in ClientNetworkAdapter Creation")
