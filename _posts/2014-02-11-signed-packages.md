---
layout: pkgsrc-post
title: Signed Packages
author: Youri Mouton
---

The pkgsrc 2013Q3 branch repo is almost finished compiling, it features all the port fixes I've been working on, and now the ports use the X11 libs from inside pkgsrc so XQuartz will only be needed to actually start the X server! I will try to get an X server working from pkgsrc to avoid having to install XQuartz from macosforge but that is more complicated than I first thought (I'll post about it later).

But more importantly, the packages are now signed! This means you can easily make sure the packages are coming from a trusted source (because you trust me, right?). 
I've got this idea from the awesome work of khorben , a NetBSD developer and leader of [EdgeBSD](http://edgebsd.org), which is a great project I'm also trying to help on. Check [this](http://video.fosdem.org/2014/AW1121/Saturday/The_EdgeBSD_Project.webm) video if you want to learn more about it and learn more about package signing on pkgsrc. khorben pushed his changes to NetBSD so all that was needed was a [patch](http://lists.edgebsd.org/edgebsd-developers/2013/09/msg00001.html) to the pkgsrc makefiles and a few config adjustments in mk.conf and pkg_install.conf. 

Technical details
------------------

The packages are signed with gnupg version 2.0.22 and here are my gpg details:

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

It's a tgz archive which contains the signing information and the actual package which is the same as  the non signed packages.

The +PKG_GPG_SIGNATURE contains the gpg public key needed to verify the authenticity of the package and the +PKG_HASH contains hashes of every 40 bytes of the package files.

How do I install signed packages?
---------------------------------

First, import my key I linked above so pkg_add, which is used by pkgin can verify that the package is coming from me.
        
        ──── gpg --import yrmtspubkey

When installing packages, you might see a message that says the key is not trusted, to silence it you must set a level of trust on my key:

        ──── gpg --edit-key 2D99C8F7

Then you'll be prompted which level of trust you want to set, then type `save` and you're done!
            
 
Add this to your /usr/pkg/etc/pkg_install.conf: 

        GPG=/usr/pkg/bin/gpg
        VERIFIED_INSTALLATION=always
    
After the steps mentionned above, you can simply install packages as you used to. 

Here's an example:

        ──── sudo pkgin -y in gtk3+
        reading local summary...
        processing local summary...
        updating database: 100%
        calculating dependencies... done.
        
        nothing to upgrade.
        1 packages to be installed: gtk3+-3.10.6 (17M to download, 70M to install)
        
        downloading packages...
        gtk3+-3.10.6.tgz                   100%   17MB 282.5KB/s 252.3KB/s   01:02    
        installing packages...
        installing gtk3+-3.10.6...
        pkg_install warnings: 0, errors: 0
        reading local summary...
        processing local summary...
        updating database: 100%
        marking gtk3+-3.10.6 as non auto-removable

How do I create signed packages?
--------------------------------

First, you must apply khorben's [patch](http://git.edgebsd.org/gitweb/?p=edgebsd-pkgsrc.git;a=blobdiff;f=mk/pkgformat/pkg/package.mk;h=d75bad26e0c460f5d1d4c69bec0536a77de79da2;hp=cdee24570f4b98b71a7bca86b0e998b9db248336;hb=16c6eceef5b4a1314096b564d68e5d990a6ae5b1;hpb=45f514b94f43afdfd93f8f25ea30c56c29d23249) on pkgsrc's makefiles 

Put your gpg ID in /usr/pkg/etc/pkg_install.conf, so for me:

        GPG_SIGN_AS=2D99C8F7

And add this in /usr/pkg/etc/mk.conf:

        SIGN_PACKAGES=gpg

Then the port will ask for your key when running `make package`.  

Here's a picture of my pkgsrc tree with a sticker I got at FOSDEM!

![bonus](http://i.imgur.com/rrGFaWz.jpg?1)

### [Link to the magnificent EdgeBSD project twitter!](https://twitter.com/EdgeBSD)
