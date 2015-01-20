---
layout: layout
title: "Download and Install"
---

Download and Install
====================

So you want to try it out, then? Great!
Before you get started: **you'll need root privileges on your system**

Want to be up and running fast?
-------------------------------
For a streamlined setup, to get you up and running in under a minute, there's the `quickstrap` script.  
To get started, grab a copy of [cmacrae](https://twitter.com/calumacrae)'s [bootstrap repo](https://github.com/cmacrae/saveosx)  

       $ git clone git://github.com/cmacrae/saveosx
	   
Open up a Terminal (this must be Apple's 'Terminal.app'), then cd to the scripts sub-directory and run the `quickstrap` script.  
If you'd prefer an interactive install, run the `bootstrap` script.  

Using the archive
-----------------

1. Download [bootstrap.tar.gz](http://pkgsrc.saveosx.org/Darwin/bootstrap/bootstrap-x86_64-2014Q4.tar.gz):

       $ curl -O http://pkgsrc.saveosx.org/Darwin/bootstrap/bootstrap-x86_64-2014Q4.tar.gz

2. extract it:

       $ sudo tar -C / -xzf bootstrap-x86_64-2014Q4.tar.gz

3. Add `/usr/pkg/bin` and `/usr/pkg/sbin` in your shell's `PATH` variable.
4. Add `/usr/pkg/man` in your shell `MANPATH` variable.

