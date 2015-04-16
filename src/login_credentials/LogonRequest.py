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

from src.utility import HTTPClient,HMCClientLogger,HmcHeaders
import getpass
import xml.etree.ElementTree as etree
log = HMCClientLogger.HMCClientLogger(__name__)

def get_x_api_session(content):
    """
    GET_X_API_SESSION FUNCTION TAKES LOGON RESPONSE AS INPUT
    AND RETURNS THE SESSION_ID
    """
    response_root = etree.fromstring(content)
    HmcHeaders_obj = HmcHeaders.HmcHeaders('web')
    session_id = response_root.findall(".//xmlns:X-API-Session",namespaces=HmcHeaders_obj.ns)
    return session_id[0].text

class Logon(object):    
    """
    performs login into hmc taking valid credentials as input
    """
    
    def LogonRequest(self):
        """
        performs login and returns x-api-session id and
        ip address of the system
        """
        while True:
            ip = input("Enter IP address of HMC: ")
            username = input("Enter username for HMC: ")
            password = getpass.getpass("Enter password for HMC: ")
            self.root = 'Logon'
            #PAYLOAD DATA FOR LOGON REQUEST.
            self.logonrequest_payload = """
                               <LogonRequest
                                schemaVersion="V1_0"
                                xmlns="http://www.ibm.com/xmlns/systems/power/firmware/web/mc/2012_10/"
                                xmlns:mc="http://www.ibm.com/xmlns/systems/power/firmware/web/mc/2012_10/">
                               <UserID>%s</UserID>
                               <Password>%s</Password>
                               </LogonRequest>""" % (username, password)
            self.service = 'web'
            self.content_type="application/vnd.ibm.powervm.web+xml"
            try:
                request_object = HTTPClient.HTTPClient(self.service, ip,
                                                      self.root, self.content_type)
                #CALLS HTTPPUT METHOD TO PERFORM LOGON WITH LOGONREQUEST AS CONTENT_TYPE
                request_object.HTTPPut(self.logonrequest_payload)
                if  not request_object.response_b :
                #RESPONSE MESSAGE FOR INVALID CREDENTIALS AND ASKS CLIENT TO ENTER AGAIN
                    print("\nEnter correct Credentials\n")
                    log.log_debug("Enter correct Credentials")
                else:
                    x_api_session = get_x_api_session((request_object.response).content)
                    log.log_debug("Logon successful")
                    return (ip,x_api_session)
            except Exception:
                    print("\nInvalid IP Address or Connection Error\n")
                    log.log_debug("Invalid IP Address or Connection Error")
                    
        
    

    
