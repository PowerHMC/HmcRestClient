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
from src.main.ManagedSystem import *
from src.main.Cluster import *
from src.main.PerformanceCapacityMonitor import *
import sys
import os

directory = os.path.dirname(os.path.dirname(__file__))
def menu():
    """
    This provides the main menu for the client to interract with the hmc
    """
    client = HmcRestClient()
    client.logon()
    back_to_menu()
    while True:
        try:
            print ("\n\n", "Main Menu".center(50))
            print_list = ['List Management Console Details', 'Managed System', 'Cluster',
                          'Performance Capacity Monitoring', 'Logoff', 'Help']
            #client choice for selecting root elements
            client_choice = int(print_obj.print_on_screen(print_list))
            if client_choice == 1:
                managementconsole_object = ListManagementConsole.ListManagementConsole()
                object_console = managementconsole_object.list_ManagementConsole(client.ip,
                                                                                 client.x_api_session)
                managementconsole_object.print_managementconsole_attributes(object_console[0])
                back_to_menu()            
            elif client_choice == 2:
                os.system("cls")
                while True:
                    print ("\n\n", "ManagedSystem Menu".center(50))
                    print_list = ['Managed System Operations', 'VirtualSwitch',
                                  'VirtualNetwork', 'NetworkBridge',
                                  'Logical Partition', 'VirtualIOServer',
                                  'SRIOV Ethernet PhysicalPort', 'Return to MainMenu','Help','Exit']
                    # select any managed system children
                    choice = int(print_obj.print_on_screen(print_list))
                    if choice == 8:
                        os.system("cls")
                        break
                    elif choice > 0 and choice < 9:
                        boolean = managedsystem_children(choice, client.ip, client.x_api_session)
                        if not boolean:
                            os.system("cls")
                            break
                    elif choice == 9:
                        print(open(directory+"/help/ManagedSystem/1ManagedSystem.txt").read())
                        back_to_menu()
                    elif choice == 10:
                        sys.exit(1)
                    else:
                        print("\nTry again using valid option")
                        back_to_menu()
                    os.system("cls")                
            elif client_choice == 3:
                os.system("cls")
                while True:
                    print ("\n\n", "Cluster".center(50))
                    print_list = ['List', 'create', 'Modify', 'Delete',
                                  'Return to MainMenu','Help','Exit']
                    choice = int(print_obj.print_on_screen(print_list))
                    if choice == 5:
                        os.system("cls")
                        break
                    elif choice > 0 and choice < 5:
                         cluster_menu(choice, client.ip, client.x_api_session)
                    elif choice == 6:
                        print(open(directory+"/help/Cluster.txt").read())
                        back_to_menu()
                    elif choice == 7:
                        sys.exit(1)
                    else:
                        print("\nTry again using valid option")
                        back_to_menu()
                    os.system("cls")
            elif client_choice == 4:
                os.system("cls")
                while True:
                    print ("\n\n", "Performance and Capacity Monitoring".center(50))
                    print_list = ['ManagedSystemPcmPreference', 'LongTermMonitor',
                                  'ShortTermMonitor', 'ProcessorMetrics',
                                  'Return to MainMenu','Help','Exit']
                    # select any performance_capacity_monitoring children
                    choice = int(print_obj.print_on_screen(print_list))
                    if choice == 5:
                        os.system("cls")
                        break
                    elif choice == 6:
                        print(open(directory+"/help/PerformanceCapacityMonitoring.txt").read())
                        back_to_menu()
                    elif choice > 0 and choice < 5:
                        performance_capacity_monitoring(choice, client.ip, client.x_api_session)
                    elif choice == 7:
                        sys.exit(1)
                    else:
                        print("\nTry again using valid option")
                        back_to_menu()
                    os.system("cls")                
            elif client_choice == 5:
                client.logoff_request()
                return
            elif client_choice == 6:
                HMC_Help()
            else:
                print("\nTry again using valid option")
                back_to_menu()
        except ValueError:
            print("\nUse valid options")
            back_to_menu() 
def main():
    """
    Blocks the HTTPS Requests insecure Warning
    """
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        menu()
        
#main()
