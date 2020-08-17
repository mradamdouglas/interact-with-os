# Interacting with the Operating System #

## \_\_init\_\_.py ##
The **\_\_init\_\_.py** file is necessary for the python interpreter to understand that individual
files are part of a module.

Installed python packages can be found in ```usr/lib/python3/dist-packages```

## Common packages for interacting with OS ##

**OS**: Routines for operating system interaction. Has methods for abstracting platform-specific functions. e.g. pathname separators, directory/file identification.

**OS.path**: A sub-module of OS. Includes additional path related functions. e.g. ```os.path.exists(path)```, ```os.path.isdir(string)```, and  ```os.path.join()```

**dsutil**: Utility functions for copying files and directory trees.

**psutil**: cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors)

**socket**: provides socket operations and related functions. Useful for mapping IP addresses, hosts, network addresses, making network socket connections, etc. e.g. ```hostIP = socket.gethostbyname('localhost')```

**requests**: Utilities for HTTP GET and POST requests. e.g. ```result = requests.get("http://www.google.com").status_code```

**CSV**: Used for reading from and writing to CSV files.

**datetime** formatting for timestamps and related date/time functions

## File Interaction ##
