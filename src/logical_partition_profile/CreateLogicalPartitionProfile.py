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
from src.generated_src import UOM
import pyxb
import time
import xml.etree.ElementTree as etree
log_object = HMCClientLogger.HMCClientLogger(__name__)

CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=LogicalPartitionProfile"
PROFILE_NAME = "PROFILE-%s"
PROFILE_TYPE = "REG_LPAR_PROFILE_TYPE"
SCHEMA_VER = "V1_3_0"
MAX_MEMORY = 256
MIN_MEMORY = 256
DES_MEMORY = 256

class CreateLogicalPartitionProfile:
    """
    class provides definitions for LogicalPartitionProfile Creation
    """
    
    def __init__(self,root):
        """
        initializes the content-type and root
        """
        
        self.content_type = CONTENT_TYPE
        self.root = root
        self.headers_obj = HmcHeaders.HmcHeaders("uom")
        
    def create_LogicalPartitionProfile(self, ip, logicalpartition_object, session_id):
        """
        Assign values to the profile object and creates the profile to the given vios
        Args:
           ip : ip address of hmc
           logicalpartition_object : VIOS/Logical Partition object on which
                                     profile should be created
           session_id : session to be used
        """
        log_object.log_debug("creation of lpar profile started")
        ns = self.headers_obj.ns
        logicalpartitionprofile_object = UOM.LogicalPartitionProfile()
        pyxb.RequireValidWhenGenerating(True)
        logicalpartitionprofile_object.ProfileName = PROFILE_NAME%(time.strftime("%d%m%y-%X"))
        logicalpartitionprofile_object.ProfileType = PROFILE_TYPE
        logicalpartitionprofile_object.schemaVersion = SCHEMA_VER
        logicalpartitionprofile_object.ProfileMemory = pyxb.BIND()
        logicalpartitionprofile_object.ProfileMemory.schemaVersion = SCHEMA_VER
        logicalpartitionprofile_object.ProfileMemory.MaximumMemory = MAX_MEMORY
        logicalpartitionprofile_object.ProfileMemory.MinimumMemory = MIN_MEMORY
        logicalpartitionprofile_object.ProfileMemory.DesiredMemory = DES_MEMORY
        xmlobject = logicalpartitionprofile_object.toDOM()
        xmlobject.documentElement.setAttribute("xmlns",ns["xmlns"])
        xmlpayload = xmlobject.toxml("utf-8")
        HTTPClient_object = HTTPClient.HTTPClient("uom",ip,self.root,self.content_type,session_id)
        HTTPClient_object.HTTPPut(payload=xmlpayload,append=str(logicalpartition_object.PartitionUUID.value())+"/LogicalPartitionProfile")
        log_object.log_debug("response of profile creation -- %s"%(HTTPClient_object.response))
        if HTTPClient_object.response_b:
            root = etree.fromstring(HTTPClient_object.response.content)
            entry = root.findall(".//LogicalPartitionProfile:LogicalPartitionProfile",
                                     namespaces={"LogicalPartitionProfile": ns["xmlns"]})
            xmlstring = etree.tostring(entry[0])
            xml_object = UOM.CreateFromDocument(xmlstring)
            log_object.log_debug("created partition successfully")
            return xml_object
        else: 
            log_object.log_error("Error in Profile creation")
