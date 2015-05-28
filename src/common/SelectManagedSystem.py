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

from src.managed_system import ListManagedSystem
from src.utility import HMCClientLogger
log_object = HMCClientLogger.HMCClientLogger(__name__)

class SelectManagedSystem:
    """ selects required managed system from src.list """
    
    def get_managedsystem_uuid(self, ip, x_api_session):
        """ get uuid for required managed system"""
        print("\nAvailable ManagedSystems : ")
        self.managedsystem_uuid = ""  
        managedsystem_object = ListManagedSystem.ListManagedSystem()
        object_list = managedsystem_object.list_ManagedSystem(ip, x_api_session)
        try:
            for i in range(0,len(object_list)):
                print("%s.%s"%(i+1,object_list[i].SystemName.value()))
            c = int(input("\nSelect any Managed System:"))
            if c<=len(object_list) and c>0:
                self.ch = c-1
                self.managedsystem_uuid = object_list[self.ch].\
                                      Metadata.Atom.AtomID.value()
                self.selected_managedsystem_object = object_list[self.ch]
                return managedsystem_object
            else:
                print("\nTry again using valid option")
        except (TypeError,AttributeError,IndexError):
            log_object.log_warn("No ManagedSystems available ")
            
            

