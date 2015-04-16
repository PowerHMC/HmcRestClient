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

from src.utility import HTTPClient,HmcHeaders,HMCClientLogger
import xml.etree.ElementTree as etree
import os
from src.common.JobStatus import *
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "Cluster"
CONTENT_TYPE = "application/vnd.ibm.powervm.web+xml; type=JobRequest"


class DeleteCluster(JobStatus):
    """
    Deletes the given cluster object if no logical
    units are associated with it
    """
    def __init__(self):
        """
        assign the root and content_type for request
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def delete_cluster(self, ip, cluster_id, x_api_session):
        """
        Args:
            ip:represents the ip address
            cluster_id:UUID of the cluster to be deleted
            x_api_session:session to be used for request
        
        """
        super().__init__(ip, self.root, self.content_type, x_api_session)
        log.log_debug("Invoking delete cluster")
        header_object = HmcHeaders.HmcHeaders("web")
        ns = header_object.ns["xmlns"]
        directory = os.path.dirname(__file__)
        xml = open(directory+"/data/delete_cluster.xml").read()
        http_object = HTTPClient.HTTPClient("uom", ip, self.root, self.content_type, x_api_session)
        http_object.HTTPPut(xml,append=cluster_id+"/do/Delete")
        log.log_debug("HTTP response for deleting cluster -- %s"%(http_object.response))
        if http_object.response_b:
           self.get_job_status(http_object)
