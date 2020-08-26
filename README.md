# Interacting with the Operating System #

## \_\_init\_\_.py ##
The **\_\_init\_\_.py** file is necessary for the python interpreter to understand that individual
files are part of a module.

Installed python packages can be found in ```usr/lib/python3/dist-packages```

## Common packages for interacting with OS ##

**os**: Routines for operating system interaction. Has methods for abstracting platform-specific functions. e.g. pathname separators, directory/file identification.

*os.environ.get*: gets environmental variables. e.g. ```os.environ.get("PATH","")```

*os.path*: A sub-module of OS. Includes additional path related functions. e.g. ```os.path.exists(path)```, ```os.path.isdir(string)```, and  ```os.path.join()```

*os.pathsep*: sets the proper OS-dependent path separator. e.g. to add a value to the path ```my_env["PATH"] = os.pathsep.join(["/opt/myapp", my_env["PATH"]])```

*os.path.expanduser*: expands the value of the path argument.  ```e.g os.path.expanduser('~')```

**sys**: Utility functions for accessing objects used by the interpreter.

*sys.argv*: stores command line arguments

*sys.path*: module path search

*sys.module*: dictionary of loaded modules

*sys.exit*: sets the exit code for the script

**dsutil**: Utility functions for copying files and directory trees.

**psutil**: cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors)

**socket**: provides socket operations and related functions. Useful for mapping IP addresses, hosts, network addresses, making network socket connections, etc. e.g. ```hostIP = socket.gethostbyname('localhost')```

**requests**: Utilities for HTTP GET and POST requests. e.g. ```result = requests.get("http://www.google.com").status_code```

**CSV**: Used for reading from and writing to CSV files.

**datetime** formatting for timestamps and related date/time functions

**re** regex module
    */usr/share/lib/american-english*: user dictionary.

**subprocess**:  allows scripts to run system commands. i.e. spawn processes, connect to input/output/error pipes, and obtain their return codes. Takes the process name followed by arguments. e.g.:

``subprocess.run(["date"])``
``subprocess.run(["sleep", "2"])``
``subprocess.run(["ls", "-l" "data"])``

**glob**: filename globbing utility.

*glob(pathname, *, recursive=False)*: Return a list of paths matching a pathname pattern. e.g ```filelist = (glob.glob("/home/adouglasx/repos/interact-with-os/*.py, recursive=False ))```

**operator**: exports a set of functions implemented in C corresponding to the intrinsic operators of Python.  For example, operator.add(x, y) is equivalent to the expression x+y.

*operator.itemgetter(n)*: gets the item identified as the argument. e.g.: given:

``fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
sorted(fruit.items())  RETURNS:
[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]``

Sort is on the first item in the set (i.e. type of fruit):

``sorted(fruit.items(), key=operator.itemgetter(0))  RETRUNS:
[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]``

Sort is on the second item in the set (i.e. number of items):

``sorted(fruit.items(), key=operator.itemgetter(1))  RETURNS:
[('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)] ``

## Environmental Processing ##

**export** updates environmental variables. e.g. ```export PATH = /usr/bin/mydir```

**unittest**: Classes and utilities for unit testing. https://docs.python.org/3/library/unittest.html

**doctest**: a streamlined and more efficient version of unittest.  See documentation. https://docs.python.org/3/library/doctest.html

## Bash stuff ##
Standard outputs:
*0*: STDIN
*1*: STDOUT
*2*: STDERR

This will take the pass the contexts of new_file.txt to streams_err.py as user input  (i.e. input(data)),  then output from the STDERR to error_file.txt: ```e.g. streams_err.py < new_file.txt 2> error_file.txt```

## Signal Processing ##
Signals are tokens delivered to running processes to indicate a desired action.

kill -(signal) <process>

**SIGINT**: (CNTL+C) Signal interrupt.  Interrupts a command and stops a process.

**SIGSTOP**: (CNTL+Z) Signal pause. Sends a signal to pause the process and can be restarted with 'fg'

**SIGCONT**: (fg) Tells a process to pick up where it left off after a SIGSTOP.

**SIGTERM**: A kill command that politely asks a signal to stop. Can be ignored or blocked. Does NOT kill the child process. It allows child process to complete.

**SIGKILL**: used for immediate termination of a process. It CANNOT be ignored or blocked. Child processes are also killed.

### Addtl commands ###
**ps**: lists the processes executing in the the current terminal for the current user

**ps ax**: lists all processes currently executing for all userlist

**ps e**: shows the environment for the processes listed

**kill <PID>**: sends the SIGTERM signal to the process identified by pid

**fg**: causes a job that was stopped or in the background to be returned to the foreground

**bg**: causes a job that was stopped to go to the background

**jobs**: lists the jobs currently running or stopped

**top**: shows the processes currently using the most CPU time (press 'q' to quit)
