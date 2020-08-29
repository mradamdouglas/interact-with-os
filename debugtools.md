**strace**: traces system calls made by a program and the results. e.g.
 ``strace ./health_checks.py ``

**-i**: writes the output to a file. e.g. ``strace -o failure.strace ./health_checks.py``

**time**:  run programs and summarize system resource usage e.g. ``time ./health_checks.py``


**ltrace**: library tracer calls. ltrace is a program that simply runs the specified command until it exits.  It intercepts and records the dynamic library calls which are called by the executed  process and  the signals which are received by that process.  It can also intercept and print the system calls executed by the program.

**top**: provides a dynamic real-time view of a running system.

**iotop**:iotop  displays columns for the I/O bandwidth read and written by each process/thread
       during  the  sampling  period.  It  also  displays  the  percentage   of   time   the
       thread/process  spent  while  swapping in and while waiting on I/O. For each process,
       its I/O priority (class/level) is shown.

**vmstat**: Display virtual memory statistics.

**ionice** - set or get process I/O scheduling class and priority

**iftop**: display bandwidth usage on an interface by host

**rsync** - a fast, versatile, remote (and local) file-copying tool

*--bwlimit**: sets the maximum bandwidth observed.  e.g. ``rsynch --bwlimit=1.5m``

**nice**: Starts a process with a different priority. Priority can be 0-19, with 0 being highest.

**renice**: Changes the priority of an already running process.

**pidof**: Identifies the process IDs of processes identified.  e.g.
``For pid in $(pidof <process name>); do renice 19 $ pid; done ``

**ab**: Apache Benchmark: Used to benchmark response times of web sites.  e.g.
``ab -n 500 site.example`` makes 500 requests site.example and returns the average response time.

**daemonize** a third party tool that runs a command as a Unix daemon https://software.clapper.org/daemonize/. e.g.
``daemonize -c $PWD/usr/bin/ffmpeg -nostats -i "$video" "mp4_video"``

system calls: calls made from a program to the system kernel

## Generic ##
**profilers**: Tools that measure the resources our code uses. Language specific.

*gprof*: C-language profiler.

*cProfile*: Pythong language profiler. Built into python (import cProfile) e.g.:

    if __name__ == '__main__':
        import cProfile, pstats
        profiler = cProfile.Profile()
        profiler.enable()
        main()
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats('ncalls')
        stats.print_stats()


##Environment monitoring##

Watch:

*the load on the computer

*the processes running at the same time

*The usage on the network

Heisenbugs:  bugs that go away while 'fiddling' with the system.
