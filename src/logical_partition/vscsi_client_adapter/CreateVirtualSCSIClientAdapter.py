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

ROOT = "LogicalPartition"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=VirtualSCSIClientAdapter"
SCHEMA_VER = "V1_3_0"
ADAPTER_TYPE = "Client"
PARTIITON_ID = 1
SLOT_NUMBER = 5

class CreateVirtualSCSIClientAdapter:
    """
    creates a virtual SCSI adapter on a given logical partition
    """
    def __init__(self):
        """
        assign the root and content_type for request
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def create_vscsi_clientadapter(self, ip, logicalpartition_uuid, x_api_session):
        """
        Args:
            ip: ip address of hmc
            logicalpartition_uuid:UUID of Logical partition on which virtual SCSI
            adapter is to be created
            x_api_session:session used to create virtual SCSI adapter
        """
        log.log_debug("creation of scsi adapter started")
        vscsi_object = UOM.VirtualSCSIClientAdapter()
        vscsi_object.AdapterType = ADAPTER_TYPE
        vscsi_object.RemoteLogicalPartitionID = PARTITION_TYPE
        vscsi_object.RemoteSlotNumber = SLOT_NUMBER
        vscsi_object.schemaVersion = SCHEMA_VER
        pyxb.RequireValidWhenGenerating(True)
        xml = vscsi_object.toxml()
        http_object = HTTPClient.HTTPClient("uom", ip, self.root,
                                            self.content_type, x_api_session)
        http_object.HTTPPut(xml,append=logicalpartition_uuid+"/VirtualSCSIClientAdapter")
        log.log_debug("response of create scsi adapter --- %s"%(http_object.response))
        if http_object.response_b:
            print("VirtualSCSIClientAdapter created successfully")
            log.log_debug("VirtualSCSIClientAdapter created successfully")
        else :
           log.log_error("Error in VirtualSCSIClientAdapter creation.Verify the attribute values")
            
