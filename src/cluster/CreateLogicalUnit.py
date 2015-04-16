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
import os
import xml.etree.ElementTree as etree
from src.common.JobStatus import *
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "Cluster"
CONTENT_TYPE = "application/vnd.ibm.powervm.web+xml; type=JobRequest"
UNIT_SIZE = 1
UNIT_NAME = "newLU"
UNIT_TYPE = "Thin"


class CreateLogicalUnit(JobStatus):
    """
    CreateLogicalUnit object is created in HmcRestClient.
    This class creates a Logical Unit of size 1GB and
    Logical Unit of type Thin
    """
    
    def __init__(self):
        """
        assign the root and content_type for request
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def create_logicalunit(self, ip, x_api_session, cluster_object):
        """
        Args:
            ip:represents the ip address
            x_api_session:session to be used for request
            cluster_object:Cluster object for which logical unit to be created
        """
        super().__init__(ip, self.root, self.content_type, x_api_session)
        log.log_debug("Invoking create logical unit")
        directory = os.path.dirname(__file__)
        xml = open(directory+"/data/create_logicalunit.xml").read()%(UNIT_NAME, UNIT_SIZE, UNIT_TYPE)
        cluster_id = cluster_object.Metadata.Atom.AtomID.value()
        http_object = HTTPClient.HTTPClient("uom", ip,
                                            self.root, self.content_type,
                                            x_api_session)
        http_object.HTTPPut(xml, append=cluster_id+"/do/CreateLogicalUnit")
        log.log_debug("Response of create logical unit -- %s"%(http_object.response))
        if http_object.response_b:
                  self.get_job_status(http_object)
            
