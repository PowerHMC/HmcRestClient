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

import requests
from src.utility import HmcHeaders
import warnings

class HTTPClient:
        
        def __init__(self, service, ip, root, content_type, session_id=None):
            """
            Initializes the default values to the arguments

            Args:
             service : To specify the type of service(web/uom/pcm)
             ip : ip address of the hmc
             root : root element in the url
             content_type : specifies the content type of the request
             session_id : id for the current X_API_Session
             
            """
             
            self.payload = None
            self.response_b = None
            self.response = None
            HmcHeaders_obj = HmcHeaders.HmcHeaders(service, ip, root,
                                                      session_id)
            global global_HmcHeaders
            global_HmcHeaders = HmcHeaders_obj
            self.head = global_HmcHeaders.getHeader(service, session_id,
                                                     content_type)
            
        def verify_response(self, response):
            """ This function verifies the status code of the request made """

            if response.status_code == 200:
                self.response_b = True
            else:
                self.response_b = False
                
        def HTTPGet(self, **kwargs):
            """ This function performs the HTTP get request """              

            global global_HmcHeaders
            url = global_HmcHeaders.url
            if any(kwargs):
                if not "url" in kwargs:
                    l_kwargs = list(kwargs.keys())
                    url = global_HmcHeaders.url+"/"+kwargs[l_kwargs[0]]
                    
                else:
                    url = kwargs["url"]
            self.response = requests.get(url, headers=self.head,
                                         verify=False)
            # call the verify function to check with the response status
            self.verify_response(self.response)
            
        def HTTPPut(self, payload, **kwargs):
            """ This function performs the HTTP put request """

            self.payload = payload
            global global_HmcHeaders
            url = global_HmcHeaders.url
            if any(kwargs):
                if not "url" in kwargs:
                    l_kwargs = list(kwargs.keys())
                    url = global_HmcHeaders.url+"/"+kwargs[l_kwargs[0]]
                else:
                    url = kwargs["url"]
            self.response = requests.put(url, headers=self.head,
                                         data=self.payload, verify=False)
            # call the verify function to check with the response status
            self.verify_response(self.response)
            
        def HTTPPost(self, payload, **kwargs):
            """ This function performs the HTTP post request """
            
            self.payload = payload
            global global_HmcHeaders
            url = global_HmcHeaders.url
            if any(kwargs):
                if not "url" in kwargs:
                    l_kwargs = list(kwargs.keys())
                    url = global_HmcHeaders.url+"/"+kwargs[l_kwargs[0]]
                else:
                    url = kwargs["url"]
            self.response = requests.post(url, headers=self.head,
                                          data=self.payload, verify=False)
            # call the verify function to check with the response status
            self.verify_response(self.response)

        def HTTPDelete(self, **kwargs):
            """ This function performs the HTTP delete request """
            
            global global_HmcHeaders
            url = global_HmcHeaders.url
            if any(kwargs):
                if not "url" in kwargs:
                    l_kwargs = list(kwargs.keys())
                    url = global_HmcHeaders.url+"/"+kwargs[l_kwargs[0]]
                else:
                    url = kwargs["url"]
            self.response = requests.delete(url, headers=self.head,
                                          verify=False)
            # call the verify function to check with the response status
            if self.response.status_code == 204:
                self.response_b = True
            else:
                self.response_b = False
                
        
        

