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

from src.generated_src import UOM
from src.utility import HTTPClient,HMCClientLogger
import pyxb
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "ManagedSystem"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=VirtualSwitch"
SCHEMA_VER = "V1_3_0"
SWITCH_NAME = "ethernet-switch"

class CreateVirtualSwitch:
    
    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE

    def create_virtualswitch(self, ip, managedsystem_uuid, x_api_session):
        """
        Args:
            ip:ip address of hmc
            managedsystem_uuid:UUID of managedsystem
            x_api_session:session to be used
        """
        log.log_debug("creation of virtual switch started")
        pyxb.RequireValidWhenGenerating(True)
        virtualswitch_object = UOM.VirtualSwitch()
        virtualswitch_object.schemaVersion = SCHEMA_VER
        virtualswitch_object.SwitchName = SWITCH_NAME
        xml = virtualswitch_object.toxml()
        http_object = HTTPClient.HTTPClient("uom",ip,self.root,self.content_type,x_api_session)
        http_object.HTTPPut(xml,append=managedsystem_uuid+"/VirtualSwitch")
        log.log_debug("response for creation of virtual switch -- %s"%(http_object.response))
        if http_object.response_b:
            return True
        else:
            return False
