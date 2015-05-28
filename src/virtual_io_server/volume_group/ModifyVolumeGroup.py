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

from src.utility import HTTPClient
from src.generated_src import UOM
import pyxb

ROOT = "VirtualIOServer"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=VolumeGroup"
LOGICALVOLUME_NAME = "lv_1"
PHYSICALVOLUME_NAME = "hdisk7"
SCHEMA_VERSION = "V1_3_0"

def sendrequest(xml, ip, root, content_type, x_api_session, vios_uuid, volumegroup_id):
        """
        performs the HTTPPost request with modified volume group
        """
        http_object = HTTPClient.HTTPClient("uom", ip, root, content_type, x_api_session)
        http_object.HTTPPost(xml,append=vios_uuid+"/VolumeGroup/"+volumegroup_id)
        if http_object.response_b:
            return True
        else:
            return False

        
class ModifyVolumeGroup:
    
    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def add_physicalvolume(self, ip, vios_uuid, x_api_session, volumegroup_object):
            """ 
            adds a Physical volume to the selected volume group
            Args:
               ip:ip address of hmc
               vios_uuid:UUID of VirtualIOServer
               x_api_session:session to be used
               volumegroup_object:volume group object to be modified
            """
            pyxb.RequireValidWhenGenerating(True)
            physicalvolume_object = UOM.PhysicalVolume()

            physicalvolume_object.VolumeName = PHYSICALVOLUME_NAME
            physicalvolume_object.schemaVersion = SCHEMA_VERSION
            volumegroup_object.PhysicalVolumes.PhysicalVolume.append(physicalvolume_object)
            xml = volumegroup_object.toxml()
            volumegroup_id = volumegroup_object.Metadata.Atom.AtomID.value()
            response = sendrequest(xml, ip, self.root, self.content_type, x_api_session, vios_uuid, volumegroup_id)
            if response :
                    print("Physical volume added to volumegroup Successfully")
            else:
                    print("Adding Physical volume to volumegroup failed")
    def add_virtualdisk(self, ip, vios_uuid, x_api_session, volumegroup_object):
         """
         creates a virtualdisk in VolumeGroup
         Args:
            ip:ip address of hmc
            vios_uuid:UUID of VirtualIOServer
            x_api_session:session to be used
            volumegroup_object:volume group object to be modified
         """
         pyxb.RequireValidWhenGenerating(True)
         virtualdisk_object = UOM.VirtualDisk()
         virtualdisk_object.DiskName = LOGICALVOLUME_NAME 
         virtualdisk_object.schemaVersion = SCHEMA_VERSION
         virtualdisk_object.DiskCapacity = volumegroup_object.GroupCapacity.value()/2
         volumegroup_object.VirtualDisks.VirtualDisk.append(virtualdisk_object)
         xml = volumegroup_object.toxml()
         volumegroup_id = volumegroup_object.Metadata.Atom.AtomID.value()
         response = sendrequest(xml, ip, self.root, self.content_type, x_api_session, vios_uuid, volumegroup_id)
         if response :
            print("VirtualDisk Created in VolumeGroup Successfully")
         else:
            print("VirtualDisk Creation unsuccessfull")
