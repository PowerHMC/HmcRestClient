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
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=Cluster"

class ListCluster:
    """
    List the details of the cluster
    """
    def __init__(self):
        """
        assign the root and content_type for request
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def list_cluster(self, ip, x_api_session):
        """
        returns the List of available Cluster objects
        Args:
           ip : ip address of HMC
           x_api_session : session to be used
        """
        log.log_debug("cluster object list is started")
        list_object = ListModule.ListModule()
        object_list = list_object.listing("uom", ip,
                            self.root, self.content_type,
                            "Cluster", x_api_session)
        log.log_debug("cluster object list is returned")
        return object_list
    
    def print_cluster_attributes(self, objects):
        """
        print the details of the given cluster object
        """
        print("\n")
        print("ClusterName".ljust(35),":",objects.ClusterName.value())
        print("Repository Disk".ljust(35),":", \
              objects.RepositoryDisk.PhysicalVolume[0].VolumeName.value())
        print("\nNodes in the cluster :\n-----------------------")
        for Node in objects.Node.Node :
            print("HostName".ljust(35),":",\
                  Node.HostName.value())
            print("PartitionID".ljust(35),":", \
                  Node.PartitionID.value())
            print()
