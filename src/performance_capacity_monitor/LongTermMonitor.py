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

from src.performance_capacity_monitor import  JsonFilesDownload 
from src.utility import HMCClientLogger,HTTPClient
import json
import time
import feedparser
import sys
log_object=HMCClientLogger.HMCClientLogger(__name__)

ROOT = "ManagedSystem"
CONTENT_TYPE = "application/atom+xml"

class LongTermMonitor:

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

    def json_download_all_files(self, HTTP_object, feedparser_LTM, object_list):
        """
        downloads all the available json files for Long term metrics
        Args:
            HTTP_object : HTTP Request object carrying the headers and URL
            feedparser_LTM : feedparser object containing the entries of LTM
            object_list : Available VIOS object List
        """
        try:
            print("press ctrl+c to exit")
            for i in range(0,len(feedparser_LTM.entries)):
                json_url_link=feedparser_LTM.entries[i].links[0].href
                # Get the links for long term monitor json files and perform get request
                HTTP_object.HTTPGet(url=json_url_link)
                log_object.log_debug("response code for Long Term Monitor json file links %s" %(HTTP_object.response))
                if not HTTP_object.response_b:
                    continue
                # Downloading the json file
                JsonFilesDownload.json_file(feedparser_LTM.entries[i].title, HTTP_object.response.text)
        except KeyboardInterrupt:
            return 5



    def json_download_recent_files_phyp(self,HTTP_object,feedparser_LTM,object_list):
        """
        downloads the recent json files for Long term metrics PHYP
        Args:
            HTTP_object : HTTP Request object carrying the headers and URL
            feedparser_LTM : feedparser object containing the entries of LTM
            object_list : Available VIOS object List
        """
    
        timestamp_phyp=[]
        # get timestamps of all the json files of category phyp
        for j in range(0, len(feedparser_LTM.entries)):
            if feedparser_LTM.entries[j].category=="phyp":
                timestamp_phyp.append(feedparser_LTM.entries[j].links[0].href[154:160])
                timestamp_phyp.sort()
        for k in range(0, len(feedparser_LTM.entries)):
            if(feedparser_LTM.entries[k].category=="phyp" and feedparser_LTM.entries[k].links[0].href[154:160]==timestamp_phyp[len(timestamp_phyp)-1]):
                json_url=feedparser_LTM.entries[k].links[0].href
                #print (feedparser_LTM.entries[i].links[0].href)
                HTTP_object.HTTPGet(url=json_url)
                log_object.log_debug(HTTP_object.response)
                print("\nThe recent json file of Powerhypervisor : ")
                JsonFilesDownload.json_file(feedparser_LTM.entries[k].title, HTTP_object.response.text)
                break

    def json_download_recent_files_vios(self,HTTP_object,feedparser_LTM,object_list):
        """
        downloads  the recent json files for Long term metrics VIOS
        Args:
            HTTP_object : HTTP Request object carrying the headers and URL
            feedparser_LTM : feedparser object containing the entries of LTM
            object_list : Available VIOS object List
        """
        try:
            timestamp_vios=[]
            vios_names=self.get_virtualioserver_list(object_list)
            #print(object_list)
            for k in range(0,len(vios_names)):
                #print(vios_names[k])
                timestamp_vios.append([])
            for j in range(0,len(vios_names)):
                for i in range(0, len(feedparser_LTM.entries)):
                    if feedparser_LTM.entries[i].category==vios_names[j]:
                        timestamp_vios[j].append(feedparser_LTM.entries[i].links[0].href[156:162])
                        timestamp_vios[j].sort()
            for j in range(0,len(vios_names)):
                for i in range(0, len(feedparser_LTM.entries)):
                    if feedparser_LTM.entries[i].category==vios_names[j] and feedparser_LTM.entries[i].links[0].href[156:162]==timestamp_vios[j][len(timestamp_vios[j])-1]:
                        #print (feedparser_LTM.entries[i].links[0].href)
                        json_url=feedparser_LTM.entries[i].links[0].href
                        HTTP_object.HTTPGet(url=json_url)
                        log_object.log_debug(HTTP_object.response)
                        print("\nThe recent json file of VirtualIOserver :%s "%(vios_names[j]))
                        JsonFilesDownload.json_file(feedparser_LTM.entries[i].title, HTTP_object.response.text)
                        break
        except TypeError:
            log_object.log_warn("There are no VIOS available in the system")
        

    def get_virtualioserver_list(self,object_list):
       
        vios_names=[]
        for i in range(0,len(object_list)):
            vios_names.append("vios_%s"%(object_list[i].PartitionID.value()))
        
        return vios_names

    ########################################
    # GET THE LONG TERM MONITOR JSON FILES
    ########################################

    def get_longtermmonitor(self,object_list):
        '''
        This function collects the long term monitor metrics of the HMC
        '''
        choice="y"
        while choice=="y":
                flag = 6
                HTTP_object =HTTPClient.HTTPClient(self.service, self.ip, self.root, self.content_type, self.x_api_session)
                # Make a get request for Long Term Monitor
                HTTP_object.HTTPGet(append=self.managedsystem_id+"/RawMetrics/LongTermMonitor")
                if not HTTP_object.response_b:
                    log_object.log_warn("Long Term Monitor not Enabled\n")
                    return
                # The response of the get request is parsed using feedparser
                feedparser_LTM = feedparser.parse(HTTP_object.response.text)
                print("\n*******Options for Long Term Monitor Metrics*********\n")
                option = input("This happens in a loop that repeats every 30 seconds \n 1.Download all the available json files \n 2.Download the recently generated json files \n 3.quit\n choose an option: ")
                if option=="1":
                    flag = self.json_download_all_files(HTTP_object,feedparser_LTM,object_list)
                    if flag == 5:
                        continue
                    elif flag == 6:
                        print("Sleeps for 30 seconds")
                        time.sleep(30)
                        print("Refreshing after 30 seconds")
                elif option=="2":
                    self.json_download_recent_files_phyp(HTTP_object,feedparser_LTM,object_list)
                    #print(object_list)
                    self.json_download_recent_files_vios(HTTP_object,feedparser_LTM,object_list)
                    print("Sleeps for 30 seconds")
                    time.sleep(30)
                    print("Refreshing after 30 seconds")
                elif option == "3":
                    choice = "n"
        
            

        
        
        
        




#LongTermMonitor_object=LongTermMonitor('9.126.138.108','f8fbeb06-09e9-39a6-91e9-be80b39cae49',x_api_session)
#LongTermMonitor_object.get_longtermmonitor()            


                
                
        


