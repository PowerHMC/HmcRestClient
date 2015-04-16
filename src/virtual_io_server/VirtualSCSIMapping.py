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
PHYSICALVOLUME_NAME = "hdisk11"

class VirtualSCSIMapping:
    
    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def create_vscsi_mapping(self, ip, managedsystem_uuid, x_api_session, virtualioserver_object, logicalPartition_id):
        """
        Creates a Virtual SCSI mapping between seleced vios and lpar
        Args:
            ip:ip address of hmc
            managedsystem_uuid:UUID of VirtualIOServer
            x_api_session:session to be used
            virtualioserver_object:vios object in which mapping is created
            logicalPartition_id:UUID of logical partition to which mapping is created
        """
        log.log_debug("create vscsi mapping started")
        logicalpartition_link = "http://"+ip+":12443/rest/api/uom/ManagedSystem/"+managedsystem_uuid+"/LogicalPartition/"+logicalPartition_id
        pyxb.RequireValidWhenGenerating(True)
        vscsi_mapping_object = UOM.VirtualSCSIMapping()
        vscsi_mapping_object.Storage = pyxb.BIND()
        vscsi_mapping_object.Storage.PhysicalVolume = pyxb.BIND()
        vscsi_mapping_object.Storage.PhysicalVolume.schemaVersion = SCHEMA_VER
        vscsi_mapping_object.Storage.PhysicalVolume.VolumeName = PHYSICALVOLUME_NAME
        vscsi_mapping_object.schemaVersion = SCHEMA_VER
        vscsi_mapping_object.AssociatedLogicalPartition = pyxb.BIND()
        vscsi_mapping_object.AssociatedLogicalPartition.href = logicalpartition_link
        vscsi_mapping_object.AssociatedLogicalPartition.rel = "related"
        virtualioserver_object.VirtualSCSIMappings.VirtualSCSIMapping.append(vscsi_mapping_object)
        virtualioserver_id = virtualioserver_object.Metadata.Atom.AtomID.value()
        xml = virtualioserver_object.toxml()
        http_object = HTTPClient.HTTPClient("uom", ip, self.root, self.content_type, x_api_session)
        http_object.HTTPPost(xml,append=virtualioserver_id)
        log.log_debug("response of scsi mapping creation -- %s"%(http_object.response))
        if http_object.response_b:
            print("VSCSIMapping Created Successfully")
        else :
            log.log_error("Error in VSCSIMapping.Verify the attribute values")
