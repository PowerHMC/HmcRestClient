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
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "Cluster"
CONTENT_TYPE = "application/atom+xml, application/vnd.ibm.powervm.uom+xml;type=SharedStoragePool"

class ListSharedStoragePool:
    """
    Lists the details of SharedStoragePool
    """
    
    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE

    def list_shared_storagepool(self, ip, cluster_id, x_api_session):
        """
        returns a  shared storage pool object of a given cluster
        Args:
           ip : ip address of HMC
           cluster_id : the UUID Of the Cluster to get ssp
           x_api_session : session to be used
        """
        log.log_debug("ssp object of a cluster is started")
        list_object = ListModule.ListModule()
        ssp_object_list = list_object.listing("uom", ip,
                                self.root, self.content_type,
                                "SharedStoragePool",
                                x_api_session, cluster_id)
        log.log_debug("ssp object of a cluster is returned")
        return ssp_object_list
    
    def print_shared_storagepool_attributes(self, objects):
        """
        prints the details of shared storage pool
        """
        print("SharedStoragePool :\n-------------------")
        print("StoragePoolName".ljust(35),":",objects.StoragePoolName.value())
        print("Capacity".ljust(35),":",objects.Capacity.value())
        print("FreeSpace".ljust(35),":",objects.FreeSpace.value())
        print("AlertThreshold".ljust(35),":",objects.AlertThreshold.value())
        print("\nPhysicalVolumes in SharedStoragePool  :\n----------------------------------------")
        for physicalvolume in objects.PhysicalVolumes.PhysicalVolume:
            print("".ljust(35),physicalvolume.VolumeName.value())
        self.print_logicalunit(objects)

    def print_logicalunit(self,objects):
        if objects.LogicalUnits.LogicalUnit != []:
            print("\nAvailable LogicalUnits :\n-----------------------")
            for logicalunit in objects.LogicalUnits.LogicalUnit:
                print("Name".ljust(35),":",logicalunit.UnitName.value())
                print("Capacity".ljust(35),":",logicalunit.UnitCapacity.value())
                print("UDID".ljust(35),":",logicalunit.UniqueDeviceID.value())
                print()
            return objects.LogicalUnits.LogicalUnit
        else :
            return None
