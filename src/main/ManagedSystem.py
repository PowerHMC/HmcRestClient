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
from src.main.LogicalPartition import *
from src.main.VirtualIOServer import *
from src.managed_system import ListManagedSystem,\
                          PowerOnManagedSystem,\
                          PowerOffManagedSystem
from src.managed_system.virtual_network import ListVirtualNetwork, \
                                           CreateVirtualNetwork, \
                                           ModifyVirtualNetwork
from src.managed_system.virtual_switch import ListVirtualSwitch, \
                                          CreateVirtualSwitch, \
                                          ModifyVirtualSwitch
from src.managed_system.network_bridge import ListNetworkBridge, \
                                         CreateNetworkBridge, \
                                         ModifyNetworkBridge
from src.managed_system.sriov_physical_port import ChangeAdapterMode, \
                                                  ListSRIOVPhysicalPort
import sys
import os


##################
# MANAGED SYSTEM 
#################

directory = os.path.dirname(os.path.dirname(__file__))
def managedsystem_children(choice, ip, x_api_session):
    """
    This function provides a detailed view of the Managed System

    Args:
     choice : client choice to select the operation to be performed 
              on the Managed system and its children
     ip : ip address of hmc
     x_api_session : session to be used

    """
    os.system("cls")
    st = 'y'
    SelectManagedSystem_obj = SelectManagedSystem.SelectManagedSystem()
    managedsystem_object = SelectManagedSystem_obj.\
                           get_managedsystem_uuid(ip,
                                                  x_api_session)
    managedsystem_uuid = SelectManagedSystem_obj.managedsystem_uuid
    back_to_menu()
    
    if SelectManagedSystem_obj.managedsystem_uuid != "":
        if choice == 1:
           while True:
                print ("\n\n","ManagedSystem Operations".center(50))
                print_list = ['List','Poweron','Poweroff',
                              'Remove Connection',
                              'Return to ManagedSystem Menu',
                              'Return to MainMenu','Help','Exit']
                #select any managed system operation
                x = int(print_obj.print_on_screen(print_list))
                 
                if x == 1:
                    # object creation and method call list the details of managed system
                    managedsystem_object.print_managedsystem_attributes(SelectManagedSystem_obj.ch)
                    
                elif x == 2:
                    #object creation and method call Power On managed system
                    poweron_managedsystem_object = PowerOnManagedSystem.PowerOnManagedSystem()
                    poweron_managedsystem_object.poweron_ManagedSystem(ip,
                                                                       managedsystem_uuid,
                                                                       x_api_session)
                              
                elif x == 3:
                    #object creation and method call Power off managed system
                    poweroff_managedsystem_object = PowerOffManagedSystem.PowerOffManagedSystem()
                    poweroff_managedsystem_object.poweroff_ManagedSystem(ip,
                                                                         managedsystem_uuid,
                                                                         x_api_session)
                               
                elif x == 4:
                    #object creation and method call to remove connection of managed system
                    removeconnection = ManagedSystemRemoveConnection.\
                                       ManagedSystemRemoveConnection(ip,
                                                                     x_api_session,
                                                                     managedsystem_uuid)
                    removeconnection.remove_connection_managedsystem()
                    
                elif x == 5:
                    os.system("cls")
                    return True
                elif x == 6:
                    os.system("cls")
                    return False
                elif x == 7:
                    print(open(directory+"/help/ManagedSystem/ManagedSystemOperations.txt").read())
                elif x == 8:
                    sys.exit(1)
                else:
                    print("\nTry again using valid option")
                back_to_menu()
                          
        elif choice == 2:
            while True:
                print ("\n\n","VirtualSwitch".center(50))
                print_list = ['List','Create','Modify',
                              'Return to ManagedSystem Menu','Return to MainMenu','Help','Exit']
                #select any VirtualSwitch operation
                x1 = int(print_obj.print_on_screen(print_list))
                list_virtualswitch_object = ListVirtualSwitch.ListVirtualSwitch()
                switch_object_list = list_virtualswitch_object.\
                                     list_virtualswitch_attributes(ip,
                                                                   managedsystem_uuid,
                                                                   x_api_session)
                if x1 == 1:
                    #object creation and method call to list the details of all virtual switch in the managed system
                   for switch_object in switch_object_list:
                       list_virtualswitch_object.print_virtualswitch_attributes(switch_object)
                   
                elif x1 == 2:
                     #object creation and method call to create virtual switch
                    virtualswitch_bool = False
                    print("\n Virtual Switch with next SwitchID will be Created\n")
                    virtualswitch_object = CreateVirtualSwitch.CreateVirtualSwitch()
                    virtualswitch_bool = virtualswitch_object.create_virtualswitch(ip,
                                                                                   managedsystem_uuid,
                                                                                   x_api_session)
                    if virtualswitch_bool :
                        print("Virtualswitch is created Successfully")
                    else :
                        log_object.log_error("Error in VirtualSwitch Creation.VirtualSwitch alredy exists.")
                    
                elif x1 == 3:
                     #object creation and method call to modify virtual switch
                    virtualswitch_bool = False
                    try:
                          for i in range(0,len(switch_object_list)):
                             print("%s.%s " % (i+1,switch_object_list[i].SwitchName.value()))
                          try:
                              c = int(input("\nSelect any Virtualswitch index the operation to be performed:"))
                              ch = c-1
                              selected_switch_object = switch_object_list[ch]
                              print("\nName of the Virtual Switch will be Modified \n")
                              virtualswitch_object = ModifyVirtualSwitch.ModifyVirtualSwitch()
                              virtualswitch_bool = virtualswitch_object.modify_virtualswitch(ip,
                                                                                   managedsystem_uuid,
                                                                                   x_api_session,
                                                                                   selected_switch_object)
                              if virtualswitch_bool :
                                    print("VirtualSwitch is updated Successfully")
                              else :
                                    log_object.log_error("Error in VirtualSwitch updation.")
                          except IndexError :
                              print("\nTry again using valid option")
                    except (TypeError, AttributeError):
                          log_object.log_warn("No VirtualSwitches are Available")
                elif x1 == 4:
                    os.system("cls")
                    return True
                elif x1 == 5:
                    os.system("cls")
                    return False
                elif x1 == 6:
                    print(open(directory+"/help/ManagedSystem/VirtualSwitch.txt").read())
                elif x1 == 7:
                    sys.exit(1)
                else:
                    print("\nTry again using valid option")
                back_to_menu()
                
        elif choice == 3:
            #virtual network operations
            while True:
                print ("\n\n","VirtualNetwork".center(50))
                print_list = ['List','Create','Modify',
                              'Return to ManagedSystem Menu',
                              'Return to MainMenu','Help','Exit']
                #select any VirtualNetwork operation
                x1 = int(print_obj.print_on_screen(print_list))
                virtualnetwork_object = ListVirtualNetwork.ListVirtualNetwork()
                object_list = virtualnetwork_object.list_VirtualNetwork(ip,managedsystem_uuid,x_api_session)
                if x1 == 1:
                     #object creation and method call to list the details of all virtual network in the system
                     for objects in object_list:   
                        virtualnetwork_object.print_virtualnetwork_attributes(objects)
                     
                elif x1 == 2:
                    virtualnetwork_bool = False
                    list_virtualswitch_object = ListVirtualSwitch.ListVirtualSwitch()
                    switch_object_list = list_virtualswitch_object.list_virtualswitch_attributes(ip,
                                                                                                 managedsystem_uuid,
                                                                                                 x_api_session)
                    try:
                          for i in range(0,len(switch_object_list)):
                             print("%s.%s " % (i+1,switch_object_list[i].SwitchName.value()))
                          try:
                              c = int(input("\nSelect any Virtualswitch index the operation to be performed:"))
                              ch = c-1
                              selected_switch_object = switch_object_list[ch]
                              print("\nVirtual Network will be created on the Selected Switch.VLAN ID is Hardcoded\n")
                              virtualnetwork_object = CreateVirtualNetwork.CreateVirtualNetwork()
                              virtualnetwork_bool = virtualnetwork_object.create_virtualnetwork(ip,
                                                                        managedsystem_uuid,
                                                                        x_api_session,
                                                                        selected_switch_object)
                              if virtualnetwork_bool :
                                  print("VirtualNetwork is created Successfully")
                              else :
                                  log_object.log_error("Error in VirtualNetwork Creation.VirtualNetwork alredy exists.")
                            
                          except IndexError :
                              print("\nTry again using valid option")
                          
                    except (TypeError, AttributeError):
                          log_object.log_warn("No VirtualSwitches are Available")  
                    
                elif x1 == 3:
                     #object creation and method call to modify selected virtual network
                    modify_virtualnetwork_bool = False
                    selected_virtulanetwork = get_selectedvirtualnetwork(object_list)
                    print("\nName of the Virtual Switch will be Modified \n")
                    virtualnetwork_object = ModifyVirtualNetwork.ModifyVirtualNetwork()
                    modify_virtualnetwork_bool = virtualnetwork_object.modify_virtualnetwork(ip,
                                                                                             managedsystem_uuid,
                                                                                             x_api_session,
                                                                                             selected_virtulanetwork)
                    if modify_virtualnetwork_bool:
                        print("VirtualNetwork is updated Successfully")
                    else :
                        log_object.log_error("Error in VirtualNetwork modification.")
                elif x1 == 4:
                    os.system("cls")
                    return True
                elif x1 == 5:
                    os.system("cls")
                    return False
                elif x1 == 6:
                    print(open(directory+"/help/ManagedSystem/VirtualNetwork.txt").read())
                elif x1 == 7:
                    sys.exit(1)
                else:
                    print("\nTry again using valid option")
                back_to_menu()
                
        elif choice == 4:
            #Network bridge operations
            while True:
                print ("\n\n","NetworkBridge".center(50))
                print_list = ['List','Create','Modify',
                              'Return to ManagedSystem Menu',
                              'Return to MainMenu','Help','Exit']
                #select any Networkbridge operation
                x1 = int(print_obj.print_on_screen(print_list))
                if x1 == 1:
                     #object creation and method call to list the details of network bridge
                    list_networkbridge = ListNetworkBridge.ListNetworkBridge()
                    object_list = list_networkbridge.list_networkbridge_attributes(ip,
                                                                                   managedsystem_uuid,
                                                                                   x_api_session)
                    if object_list != None:
                        for objects in object_list:
                            list_networkbridge.print_networkbridge_attributes(objects)
                    else:
                        log_object.log_warn("No NetworkBridge is Available")
                        
                elif x1 == 2:
                     #object creation and method call to create virtual network
                    virtualnetwork_object = ListVirtualNetwork.ListVirtualNetwork()
                    virtualnetwork_object_list = virtualnetwork_object.list_VirtualNetwork(ip,
                                                                                           managedsystem_uuid,
                                                                                           x_api_session)
                    print("\nselect a VirtualNetwork on which Trunk Adapter to be created")
                    selected_virtualnetwork_object = get_selectedvirtualnetwork(virtualnetwork_object_list)
                    virtualioserver_object = ListVirtualIOServer.ListVirtualIOServer()
                    vios_object_list = virtualioserver_object.\
                                       list_VirtualIOServer(ip,
                                                            managedsystem_uuid,
                                                          x_api_session)
                    print("\nselect a VirtualIOServer on which Trunk Adapter to be created")
                    selected_vios_object = get_selectedobject(vios_object_list)
                    print("\nNetwork Bridge will be created with one Load Group containing one Trunk Adapter",
                          "of selected virtual network\n")
                    vios_id = selected_vios_object.Metadata.Atom.AtomID.value()
                    virtualnetwork_id = selected_virtualnetwork_object.Metadata.\
                                        Atom.AtomID.value()
                    networkbridge_object = CreateNetworkBridge.CreateNetworkBridge()
                    created_networkbridge = networkbridge_object.\
                                            create_network_bridge(ip,
                                                                  managedsystem_uuid,
                                                                  x_api_session,
                                                                  vios_id,
                                                                  virtualnetwork_id)
                    if created_networkbridge != None:
                        print("NetworkBridge Created Successfully")
                    else :
                        log_object.log_error("Error in NetworkBridge Creation.Verify the attribute values")
                elif x1 == 3:
                     #object creation and method call to modify Network bridge
                    modifybool = False
                    print("\nAvailable NetworkBridges :\n")
                    list_networkbridge = ListNetworkBridge.ListNetworkBridge()
                    object_list = list_networkbridge.list_networkbridge_attributes(ip,
                                                                     managedsystem_uuid,
                                                                     x_api_session)
                    
                    for i in range(0,len(object_list)):
                         print("%s.NetworkBridge PortVLANID %s " % (i+1,object_list[i].PortVLANID.value()))
                    try:
                              c = int(input("\nSelect any NetworkBridge the operation to be performed:"))
                              ch = c-1
                              selected_networkbridge_object = object_list[ch]
                              option = int(input("\n1.Add Additional VLANID to existing TrunkAdapter\n2.Add a New LoadGroup\nselect an option for modification :"))
                              if option > 0 and option < 3:
                                  virtualnetwork_object = ListVirtualNetwork.ListVirtualNetwork()
                                  virtualnetwork_object_list = virtualnetwork_object.list_VirtualNetwork(ip,
                                                                                                       managedsystem_uuid,
                                                                                                       x_api_session)
                                  print("\nselect a VirtualNetwork to be added to networkbridge")
                                  selected_virtualnetwork_object = get_selectedvirtualnetwork(virtualnetwork_object_list)
                                  virtualnetwork_id = selected_virtualnetwork_object.Metadata.Atom.AtomID.value()
                                  modify_networkbridge_object = ModifyNetworkBridge.ModifyNetworkBridge()
                                  if option == 1:
                                      modifybool = modify_networkbridge_object.add_vlan_to_loadgroup(ip,
                                                                                         managedsystem_uuid,
                                                                                         x_api_session,
                                                                                         selected_networkbridge_object,
                                                                                         virtualnetwork_id)
                                      if modifybool :
                                          print("NetworkBridge Updated sucessfully")
                                      else :
                                          log_object.log_error("Error in updating NetworkBridge")                   
                        
                                  elif option == 2:
                                      modifybool = modify_networkbridge_object.add_loadgroup(ip,
                                                                              managedsystem_uuid,
                                                                              x_api_session,
                                                                              selected_networkbridge_object,
                                                                              selected_virtualnetwork_object)
                                      if modifybool :
                                          print("NetworkBridge Updated sucessfully")
                                      else :
                                          log_object.log_error("Error in updating NetworkBridge")
                              else :
                                 print("\nTry again using valid option") 
                    except IndexError :
                              print("\nTry again using valid option")
                elif x1 == 4:
                    os.system("cls")
                    return True
                elif x1 == 5:
                    os.system("cls")
                    return False
                elif x1 == 6:
                    print(open(directory+"/help/ManagedSystem/NetworkBridge.txt").read())
                elif x1 == 7:
                    sys.exit(1)
                else:
                    print("\nTry again using valid option")
                back_to_menu()
                
        elif choice == 5:   
            while True:
                print ("\n\n","LogicalPartition Menu".center(50))
                print_list = ['LogicalPartition operations','LogicalPartitionProfile',
                            'ClientNetworkAdapter','VirtualSCSIClientAdapter',
                            'VirtualFibreChannelClientAdapter',
                              'SRIOVEthernetLogicalPort',
                              'Return to ManagedSystem Menu','Return to MainMenu','Help','Exit']
                #select any Logical partition operations
                n = int(print_obj.print_on_screen(print_list))
                if n == 7:
                    os.system("cls")
                    return True
                elif n == 8:
                    os.system("cls")
                    return False
                elif n > 0 and n < 7:
                    k = logicalpartition_children(n,
                                                  managedsystem_uuid,
                                                  ip, x_api_session)
                    if k == 1:
                        pass
                    elif k == 2:
                        return True
                    elif k == 3:
                        return False
                elif n == 9:
                    print(open(directory+"/help/LogicalPartition/1LogicalPartition.txt").read())
                    back_to_menu()
                elif n == 10 :
                    sys.exit(1)
                else:
                    print("\nTry again using valid option")
                    back_to_menu()
                
            
        elif choice == 6:
            while True:
                print ("\n\n","Virtual IO Server Menu".center(50))
                print_list = ['VirtualIOServer operations',
                              'LogicalPartitionProfile','VolumeGroup',
                              'create vscsi mappings',
                              'create Virtual FibreChannel Mappings',
                              'Return to ManagedSystem Menu','Return to MainMenu','Help','Exit']
                #select any VirtualIOServer children
                n = int(print_obj.print_on_screen(print_list))
                if n == 6:
                    os.system("cls")
                    return True
                elif n == 7:
                    os.system("cls")
                    return False
                elif n > 0 and n < 6:
                    k = virtualioserver_children(n,
                                                 managedsystem_uuid,
                                                 ip, x_api_session)
                    if k == 1:
                       pass
                    elif k == 2:
                        os.system("cls")
                        return True
                    elif k == 3:
                        os.system("cls")
                        return False
                elif n == 8:
                    print(open(directory+"/help/VirtualIOServer/1VirtualIOServer.txt").read())
                    back_to_menu()                
                elif n == 9:
                    sys.exit(1)
                else:
                     print("\nTry again using valid option")
                     back_to_menu()
                
        elif choice == 7:
            while True:
               print ("\n\n","SRIOV Ethernet Physical Port ".center(50))
               print_list = ['List SRIOV Ethernet Physical Port',
                             'Change Adapter Mode', 'Return to ManagedSystem Menu',
                             'Return to MainMenu','Help','Exit']
               n = int(print_obj.print_on_screen(print_list))
               if n == 1:
                   #object creation and method call to List SRIOVEthernet Physical Port
                   sriov_physicalport = ListSRIOVPhysicalPort.ListSRIOVPhysicalPort()
                   sriov_list = sriov_physicalport.list_sriov_physicalport(ip,
                                                                           managedsystem_uuid,
                                                                           x_api_session)
                   if sriov_list != []:
                       for i in range(0,len(sriov_list)):
                               sriov_physicalport.print_sriov_physicalport(sriov_list[i])
                   else :
                        log_object.log_warn("No SRIOV physical ports are available")
               elif n == 2:
                   #object creation and method call to change SRIOVadapter mode
                   selected_managedsystem_object = SelectManagedSystem_obj.selected_managedsystem_object
                   if selected_managedsystem_object.AssociatedSystemIOConfiguration.SRIOVAdapters != None:                   
                       sriovadapter = selected_managedsystem_object.\
                                      AssociatedSystemIOConfiguration.SRIOVAdapters.IOAdapterChoice
                       for i in range(0,len(sriovadapter)):
                           sriov = sriovadapter[i].SRIOVAdapter
                           print("%s.SRIOV AdapterID %s"%(i+1,sriov.SRIOVAdapterID.value()))
                       ch = int(input("select a SRIOV adapter to change its mode "))
                       change_mode = ChangeAdapterMode.ChangeSRIOVAdapterMode()
                       adapter_object = sriovadapter[ch-1].SRIOVAdapter
                       change_mode.change_sriov_adaptermode(ip,
                                                            managedsystem_uuid,
                                                            adapter_object,
                                                            x_api_session)
                   else :
                        log_object.log_warn("No SRIOV physical ports are available")
               elif n == 3:
                 os.system("cls")
                 return True
               elif n == 4:
                 os.system("cls")
                 return False
               elif n == 8:
                    print(open(directory+"/help/ManagedSystem/SRIOVPhysicalPort.txt").read())              
               elif n == 6:
                   sys.exit(1)
               else:
                    print("\nTry again using valid option")
               back_to_menu()
                
        else:
            print("\nTry again using valid option")
        back_to_menu()

    return True    
