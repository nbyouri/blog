---
layout: post
title: Using pkgin on Mac OS X
author: Youri Mouton
---

##Getting started with pkgin on Mac OS X

Pkgsrc is a framework for building third-party software originally developped for NetBSD but
 also runs on FreeBSD, OpenBSD, illumos/SmartOS, Linux, Minix and many other Unix likes including Mac OS X. 

It is a good alternative to the frustrating macports and it's design is very simple and you 
don't have to deal with another languagle like tcl for macports or ruby for homebrew. 

A package manager is also included, `pkgin` which is what we're interested in in this post. 
We made a saveosx.org repository because we want to bring new packages that aren't in the 
other pkgin repos for Mac OS X like rxvt-unicode, cmus, ranger, ... 
You can look at the repo [here](http://saveosx.org/packages).

## Installing the required files for running pkgin:

This installer was made for Maverick, it won't work on Mountain Lion or previous Mac OS X releases. yet.

[Download](http://saveosx.org/packages/Darwin/bootstrap/bootstrap-x86_64.pkg) the installer needed to install pkgsrc and pkgin (34m)

## Getting ready:     

Update pkgin with the new repositories information     

`$ sudo pkgin -y update`

Add /usr/pkg/bin and /usr/pkg/sbin to your $PATH   

`$ PATH=/usr/pkg/bin:/usr/pkg/sbin:$PATH`     

Add /usr/pkg/man to your $MANPATH    

`$ MANPATH=/usr/pkg/man:$MANPATH`    

You might want to add this to your shell configuration.

## Using pkgin:

Search for a package       

`$ pkgin search tmux`      

Install a package       

`$ sudo pkgin in tmux`      

List available packages     

`$ pkgin avail`      

List installed packages      

`$ pkgin list`      

## Example:

![img](http://paste.unixhub.net/index.php/Za2/)

# Read the pkgin man page!     

