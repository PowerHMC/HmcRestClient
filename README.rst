About:
------
	This package has set of examples to understand how to use HMC REST APIs. For each operation it has a Python module. Target audience for these examples are the users interested in exploiting the HMC REST APIs. The objective is to provide a starter kit for creating a REST client. The users can take the source code and modify it according to their needs.

Disclaimer:
-----------
	These examples are shared as is and they are not formally supported by IBM or any of the authors and contributors. User assumes complete ownership and responsibility before modifying or executing them.

Installation:
-------------	
	``python setup.py install`` - the script files will be created in ``[Python installation directory]/scripts``

	``python setup.py install --install-scripts=[Target location]`` - the script files will get created in the specified target location.

Requirements:
-------------
	Power Hardware Management Console Version 8 Release 8.2
	
	Python Version >= 3.4.2
	
	**Python Libraries:**
		Requests version >= 2.5.3
			https://pypi.python.org/pypi/requests
			
			Used for processing HTTP requests and responses from the HMC.
		
		PyXB version = 1.2.4
			https://pypi.python.org/pypi/PyXB/
			
			Used for generating Python source code from HMC XSDs. The generated source code is used for processing UOM and PCM objects. If you upgrade HMC and if there is new schema version from HMC you may need to regenerate the source code to make it compatible with new version.
		
			Command to generate source code for UOM objects: ``python pyxbgen -u [UOM.xsd] -m [Output python file name e.g. UOM] --location-prefix-rewrite=platform:/resource/PMC.SCHEMA.UOM/tmp/build/schema=[Location of HMC schema]``
		
			Command to generate source code for PCM objects: ``python pyxbgen -u [ManagedSystemPcmPreference.xsd] -m [Output python file name e.g. ManagedSystemPcmPreferences]``
		
		feedparser version >= 5.1.3 
			https://pypi.python.org/pypi/feedparser

			Used for processing Atom feed from the HMC.
		
		The program uses OS specific APIs to read user input from the command line. To execute the program on Linux install getch module.
		https://pypi.python.org/pypi/getch
			 

Execution:
----------
	Go to the install script directory and execute "HmcRestClient" from the command prompt. It starts interactive command line interface with main menu with options like ManagedSystem, Cluster, Performance and capacity monitoring, Help, etc. 

	The ManagedSystem have options for ManagedSystem operations such as List, PowerOn, PowerOff, RemoveConnection. It also has its child objects LogicalPartition, VirtualIOServer, NetworkBridge, VirtualNetwork, VirtualSwitch, SRIOVEthernetPhysicalPort, etc.
	
	Each option provides the operation on that object such as List, Create, Modify, Delete.
	
	List operation on objects provides the details of the object. The operations such as Create, Modify requires set of values. The source code has the values hard coded into it. Before performing these operations the user should check and if required set appropriate values in the source code. E.g.

	1. Create LogicalPartition module creates partition with min, max and desired memory 256MB and shared processor in capped mode.
	2. List operation on LogicalPartition lists logical partition name, its state, memory attributes, shared/dedicated processor, partition type and uuid.

	Performance and Capacity Monitoring have options enabling/disabling performance monitoring on a managed system. It also has options for downloading the JSON files of Long term, Short term and Processed Metrics.

	Help option gives the overview of each usecase.


Reference to useful resources:
------------------------------
	PowerHMC developerworks community: https://www.ibm.com/developerworks/community/groups/community/powerhmc
	
	Link to PowerVM Python SDK: https://github.com/pypowervm/pypowervm
	
