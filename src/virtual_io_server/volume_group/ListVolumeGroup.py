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


from src.common import ListModule
from src.utility import HMCClientLogger
import xml.etree.ElementTree as etree
log = HMCClientLogger.HMCClientLogger(__file__)

ROOT = "VirtualIOServer"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=VolumeGroup"


class ListVolumeGroup:
    
    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def list_volumegroup(self, ip, virtualioserver_id, x_api_session):
        """
        returns a list of volume group objects available in the given virtualioserver
        Args:
            ip : ip address of HMC
            virtualioserver_id : UUID of VirtualIOServer on which VolumeGroups are to be listed
            x_api_session : session to be used
        """
        log.log_debug("List of Volume Group started")
        list_object = ListModule.ListModule()
        volumegroup_list = list_object.listing("uom" ,ip,
                                               self.root, self.content_type,
                                               "VolumeGroup", x_api_session,
                                               virtualioserver_id)
        log.log_debug("List of Volume Group returned")
        return volumegroup_list
    
    def print_volumegroup_attributes(self, volumegroup_object):
        """
        prints the details of the given volume group object
        """
        print("\n")
        print("VolumeGroup Name".ljust(35),":",volumegroup_object.GroupName.value())
        print("\nPHYSICAL VOLUMES : \n--------------------")
        for physicalvolume in volumegroup_object.PhysicalVolumes.PhysicalVolume:
            print("PhysicalVolume Name".ljust(35),":",physicalvolume.VolumeName.value())
            print("PhysicalVolume Capacity".ljust(35),":",physicalvolume.VolumeCapacity.value())
            print("\n")
        if volumegroup_object.VirtualDisks.VirtualDisk != []:
            print("\nVIRTUAL DISKS :\n-----------------")
        for virtualdisk in volumegroup_object.VirtualDisks.VirtualDisk:
            print("DiskName".ljust(35),":",virtualdisk.DiskName.value())
            print("DiskCapacity".ljust(35),":",virtualdisk.DiskCapacity.value())
            print("\n")
            
