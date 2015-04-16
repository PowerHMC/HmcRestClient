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
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "SharedStoragePool"
CONTENT_TYPE = "application/atom+xml,application/vnd.ibm.powervm.uom+xml;type=SharedStoragePool"

class DeleteLogicalUnit:
    """
    Deletes the Logical Unit from the shared storage pool.
    """
    def __init__(self):
        """
        assign the root and content_type for request
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def delete_logicalunit(self, ip, ssp_object, x_api_session, logicalunit_name ):
        """
        Args:
            ip:ip address of the hmc
            ssp_object:ssp object from which Logical unit is to
                       be deleted
            x_api_session:session to be used to delete Logical unit
            logicalunit_name:name of the Logical Unit to be deleted
        """
        log.log_debug("Invoking delete Logical Unit")
        ssp_id = ssp_object.Metadata.Atom.AtomID.value()
        log.log_debug("LU to be removed -- %s"%(logicalunit_name))
        for logicalunit in ssp_object.LogicalUnits.LogicalUnit:
            if logicalunit.UnitName.value() == logicalunit_name:
                ssp_object.LogicalUnits.LogicalUnit.remove(logicalunit)
                http_object = HTTPClient.HTTPClient("uom", ip, self.root, self.content_type, x_api_session)
                xml = ssp_object.toxml()
                http_object.HTTPPost(xml, append=ssp_id)
                log.log_debug("response status code for delete LU --- %s"%(http_object.response))
                if http_object.response_b:
                    print("\nLogical unit %s is removed successfully"%(logicalunit_name))
                    log.log_debug("Logical unit %s is removed successfully"%(logicalunit_name))
                return
        log.log_error("\nProvided LogicalUnit name is not available")
            
