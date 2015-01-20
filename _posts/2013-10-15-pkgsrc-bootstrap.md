---
layout: post
title: Building 64 bit pkgsrc ports on Mac OS X from git
author: Youri Mouton
---

You'll need the Xcode command line tools for this.

First clone the pkgsrc git repository:        

`git clone https://github.com/jsonn/pkgsrc`       

`cd pkgsrc/bootstrap`     

`git checkout pkgsrc_2014Q4`

`sudo ./bootstrap --prefix=/usr/pkg --pkgdbdir=/var/db/pkg --abi=64 --compiler=clang`     

Don't forget to add /usr/pkg/bin and /usr/pkg/sbin in your PATH shell variable.

There, you have pkgsrc set up! Now start installing packages like this:

`cd pkgsrc/<category>/<portname>`       

`sudo bmake install clean`     


