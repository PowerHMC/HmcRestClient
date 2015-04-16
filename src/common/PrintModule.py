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

class PrintModule:
    
    def print_on_screen(self, lis):
        n = len(lis)
        i = 0
        print("=============================================================")
        for i in range(0,n):                          
            print("%d. %s"%(i+1,lis[i]))
        choice = input("\nEnter your Choice: ")
        return choice
    
    
    
    

   
