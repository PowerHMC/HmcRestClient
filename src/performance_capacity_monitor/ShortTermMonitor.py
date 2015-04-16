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

from src.performance_capacity_monitor import JsonFilesDownload 
from src.utility import HTTPClient, HMCClientLogger
import json
import time
import feedparser
log_object=HMCClientLogger.HMCClientLogger(__name__)

ROOT = "ManagedSystem"
CONTENT_TYPE = "application/atom+xml"


class ShortTermMonitor:

    def __init__(self, ip, managedsystem_id, x_api_session):
        """
        initializes root,content_type and services
        Args:
           ip : ip address of HMC
           managedsystem_id : UUID of ManagedSystem
           x_api_session : session to be used
        """
        self.service = "pcm"
        self.root = ROOT
        self.ip = ip
        self.managedsystem_id = managedsystem_id
        self.x_api_session = x_api_session
        self.content_type = CONTENT_TYPE

    
    def json_download_all_files(self, HTTP_object, feedparser_STM, object_list):
        """
        downloads all the available json files for Short term metrics
        Args:
            HTTP_object : HTTP Request object carrying the headers and URL
            feedparser_STM : feedparser object containing the entries of STM
            object_list : Available VIOS object List
        """
        try:
            print("press ctrl+c to exit")
            for i in range(0,len(feedparser_STM.entries)):
                json_url = feedparser_STM.entries[i].links[0].href
                # Get the links for short term monitor json files and perform get request
                HTTP_object.HTTPGet(url=json_url)
                log_object.log_debug("response code for Short Term Monitor json file links %s" %(HTTP_object.response))
                if not HTTP_object.response_b:
                    continue
                # Downloading the json file
                JsonFilesDownload.json_file(feedparser_STM.entries[i].title, HTTP_object.response.text)
        except KeyboardInterrupt:
            return 5


    def json_download_recent_files_phyp(self, HTTP_object, feedparser_STM, object_list):
        """
        downloads the recent json files for Short term metrics PHYP
        Args:
            HTTP_object : HTTP Request object carrying the headers and URL
            feedparser_STM : feedparser object containing the entries of STM
            object_list : Available VIOS object List
        """
    
        timestamp_phyp=[]
        # get timestamps of all the json files of category phyp
        for j in range(0, len(feedparser_STM.entries)):
            if feedparser_STM.entries[j].category=="phyp":
                timestamp_phyp.append(feedparser_STM.entries[j].links[0].href[154:160])
                timestamp_phyp.sort()
        for k in range(0, len(feedparser_STM.entries)):
            if(feedparser_STM.entries[k].category=="phyp" and feedparser_STM.entries[k].links[0].href[154:160]==timestamp_phyp[len(timestamp_phyp)-1]):
                #print (CreateFromDocument.entries[i].links[0].href)
                HTTP_object.HTTPGet(url=feedparser_STM.entries[k].links[0].href)
                log_object.log_debug(HTTP_object.response)
                print("\nThe recent json file of PowerHypervisor :")
                JsonFilesDownload.json_file(feedparser_STM.entries[k].title, HTTP_object.response.text)
                break
    


    def json_download_recent_files_vios(self, HTTP_object, feedparser_STM,object_list):
        """
        downloads the recent json files for Short term metrics VIOS
        Args:
            HTTP_object : HTTP Request object carrying the headers and URL
            feedparser_STM : feedparser object containing the entries of STM
            object_list : Available VIOS object List
        """
        try:
            timestamp_vios=[]

            vios_names=self.get_virtualioserver_list(object_list)
            for k in range(0,len(vios_names)):
                #print(vios_names[k])
                timestamp_vios.append([])
            for j in range(0,len(vios_names)):
                for i in range(0, len(feedparser_STM.entries)):
                    if feedparser_STM.entries[i].category==vios_names[j]:
                        timestamp_vios[j].append(feedparser_STM.entries[i].links[0].href[156:162])
                        timestamp_vios[j].sort()
            for j in range(0,len(vios_names)):
                for i in range(0, len(feedparser_STM.entries)):
                    if feedparser_STM.entries[i].category==vios_names[j] and feedparser_STM.entries[i].links[0].href[156:162]==timestamp_vios[j][len(timestamp_vios[j])-1]:
                        #print (CreateFromDocument.entries[i].links[0].href)
                        HTTP_object.HTTPGet(url=feedparser_STM.entries[i].links[0].href)
                        log_object.log_debug(HTTP_object.response)
                        print("\nThe recent json file of VirtualIOServer :%s "%(vios_names[j]))
                        JsonFilesDownload.json_file(feedparser_STM.entries[i].title, HTTP_object.response.text)
                        break
        except TypeError:
            log_object.log_warn("There are no VIOS available in the system")

    def get_virtualioserver_list(self,object_list):
        vios_names=[]
        for i in range(0,len(object_list)):
            vios_names.append("vios_%s"%(object_list[i].PartitionID.value()))

        return vios_names

    
    ########################################
    # GET THE SHORT TERM MONITOR JSON FILES
    ########################################
    
    def get_shorttermmonitor(self,object_list):
        ''' This function collects the short term monitor metrics of the HMC'''
        
        
        choice="y"
        while choice=="y":
            HTTP_object =HTTPClient.HTTPClient(self.service, self.ip, self.root, self.content_type, self.x_api_session)
            # Make a get request for short Term Monitor
            HTTP_object.HTTPGet(append=self.managedsystem_id+"/RawMetrics/ShortTermMonitor")
            if not HTTP_object.response_b:
                log_object.log_warn("short Term Monitor not Enabled %s\n"%(HTTP_object.response))
                return
            # The response of the get request is parsed using feedparser
            feedparser_STM = feedparser.parse(HTTP_object.response.text)
            print("\n******Options for short Term Monitor Metrics******\n")
            option = input("This happens in a loop that repeats every 30 seconds \n 1.Download all the available json files \n 2.Download the recently generated json files \n 3.quit\n choose an option: ")
            if option=="1":
                flag = self.json_download_all_files(HTTP_object,feedparser_STM,object_list)
                if flag == 5:
                    continue
                elif flag == 6:
                    print("Sleeps for 5 seconds")
                    time.sleep(5)
                    print("Refreshing after 5 seconds")
            elif option=="2":
                self.json_download_recent_files_phyp(HTTP_object,feedparser_STM,object_list)
                self.json_download_recent_files_vios(HTTP_object,feedparser_STM,object_list)
                print("Sleeps for 5 seconds")
                time.sleep(5)
                print("Refreshing after 5 seconds")
            elif option == "3":
                choice = "n"

        
            
        



