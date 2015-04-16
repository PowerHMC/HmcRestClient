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

from src.performance_capacity_monitor import CreateFromDocument
from src.performance_capacity_monitor import ToXml
from src.utility import HTTPClient,HMCClientLogger
import pyxb
from src.generated_src import ManagedSystemPcmPreferences
log_object=HMCClientLogger.HMCClientLogger(__name__)

class ManagedSystemPcmPreference:
    

    def __init__(self, ip, managedsystem_id, x_api_session):
        '''
        Initializes the required arguments for ManagedSystemPcmPreferences

        Args:
         ip : IP address of the HMC
         Managedsystem_id : The managed system uuid for which the pcm preferences has to be obtained
         x_api_session: The session id for the current session

        '''

        self.service = "pcm"
        self.root = "ManagedSystem"
        self.ip = ip
        self.x_api_session = x_api_session
        self.managedsystem_id = managedsystem_id

    #####################################
    # GET MANAGED SYTEM PCM PREFERENCES
    #####################################

    def get_managedsystempcmpreference(self):
        ''' This function is used to get the PCM Preferences of the Managed System '''

        HTTP_object = HTTPClient.HTTPClient(self.service, self.ip,
                                           self.root, "application/vnd.ibm.powervm.pcm.xml", self.x_api_session)
        # perform the get request for Managed System Pcm Preferences
        HTTP_object.HTTPGet(append=self.managedsystem_id+"/preferences")   
        log_object.log_debug("response code for get_managedsystempcmpreference %s" %(HTTP_object.response))
        response_content = HTTP_object.response.text
        xml = CreateFromDocument.xpath(response_content)
        # Create the python object using CreateFromDocument function
        get_managedsystempcmpreference_object = ManagedSystemPcmPreferences.CreateFromDocument(xml)
        # Return the above created object to the main program
        return get_managedsystempcmpreference_object   


    #############################################
    # SET/UPDATE MANAGED SYSTEM PCM PREFERENCES
    #############################################

    def set_managedsystempcmpreference(self):
        ''' This function is used to set/update the existing PCM Preferences of the Managed System '''

        get_managedsystempcmpreference_object1 = self.get_managedsystempcmpreference()
        pyxb.RequireValidWhenGenerating(True)
        print("options for set/update Managed System Pcm Preferences \n")
        option=input(" Choose an option \n 1.ComputeLTM \n 2.ComputeLTM + Long term monitor \n 3.ComputeLTM + Long term monitor + AggregationEnabled \n")
 
        if option=="1":
            get_managedsystempcmpreference_object1.ComputeLTMEnabled = "true"
            get_managedsystempcmpreference_object1.ComputeLTMEnabled.ksv = "V1_1_0"

            get_managedsystempcmpreference_object1.AggregationEnabled = "false"
            get_managedsystempcmpreference_object1.LongTermMonitorEnabled = "false"


        elif option=="2":
            get_managedsystempcmpreference_object1.LongTermMonitorEnabled = "true"
            get_managedsystempcmpreference_object1.ComputeLTMEnabled = "true"
            get_managedsystempcmpreference_object1.ComputeLTMEnabled.ksv = "V1_1_0"
       
            get_managedsystempcmpreference_object1.LongTermMonitorEnabled = "false"

        elif option=="3":
            get_managedsystempcmpreference_object1.AggregationEnabled = "true"
            get_managedsystempcmpreference_object1.LongTermMonitorEnabled = "true"
            get_managedsystempcmpreference_object1.ComputeLTMEnabled = "true"
            get_managedsystempcmpreference_object1.ComputeLTMEnabled.ksv = "V1_1_0"

        
        short_term_monitor = input("do u want to enable ShortTermMonitorEnabled ? y/n\n")
        if short_term_monitor == "y":
            get_managedsystempcmpreference_object1.ShortTermMonitorEnabled = "true"
        else:
            get_managedsystempcmpreference_object1.ShortTermMonitorEnabled = "false"
        

        # genarating the xml request body for the post reqeust by using ToXml method
        post_payload = ToXml.ToXml(get_managedsystempcmpreference_object1)
        HTTP_object = HTTPClient.HTTPClient(self.service, self.ip,
                                           self.root, "application/xml", self.x_api_session)
        # perform the post request for managed system pcm preferences
        HTTP_object.HTTPPost(post_payload, append=self.managedsystem_id+"/preferences")
        log_object.log_debug("response code for set_managedsystempcmpreference %s" %(HTTP_object.response))
        if HTTP_object.response.status_code==200:
            self.print_managedsystempcmpreference(get_managedsystempcmpreference_object1)
        

    ############################################
    # PRINT THE MANAGED SYSTEM PCM PREFERENCES
    ############################################

    def print_managedsystempcmpreference(self, get_pcm_object):
        '''
        This function prints the values of the Managed System PCM preferences

        Args:
         get_pcm_object : The get_managedsystempcmpreference method object

        '''

        print("LongTermMonitorEnabled   :", get_pcm_object.LongTermMonitorEnabled.value())
        print("AggregationEnabled       :", get_pcm_object.AggregationEnabled.value())
        print("ShortTermMonitorEnabled  :", get_pcm_object.ShortTermMonitorEnabled.value())
        print("ComputeLTMEnabled        :", get_pcm_object.ComputeLTMEnabled.value())
         


    
        
        
    
        
        
        
        
        
