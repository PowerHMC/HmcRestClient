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

import logging
import os
class HMCClientLogger:
                def __init__(self,module_name):
                                self.logger_module = logging.getLogger(module_name)
                                self.logger_module.setLevel(logging.DEBUG)
                                
# create file handler which logs even debug messages
                                if not os.path.exists("output/Log"):
                                    os.makedirs("output/Log")
                                filehandler = logging.FileHandler('output/Log/Debug.log')
                                filehandler.setLevel(logging.DEBUG)
                                consolehandler=logging.StreamHandler()
                                consolehandler.setLevel(logging.WARNING)
# create formatter and add it to the handlers
                                fileformatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s -  %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
                                consoleformatter = logging.Formatter(' %(levelname)s : %(message)s')
                                filehandler.setFormatter(fileformatter)
                                consolehandler.setFormatter(consoleformatter)
# add the handlers to logger
                                self.logger_module.addHandler(filehandler)
                                self.logger_module.addHandler(consolehandler)
                                
                def log_debug(self,message):
                                self.logger_module.debug(message)
                def log_info(self,message):
                                self.logger_module.info(message)
                def log_error(self,message):
                                self.logger_module.error(message)
                def log_warn(self,message):
                                self.logger_module.warn(message)
                

if __name__=="__main__":
    Log=HMCClientLogger("object of log")
    Log.log_debug("Debug")
    Log.log_info("Info")
    Log.log_error("Error")
    Log.log_warn("Warn")
    
