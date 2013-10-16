Title: Building 64 pkgsrc ports on Mac OS X
Date: 2013-10-15 21:10
Category: Mac OS X
Tags: Mac OS X, packages
Slug: pkgsrc-osx-64
Author: Youri Mouton
Summary: A little guide on building 64bit ports on Mac OS X.

You'll need the Xcode command line tools for this.

## First clone the pkgsrc git repository:        

> `git clone https://github.com/jsonn/pkgsrc`       

> `cd pkgsrc/bootstrap`     

> `sudo ./bootstrap --prefix=/usr/pkg --pkgdbdir=/var/db/pkg --abi=64 --compiler=clang`     

Don't forget to add /usr/pkg/bin and /usr/pkg/sbin in your PATH shell variable.

There, you have pkgsrc set up! Now start installing packages like this:

> `cd pkgsrc/<category>/<portname>`       

> `sudo bmake install`          


