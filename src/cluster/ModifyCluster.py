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

from src.utility import HTTPClient,HMCClientLogger
from src.generated_src import UOM
import pyxb
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "Cluster"
CONTENT_TYPE = "application/atom+xml, application/vnd.ibm.powervm.uom+xml;type=Cluster"
SCHEMA_VER = "V1_3_0"
NODE_HOST_NAME = ""

class ModifyCluster:
    """
    adds a vios node to the existing cluster
    """
    def __init__(self):
        """
        assign the root and content_type for request
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def add_node(self, ip, x_api_session, cluster_object, vios_id):
        """
        Args:
            ip: ip address of hmc
            x_api_session: session to be used for adding a node
            cluster_object:cluster object into which the node is to be added
            vios_id:UUID of the vios to be added
        """
        log.log_debug("adding a node to a cluster process starting")
        link = "https://"+ip+":12443/rest/api/uom/VirtualIOServer/"+vios_id
        log.log_debug("vios to be added to the cluster -- %s"%(link))
        node_object = UOM.Node()
        node_object.HostName = NODE_HOST_NAME
        node_object.VirtualIOServer = pyxb.BIND()
        node_object.VirtualIOServer.href = link
        node_object.VirtualIOServer.rel = "related"
        node_object.schemaVersion = SCHEMA_VER
        cluster_object.Node.schemaVersion = SCHEMA_VER
        cluster_object.Node.Node.append(node_object)
        cluster_xml = cluster_object.toxml()
        cluster_id = cluster_object.Metadata.Atom.AtomID.value()
        http_object = HTTPClient.HTTPClient("uom", ip,
                                            self.root, self.content_type,
                                            x_api_session)
        http_object.HTTPPost(cluster_xml, append = cluster_id)
        log.log_debug("response for adding a node to cluster --- %s"%(http_object.response))
        if http_object.response_b:
            print("Node is added to the cluster successfully")
            log.log_debug("node added successfully")
        else :
            log.log_error("Error occured while adding a node to the cluster")
    
        
