---
layout: layout
title: "Download and Install"
---

Download and Install
====================

So you want to try it out, then? Great! Just a word of warning before you get started: **you need root access on your Mac**. If you don't have it, don't even bother to try anything, as the distributed tools won't work anyway.

Then, once you're sure you can sudo on your machine, please continue. :)
We've gathered three methods for you to use pkgsrc and pkgin on Mac:

Using the archive
-----------------

This is the default, and the recommended one, for two reasons: first, it's the most tested method; and second, you'll be aware of the steps you do, in case you want to remove it, or if, out of luck, something goes wrong.

1. Download [bootstrap.tar.gz](http://saveosx.org/packages/Darwin/bootstrap/bootstrap-x86_64.tar.gz):

      $ curl -o bootstrap-x86_64.tar.gz http://saveosx.org/packages/Darwin/bootstrap/bootstrap-x86_64.tar.gz

2. As root, extract it:

       $ tar -C / -xzf bootstrap-x86_64.tar.gz

3. Add `/usr/pkg/bin` and `/usr/pkg/sbin` in your shell `PATH` variable.
4. Add `/usr/pkg/man` in your shell `MANPATH` variable.

Using the .pkg file (not properly tested)
-----------------------------------------

1. Download [bootstrap.pkg](http://saveosx.org/packages/Darwin/bootstrap/bootstrap-x86_64.pkg).
2. Install the .pkg file.
3. Add `/usr/pkg/bin` and `/usr/pkg/sbin` in your shell `PATH` variable.
4. Add `/usr/pkg/man` in your shell `MANPATH` variable.

From the source
---------------

    $ git clone https://github.com/yrmt/pkgsrc
    $ cd pkgsrc/bootstrap
    $ git checkout pkgsrc_2013Q3
    $ sudo ./bootstrap --prefix=/usr/pkg --pkgdbdir=/var/db/pkg --abi=64 --compiler=clang

Add `/usr/pkg/bin` and `/usr/pkg/sbin` in your shell `PATH` variable.

There, you have pkgsrc set up! Now start installing packages like this:

    $ cd pkgsrc/<category>/<portname>
    $ sudo bmake install clean
