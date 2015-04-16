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
import pyxb
log = HMCClientLogger.HMCClientLogger(__name__)

ROOT = "ManagedSystem"
CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=NetworkBridge"
SCHEMA_VER = "V1_3_0"

class ModifyNetworkBridge:
    """
    Modifies NetworkBridge by adding a VLAN to the LoadGroup
    and adding a load group to existing network bridge
    """
    
    def __init__(self):
        """
        Initializes root and content-type
        """
        self.root = ROOT
        self.content_type = CONTENT_TYPE
        
    def add_vlan_to_loadgroup(self, ip, managedsystem_uuid, session_id, networkbridge_object, virtualnetwork_id):
        """
        additional VLAN to exiting Loadgroup
        Args:
            ip:ip address of hmc
            managedsystem_uuid:UUID of the managedsystem
            session_id:session to be used
            networkbridge_object:networkbridge object to be modified
            vrtualnetwork_id:UUID of the virtual network to be added
        Returns:
             boolen value
        """
        log.log_debug("addition of vlan to load group started")
        link = "https://"+ip+":12443/rest/api/uom/ManagedSystem/"+managedsystem_uuid+"/VirtualNetwork/"+virtualnetwork_id
        networkbridge_object.LoadGroups.LoadGroup[0].VirtualNetworks.link.append(UOM.AtomLink_Type(rel="related",href=link))
        xml = networkbridge_object.toxml()
        httpclient_object = HTTPClient.HTTPClient("uom",ip,self.root,self.content_type,session_id)
        httpclient_object.HTTPPost(xml,append=str(managedsystem_uuid)+"/NetworkBridge/"+networkbridge_object.Metadata.Atom.AtomID.value())
        log.log_debug("reponse for addition of vlan -- %s"%(httpclient_object.response))
        if  httpclient_object.response_b:
            return True
        else:
            return False
        
    def add_loadgroup(self, ip, managedsystem_uuid, session_id, networkbridge_object, virtualnetwork_object):
        """
        addition of a Loadgroup
        Args:
            ip:ip address of hmc
            managedsystem_uuid:UUID of the managedsystem
            session_id:session to be used
            networkbridge_object:networkbridge object to be modified
            vrtualnetwork_object:virtual network object on which Loadgroup is to be added
        Returns:
             boolen value
        """
        log.log_debug("addition of load group started")
        link = "https://"+ip+":12443/rest/api/uom/ManagedSystem/"+managedsystem_uuid+"/VirtualNetwork/"+virtualnetwork_object.Metadata.Atom.AtomID.value()
        loadgroup_object = UOM.LoadGroup()
        loadgroup_object.PortVLANID = virtualnetwork_object.NetworkVLANID.value()
        loadgroup_object.VirtualNetworks = pyxb.BIND()
        loadgroup_object.VirtualNetworks.link.append(UOM.AtomLink_Type(rel="related",href=link))
        loadgroup_object.schemaVersion = SCHEMA_VER
        networkbridge_object.LoadGroups.LoadGroup.append(loadgroup_object)
        xml = networkbridge_object.toxml()
        httpclient_object = HTTPClient.HTTPClient("uom",ip,self.root,self.content_type,session_id)
        httpclient_object.HTTPPost(xml,append=str(managedsystem_uuid)+"/NetworkBridge/"+networkbridge_object.Metadata.Atom.AtomID.value())
        log.log_debug("reponse for addition of loadgroup -- %s"%(httpclient_object.response))
        if  httpclient_object.response_b:
            return True
        else:
            return False
