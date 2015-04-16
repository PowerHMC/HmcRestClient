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
log = HMCClientLogger.HMCClientLogger(__name__)

class ManagedSystemRemoveConnection(object):
    """
    Removes connection of the selected ManagedSystem
    """
    
    def __init__(self, ip, x_api_session, managedsystem_uuid):
        """
        Creates HTTP Request object to perform Remove Connection operation
        Args:
          ip : ip address of HMC
          x_api_session : session to be used
          managedsystem_uuid : UUID of managedsystem to remove connection
        """
        
        self.managedsystem_uuid=managedsystem_uuid
        self.request_obj=HTTPClient.HTTPClient('uom',ip,'ManagedSystem',content_type='application/vnd.ibm.powervm.web+xml; type=JobRequest',session_id=x_api_session)

    def remove_connection_managedsystem(self):
        
        self.payload="""<JobRequest:JobRequest xmlns:JobRequest="http://www.ibm.com/xmlns/systems/power/firmware/web/mc/2012_10/" xmlns="http://www.ibm.com/xmlns/systems/power/firmware/web/mc/2012_10/" xmlns:ns2="http://www.w3.org/XML/1998/namespace/k2" schemaVersion="V1_0">
	<Metadata>
		<Atom/>
	</Metadata>
	<RequestedOperation kb="CUR" kxe="false" schemaVersion="V1_0">
		<Metadata>
			<Atom/>
		</Metadata>
		<OperationName kb="ROR" kxe="false">RemoveConnection</OperationName>
		<GroupName kb="ROR" kxe="false">ManagedSystem</GroupName>
	</RequestedOperation>
	<JobParameters kb="CUR" kxe="false" schemaVersion="V1_0">
		<Metadata>
			<Atom/>
		</Metadata>
	</JobParameters>
</JobRequest:JobRequest>"""
        self.request_obj.HTTPPut(self.payload,append=str(self.managedsystem_uuid)+"/do/RemoveConnection")
        log.log_debug("remove connection managed system - %s"%(self.request_obj.response))
        if self.request_obj.response_b == False:
            print("\nSorry! Remove Connection operation is UNSUCCESSFUL")
        else:
            print("\nRemoval of the selected Managed System connection from  Management Console is successful. ")
              
    


