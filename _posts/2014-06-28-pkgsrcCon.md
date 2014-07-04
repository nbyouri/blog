---
layout: pkgsrc-post
title: pkgsrcCon 2014 London
author: Youri Mouton
---

It happened just a few days ago and I had a great time meeting the people working on the framework we like so much. There were lots of NetBSD developers but also Mac OS X and SmartOS users and more.

## conference highlights

We had 3 minutes talks and longer talks on the first day and we were about 20 people in there.

Here's a list of pkgsrc related talks that were given:

- bulktracker by @bsiegert (Benny Siegert), a nice way to visualize bulk builds statistics

       http://bulktracker.appspot.com


- @wiedi's (Sebastian Wiedenroth) common pkgsrc errors web page 

	[https://up.frubar.net/2915/report.html](https://up.frubar.net/2915/report.html)

- "Pretty tabular data without much effort" by @abs  (David Brownlee)

	[http://sync.absd.org/www/pkgsrc-report.html](http://sync.absd.org/www/pkgsrc-report.html)

- OCaml packages on pkgsrc for functional programming wizards like @jaap (Jaap Boender, pkgsrcCon host) and how OCaml updates breaks it's related packages like with Golang

- Cross Compiling with qemu by @justin (Justin Cormack)

- Sevan Janiyan's GCC fixes for Mac OS X on PowerPC and how he got 4.7 to build

- How package installs and upgrades are handled on The NetBSD Foundation servers by @spz (S.P Zeidler, who admitted using her beloved Amiga as a mirror for [http://netbsd.org](http://netbsd.org), but only for static content of course :])

- NetBSD thin clients by ThinIT @sborill (Stephen Borill)

	[Paper from EuroBSDCon 2007](http://www.bsdcan.org/2009/schedule/attachments/77_BuildingProductsWithNetBSDthin-clients-Stephen-Borrill.pdf)

- A great talk by @schmonz (Amitai Schlair), president of TNF (The NetBSD Foundation) looking at pkgsrc in the future
	- how do we make pkgsrc easier for developers 
 	- allow users to post in wiki and other changes to allow more much, much needed documentation
  	- use a scripted language instead of a `Makefile` for ports, lua?
   - automated testing of packages
   - move away from cvs 
   - lots of other ideas...
   - it was the only filmed talk, it should be up soon 
- The talks were recorded, I will link them when they're available.

- I talked a bit about being a new pkgsrc user and how documentation could be improved and introduced the SaveOSX project. I was a bit nervous at first but I was pleased with the positive response I got from a lot of really skilled people.

## Hackathon

On the second day, we had a day of hacking on pkgsrc things

- @schmonz helped me fix pkgsrc for Mac OS X Yosemite which happened to be an easy fix.
- Calum and I worked on the SaveOSX scripts 
- I looked at the much needed Xfce 4.10 [port](https://github.com/NetBSDfr/xfce4) and got it to work on Mac OS  X
- @spz and @schmonz worked on the wiki
- pkgtools/pkg_regress for package testing
- Sevan got a free G4 Mac mini so he can work on pkgsrc along with his cute 12" G4 MacBook, he got gcc44 to gcc47 to build fine
- @wiedi got started working on getting FUSE support for Mac OS X in pkgsrc, it's build system appears to make it hard.
- more stuff quiet people were working on I don't know about..

## Drinks

Calum and I had drinks with Sevan, @jaap, @schmonz, @wiedi, we talked for hours about making the world a better place and how projects like NetBSD and pkgsrc was impacting our lives.
