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


from src.main.HmcRestClient import *
from src.performance_capacity_monitor import LongTermMonitor, \
     ShortTermMonitor, ProcessedMetrics

from src.performance_capacity_monitor import ManagedSystemPcm
from src.virtual_io_server import ListVirtualIOServer


###################################
# PERFORMANCE CAPACITY MONITORING
###################################

def performance_capacity_monitoring(n1, ip, x_api_session):
    """
    This function is used for the performance and capacity monitoring of the hmc

    Args:
     n1 : variable for client selected choices
     ip: ip address of HMC
     x_api_session : Session to be used

    """
    os.system("cls")
    SelectManagedSystem_obj = SelectManagedSystem.SelectManagedSystem()
    managedsystem_object = SelectManagedSystem_obj.\
                          get_managedsystem_uuid(ip, x_api_session)
    managedsystem_uuid = SelectManagedSystem_obj.managedsystem_uuid
    virtualioserver_object = ListVirtualIOServer.ListVirtualIOServer()
    object_list = virtualioserver_object.list_VirtualIOServer(ip,
                                                              managedsystem_uuid,
                                                              x_api_session)
    if managedsystem_uuid != "":
        st = 'y'
        n = n1
        if n == 1:
            ManagedSystemPcmPreference_object = ManagedSystemPcm.ManagedSystemPcmPreference(ip,
                                                                           managedsystem_uuid,
                                                                           x_api_session)
            while True:
                print ("\n\n","ManagedSystemPcmPreference".center(50))
                print_list = ['Get ManagedSystemPcmPreference','Set/Update ManagedSystemPcmPreference','Return to PCM Menu']
                #select any performance_capacity_monitoring operation
                x = int(print_obj.print_on_screen(print_list) )
                if x == 1:
                    get_managedsystempcmpreference_object = ManagedSystemPcmPreference_object.get_managedsystempcmpreference()
                    ManagedSystemPcmPreference_object.print_managedsystempcmpreference(get_managedsystempcmpreference_object)
                    
                elif x == 2:
                    set_managedsystempcmpreference_object = ManagedSystemPcmPreference_object.\
                                                            set_managedsystempcmpreference()
                    
                elif x == 3:
                    os.system("cls")
                    break
                else:
                            print("\nTry again using valid option")
                back_to_menu()
        elif n == 2:
            #object creation and Method call to Longterm monitor
            LongTermMonitor_object = LongTermMonitor.LongTermMonitor(ip,
                                                                     managedsystem_uuid,
                                                                     x_api_session)
            LongTermMonitor_object.get_longtermmonitor(object_list)
        
            back_to_menu()
             
        elif n == 3:
            #object creation and Method call to Shortterm monitor
            ShortTermMonitor_object = ShortTermMonitor.ShortTermMonitor(ip,
                                                                        managedsystem_uuid,
                                                                        x_api_session)
            ShortTermMonitor_object.get_shorttermmonitor(object_list)
        
            back_to_menu()
            
        elif n == 4:
            #object creation and Method call to Processed Metrics
            process_metrics_object = ProcessedMetrics.ProcessedMetrics(ip,managedsystem_uuid ,x_api_session)
            process_metrics_object.get_processedmetrics()
            back_to_menu()
            
        else:
            print("\nTry again using valid option")
            back_to_menu()
    else:
        back_to_menu()



