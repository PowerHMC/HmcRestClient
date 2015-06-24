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

from src.utility import HTTPClient, HmcHeaders, HMCClientLogger
from src.generated_src import UOM
import pyxb
import os
import time
import xml.etree.ElementTree as etree
from src.common.JobStatus import *
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "Cluster"
CONTENT_TYPE = "application/vnd.ibm.powervm.web+xml; type=JobRequest"
SCHEMA_VER = "V1_3_0"
CLUSTER_NAME = "Cluster-%s"
PHYSICAL_VOLUME_REPODISK = "hdisk4"
HOST_NAME = "falcon8vios1.blr.stglabs.ibm.com"
PHYSICAL_VOLUME_SSP1 = "hdisk5"
PHYSICAL_VOLUME_SSP2 = "hdisk6"
POOL_NAME ="pool_1"

class CreateCluster(JobStatus):
    """
    creates cluster with one node.The vios node to be added
    is given as input parameter
    """
    def __init__(self):
        """
        initializes the root and content_type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def create_cluster(self, ip, x_api_session, vios_id ):
        """
        xml for cluster and shared storage pool are created
        from python objects and are inserted in to job request
        input xml.
        Args:
            ip:ip address of hmc
            x_api_session:session used to create cluster
            vios_id:UUID of vios to be added to the cluster
        """
        super().__init__(ip, self.root, self.content_type, x_api_session)
        log.log_debug("Invoking create cluster")
        directory = os.path.dirname(__file__)+"/data/create_cluster.xml"
        xml = open(directory).read()
        link = "https://"+ip+":12443/rest/api/uom/VirtualIOServer/"+vios_id
        log.log_debug("Link of vios to be added to cluster %s"%(link))
        cluster_object = UOM.Cluster()
        cluster_object.ClusterName = CLUSTER_NAME%(time.strftime("%d%m%y-%X"))
        cluster_object.schemaVersion=SCHEMA_VER

        physicalvolume_object = UOM.PhysicalVolume()
        physicalvolume_object.VolumeName = PHYSICAL_VOLUME_REPODISK
        physicalvolume_object.schemaVersion = SCHEMA_VER
        cluster_object.RepositoryDisk = pyxb.BIND()
        cluster_object.RepositoryDisk.schemaVersion = SCHEMA_VER
        cluster_object.RepositoryDisk.PhysicalVolume.append(physicalvolume_object)
            
        cluster_object.Node = pyxb.BIND()
        node_object = UOM.Node()
        node_object.HostName = HOST_NAME
        node_object.VirtualIOServer = pyxb.BIND()
        node_object.VirtualIOServer.href = link
        node_object.VirtualIOServer.rel = "related"
        node_object.schemaVersion = SCHEMA_VER
        cluster_object.Node.schemaVersion = SCHEMA_VER
        cluster_object.Node.Node.append(node_object)
        cluster_xml = cluster_object.toxml()

        ssp_object = UOM.SharedStoragePool()
        ssp_object.schemaVersion = SCHEMA_VER
        physicalvolume_object.VolumeName = PHYSICAL_VOLUME_SSP1
        ssp_object.PhysicalVolumes = pyxb.BIND()
        ssp_object.PhysicalVolumes.schemaVersion = SCHEMA_VER
        ssp_object.PhysicalVolumes.PhysicalVolume.append(physicalvolume_object)
        physicalvolume_object.VolumeName = PHYSICAL_VOLUME_SSP2
        ssp_object.PhysicalVolumes.PhysicalVolume.append(physicalvolume_object)
        ssp_object.StoragePoolName = POOL_NAME
        sspxml = ssp_object.toxml()

        xml = xml%(cluster_xml,sspxml) 
        
        http_object = HTTPClient.HTTPClient("uom", ip,
                                            self.root, self.content_type,
                                            x_api_session)
        http_object.HTTPPut(xml,append="/do/create")
        log.log_debug("HTTP response for creating cluster -- %s"%(http_object.response))
        if http_object.response_b:
            self.get_job_status(http_object)
