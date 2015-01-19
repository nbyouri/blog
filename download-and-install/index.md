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

Using the .pkg file 
-------------------

1. Download [bootstrap.pkg](http://pkgsrc.saveosx.org/Darwin/bootstrap/bootstrap-x86_64-2013Q4.pkg).
2. Install the .pkg file.
3. Add `/usr/pkg/bin` and `/usr/pkg/sbin` in your shell `PATH` variable.
4. Add `/usr/pkg/man` in your shell `MANPATH` variable.


Using the archive
-----------------

This is the default, and the recommended method, for two reasons: it's the most tested and you'll be aware of the changes you're making to your system.

1. Download [bootstrap.tar.gz](http://pkgsrc.saveosx.org/Darwin/bootstrap/bootstrap-x86_64-2013Q4.tar.gz):

       $ curl -O http://pkgsrc.saveosx.org/Darwin/bootstrap/bootstrap-x86_64-2013Q4.tar.gz

       or

       $ rsync -P rsync://saveosx.org/pkgsrc/Darwin/bootstrap/bootstrap-x86_64-2013Q4.tar.gz .

2. As root, extract it:

       $ tar -C / -xzf bootstrap-x86_64-2013Q4.tar.gz

3. Or, use pipes and combine the steps mentioned above

       $ curl http://pkgsrc.saveosx.org/Darwin/bootstrap/bootstrap-x86_64-2013Q4.tar.gz | gzcat | (cd /; sudo tar -xpf -)

3. Add `/usr/pkg/bin` and `/usr/pkg/sbin` in your shell's `PATH` variable.
4. Add `/usr/pkg/man` in your shell `MANPATH` variable.


From source
-----------

    $ git clone https://github.com/yrmt/pkgsrc
    $ cd pkgsrc/bootstrap
    $ git checkout pkgsrc_2013Q4
    $ sudo ./bootstrap --prefix=/usr/pkg --pkgdbdir=/var/db/pkg --abi=64 --compiler=clang

Add `/usr/pkg/bin` and `/usr/pkg/sbin` in your shell `PATH` variable.

There, you have pkgsrc set up! Now start installing packages like this:

    $ cd pkgsrc/<category>/<portname>
    $ sudo bmake install clean
