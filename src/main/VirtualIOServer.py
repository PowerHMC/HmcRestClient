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
from src.virtual_io_server import ListVirtualIOServer, \
                                  VirtualSCSIMapping, \
                                  VirtualFibreChannelMapping
from src.virtual_io_server.volume_group import CreateVolumeGroup, \
                                               ListVolumeGroup, \
                                               ModifyVolumeGroup
from src.partition_operation_util import PowerOnPartition,\
                                     PowerOffPartition,\
                                     ModifyPartition, \
                                     CreatePartition
                                                         
from src.logical_partition_profile import ListLogicalPartitionProfile,\
                                          CreateLogicalPartitionProfile,\
                                          ModifyLogicalPartitionProfile
from src.logical_partition import ListLogicalPartition
import sys
import os

#####################
# VIRTUAL IO SERVER
####################

def virtualioserver_children(n1, managedsystem_uuid, ip, x_api_session):
    """
    This function provides a detailed view of the virtualIOserver

    Args:
     n1 : variable for client selected choices
     managedsystem_uuid : The unique id of the Managed system
     ip : ip address of hmc
     x_api_session : session to be used

    """
    
    os.system("cls")
    st = 'y'
    n = n1
    
            
    if n == 1:
        while True:
            print ("\n\n","VirtualIOServer operations".center(50))
            print_list = ['List','Create','Modify',
                          'Poweron','Poweroff','Return to vios menu',
                          'Return to ManagedSystem menu','Return to MainMenu','Help','Exit' ]
            #select any VirtualIOServer operation
            x = int(print_obj.print_on_screen(print_list) )
            if x in [1,3,6]:
                print("\nAvailable VirtualIOServers : ")
                virtualioserver_object = ListVirtualIOServer.ListVirtualIOServer()
                object_list = virtualioserver_object.\
                              list_VirtualIOServer(ip, managedsystem_uuid,
                                                              x_api_session)
                selected_vios = get_selectedobject(object_list)
            try:
                if x == 1:
                    #object creation and method call to list the details of the selected vios 
                   if selected_vios != None:
                       virtualioserver_object.print_virtualioserver_attributes(selected_vios)
                   
                elif x == 2:
                     #object creation and method call to create vios
                    try:
                         print("\nVirtualIOServer will be created with Following configruations,\n maximum,mimimum and desired memory = 256",
                               "\nShared processors,Minimum,Desired and maximum processing units = 0.5")
                         logicalpartition_object = CreatePartition.CreatePartition("VirtualIOServer")
                         created_logicalpartition_object = logicalpartition_object.create_Partition(ip,managedsystem_uuid,x_api_session)
                         print("\nPartition %s Created Successfully\n"%(created_logicalpartition_object.PartitionName.value()))
                    except (TypeError,AttributeError) :
                         log_object.log_error("Error in VIOS creation")
                 
                elif x == 3:
                     #object creation and method call to modify existing vios memory attributes
                     if selected_vios != None:
                         print("\nVIOS memory attributes are modified as maximum ,minimum ,desired memory = 512") 
                         modify_logicalpartition_object = ModifyPartition.ModifyPartition("VirtualIOServer")
                         result = modify_logicalpartition_object.modify_Partition(ip,selected_vios,x_api_session)
                         if result:
                             print("\nModifications are updated successfully")
                         else:
                             log_object.log_error("Error occured while updating the modifications.Verify \
                                   whether the vios is in running or not activated state before updating it")
                elif x == 4:
                     #object creation and method call to poweron inactive vios
                     virtualioserver_object = ListVirtualIOServer.ListVirtualIOServer()
                     object_list = virtualioserver_object.\
                              list_VirtualIOServer(ip, managedsystem_uuid,
                                                              x_api_session)
                     print("\nList of VIOS in inactive state")
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
                                 selected_vios = inactive_object_list[ch]
                                 logicalpartition_object = PowerOnPartition.PowerOnPartition("VirtualIOServer")
                                 logicalpartition_object.poweron_Partition(ip,selected_vios,x_api_session)
                                 
                             else :
                                print("\nTry again using valid option")
                        except IndexError :
                             print("\nTry again using valid option")
                     else:
                         log_object.log_warn("No Partitions are in inactive state")
                elif x == 5:
                     #object creation and method call to poweroff selected active state vios
                         virtualioserver_object = ListVirtualIOServer.ListVirtualIOServer()
                         object_list = virtualioserver_object.\
                              list_VirtualIOServer(ip, managedsystem_uuid,
                                                              x_api_session)
                         print("\nList of VIOS in active state")
                         k = 0
                         active_object_list = []
                         for i in range(0,len(object_list)):
                                if object_list[i].PartitionState.value() == "open firmware" or object_list[i].PartitionState.value() == "running":
                                     k = k+1
                                     print("%s.%s" % (k,object_list[i].PartitionName.value()))
                                     active_object_list.append(object_list[i])
                         if k>0 :
                             try:
                                 c = int(input("\nSelect any VIOS index the operation to be performed:"))
                                 if c > 0:
                                     ch = c-1
                                     selected_vios = active_object_list[ch]
                                     logicalpartition_object = PowerOffPartition.PowerOffPartition("VirtualIOServer")
                                     logicalpartition_object.poweroff_Partition(ip,selected_vios,x_api_session)
                                 else:
                                    print("\nTry again using valid option")
                             except IndexError :
                                 print("\nTry again using valid option")
                elif x == 6:
                    os.system("cls")
                    return 1
                elif x == 7:
                    os.system("cls")
                    return 2
                elif x == 8:
                    os.system("cls")
                    return 3
                elif x == 10:
                    sys.exit(1)
                else:
                    print("\nTry again using valid option")
                back_to_menu()
                    
            except TypeError :
                log_object.log_warn("No VirtualIOServers Available")
                back_to_menu()
                
    elif n == 2:
        while True:
            print ("\n\n","LogicalPartitionProfile".center(50))
            print_list = ['List','Create','Modify','Return to vios menu',
                          'Return to ManagedSystem menu','Return to MainMenu',
                          'Help','Exit']
            #select any  LogicalPartitionProfile operation
            x1 = int(print_obj.print_on_screen(print_list))
            if x1 > 0  and x1 < 4:
                print("\nAvailable VirtualIOServers :")
                virtualioserver_object = ListVirtualIOServer.ListVirtualIOServer()
                object_list = virtualioserver_object.\
                              list_VirtualIOServer(ip, managedsystem_uuid,
                                                              x_api_session)
                selected_vios = get_selectedobject(object_list)
                list_logicalpartitionprofile_object=ListLogicalPartitionProfile.ListLogicalPartitionProfile("VirtualIOServer")
            if x1 == 1:
                 #object creation and method call to list the details of the selected vios profiles
              if selected_vios != None:
                   partition_id = selected_vios.PartitionUUID.value()
                   profile_object_list = list_logicalpartitionprofile_object.\
                                               list_LogicalPartitionProfile(ip,partition_id,x_api_session)
                   for i in range(0,len(profile_object_list)):
                       list_logicalpartitionprofile_object.\
                                         print_logicalpartitionprofile_attributes(profile_object_list[i])
                   
            elif x1 == 2:
                 #object creation and method call to create profile in the selected vios
                if selected_vios != None:
                    print("\nLogical Partition profile is created with Following configruations,\n maximum,mimimum and desired memory = 256",
                           "\nprofile type = REG_LPAR_PROFILE_TYPE")
                    create_logicalpartitionprofile_object = CreateLogicalPartitionProfile.\
                                                            CreateLogicalPartitionProfile("VirtualIOServer")
                    created_logicalpartitionprofile_object = create_logicalpartitionprofile_object.\
                                                             create_LogicalPartitionProfile(ip,selected_vios,x_api_session)
                    if created_logicalpartitionprofile_object != None:
                        print("\nProfile %s Created Successfully\n"%(created_logicalpartitionprofile_object.\
                                                                     ProfileName.value()))
                        list_logicalpartitionprofile_object.\
                                    print_logicalpartitionprofile_attributes(created_logicalpartitionprofile_object)
               
            elif x1 == 3:
                 #object creation and method call to modify selected profiles memory attributes
                if selected_vios != None:
                    partition_id = selected_vios.PartitionUUID.value()
                    profile_object_list = list_logicalpartitionprofile_object.\
                    list_LogicalPartitionProfile(ip,partition_id, x_api_session)
                    print("\nAvailable LogicalPartitionProfile:")
                    for i in range(0,len(profile_object_list)):
                        print("%s.%s"%(i+1,profile_object_list[i].ProfileName.value()))
                    try:
                        ch=int(input("\nselect any profile index to modify :"))
                        print("\nLogical partition profile memory attributes are modified as maximum ,minimum ,desired memory = 512")
                        modify_logicalpartitionprofile_object = ModifyLogicalPartitionProfile.\
                                                                ModifyLogicalPartitionProfile("VirtualIOServer")
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
            elif x1 == 7:
                sys.exit(1)
            else:
                    print("\nTry again using valid option")
            back_to_menu()
                
    elif n == 3:
        while True:
            print ("\n\n","VolumeGroup".center(50))
            print_list = ['List','Create','Modify','Return to vios menu',
                          'Return to ManagedSystem menu',
                          'Return to MainMenu','Help','Exit']
            x1 = int(print_obj.print_on_screen(print_list))
            if x1 > 0 and x1 < 4:
                print("\nAvailable VirtualIOServers : ")
                virtualioserver_object = ListVirtualIOServer.ListVirtualIOServer()
                object_list = virtualioserver_object.\
                              list_VirtualIOServer(ip, managedsystem_uuid,
                                                              x_api_session)
                selected_vios = get_selectedobject(object_list)
            #select any VolumeGroup operation
            if x1 == 1:
                 #object creation and method call to list the details of the volume group
                if selected_vios != None:
                    vios_id = selected_vios.Metadata.Atom.AtomID.value()
                    print("\nAvailable VolumeGroups :")
                    volumegroup_list_object = ListVolumeGroup.ListVolumeGroup()
                    volumegroup_list = volumegroup_list_object.list_volumegroup(ip, vios_id,
                                                                                x_api_session)
                    try:
                        for i in range(0,len(volumegroup_list)):
                            print("%s.%s"%(i+1,volumegroup_list[i].GroupName.value()))
                        ch = int(input("\nEnter your choice :"))
                        volumegroup_list_object.print_volumegroup_attributes(volumegroup_list[ch-1])
                    except TypeError:
                        log_object.log_warn("No VolumeGroups are available")
                    except IndexError:
                        print("\nTry using vaild option")
                            
                back_to_menu()
                
            elif x1 == 2:
                 #object creation and method call to create a volume group
                vios_uuid = selected_vios.Metadata.Atom.AtomID.value()
                print("\nVolumeGroup will be created with one PhysicalVolume,the name of the disk is hardcoded")
                volumegroup_object = CreateVolumeGroup.CreateVolumeGroup()
                volumegroup_object.create_volumegroup(ip, vios_uuid, x_api_session)
                back_to_menu()
                
            elif x1 == 3:
                 #object creation and method call to modify volume group
                 #by adding a physical volume or creating a virtual disk
                vios_id = selected_vios.Metadata.Atom.AtomID.value()
                volumegroup_modify_object = ModifyVolumeGroup.ModifyVolumeGroup()
                print("\nAvailable VolumeGroups :")
                volumegroup_list_object = ListVolumeGroup.ListVolumeGroup()
                volumegroup_list = volumegroup_list_object.list_volumegroup(ip, vios_id,
                                                                                x_api_session)
                if  volumegroup_list != None:
                    for i in range(0,len(volumegroup_list)):
                         print("%s.%s"%(i+1,volumegroup_list[i].GroupName.value()))
                    choice = int(input("\nEnter your choice :"))
                    selected_volumegroup = volumegroup_list[choice-1]
                    ch = int(input("\n1.Add PhysicalVolume to VolumeGroup\n2.Create VirtualDisk in VolumeGroup\nEnter your choice :"))
                    if ch == 1:
                        volumegroup_modify_object.add_physicalvolume(ip, vios_id, x_api_session, selected_volumegroup)
                    elif ch == 2:
                        print("\nVirtualDisk of size VolumeGroup_size/2 will be created")
                        volumegroup_modify_object.add_virtualdisk(ip, vios_id, x_api_session, selected_volumegroup)
                    else:
                        print("\nTry again using valid option")
                    
                else :
                    log_object.log_warn("No VolumeGroups are available")
                back_to_menu()
                
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
    

    elif n == 4:
        #creates a vscsi mapping from selected vios to selected lpar
        print("\nAvailable VirtualIOServers : ")
        virtualioserver_object = ListVirtualIOServer.ListVirtualIOServer()
        object_list = virtualioserver_object.\
                      list_VirtualIOServer(ip, managedsystem_uuid,
                                                      x_api_session)
        selected_vios = get_selectedobject(object_list)
        print("\nAvailable LogicalPartitions : ")
        logicalpartition_object = ListLogicalPartition.ListLogicalPartition()
        logicalpartition_object_list = logicalpartition_object.\
                      list_LogicalPartition(ip, managedsystem_uuid,
                                             x_api_session)
        selected_lpar = get_selectedobject(logicalpartition_object_list)
        if selected_vios != None and selected_lpar !=None:
            vscsi_object = VirtualSCSIMapping.VirtualSCSIMapping()
            lpar_id = selected_lpar.Metadata.Atom.AtomID.value()
            vscsi_object.create_vscsi_mapping(ip,managedsystem_uuid,x_api_session,selected_vios,lpar_id)
        back_to_menu()
        return 1
    elif n == 5:
        #creates a virtual fibre channel mapping from selected vios to selected lpar
        print("\nAvailable VirtualIOServers : ")
        virtualioserver_object = ListVirtualIOServer.ListVirtualIOServer()
        object_list = virtualioserver_object.\
                      list_VirtualIOServer(ip, managedsystem_uuid,
                                                      x_api_session)
        selected_vios = get_selectedobject(object_list)
        print("\nAvailable LogicalPartitions : ")
        logicalpartition_object = ListLogicalPartition.ListLogicalPartition()
        logicalpartition_object_list = logicalpartition_object.\
                      list_LogicalPartition(ip, managedsystem_uuid,
                                             x_api_session)
        selected_lpar = get_selectedobject(logicalpartition_object_list)
        if selected_vios != None and selected_lpar !=None:
            vfc_object = VirtualFibreChannelMapping.VirtualFibreChannelMapping()
            lpar_id = selected_lpar.Metadata.Atom.AtomID.value()
            vfc_object.create_virtualfibrechannel_mapping(ip, managedsystem_uuid, x_api_session, selected_vios, lpar_id)
        back_to_menu()
        return 1
            
