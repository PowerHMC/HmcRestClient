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

class logoff(object):
    
    """
    class logoff takes ip address and x-api-session as
    input and performs HTTP delete
    """
    
    def __init__(self, ip, x_api_session):
        self.service = 'web'
        self.root = 'Logon'
        self.content_type = 'application/vnd.ibm.powervm.web+xml'
        # PERFORMS HTTP DELETE METHOD USING CURRENT X_API_SESSION
        request_object = HTTPClient.HTTPClient(self.service, ip, self.root, 
                                              self.content_type, x_api_session)  
        request_object.HTTPDelete()
        # PRINTS THE STATUS MESSAGE FOR DELETE METHOD
        print("Logoff Successful!!!")
