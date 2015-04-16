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
log = HMCClientLogger.HMCClientLogger(__name__)
from src.common.JobStatus import *

ROOT = 'ManagedSystem'
CONTENT_TYPE ='application/vnd.ibm.powervm.web+xml; type=JobRequest'

class PowerOffManagedSystem(JobStatus):
    """
    Power OFF the Selected ManagedSystem if they are in not operating state else
    shows error
    """
    
    def __init__(self):
        """
        initializes root and content-type
        """
        self.content_type = CONTENT_TYPE
        self.root = ROOT

    def poweroff_ManagedSystem(self, ip, managedsystem_uuid, x_api_session):
        """
        Args:
            ip:ip address of hmc
            managedsystem_uuid:UUID of managedsystem
            x_api_session:session to be used
        """
        super().__init__(ip, self.root, self.content_type, x_api_session)
        log.log_debug("power off managed system started")
        headers_object=HmcHeaders.HmcHeaders("web")
        namespace=headers_object.ns["xmlns"]
        directory = os.path.dirname(__file__)
        inputpayload=open(directory+"\data\poweroff_mangedsystem.xml","r")
        request_object=HTTPClient.HTTPClient('uom',ip,self.root,self.content_type,session_id=x_api_session)
        request_object.HTTPPut(payload=inputpayload,append=str(managedsystem_uuid)+"/do/PowerOff")
        log.log_debug(request_object.response)
        if request_object.response_b:
            self.get_job_status(request_object)
              
    
