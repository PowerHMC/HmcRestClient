#!/usr/bin/env python

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

from setuptools import setup,find_packages
setup(name='HmcRestClient',
      version='1.0',
      description='Python sample programs for accessing the Power HMC through REST APIs',
      license='Apache',
      author='Niraj Shah, Manjunath Shanbhag',
      author_email='niraj.shah@in.ibm.com,manjunathns@in.ibm.com',
      include_package_data = True,
      packages = find_packages(),  # include all packages
      py_modules=["_xmlk2"],      
      package_data = { '': [ '*.xml' ],'':['*.txt'] ,'src/help':["*.txt"]},
      entry_points={
          'console_scripts' : ['HmcRestClient=src.main.Main:main']
          },
      classifiers=['Intended Audience :: Information Technology',
                   'Intended Audience :: System Administrators',
                   'Intended Audience :: Developers',
                   'Topic :: System :: Systems Administration',  
                   'Topic :: Software Development :: Data Center Automation Tools',
                   'License :: OSI Approved :: Apache Software License',
                   'Programming Language :: Python :: 3.4.2',
                   'Environment :: Console'
                   ],
      )
      
