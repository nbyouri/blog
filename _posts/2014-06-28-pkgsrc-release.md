--- 
layout: pkgsrc-post
title: pkgsrc_2013Q4 available, update your packages
author: Youri Mouton
---

pkgsrc just finished building a new batch of 64 bit gpg signed packages on Mac OS X 10.9.3 with clang ! 

It took a good week and here are the results

	Packages available: 8105
	Total size of packages: 7223M

You can take a look at the available packages here: 

### How to update

Update the repository name in `/usr/pkg/etc/pkgin/repositories.conf` and make sure the only uncommented line is:
	
	http://pkgsrc.saveosx.org/Darwin/2013Q4/x86_64/All


Then update the pkgin database:

	sudo pkgin up

And fully upgrade your packages:

	sudo pkgin fug

### More information

We're still fixing packages though, so that number might go up! 

If you have package requests or questions, you're welcome to ask on our IRC channel or send us an email
	
	irc.oftc.net
	#saveosx

	calum0macrae@gmail.com 
	youri.mout@gmail.com


For anyone wondering, yes we're working in pkgsrc_2014Q1 ! :)

