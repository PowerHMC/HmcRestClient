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

class LULinkedClone(JobStatus):
    """
    makes a clone of Logical unit
    """
    def __init__(self):
        """
        assign the root and content_type for request
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def lu_linked_clone(self, ip, cluster_id, x_api_session, source_udid, dest_udid):
        """
        Args:
           ip: ip address of hmc
           cluster_id: the UUID of the cluster in which the LU to be clonned
           x_api_session: the session used for cloning LU
           source_udid: source LUs Unique Device ID
           dest_udid: Destination LUs Unique Device ID
        """
        super().__init__(ip, self.root, self.content_type, x_api_session)
        log.log_debug("lu linked clone job is invoked")
        header_object = HmcHeaders.HmcHeaders("web")
        ns = header_object.ns["xmlns"]
        directory = os.path.dirname(__file__)
        xml = open(directory+"/data/LUlinked_clone.xml").read()
        xml = xml%(source_udid,dest_udid)
        http_object = HTTPClient.HTTPClient("uom", ip, self.root,
                                            self.content_type, x_api_session)
        http_object.HTTPPut(xml,append=cluster_id+"/do/LULinkedClone")
        log.log_debug("response of job request for lu linked clone ---- %s"%(http_object.response))
        if http_object.response_b:
           self.get_job_status(http_object)
