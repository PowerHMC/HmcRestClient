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


from src.utility import HTTPClient,HmcHeaders, HMCClientLogger
import xml.etree.ElementTree as etree
log = HMCClientLogger.HMCClientLogger(__name__)

class JobStatus(object):
    """
    verfiies whether the job request is completetd successfully
    """
    
    def __init__(self, ip, root, content_type, session):
        header_object = HmcHeaders.HmcHeaders("web")
        self.ns = header_object.ns["xmlns"]
        self.root = root
        self.ip = ip
        self.content_type = content_type
        self.session =session
        
    def get_job_status(self, http_object):
            """
            performs the get of job status and verifies whether
            the job request is completetd successfully
            Args:
              http_object : HTTP Request object of a job request
            """
            

            root = etree.fromstring(http_object.response.content)
            job_id = root.findall(".//{%s}JobID"%(self.ns))[0].text
            http_job_object = HTTPClient.HTTPClient("uom", self.ip,
                                                "jobs", self.content_type,
                                                self.session )
            job_status = " "
            print("Processing...")
            while job_status != "COMPLETED_OK":
                http_job_object.HTTPGet(append=job_id)
                if http_job_object.response_b:
                    root = etree.fromstring(http_job_object.response.content)
                    job_status = root.findall(".//{%s}Status"%(self.ns))[0].text
                    if job_status == "FAILED_BEFORE_COMPLETION" or job_status == "COMPLETED_WITH_ERROR":
                        try:
                            error = root.findall(".//{%s}Message"%(self.ns))[0].text
                            log.log_error(error)
                        except IndexError:
                            log.log_error("An error occured while performing job request")
                        break
            print("Job Status :",job_status)
