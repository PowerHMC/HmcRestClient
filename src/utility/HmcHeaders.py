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

class HmcHeaders:

    """ Contains Headers used in HMC"""
    
    
    def __init__(self,service=None,ip=None,root=None,session_id=None):
        """ Initializes url,namespaces """
        
        self.url="https://%s:12443/rest/api/%s/%s"%(ip,service,root)
        self.ns={'xmlns':'http://www.ibm.com/xmlns/systems/power/firmware/%s/mc/2012_10/'%(service)}
        self.feed_ns={'atom':'http://www.w3.org/2005/Atom'}
        
    def getHeader(self,service,session_id,content_type):
        header={"Content-Type":"%s"%(content_type),"X-API-Session":session_id} 
        return header
                                                                                                                   
    
