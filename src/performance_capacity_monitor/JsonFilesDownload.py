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

import os
import sys
import json
import time

def json_file(filename, file_content):
    """
     The Json files of monitoring will be downloaded
    """

    json_filename = filename.replace('*','-')
    json_file_content = json.dumps(json.loads(file_content),
                                   sort_keys=True,indent=4,
                                   separators=(',',':'))
    directory=os.getcwd()
    location=directory+"/output/json-files"
    if not os.path.exists("output/json-files"):
             os.makedirs("output/json-files")
    file_object = open(directory+"\output\json-files\ " + json_filename,'w')
    file_object.write(json_file_content)
    file_object.close()
    print("JSON file Downloaded at %s"%(location))
    
   

    
    
