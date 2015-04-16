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


from src.common.JobStatus import *
from src.utility import HTTPClient,HMCClientLogger
import os

ROOT = "LogicalPartition"
CONTENT_TYPE = "application/vnd.ibm.powervm.web+xml; type=JobRequest"

class ClearSRIOVLogicalPortStatistics(JobStatus):
    
    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE

    def clear_sriov_logicalport_statistics(self, ip, logicalpartition_uuid, sriov_logicalport_uuid, x_api_session):
        """
        clear the statistical data stored for the selected SRIOV LogicalPort
        Args:
           ip : ip address of HMC
           logicalparrtition_uuid : UUID of Logical Partition in which
                                    SRIOV Logical Port statistics are to be cleared
           sriov_logicalport_uuid : UUID of SRIOV ethernet Logical Port for which statistics to be cleared
           x_api_session : session to be used
        """
        super().__init__(ip, self.root, self.content_type, x_api_session)
        directory = os.path.dirname(__file__)
        xml = open(directory+"/data/clearstatistics.xml").read()
        http_object = HTTPClient.HTTPClient("uom", ip,
                                            self.root, self.content_type,
                                            x_api_session)
        url_append = logicalpartition_uuid+"/SRIOVEthernetLogicalPort/"+sriov_logicalport_uuid+"/do/ClearStatistics"
        http_object.HTTPPut(xml, append = url_append)
        if http_object.response_b:
            self.get_job_status(http_object)
