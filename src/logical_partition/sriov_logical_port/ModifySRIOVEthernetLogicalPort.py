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
import xml.etree.ElementTree as etree
import time
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "LogicalPartition"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml;type=SRIOVEthernetLogicalPort"
PORT_VLAN_ID = 2

class ModifySRIOVEthernetLogicalPort(object):
    def __init__(self):
        """
        initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def modify_sriov_logicalport(self, ip, lpar_uuid, sriov_object, x_api_session):
        """
        Modifies the portvlan id of the selected sriov object
        Args:
          ip : ip address of hmc
          lpar_uuid : Logical Partition UUID on which the selected
                      SRIOV Logical Port is to be modified
          sriov_object : The SRIOV Logical port object to be modified
          x_api_session : session to be used
        """
        header = HmcHeaders.HmcHeaders("uom")
        ns = header.ns["xmlns"]
        sriov_object.PortVLANID = PORT_VLAN_ID
        xml = sriov_object.toxml()
        http_object = HTTPClient.HTTPClient("uom", ip,
                                            self.root, self.content_type,
                                            x_api_session)
        sriov_id = sriov_object.Metadata.Atom.AtomID.value()
        http_object.HTTPPost(xml,append=lpar_uuid+"/SRIOVEthernetLogicalPort/"+sriov_id)
        print("\nProcessing ...This may take few seconds")
        log.log_debug("Modification of SRIOV Logical Port Post Performed.Waiting for 60 seconds")
        time.sleep(60)
        http_object.HTTPGet(append=lpar_uuid+"/SRIOVEthernetLogicalPort/"+sriov_id)
        if http_object.response_b:
              root = etree.fromstring(http_object.response.content)
              if root.findall(".//{%s}PortVLANID"%(ns))[0].text == str(sriov_object.PortVLANID.value()):
                  print("\n SRIOVEthernetLogicalPort PortVLANID is modified successfully")
                  log.log_debug("SRIOVEthernetLogicalPort PortVLANID is modified successfully")
              else:
                   log.log_error("Error occured while updating SRIOVEthernetLogicalPort")
                
