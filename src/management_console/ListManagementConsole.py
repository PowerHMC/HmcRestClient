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

from src.utility  import HTTPClient,HMCClientLogger,HmcHeaders
from src.common import ListModule
log_object=HMCClientLogger.HMCClientLogger(__name__)

CONTENT_TYPE = "application/vnd.ibm.powervm.uom+xml; type=ManagementConsole"

class ListManagementConsole(object):
    """"
    lists the details of Management Console
    """
    
    def __init__(self):
        """
        Initializes the log object to use Log module

        """
        self.content_type = CONTENT_TYPE
        
    def list_ManagementConsole(self, ip, session_id):
        """
        collects the xml content of the management console and
        returns a reference to it
        Args:
            ip : ip address of HMC
            session_id : session to be used
        """
        log_object.log_debug("List of ManagementConsole started")
        listing_object = ListModule.ListModule()
        #call to get the xml content of managed system #
        object_list = listing_object.listing("uom",ip, "ManagementConsole", self.content_type, "ManagementConsole", session_id)
        log_object.log_debug("Returns ManagementConsole"
                                  " objects to the main module")
        return object_list
        
    def print_managementconsole_attributes(self, managementconsole_object):
        """
         Prints the quick property values from the retrieved xml content
         
           Args:
                object_list:represents user selected choice of specific
                management console
        """
        print("\n")
        print("ManagementConsoleName".ljust(35), ":",
              managementconsole_object.ManagementConsoleName.value())
        print("BaseVersion".ljust(35), ":", managementconsole_object.BaseVersion.value())
        print("Management Console id".ljust(35), ":",
              managementconsole_object.Metadata.Atom.AtomID.value())
        #print("\nNETWORK INTERFACES\n")
        try:
            for entry in range(0, len(managementconsole_object.NetworkInterfaces.\
                                      ManagementConsoleNetworkInterface)):
                print ("MANAGEMENT CONSOLE NETWORK INTERFACE".ljust(35), ":", entry)
                print ("InterfaceName".ljust(35), ":",managementconsole_object.\
                       NetworkInterfaces.ManagementConsoleNetworkInterface[entry].\
                       InterfaceName.value())
                print ("NetworkAddress".ljust(35), ":", managementconsole_object.\
                       NetworkInterfaces.ManagementConsoleNetworkInterface[entry].\
                       NetworkAddress.value())
        except Exception:
            pass



        
    
    
    
    

    
    
 
