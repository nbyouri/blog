Title: Using pkgsrc on Mac OS X
Date: 2013-10-09 18:48
Category: Mac OS X
Tags: Mac OS X, packages
Slug: pkgsrc-osx
Author: Youri Mouton
Summary: Intro on pkgin on Mac OS X.

#Getting started with pkgin on Mac OS X

Pkgsrc is a framework for building third-party software originally developped for NetBSD but
 also runs on FreeBSD, OpenBSD, illumos/SmartOS, Linux, Minix and many other Unix likes including Mac OS X. 

It is a good alternative to the frustrating macports and it's design is very simple and you 
don't have to deal with another languagle like tcl for macports or ruby for homebrew. 

A package manager is also included, `pkgin` which is what we're interested in in this post. 
We made a saveosx.org repository because we want to bring new packages that aren't in the 
other pkgin repos for Mac OS X like rxvt-unicode, cmus, ranger, ... 
You can look at the repo [here](http://saveosx.org/packages).

## Installing the required files for running pkgin:

> Fetch the files needed to install pkgsrc and pkgin (34m)

`$ curl -O http://saveosx.org/packages/Darwin/bootstrap/bootstrap.tar.gz`    

> Or, if you have a slow internet connection, you can use the xz file (5m)    

`$ curl -O http://saveosx.org/packages/Darwin/bootstrap/bootstrap.tar.gz.xz`     

### The bootstrap and repos are 32bit intel binaries only! We're working on a x86_64 binaries repo and bootstrap.

> Then extract the file from your root directory      

`$ cd /; sudo tar xf /path/to/bootstrap.tar.gz`     

> Or, if you used the xz file     

`$ unxz /path/to/bootstrap.tar.gz.xz`    

`$ cd /; sudo tar xf /path/to/bootstrap.tar.gz`     

## Getting ready:     

> Add this to the /usr/pkg/etc/pkgin/repositories.conf file to get the repos     

`http://pkgsrc.smartos.org/packages/Darwin/2013Q2/All`        

`http://saveosx.org/packages/Darwin/2013Q2/All`     

> Update pkgin with the new repositories information     

`$ sudo pkgin -y update`

> Add /usr/pkg/bin and /usr/pkg/sbin to your $PATH       

`$ PATH=/usr/pkg/bin:/usr/pkg/sbin:$PATH`     

> You might want to add this to your shell configuration.

## Using pkgin:

> Searching for a package       

`$ pkgin search tmux`      

> Installing a package       

`$ sudo pkgin in tmux`      

> List available packages     

`$ pkgin avail`      

> List installed packages      

`$ pkgin list`      

## Example:

> We're going to install 2bwm from the saveosx.org repo.     
> It's the only available package at the moment anyway.    

![img](http://paste.unixhub.net/index.php/Za2/)

> There, we installed 2bwm and it's dependencies in seconds!

### Read the pkgin man page!     
