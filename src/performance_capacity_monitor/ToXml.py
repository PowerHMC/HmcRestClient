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

import xml.etree.ElementTree as etree

def ToXml(ManagedSystemPcmPreference_obj):
    get_ManagedSystemPcmPreference_object=ManagedSystemPcmPreference_obj.toDOM()
    get_ManagedSystemPcmPreference_object.documentElement.setAttribute("xmlns","http://www.ibm.com/xmlns/systems/power/firmware/uom/mc/2012_10/") 
    payload=get_ManagedSystemPcmPreference_object.toxml("utf-8")
    return payload
