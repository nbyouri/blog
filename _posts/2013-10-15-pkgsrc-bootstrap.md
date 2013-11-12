---
layout: post
title: Building 64 pkgsrc ports on Mac OS X
author: Youri Mouton
---

You'll need the Xcode command line tools for this.

First clone the pkgsrc git repository:        

`git clone https://github.com/jsonn/pkgsrc`       

`cd pkgsrc/bootstrap`     

`git checkout pkgsrc_2013Q2`

`sudo ./bootstrap --prefix=/usr/pkg --pkgdbdir=/var/db/pkg --abi=64 --compiler=clang`     

Don't forget to add /usr/pkg/bin and /usr/pkg/sbin in your PATH shell variable.

There, you have pkgsrc set up! Now start installing packages like this:

`cd pkgsrc/<category>/<portname>`       

`sudo bmake install`          


