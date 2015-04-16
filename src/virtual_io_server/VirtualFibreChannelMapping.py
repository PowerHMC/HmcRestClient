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

ROOT = "VirtualIOServer"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=VirtualIOServer"
SCHEMA_VER = "V1_3_0"
FIBRE_CHANNEL_PORT_NAME = "fcs0"

class VirtualFibreChannelMapping:
    
    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def create_virtualfibrechannel_mapping(self, ip, managedsystem_uuid, x_api_session, vios_object, lpar_id):
        """
        creates a virtual fibre mapping between given vios object and lpar
        Args:
            ip:ip address of hmc
            managedsystem_uuid:UUID of VirtualIOServer
            x_api_session:session to be used
            vios_object:vios object in which mapping is created
            lpar_id:UUID of logical partition to which mapping is created
        """
        log.log_debug("creation of fc mapping started")
        pyxb.RequireValidWhenGenerating(True)
        lpar_link = "https://"+ip+":12443/rest/api/uom/ManagedSystem/"+managedsystem_uuid+"/LogicalPartition/"+lpar_id
        virtualfibrechannel_mapping_object = UOM.VirtualFibreChannelMapping() 
        virtualfibrechannel_mapping_object.AssociatedLogicalPartition = pyxb.BIND()
        virtualfibrechannel_mapping_object.AssociatedLogicalPartition.href = lpar_link
        virtualfibrechannel_mapping_object.AssociatedLogicalPartition.rel = "related"
        virtualfibrechannel_mapping_object.Port = pyxb.BIND()
        virtualfibrechannel_mapping_object.Port.PortName = FIBRE_CHANNEL_PORT_NAME
        virtualfibrechannel_mapping_object.Port.schemaVersion = SCHEMA_VER
        virtualfibrechannel_mapping_object.schemaVersion = SCHEMA_VER
        vios_object.VirtualFibreChannelMappings.append(virtualfibrechannel_mapping_object)
        xml = vios_object.toxml()
        http_object = HTTPClient.HTTPClient("uom", ip, self.root,
                                            self.content_type, x_api_session)
        http_object.HTTPPost(xml,append=vios_object.Metadata.Atom.AtomID.value())
        log.log_debug("response of fc mapping creation -- %s"%(http_object.response))
        if http_object.response_b:
            print("\nVirtual FibreChannel Mapping created successfully")
        else:
            log.log_error("\nError in creation of FibreChannelMapping.Verify the attribute values")
