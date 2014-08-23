---
layout: layout
title: "Download and Install"
---

Just click on the icon! 
-----------------------

<a href="http://pkgsrc.saveosx.org/Darwin/bootstrap/bootstrap-x86_64-2013Q4.pkg"><img src="http://www.3tb.de/netbsd/pkgsrc-logo-outline.png" width="500" height="300" /></a>
Download and Install
====================

So you want to try it out, then? Great!
Before you get started: **you'll need root privileges on your system**

We provide three methods for setting up pkgsrc and pkgin on OS X

Using the .pkg file 
-----------------------------------------

1. Download [bootstrap.pkg](http://pkgsrc.saveosx.org/Darwin/bootstrap/bootstrap-x86_64-2013Q4.pkg).
2. Install the .pkg file.
3. Add `/usr/pkg/bin` and `/usr/pkg/sbin` in your shell `PATH` variable.
4. Add `/usr/pkg/man` in your shell `MANPATH` variable.


Using the archive
-----------------

This is the default, and the recommended method, for two reasons: it's the most tested and you'll be aware of the changes you're making to your system.

1. Download [bootstrap.tar.gz](http://pkgsrc.saveosx.org/Darwin/bootstrap/bootstrap-x86_64-2013Q4.tar.gz):

       $ curl -o bootstrap-x86_64-2013Q4.tar.gz http://pkgsrc.saveosx.org/Darwin/bootstrap/bootstrap-x86_64-2013Q4.tar.gz

       or

       $ rsync -P rsync://saveosx.org/pkgsrc/Darwin/bootstrap/bootstrap-x86_64-2013Q4.tar.gz .

2. As root, extract it:

       $ tar -C / -xzf bootstrap-x86_64-2013Q4.tar.gz

3. Or, use pipes and combine the steps mentioned above

       $ curl -o bootstrap-x86_64-2013Q4.tar.gz http://pkgsrc.saveosx.org/Darwin/bootstrap/bootstrap-x86_64-2013Q4.tar.gz | gzcat | (cd /; sudo tar -xpf -)

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
