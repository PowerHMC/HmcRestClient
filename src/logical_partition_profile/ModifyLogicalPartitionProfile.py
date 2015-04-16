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
from src.common import ListModule
from src.generated_src import UOM
import pyxb
import xml.etree.ElementTree as etree
log_object = HMCClientLogger.HMCClientLogger(__name__)

CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=LogicalPartitionProfile"

class ModifyLogicalPartitionProfile:
    """
    class provides definitions for Modifying LogicalPartitionProfile
    """
    
    def __init__(self,root):
        """
        initializes the content-type and root
        """
        
        self.content_type = CONTENT_TYPE
        self.root = root
        self.headers_obj = HmcHeaders.HmcHeaders("uom")
        
    def modify_LogicalPartitionProfile(self, ip, logicalpartition_uuid, logicalpartitionprofile_object, session_id):
            """
            Modifies the Memory attributes of provided logicalpartitionprofile object
            Args:
               ip : IP address of HMC
               logicalpartition_uuid : the Logical partition uuid under which the profile to be modified
               logicalpartitionprofile_object : the Logical partition profile uuid which is to be modified
               session_id : session to be used
            """
            log_object.log_debug("LPAR profile modification started")
            logicalpartitionprofile_object.ProfileMemory.DesiredMemory = 512
            logicalpartitionprofile_object.ProfileMemory.MaximumMemory = 512
            logicalpartitionprofile_object.ProfileMemory.MinimumMemory = 512
            inputpayload = logicalpartitionprofile_object.toxml("utf-8")
            profileuuid = str(logicalpartitionprofile_object.Metadata.Atom.AtomID.value())
            request_object = HTTPClient.HTTPClient("uom",ip,self.root,self.content_type,session_id)
            request_object.HTTPPost(payload=inputpayload,append=str(logicalpartition_uuid)+"/LogicalPartitionProfile/%s" \
                                                                    %(profileuuid))
            log_object.log_debug("response of profile modification --- %s"%(request_object.response))
            if request_object.response_b:
                log_object.log_debug("partitions are updated successfully")
                return True
            else:
                return False
