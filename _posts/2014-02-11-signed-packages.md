---
layout: post
title: Signed Packages
author: Youri Mouton
---

The pkgsrc 2013Q3 branch repo is almost finished compiling, it features all the port fixes I've been working on, and now the ports use the X11 libs from inside pkgsrc so XQuartz will only be needed to actually start the X server! I will try to get an X server working from pkgsrc to avoid having to install XQuartz from macosforge but that is more complicated than I first thought (I'll post about it later).

But more importantly, the packages are now signed! This means you can easily make sure the packages are coming from a trusted source (because you trust me, right?). 
I've got this idea from the awesome work of khorben , a NetBSD developer and leader of [EdgeBSD](http://edgebsd.org), which is a great project I'm also trying to help on. Check [this](http://video.fosdem.org/2014/AW1121/Saturday/The_EdgeBSD_Project.webm) video if you want to learn more about it and learn more about package signing on pkgsrc. khorben pushed his changes to NetBSD so all that was needed was a [patch](http://lists.edgebsd.org/edgebsd-developers/2013/09/msg00001.html) to the pkgsrc makefiles and a few config adjustments in mk.conf and pkg_install.conf. 

The packages are signed with gnupg version 2.0.22 and here's my info:

        pub   4096R/2D99C8F7 2014-02-05     
        uid                  Youri Mouton <youri.mout@gmail.com>     
        uid                  Youri Mouton <yrmt@edgebsd.org>     
        sub   4096R/B6BAE02C 2014-02-05     
        Key fingerprint = 81F7 EC68 C5BD 5DED 7A7B  2832 6A09 5CC6 2D99 C8F7


And [here](http://paste.unixhub.net/index.php/hO8S/)'s my gpg public key if you need it.

So how do the packages compare to the non signed ones? Here's the anatomy of a signed package: 

        ──── ar -t /Volumes/pkgsrc/packages/All/nmap-6.40.tgz
        +PKG_HASH
        +PKG_GPG_SIGNATURE
        nmap-6.40.tgz

So basically it's a tgz archive which contains the signing information and the actual package which is the same as  the non signed packages.

How do I install signed packages?
---------------------------------

You can simply keep installing the packages as you used to, no specific configuration needed on your side.

Where's my bonus picture?
-------------------------

Here's a bonus picture of my pkgsrc tree :)

![bonus](http://i.imgur.com/rrGFaWz.jpg?1)

# [Link to the magnificent EdgeBSD project twitter!](https://twitter.com/EdgeBSD)
