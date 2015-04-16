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
from src.utility import HTTPClient,HMCClientLogger
import json
import time
import feedparser
log_object=HMCClientLogger.HMCClientLogger(__name__)

ROOT = "ManagedSystem"
CONTENT_TYPE = "application/atom+xml"
 
class ProcessedMetrics:

    def __init__(self, ip, managedsystem_id, x_api_session):

        self.service = "pcm"
        self.root = ROOT
        self.ip = ip
        self.managedsystem_id = managedsystem_id
        self.x_api_session = x_api_session
        self.content_type = CONTENT_TYPE

    def json_download_managedsystem(self, HTTP_object, feedparser_processed_metrics):
        """
        downloads the json files for the managed system
        Args:
          HTTP_object : HTTP Request object carrying the headers and URL
          feedparser_processed_metrics : Feedparser object containing the processed metrics entries
        """

        for i in range(0,len(feedparser_processed_metrics.entries)):
            if feedparser_processed_metrics.entries[i].category=="ManagedSystem":
                json_url_managedsystem=feedparser_processed_metrics.entries[i].links[0].href
                HTTP_object.HTTPGet(url = json_url_managedsystem)
                log_object.log_debug(HTTP_object.response)
                if not HTTP_object.response_b :
                    continue
                print("\nManagedSystem json file:")
                JsonFilesDownload.json_file(feedparser_processed_metrics.entries[i].title, HTTP_object.response.text)


    def json_download_logicalpartitions(self, HTTP_object, feedparser_processed_metrics):
        """
        downloads the json files for the LogicalPartition
        Args:
          HTTP_object : HTTP Request object carrying the headers and URL
          feedparser_processed_metrics : Feedparser object containing the processed metrics entries
        """


        for k in range(0,len(feedparser_processed_metrics.entries)):
            if feedparser_processed_metrics.entries[k].category=="LogicalPartition" :
                json_url_lpar = feedparser_processed_metrics.entries[k].links[0].href
                HTTP_object.HTTPGet(url=json_url_lpar)
                log_object.log_debug("into lpar/uuid/processedmetrics %s"%(HTTP_object.response))
                feedparser_processed_metrics_lpar=feedparser.parse(HTTP_object.response.text)
                for j in range(0,len(feedparser_processed_metrics_lpar.entries)):
                    json_url_lpar_jsonlink= feedparser_processed_metrics_lpar.entries[j].links[0].href
                    HTTP_object.HTTPGet(url=json_url_lpar_jsonlink)
                    log_object.log_debug("into lpar/uuid/processedmetrics/jsonfile %s"%(HTTP_object.response))
                    if not HTTP_object.response_b :
                        continue
                    print("\nLogicalPartition json file:")
                    JsonFilesDownload.json_file(feedparser_processed_metrics_lpar.entries[j].title, HTTP_object.response.text)
        



    def get_processedmetrics(self):
        """
        Downloads the json files for ManagedSystem and LogicalPartition
        """

        choice="y"
        try:
            while choice=="y":
                HTTP_object =HTTPClient.HTTPClient(self.service, self.ip, self.root, self.content_type, self.x_api_session)
                # Make a get request for processedmetrics
                HTTP_object.HTTPGet(append=self.managedsystem_id+"/ProcessedMetrics")
                if not HTTP_object.response_b:
                    log_object.log_warn("Long Term Monitor not Enabled\n")
                    return
                # The response of the get request is parsed using feedparser
                feedparser_processed_metrics=feedparser.parse(HTTP_object.response.text)
                print("Processed Metrics: Downloads the json files for the ManagedSystem and Logicalpartitions available in the ManagaedSystem")
                self.json_download_managedsystem(HTTP_object, feedparser_processed_metrics)
                self.json_download_logicalpartitions(HTTP_object,feedparser_processed_metrics)

                print("Sleeps for 30 seconds")
                time.sleep(30)
                print("Refreshing after 30 seconds")
        except KeyboardInterrupt:
            return

        
        



