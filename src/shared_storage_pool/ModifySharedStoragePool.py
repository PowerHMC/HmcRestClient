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
from src.generated_src import UOM
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "SharedStoragePool"
CONTENT_TYPE = "application/atom+xml, application/vnd.ibm.powervm.uom+xml;type=SharedStoragePool"

class ModifySharedStoragePool:
    """
    Modifies the selected SSP by adding a Physical Volume to it
    """
    
    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def add_physicalvolume(self, ip, x_api_session, ssp_object, physicalvolume_object):
        """
        adds a physical volume to the selected ssp
        Args:
            ip:ip address of hmc
            x_api_session:session to be used
            ssp_object:shared storage pool object to be modified
            physicalvolume_object:physical volume object to be added to shared storage pool
        """
        log.log_debug("add physical volume to ssp invoked")
        ssp_uuid = ssp_object.Metadata.Atom.AtomID.value()
        ssp_object.PhysicalVolumes.PhysicalVolume.append(physicalvolume_object)
        xml = ssp_object.toxml()
        http_object = HTTPClient.HTTPClient("uom", ip,
                                            self.root, self.content_type,
                                            x_api_session)
        http_object.HTTPPost(xml, append = ssp_uuid)
        log.log_debug("response of adding a physical volume to ssp -- %s"%(http_object.response))
        if http_object.response_b:
            print("\nPhysicalVolume added to the SharedStoragePool Successfully")
            log.log_debug("PhysicalVolume added to the SharedStoragePool Successfully")
        else :
            log.log_error("\nVerify whether the physical volume tried to add is free.")
    
