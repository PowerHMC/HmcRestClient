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


from src.utility import HMCClientLogger,HTTPClient,HmcHeaders
from src.generated_src import UOM
import xml.etree.ElementTree as etree
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "LogicalPartition"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml;type=SRIOVEthernetLogicalPort"
SCHEMA_VER = "V1_3_0"
ADAPTER_ID = 1
PHYSICALPORT_ID = 2

class CreateSRIOVLogicalPort(object):

    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE

    def create_sriov_logicalport(self, ip, logicalpartition_uuid, x_api_session):
        """
        Creates SRIOV Logical Port for a given LogicaPartition
        Args:
            ip:ip address of hmc
            logicalpartition_uuid : UUID of partition the LoicalPort to be created
            x_api_session :session to be used
        """
        log.log_debug("starting SRIOV LogicalPort creation")
        header_object = HmcHeaders.HmcHeaders("web")
        ns = header_object.ns["xmlns"]
        sriov_logical_port_object = UOM.SRIOVEthernetLogicalPort()
        sriov_logical_port_object.AdapterID = ADAPTER_ID
        sriov_logical_port_object.PhysicalPortID = PHYSICALPORT_ID
        sriov_logical_port_object.schemaVersion = SCHEMA_VER
        xml = sriov_logical_port_object.toxml()
        http_object = HTTPClient.HTTPClient("uom", ip, self.root, self.content_type, x_api_session)
        http_object.HTTPPut(xml, append = logicalpartition_uuid+"/SRIOVEthernetLogicalPort")
        log.log_debug("response of SRIOV logical port creation %s"%(http_object.response))
        if http_object.response_b:
            print("SRIOV Logical Port created successfully")
        else :
            root = etree.fromstring(http_object.response.content)
            error = root.findall(".//{%s}Message"%(ns))[0]
            log.log_error(error.text)
