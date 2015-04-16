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


from src.utility import HMCClientLogger,HTTPClient
from src.common.JobStatus import *
import os
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "ManagedSystem"
CONTENT_TYPE = "application/vnd.ibm.powervm.web+xml; type=JobRequest"

class ChangeSRIOVAdapterMode(JobStatus):

    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
        
    def change_sriov_adaptermode(self, ip, managedsystem_uuid, adapter_object, x_api_session):
        """
        Changes the adapter mode from shared to dedicated and dedicated to shared
        Args:
            ip : ip address of HMC
            managedsystem_uuid : UUID of the Managedsystem
            adapter_object : object of SRIOV Adapter to change the mode
            x_api_session : session to be used
        """
        super().__init__(ip, self.root, self.content_type, x_api_session)
        directory = os.path.dirname(__file__)
        adapter_id = adapter_object.AdapterID.value()
        if adapter_object.AdapterMode == "Dedicated":
            xml = open(directory+"/data/dedicated_to_shared_adaptermode.xml").read()
        else:
            xml = open(directory+"/data/shared_to_dedicated_adaptermode.xml").read()
        xml = xml%(adapter_id)
        http_object = HTTPClient.HTTPClient("uom", ip,
                                            self.root, self.content_type,
                                            x_api_session)
        http_object.HTTPPut(xml, append="/"+managedsystem_uuid+"/do/ModifySRIOVAdapterMode")
        if http_object.response_b:
            self.get_job_status(http_object)
