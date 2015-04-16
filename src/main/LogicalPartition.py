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
from src.logical_partition import ListLogicalPartition, \
                                  DeleteLogicalPartition

from src.logical_partition.sriov_logical_port import ListSRIOVLogicalPort, \
                                                    CreateSRIOVLogicalPort, \
                                                    ClearSRIOVLogicalPortStatistics, \
                                                    ModifySRIOVEthernetLogicalPort
                                                    
from src.logical_partition.virtual_fibrechannel_client_adapter  import ListVirtualFibreChannelClientAdapter, \
                                                                       CreateVirtualFibreChannelClientAdapter
from src.logical_partition.vscsi_client_adapter import ListVirtualSCSIClientAdapter, \
                                                       CreateVirtualSCSIClientAdapter

from src.logical_partition.client_network_adapter import CreateClientNetworkAdapter, \
                                                         ListClientNetworkAdapter

from src.partition_operation_util import PowerOnPartition,\
                                     PowerOffPartition,\
                                     ModifyPartition, \
                                     CreatePartition
                                                         
from src.logical_partition_profile import ListLogicalPartitionProfile,\
                                          CreateLogicalPartitionProfile,\
                                          ModifyLogicalPartitionProfile
import sys
import os


####################
# LOGICAL PARTITON
####################

def logicalpartition_children(n1, managedsystem_uuid, ip, x_api_session):
    """
    This function provides a detailed view of the Logical Partitions

    Args:
     n1 : variable for client selected choices
     managedsystem_uuid : The unique id of the Managed system
     ip: ip address of hmc
     x_api_session : session to be used

    """
    os.system("cls")
    n = n1
    if n == 1:
        #Logical Partition operations
        while True:
            print ("\n\n","LogicalPartition operations".center(50))
            print_list = ['List','Create','Delete','Poweron',
                         'Poweroff','Modify','Return to LogicalPartition Menu',
                          'Return to ManagedSystem Menu','Return to MainMenu','Help','Exit']
            #select any one Logical partition operation
            x = int(print_obj.print_on_screen(print_list))
            listlogicalpartition_object = ListLogicalPartition.ListLogicalPartition()
            object_list = listlogicalpartition_object.\
                              list_LogicalPartition(ip, managedsystem_uuid,
                                                     x_api_session)                              
            if x == 1:
                # object creation and method call to List Logical Partition
                print("\nAvailable LogicalPartitions :")
                selected_logicalpartition_object = get_selectedobject(object_list)
                if selected_logicalpartition_object != None:
                    listlogicalpartition_object.print_logicalpartition_attributes(selected_logicalpartition_object)
                
            elif x == 2:
                #object creation and method call to create Logicalpartition
                 try:
                     print("\nLogical Partition will be created with Following configruations,\n maximum,mimimum and desired memory = 256",
                           "\nShared processors,Minimum,Desired and maximum processing units = 0.5,\npartition type = AIX/Linux")
                     logicalpartition_object = CreatePartition.CreatePartition("LogicalPartition")
                     created_logicalpartition_object = logicalpartition_object.create_Partition(ip,
                                                                                                managedsystem_uuid,
                                                                                                x_api_session)
                     print("\nPartition %s Created Successfully\n"%(created_logicalpartition_object.PartitionName.value()))
                     listlogicalpartition_object.print_logicalpartition_attributes(created_logicalpartition_object)
                 except (TypeError,AttributeError) :
                     log_object.log_error("Error in lpar creation")
                 
            elif x == 3:
                #object creation and method call to delete Logical partition
                 selected_logicalpartition_object = None
                 print("\nAvailable LogicalPartitions :")
                 selected_logicalpartition_object = get_selectedobject(object_list)
                 if selected_logicalpartition_object != None:
                     logicalpartition_object = DeleteLogicalPartition.DeleteLogicalPartition()
                     logicalpartition_object.delete_LogicalPartition(ip,
                                                                     managedsystem_uuid,
                                                                     selected_logicalpartition_object,
                                                                     x_api_session)
                    
            elif x == 4:
                #object creation and method call to Poweron Logical partition
                 listlogicalpartition_object = ListLogicalPartition.ListLogicalPartition()
                 object_list = listlogicalpartition_object.\
                              list_LogicalPartition(ip, managedsystem_uuid,
                                                     x_api_session)
                 print("\nList of Partitions in inactive state")
                 k = 0
                 inactive_object_list = []
                 for i in range(0,len(object_list)):
                         if object_list[i].PartitionState.value() == "not activated":
                             k = k+1
                             print("%s.%s" % (k,object_list[i].PartitionName.value()))
                             inactive_object_list.append(object_list[i])
                 if k>0:
                    try:
                         c = int(input("\nSelect any partition index the operation to be performed:"))
                         if c > 0:
                             ch = c-1               
                             selected_logicalpartition_object = inactive_object_list[ch]
                             logicalpartition_object = PowerOnPartition.PowerOnPartition("LogicalPartition")
                             logicalpartition_object.poweron_Partition(ip,
                                                                       selected_logicalpartition_object,
                                                                       x_api_session)
                             
                         else :
                            print("\nTry again using valid option")
                    except IndexError :
                         print("\nTry again using valid option")
                 else:
                     log_object.log_warn("No Partitions are in inactive state")
                 
            elif x == 5:
                #object creation and method call to Poweroff Logical Partition
                 listlogicalpartition_object = ListLogicalPartition.ListLogicalPartition()
                 object_list = listlogicalpartition_object.\
                              list_LogicalPartition(ip, managedsystem_uuid,
                                                     x_api_session)
                 print("\nList of Partitions in active state")
                 k = 0
                 active_object_list = []
                 for i in range(0,len(object_list)):
                        if object_list[i].PartitionState.value() == "open firmware" or object_list[i].PartitionState.value() == "running":
                             k = k+1
                             print("%s.%s" % (k,object_list[i].PartitionName.value()))
                             active_object_list.append(object_list[i])
                 if k>0 :
                     try:
                         c = int(input("\nSelect any partition index the operation to be performed:"))
                         if c > 0:
                             ch = c-1
                             selected_logicalpartition_object = active_object_list[ch]
                             logicalpartition_object = PowerOffPartition.PowerOffPartition("LogicalPartition")
                             logicalpartition_object.poweroff_Partition(ip,
                                                                        selected_logicalpartition_object,
                                                                        x_api_session)
                             
                         else:
                            print("\nTry again using valid option")
                     except IndexError :
                         print("\nTry again using valid option")
                         
                 else:
                     log_object.log_warn("No Partitions are in active state")
                 
            elif x == 6:
                #object creation and method call to Modify Logical Partition
                 print("\nAvailable LogicalPartitions :")
                 selected_logicalPartition_object = get_selectedobject(object_list)
                 if selected_logicalpartition_object != None:
                     print("\nLogical partition memory attributes are modified as maximum ,minimum ,desired memory = 512") 
                     modify_logicalpartition_object = ModifyPartition.ModifyPartition("LogicalPartition")
                     result = modify_logicalpartition_object.modify_Partition(ip,selected_logicalPartition_object,x_api_session)
                     if result:
                         print("\nModifications are updated successfully")
                     else:
                         log_object.log_error("Error occured while updating the modifications.Verify \
                               whether the partitions are in running or not activated state before updating it")
                 
            elif x == 7:
                      os.system("cls")
                      return 1
            elif x == 8:
                      os.system("cls")
                      return 2
            elif x == 9:
                      os.system("cls")
                      return 3
            elif x == 11:
                sys.exit(1)
            else:
                    print("\nTry again using valid option")
            back_to_menu()
                          
                
             
    elif n == 2:
        #LogicalPartition Profile operations
        while True:
             print ("\n\n","LogicalPartition Profile".center(50))
             print_list = ['List','Create',
                           'Modify','Return to LogicalPartition Menu',
                           'Return to ManagedSystem Menu','Return to MainMenu',
                           'Help','Exit']
             
             #select any one LogicalPartitionProfile operation
             x1 = int(print_obj.print_on_screen(print_list))
             try:
                 if x1 > 0 and  x1 < 4:
                     print("\nAvailable LogicalPartitions :")
                     logicalpartition_object = ListLogicalPartition.ListLogicalPartition()
                     object_list = logicalpartition_object.\
                                  list_LogicalPartition(ip, managedsystem_uuid,
                                                         x_api_session)
                     list_logicalpartitionprofile_object = ListLogicalPartitionProfile.\
                                                           ListLogicalPartitionProfile("LogicalPartition")
                     selected_logicalpartition_object=get_selectedobject(object_list)
                    
                 if x1 == 1:
                     # object creation and method call to list all profiles for selected LPAR
                    if selected_logicalpartition_object != None:
                        partition_id =selected_logicalpartition_object.PartitionUUID.value()
                        profile_object_list = list_logicalpartitionprofile_object.\
                                     list_LogicalPartitionProfile(ip,partition_id,
                                                                   x_api_session)
                        for i in range(0,len(profile_object_list)):
                             list_logicalpartitionprofile_object.\
                                                print_logicalpartitionprofile_attributes(profile_object_list[i])
                    
                 elif x1 == 2:
                     # object creation and method call to create LPAR Profile
                     if selected_logicalpartition_object != None:
                         print("\nLogical Partition profile will be created with Following configruations,",
                               "\n maximum,mimimum and desired memory = 256",
                               "\nprofile type = REG_LPAR_PROFILE_TYPE")
                         create_logicalpartitionprofile_object = CreateLogicalPartitionProfile.\
                                                                 CreateLogicalPartitionProfile("LogicalPartition")
                         created_logicalpartitionprofile_object = create_logicalpartitionprofile_object.\
                                                                  create_LogicalPartitionProfile(ip,
                                                                                                 selected_logicalpartition_object,
                                                                                                 x_api_session)
                         if created_logicalpartitionprofile_object != None :
                             print("\nProfile %s Created Successfully\n"%(created_logicalpartitionprofile_object.ProfileName.value()))
                             list_logicalpartitionprofile_object.\
                                            print_logicalpartitionprofile_attributes(created_logicalpartitionprofile_object)
                         
                 elif x1 == 3:
                     # object creation and method call to Modify selected Profile
                      if selected_logicalpartition_object != None:
                          partition_id =selected_logicalpartition_object.PartitionUUID.value()
                          profile_object_list = list_logicalpartitionprofile_object.\
                                     list_LogicalPartitionProfile(ip,partition_id,
                                                                   x_api_session)
                          print("\nAvailable LogicalPartitionProfile:")
                          for i in range(0,len(profile_object_list)):
                               print("%s.%s"%(i+1,profile_object_list[i].ProfileName.value()))
                          try:
                              ch=int(input("\nselect any profile index to modify :"))
                              print("\nLogical partition profile memory attributes are modified as maximum ,minimum ,desired memory = 512")
                              modify_logicalpartitionprofile_object = ModifyLogicalPartitionProfile.\
                                                                      ModifyLogicalPartitionProfile("LogicalPartition")
                              modify_bool = modify_logicalpartitionprofile_object.\
                                            modify_LogicalPartitionProfile(ip,
                                                                           partition_id,
                                                                           profile_object_list[ch-1],
                                                                           x_api_session)
                              if modify_bool:
                                  print("\nUpdations to the profile are made Successfully")
                              else:
                                  log_object.log_error("\nError occured while updating")
                          except IndexError :
                              print("\nTry again using valid option")
                          
                 elif x1 == 4:
                      os.system("cls")
                      return 1
                 elif x1 == 5:
                      os.system("cls")
                      return 2
                 elif x1 == 6:
                      os.system("cls")
                      return 3
                 elif x1 == 8:
                     sys.exit(1)
                 else:
                    print("\nTry again using valid option")
                 back_to_menu()         
             except IndexError :
                 log_object.log_warn("No LogicalPartition Available")
                 back_to_menu()
            
            
    elif n == 3:
        #ClientNetworkAdapter operations
        while True:
            print ("\n\n","ClientNetworkAdapter".center(50))
            print_list = ['List','Create','Return to LogicalPartition Menu',
                          'Return to ManagedSystem Menu','Return to MainMenu','Help','Exit']
            #select any ClientNetworkAdapter operation
            x1 = int(print_obj.print_on_screen(print_list))
            if x1 > 0 and x1 < 3 :
                print("\nAvailable LogicalPartitions :")
                logicalpartition_object = ListLogicalPartition.ListLogicalPartition()
                object_list = logicalpartition_object.\
                                  list_LogicalPartition(ip, managedsystem_uuid,
                                                         x_api_session)
                selected_logicalpartition_object=get_selectedobject(object_list)
            if x1 == 1:
                #object creation and method call to list all client network adapters available in th selected LPAR
                if selected_logicalpartition_object != None:
                    logicalpartition_id = selected_logicalpartition_object.Metadata.Atom.AtomID.value()
                    list_clientnetwork_adapter_object = ListClientNetworkAdapter.ListClientNetworkAdapter()
                    clientnetwork_adapter_list = list_clientnetwork_adapter_object.\
                                                 list_clientnetwork_adapter(ip,
                                                                            logicalpartition_id,
                                                                            x_api_session)
                    try:
                        for clientnetwork_adapter in clientnetwork_adapter_list:
                            list_clientnetwork_adapter_object.print_clientnetwork_adapter_attributes(clientnetwork_adapter)
                    except TypeError:
                        log_object.log_warn("\nNo ClientNetworkAdapters are Available")
            elif x1 == 2:
                #object creation and method call to create client network adapter
               if selected_logicalpartition_object != None: 
                    logicalpartition_id = selected_logicalpartition_object.Metadata.Atom.AtomID.value()
                    client_networkadapter_object = CreateClientNetworkAdapter.\
                                                   CreateClientNetworkAdapter()
                    client_networkadapter_object.create_clientnetwork_adapter(ip,
                                                                              logicalpartition_id ,
                                                                              x_api_session)
            elif x1 == 3:
                      os.system("cls")
                      return 1
            elif x1 == 4:
                      os.system("cls")
                      return 2
            elif x1 == 5:
                      os.system("cls")
                      return 3
            elif x1 == 7:
                sys.exit(1)
            else:
                    print("\nTry again using valid option")
            back_to_menu()
    elif n == 4:
        #virtual scsi adapter operations
        while True:
            print ("\n\n","VirtualSCSIClientAdapter".center(50))
            print_list = ['List','Create','Return to LogicalPartition Menu',
                          'Return to ManagedSystem Menu','Return to MainMenu','Help','Exit']
            #select any VirtualSCSIClientAdapter operation
            x1 = int(print_obj.print_on_screen(print_list))
            if x1 > 0 and x1 < 3:
                print("\nAvailable LogicalPartitions :")
                logicalpartition_object = ListLogicalPartition.\
                                          ListLogicalPartition()
                object_list = logicalpartition_object.\
                                  list_LogicalPartition(ip,
                                                        managedsystem_uuid,
                                                         x_api_session)
                selected_logicalpartition_object=get_selectedobject(object_list)
                
            if x1 == 1:
                #object creation and method call to list all virtual scsi adapters in the selected lpar
                if selected_logicalpartition_object != None:
                    lpar_id = selected_logicalpartition_object.Metadata.Atom.AtomID.value()
                    vscsi_list_object = ListVirtualSCSIClientAdapter.\
                                        ListVirtualSCSIClientAdapter()
                    object_list = vscsi_list_object.list_virtualscsi_clientadapter(ip,
                                                                                   lpar_id,
                                                                                   x_api_session)
                    if object_list != None:
                        print("\nDetails of Available VirtualSCSIClientAdapters  :",
                              "\n--------------------------------------------------")
                        for i in range(0,len(object_list)):
                            vscsi_list_object.print_vscsi_attributes(object_list[i])
                    else :
                        log_object.log_warn("There are No VirtualSCSIClientAdapters in the selected LogicalPartition")
            elif x1 == 2:
                #object creation and method call to create a virtual scsii adapter in the selected lpar
                if selected_logicalpartition_object != None:                    
                    lpar_id = selected_logicalpartition_object.Metadata.Atom.AtomID.value()
                    vscsi_create_object = CreateVirtualSCSIClientAdapter.\
                                          CreateVirtualSCSIClientAdapter()
                    vscsi_create_object.create_vscsi_clientadapter(ip,
                                                                   lpar_id,
                                                                   x_api_session)
                       
            elif x1 == 3:
                      os.system("cls")
                      return 1
            elif x1 == 4:
                      os.system("cls")
                      return 2
            elif x1 == 5:
                      os.system("cls")
                      return 3
            elif x1 == 7:
                sys.exit(1)
            else:
                    print("\nTry again using valid option")
            back_to_menu()
                    
    elif n == 5:
        while True:
            #virtual fibre channel adapter operations
            print ("\n\n","VirtualFibreChannelClientAdapter".center(50))
            print_list = ['List','Create','Return to LogicalPartition Menu',
                          'Return to ManagedSystem Menu','Return to MainMenu','Help','Exit']
            #select any VirtualFibreChannelClientAdapter operation
            x1 = int(print_obj.print_on_screen(print_list))
            if x1 > 0 and x1 < 3 :
                print("\nAvailable LogicalPartitions :")
                logicalpartition_object = ListLogicalPartition.\
                                          ListLogicalPartition()
                object_list = logicalpartition_object.\
                                  list_LogicalPartition(ip,
                                                        managedsystem_uuid,
                                                        x_api_session)
                selected_logicalpartition_object=get_selectedobject(object_list)
            if x1 == 1:
                # object creation and method call to list all virtual fibre channel adapters in the selected lpar
                if selected_logicalpartition_object != None:
                    lpar_id = selected_logicalpartition_object.Metadata.Atom.AtomID.value()
                    vfc_list_object = ListVirtualFibreChannelClientAdapter.\
                                      ListVirtualFibreChannelClientAdapter()
                    object_list = vfc_list_object.\
                                  list_virtualfibrechannel_clientadapter(ip,
                                                                         lpar_id,
                                                                         x_api_session)
                    if object_list != None:
                        print("\nDetails of Available VirtualFibreChannelClientAdapters  :",
                              "\n--------------------------------------------------")
                        for i in range(0,len(object_list)):
                            vfc_list_object.print_virtualfibrechannel_attributes(object_list[i])
                    else :
                        log_object.log_warn("There are No VirtualFibreChannelClientAdapters in the selected LogicalPartition")
                        
            elif x1 == 2:
                #object creation and method call to create virtual fibre channel adapter in the selected lpar
                if selected_logicalpartition_object != None:
                    lpar_id = selected_logicalpartition_object.Metadata.Atom.AtomID.value()
                    virtualfibrechannel_create_object = CreateVirtualFibreChannelClientAdapter.\
                                                        CreateVirtualFibreChannelClientAdapter()
                    virtualfibrechannel_create_object.create_virtualfibrechannel_clientadapter(ip,
                                                                                               lpar_id,
                                                                                               x_api_session)
            elif x1 == 3:
                      os.system("cls")
                      return 1
            elif x1 == 4:
                      os.system("cls")
                      return 2
            elif x1 == 5:
                      os.system("cls")
                      return 3
            elif x1 == 7:
                sys.exit(1)
            else:
                    print("\nTry again using valid option")
            back_to_menu()
            
    elif n == 6:
        #SRIOV ethernet Logical Port operations
        while True:
            print ("\n\n","SRIOV Ethernet Logical Port".center(50))
            print_list = ['List','Create','Clear Statistics','Modify',
                          'Return to LogicalPartition Menu',
                          'Return to ManagedSystem Menu',
                          'Return to MainMenu','Help','Exit']
            x1 = int(print_obj.print_on_screen(print_list))
            if x1 > 0 and x1 < 5 :
                print("\nAvailable LogicalPartitions :")
                logicalpartition_object = ListLogicalPartition.ListLogicalPartition()
                object_list = logicalpartition_object.\
                                  list_LogicalPartition(ip,
                                                        managedsystem_uuid,
                                                         x_api_session)
                selected_logicalpartition_object = get_selectedobject(object_list)
                if selected_logicalpartition_object != None:
                    lpar_uuid = selected_logicalpartition_object.Metadata.Atom.AtomID.value()
                
            if x1 == 1:
                #object creation and method call to list all SRIOV Ethernet Logical Port
                if selected_logicalpartition_object != None:                
                    sriov_logicalPort = ListSRIOVLogicalPort.\
                                        ListSRIOVLogicalPort()
                    sriov_list = sriov_logicalPort.list_sriov_logical_port(ip,
                                                                           lpar_uuid,
                                                                           x_api_session)
                    try:
                        for i in range(0,len(sriov_list)):
                            sriov_logicalPort.print_sriov_logical_port(sriov_list[i])
                    except (TypeError , AttributeError)as e:
                         log_object.log_warn("No SRIOV LogicalPorts are available")
                         
            elif x1 == 2:
                #object creation and method call to create SRIOV Ethernet Logical Port
                if selected_logicalpartition_object != None:                
                    create_sriov_logicalport = CreateSRIOVLogicalPort.\
                                               CreateSRIOVLogicalPort()
                    create_sriov_logicalport.create_sriov_logicalport(ip,
                                                                      lpar_uuid,
                                                                      x_api_session)

            elif x1 == 3:
                #object creation and method call to Clear statistics of SRIOV Ethernet Logical Port
                if selected_logicalpartition_object != None:                
                    sriov_logicalPort = ListSRIOVLogicalPort.ListSRIOVLogicalPort()
                    sriov_list = sriov_logicalPort.list_sriov_logical_port(ip,
                                                                           lpar_uuid,
                                                                           x_api_session)
                    try:
                        for i in range(0,len(sriov_list)):
                            print("%s.ConfigurationID %s"%(i+1,sriov_list[i].ConfigurationID.value()))
                        ch = int(input("Select a SRIOV Port to clear statistics :"))
                        if ch > 0 and ch <= len(sriov_list):
                            sriov_uuid = sriov_list[ch-1].Metadata.Atom.AtomID.value()
                            clear_statistics = ClearSRIOVLogicalPortStatistics.\
                                               ClearSRIOVLogicalPortStatistics()
                            clear_statistics.clear_sriov_logicalport_statistics(ip,
                                                                                lpar_uuid,
                                                                                sriov_uuid,
                                                                                x_api_session)
                        else:
                            print("\nTry again using valid option")
                    except (TypeError , AttributeError)as e:
                         log_object.log_warn("No SRIOV LogicalPorts are available")
                         
            elif x1 == 4:
                #object creation and method call to modify SRIOV Ethernet Logical Port
                if selected_logicalpartition_object != None:                
                    sriov_logicalPort = ListSRIOVLogicalPort.ListSRIOVLogicalPort()
                    sriov_list = sriov_logicalPort.list_sriov_logical_port(ip,
                                                                           lpar_uuid,
                                                                           x_api_session)
                    try:
                        for i in range(0,len(sriov_list)):
                            print("%s.ConfigurationID %s"%(i+1,sriov_list[i].ConfigurationID.value()))
                        ch = int(input("Select a SRIOV Port to modify :"))
                        if ch > 0 and ch <= len(sriov_list):
                            modify_sriov = ModifySRIOVEthernetLogicalPort.ModifySRIOVEthernetLogicalPort()
                            modify_sriov.modify_sriov_logicalport(ip,
                                                                  lpar_uuid,
                                                                  sriov_list[ch-1],
                                                                  x_api_session)
                    except (TypeError , AttributeError)as e:
                         log_object.log_warn("No SRIOV LogicalPorts are available")
                         print(e)
                         
            elif x1 == 5:
                      os.system("cls")
                      return 1
            elif x1 == 6:
                      os.system("cls")
                      return 2
            elif x1 == 7:
                      os.system("cls")
                      return 3
            elif x1 == 9 :
                sys.exit(1)
            else:
                    print("\nTry again using valid option")
            back_to_menu()
