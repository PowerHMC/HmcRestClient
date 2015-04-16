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
from src.utility import HTTPClient, HMCClientLogger
import pyxb
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "VirtualIOServer"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=VolumeGroup"
SCHEMA_VER = "V1_3_0"
VOLUMEGROUP_NAME = "vg_1"
PHYSICALVOLUME_NAME = "hdisk10"

class CreateVolumeGroup:
    """
    Creates a VolumeGroup with one physical Volume
    """
    
    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def create_volumegroup(self, ip, virtualioserver_uuid, x_api_session):
        """
        Args:
            ip:ip address of hmc
            virtualioserver_uuid:UUID of VirtualIOServer
            x_api_session:session to be used
        """
        log.log_debug("create volume group started")
        pyxb.RequireValidWhenGenerating(True)
        volumegroup_object = UOM.VolumeGroup()
        volumegroup_object.schemaVersion = SCHEMA_VER
        volumegroup_object.GroupName = VOLUMEGROUP_NAME
        physicalvolume_object = UOM.PhysicalVolume()
        physicalvolume_object.VolumeName = PHYSICALVOLUME_NAME
        physicalvolume_object.schemaVersion = SCHEMA_VER
        volumegroup_object.PhysicalVolumes = pyxb.BIND()
        volumegroup_object.PhysicalVolumes.schemaVersion = SCHEMA_VER
        volumegroup_object.PhysicalVolumes.append( physicalvolume_object)
        xml = volumegroup_object.toxml()
        http_object = HTTPClient.HTTPClient("uom", ip, self.root, self.content_type, x_api_session)
        http_object.HTTPPut(xml,append=virtualioserver_uuid+"/VolumeGroup")
        log.log_debug("response of volume group creation -- %s"%(http_object.response))
        if http_object.response_b:
            print("VolumeGroup Created Successfully")
            log.log_debug("VolumeGroup Created Successfully")
        else :
            log.log_error("Error in VolumeGroup creation.Verify the attribute values")
