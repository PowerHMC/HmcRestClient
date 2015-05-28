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
from src.cluster import ListCluster, \
                        CreateCluster, \
                        ModifyCluster, \
                        CreateLogicalUnit, \
                        DeleteCluster, \
                        DeleteLogicalUnit, \
                        LULinkedClone
from src.shared_storage_pool import ListSharedStoragePool, \
                                    ModifySharedStoragePool


def cluster_menu(choice, ip, x_api_session):
    """
    controls the cluster menu 
    Args:
      choice:Option to perform corresponding function
      ip : ip address of HMC
      x_api_session : session to be used
    """
    if choice == 1:
        
        #object creation and method call to List the details of all available cluster
        cluster_object = ListCluster.ListCluster()
        ssp_object = ListSharedStoragePool.ListSharedStoragePool()
        object_list = cluster_object.list_cluster(ip, x_api_session)
        
        if object_list != None:
            for objects in object_list:
                cluster_object.print_cluster_attributes(objects)
                cluster_id = objects.Metadata.Atom.AtomID.value()
                ssp_object_list = ssp_object.list_shared_storagepool(ip, cluster_id,
                                                                     x_api_session)
                ssp_object.print_shared_storagepool_attributes(ssp_object_list[0])
        else  :
           log_object.log_warn("No clusters are available")
           
    elif choice == 2:
        
        #object creation and method call to create a cluster for a given vios
        print("\nVIOS Selected by the user will be added as a node to cluster",
              "The Physical disk for Virtual Repository disk and SSP are hardcoded.",
              "The ssp will be created with 1 physical volume")
        list_object = ListModule.ListModule()
        vios_content_type = "application/vnd.ibm.powervm.uom+xml;Type=VirtualIOServer"
        vios_list = list_object.listing("uom", ip,
                                        "VirtualIOServer", vios_content_type,
                                        "VirtualIOServer", x_api_session)
        if vios_list != None:
            print("\nAvailable Virtual IO Serevers :")
            for i in range (0,len(vios_list)):
                print("%s.%s"%(i+1,vios_list[i].PartitionName.value()))
            ch = int(input("\nselect a vios to be added to the cluster :"))
            vios_id = vios_list[ch-1].Metadata.Atom.AtomID.value()
            create_cluster_object = CreateCluster.CreateCluster()
            create_cluster_object.create_cluster(ip, x_api_session, vios_id)
        else :
            log_object.log_warn("There are no VirtualIOServers")
    
    elif choice == 3:
        
        #provides options in modifying a cluster
        modify_cluster_object = ModifyCluster.ModifyCluster()
        cluster_object = ListCluster.ListCluster()
        object_list = cluster_object.list_cluster(ip, x_api_session)
        if object_list != None:
            for i in range(0,len(object_list)):
                print("%s.%s"%(i+1,object_list[i].ClusterName.value()))
            ch = int(input("Select a cluster to be modified :"))
            try:
                selected_cluster = object_list[ch-1]
                print_list = ['Add a node to cluster','Add a PhysicalVolume to ssp',
                              'Create LogicalUnit','Delete LogicalUnit','LULinkedClone']
                modify_choice = int(print_obj.print_on_screen(print_list))
                
                if modify_choice == 1:
                    #add a node to cluster
                    print("\nVIOS Selected by the user will be added as a node to cluster")
                    list_object = ListModule.ListModule()
                    vios_content_type = "application/vnd.ibm.powervm.uom+xml;Type=VirtualIOServer"
                    vios_list = list_object.listing("uom", ip, "VirtualIOServer", vios_content_type,
                                                    "VirtualIOServer",x_api_session)
                    if vios_list != None:
                        print("\nAvailable Virtual IO Serevers :")
                        for i in range (0,len(vios_list)):
                            print("%s.%s"%(i+1,vios_list[i].PartitionName.value()))
                        ch = int(input("\nselect a vios to be added to the cluster :"))
                        vios_id = vios_list[ch-1].Metadata.Atom.AtomID.value()
                        modify_cluster_object.add_node(ip, x_api_session, selected_cluster, vios_id)
                        
                elif modify_choice == 2:
                    #Add a PhysicalVolume to ssp
                    print("\nThe Physical volume selected by the user will be added to ssp if it is not in use")
                    physicalvolumes = []
                    ssp_modify_object = ModifySharedStoragePool.ModifySharedStoragePool()
                    ssp_object = ListSharedStoragePool.ListSharedStoragePool()
                    cluster_id = selected_cluster.Metadata.Atom.AtomID.value()
                    ssp_object_list = ssp_object.list_shared_storagepool(ip, cluster_id, x_api_session)
                    print("\nSharedStoragePool of the selected cluster :%s"%(ssp_object_list[0].StoragePoolName.value()))
                    http_object = HTTPClient.HTTPClient("uom", ip, "ManagedSystem",
                                                        "application/vnd.ibm.powervm.uom+xml; type=VirtualIOServer",
                                                         x_api_session)
                    for node in selected_cluster.Node.Node:
                        http_object.HTTPGet(url=node.VirtualIOServer.href)
                        root = etree.fromstring(http_object.response.content)
                        header_object = HmcHeaders.HmcHeaders("uom")
                        ns = header_object.ns["xmlns"]
                        entries = root.findall(".//{%s}PhysicalVolume"%(ns))
                        if entries != []:
                            for entry in entries :
                                physicalvolume_object = UOM.CreateFromDocument(etree.tostring(entry))
                                physicalvolumes.append(physicalvolume_object)
                    try:
                        print("\nAvailable PhysicalVolumes  :")
                        for i in range(0,len(physicalvolumes)):
                            print("%s.%s"%(i+1,physicalvolumes[i].VolumeName.value()))
                        ch = int(input("\nselect a physicalvolume to be added :" ))
                        if ch > 0 and ch < len(physicalvolumes):
                            ssp_modify_object.add_physicalvolume(ip, x_api_session,
                                                                 ssp_object_list[0],
                                                                 physicalvolumes[ch-1])
                        else:
                            print("\nTry using valid option")
                    except IndexError :
                                log_object.log_warn("No PhysicalVolumes are available")
                    
                elif modify_choice == 3:                    
                    #Create LogicalUnit
                    print("\nLogicalUnit of size 1GB and Thin type LU will be created")
                    logicalunit_object = CreateLogicalUnit.CreateLogicalUnit()
                    logicalunit_object.create_logicalunit(ip, x_api_session,
                                                          selected_cluster)
                    
                elif modify_choice == 4:
                    #delete  LogicalUnit
                    ssp_object = ListSharedStoragePool.ListSharedStoragePool()
                    cluster_id = selected_cluster.Metadata.Atom.AtomID.value()
                    ssp_object_list = ssp_object.list_shared_storagepool(ip,
                                                                         cluster_id,
                                                                         x_api_session)
                    lu_list = ssp_object.print_logicalunit(ssp_object_list[0])
                    if lu_list != None:
                        logicalunit_name = input("Enter the name of the LogicalUnit to be deleted")
                        delete_logicalunit_object = DeleteLogicalUnit.DeleteLogicalUnit()
                        delete_logicalunit_object.delete_logicalunit(ip, ssp_object_list[0],
                                                                     x_api_session, logicalunit_name)
                    else:
                        log_object.log_warn("There are no Logical units")
                        
                elif modify_choice == 5:
                    #LULinkedClone
                    ssp_object = ListSharedStoragePool.ListSharedStoragePool()
                    cluster_id = selected_cluster.Metadata.Atom.AtomID.value()
                    ssp_object_list = ssp_object.list_shared_storagepool(ip, cluster_id,
                                                                         x_api_session)
                    lu_list = ssp_object.print_logicalunit(ssp_object_list[0])
                    if lu_list != None:
                        for i in range(0,len(lu_list)):
                            print("%s.%s"%(i+1,lu_list[i].UnitName.value()))
                        source_lu = int(input("select the source LU "))
                        try:
                            source_lu_udid = lu_list[source_lu-1].UniqueDeviceID.value()
                            dest_lu = int(input("select the destination LU "))
                            dest_lu_udid = lu_list[dest_lu-1].UniqueDeviceID.value()
                            linked_clone_object = LULinkedClone.LULinkedClone()
                            linked_clone_object.lu_linked_clone(ip, cluster_id, x_api_session,
                                                                source_lu_udid, dest_lu_udid)
                        except IndexError:
                            print("\nTry using valid option")
                else :
                    print("\nTry using valid option")
            except IndexError:
                            print("\nTry using valid option")
        else  :
             log_object.log_warn("No clusters are available")
    elif choice == 4:
        #object creation and method call to delete an existing cluster
        delete_cluster_object = DeleteCluster.DeleteCluster()
        cluster_object = ListCluster.ListCluster()
        cluster_object_list = cluster_object.list_cluster(ip, x_api_session)
        if cluster_object_list != None:
            for i in range(0,len(cluster_object_list)):
                print("%s.%s"%(i+1,cluster_object_list[i].ClusterName.value()))
            ch = int(input("Select a cluster to be modified :"))
            try:
                selected_cluster = cluster_object_list[ch-1]
                if selected_cluster != None:
                    cluster_id = selected_cluster.Metadata.Atom.AtomID.value()
                delete_cluster_object.delete_cluster(ip, cluster_id, x_api_session)
            except IndexError:
                print("Try again using valid option")
        else  :
             log_object.log_warn("No clusters are available")
    back_to_menu()
