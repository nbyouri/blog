---
layout: pkgsrc-post
title: An introduction to pkgsrc
author: Youri Mouton
---

This guide should allow you to learn how to create a new port or simply fix a port that you need. There are three target demographics listed below:

	- binary packages user with pkgin or pkg_add 
 		(you should be confident here)
	- build from source, use options 
 		(you will know this after reading the guide)
	- port developers
		(you should be able to get started here)


## pkgsrc tree

You should have a copy of the pkgsrc tree sitting somewhere on your disk, already bootstrapped, see this [blog post](http://saveosx.org/pkgsrc-bootstrap/) on how to do this.

The tree contains a `Makefile`, a `README`, distfiles, packages, category directories containing the ports, the bootstrap directory and some documentation.

The `mk/*` directory contains the pkgsrc framework Makefiles but also shell and Awk scripts

`pkglocate` is a script to find port names in the tree, though `pkgtools/pkgfind` is much faster.


## use the right tools

If you want to get started working on ports like creating new ones or simply fix ones you need, you should know about these tools:

 - install package developer utilities: 
	
		pkgin -y in pkg_developer

It contains very useful programs like:

 - checkperms: 
 		
		verify file permissions
 - createbuildlink:
 
		create buildlink3.mk files, which I'll explain later
 - digest:
 
		create hashes for messages with crypto algorithms such as sha512 and many others
 - lintpkgsrc:

		checks the whole pkgsrc tree, list all explicitly broken packages for example
 - pkg_chk:

		checks package versions and update if necessary
 - pkg_tarup:

		create archives of installed programs for later use on other machines or backups
 - pkgdiff:
 
		show diffs of patched files 
 - pkglint:

		verify the port you're creating for common mistakes (very useful!)
 - revbump:
 	
		update package version by one bump by increasing PKGREVISION
 - url2pkg:

		create a blank port from the software download link, it saves you some time by filling out a few basic Makefile settings
 - verifypc:

		sanity check for pkg-config in ports


## port contents

A pkgsrc port should at least contain:

- `Makefile` : a comment, developer info, software download site and lots of other possibilities
- `DESCR` : a paragraph containing the description for the software of the port we're making
- `PLIST` : the list of files to install, pkgsrc will only install the files listed here to your prefix
- `distinfo` : hashes of the software archive and patches or files in the port


Here's how they would look like for a small port I submitted not long ago in pkgsrc-wip

Makefile: 
	
{% highlight make %}
# $NetBSD$

PKGNAME=      osxinfo-0.1
CATEGORIES=   misc
GHCOMMIT=     de74b8960f27844f7b264697d124411f81a1eab6
DISTNAME=     ${GHCOMMIT}
MASTER_SITES= https://github.com/yrmt/osxinfo/archive/

MAINTAINER=   youri.mout@gmail.com
HOMEPAGE=     http://github.com/yrmt/osxinfo
COMMENT=      Small Mac OS X Info Program
LICENSE=      isc

ONLY_FOR_PLATFORM= Darwin-*-*

DIST_SUBDIR= osxinfo
WRKSRC= ${WRKDIR}/osxinfo-${GHCOMMIT}

.include "../../databases/sqlite3/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
{% endhighlight %}

DESCR: 
	
	Small and fast Mac OS X info program written in C
	by Youri Mouton.


PLIST:
	
	@comment $NetBSD$
	bin/osxinfo

distinfo:

	$NetBSD$

	SHA1 (osxinfo/de74b8960f27844f7b264697d124411f81a1eab6.tar.gz) = 83a2838ad95ff73255bea7f496a8cc9aaa4e17ca
	RMD160 (osxinfo/de74b8960f27844f7b264697d124411f81a1eab6.tar.gz) = 9102eb2a938be38c4adf8cfbf781c04d0844d09a
	Size (osxinfo/de74b8960f27844f7b264697d124411f81a1eab6.tar.gz) = 5981 bytes


## make

Now you know what kind of files you can see when you're in a port directory. The command used to compile it is the NetBSD `make` but often `bmake` on non NetBSD systems to avoid Makefile errors. Typing make alone will only compile the program but you can also use other command line arguments to make such as extract, patch, configure, install, package, ...

I'll try to list them and explain them in logical order. You can run them together.

- `make clean` will remove the source file from the work directory so you can restart with either new options, new patches, ...
- `make fetch` will simply fetch the file and check if the hash corresponds. It will throw an error if it doesn't.
- `make distinfo` or `make mdi` to update the file hashes in the `distinfo` file mentionned above.
- `make extract` extracts the program source files from it's archive in the work directory
- `make patch` applies the local pkgsrc patches to the source
- `make configure` run the GNU configure script
- `make` or `make build` or `make all` will stop after the program is compiled
- `make stage-install` will install in the port destdir, where pkgsrc first installs program files to check if the files correspond with the `PLIST` contents before installing to your prefix. For `wget`, if you have a default WRKOBJDIR (I'll explain later), the program files will first be installed in `<path>/pkgsrc/net/wget/work/.destdir` then after a few checks, in your actual prefix like `/usr/pkg`
- `make test` run package tests, if they have any
- `make package` create a package without installing it, it will install dependencies though
- `make replace` upgrade or reinstall the port if already installed
- `make deinstall` deinstall the program
- `make install` installs from the aforementionned `work/.destdir` to your prefix
- `make bin-install` installs a package for the port, locally if previously built or remotely, as defined by BINPKG_SITES in `mk.conf`, you can make a port install dependencies from packages rather than building them with the DEPENDS_TARGET= bin-install in `mk.conf`
- `make show-depends` show port dependencies
- `make show-options` show various port options, as defined by `options.mk`
- `make clean-depends` cleans all port dependencies
- `make distclean` remove the source archive
- `make package-clean` remove the package
- `make distinfo` or `make mdi` to update the `distinfo` file containing file hashes if you have a new distfile or patch
- `make print-PLIST` to generate a `PLIST` file from files found in `work/.destdir`

You should be aware that there are many make options along with these targets, like 

- `PKG_DEBUG_LEVEL`
- `CHECK_FILES`
- and many others described the the NetBSD pkgsrc guide


## pkgsrc configuration

The framework uses an `mk.conf` file, usually found in /etc. Here's how mine looks:

{% highlight make %}
# Tue Oct 15 21:21:46 CEST 2013

.ifdef BSD_PKG_MK          # begin pkgsrc settings

DISTDIR=                   /pkgsrc/distfiles
PACKAGES=                  /pkgsrc/packages
WRKOBJDIR=                 /pkgsc/work
ABI=                       64
PKGSRC_COMPILER=           clang
CC=                        clang
CXX=                       clang++
CPP=                       ${CC} -E

PKG_DBDIR=                 /var/db/pkg
LOCALBASE=                 /usr/pkg
VARBASE=                   /var
PKG_TOOLS_BIN=             /usr/pkg/sbin
PKGINFODIR=                info
PKGMANDIR=                 man
BINPKG_SITES=              http://pkgsrc.saveosx.org/Darwin/2013Q4/x86_64
DEPENDS_TARGET=            bin-install
X11_TYPE=                  modular
TOOLS_PLATFORM.awk?=       /usr/pkg/bin/nawk
TOOLS_PLATFORM.sed?=       /usr/pkg/bin/nbsed
ALLOW_VULNERABLE_PACKAGES= yes
MAKE_JOBS=                 8
SKIP_LICENSE_CHECK=        yes
PKG_DEVELOPER=             yes
SIGN_PACKAGES=             gpg
PKG_DEFAULT_OPTIONS+=      -pulseaudio -x264 -imlib2-amd64 -dconf
.endif			   # end pkgsrc settings
{% endhighlight %}

- I use `DISTDIR`, `PACKAGES`, `WRKOBJDIR` to move distfiles, packages and source files somewhere else to keep my pkgsrc tree clean
- `PKGSRC_COMPILER`, `CC`, `CXX`, `CPP` and `ABI` are my compiler options. I'm using clang to create 64 bit binaries here
- `PKG_DBDIR`, `VARBASE`, `LOCALBASE`, `PKG_TOOLS_BIN` are my prefix and package database path and package tools settings
- `PKGINFODIR`, `PKGMANDIR` are the info and man directories 
- `BINPKG_SITES` is the remote place where to get packages with the `bin-install` make target
- `DEPENDS_TARGET` is the way port dependencies should be installed. `bin-install` will simply install a package instead of building the port
- `X11_TYPE` sould be `native` or `modular`, the latter meaning we want X11 libraries from pkgsrc instead of using the `native` ones usually in `/usr/X11R7` in Linux or BSD systems and `/opt/X11` on Mac OS X with XQuartz
- `TOOLS_PLATFORM.*` points to specific programs used by pkgsrc, here I use the one that was generated by pkgsrc bootstrap for maximum compatibility
- `ALLOW_VULNERABLE_PACKAGES` allows you to disallow the installation of vulnerable packages in critical environments like servers
- `MAKE_JOBS` the number of concurrent make jobs, I set it to 8 but it breaks some ports
- `SKIP_LICENSE_CHECK` will skip the license check. If disabled you will have to define a list of licenses you find acceptable with `ACCEPTABLE_LICENSES`
- `PKG_DEVELOPER` this option will show more details during the port building 
- `SIGN_PACKAGES` allows you to `gpg` sign packages. More info in my [blog post](http://saveosx.org/signed-packages/) about it
- `PKG_DEFAULT_OPTIONS` allows you to enable or disable specific options for all ports (as defined with ports' options.mk files), I disabled a few options so less ports would break, pulseaudio doesn't build on Mac OS X for example, neither do x264, dconf

Keep in mind that there are many other available options documented in the official pkgsrc guide.


## creating a simple port

Let's create a little port using the tools we've talked about above. I will use a little window manager called 2bwm.

- We need an url for the program source files archive. It can be a direct link to a tar or xz archive. Mine's `http://pkgsrc.saveosx.org/Darwin/distfiles/2bwm-0.1.tar.gz`

- Now that we have a proper link for our program source, create a directory for your port:
	
		$ mkdir ~/pkgsrc/wm/2bwm

- Use `url2pkg` to create the needed files automatically:
		
		$ url2pkg http://pkgsrc.saveosx.org/Darwin/distfiles/2bwm-0.1.tar.gz

You'll be presented with a text editor like `vim` to enter basic Makefile options:

- `DISTNAME`, `CATEGORIES`, `MASTER_SITES` should be set automatically 
- enter your mail address for `MAINTAINER` so users know whom to contact if the port is broken
- make sure the `HOMEPAGE` is set right, for 2bwm it is a github page
- write a `COMMENT`, it should be a one-line description of the program
- find out which license the program uses, in my case it is the `isc` license. You can find a list of licenses in `pkgsrc/mk/licenses.mk`.
- Below you will see `.include "../../mk/bsd.pkg.mk"` at the end of the Makefile and above this should go the port's needed dependencies to build, we'll leave that empty at the moment and try to figure out what 2bwm needs
- exit vim and it should fetch and update the file hashes for you. If it says `permission denied` you can just run `make mdi` to fetch and upadate the `distinfo` file

So now you have valid `Makefile` and `distinfo` files but you need to write a paragraph in `DESCR`. You can usually find inspiration on the program's homepage.

Here's how they look like at the moment: 
	
 Makefile:
{% highlight make %} 
# $NetBSD$

DISTNAME=       2bwm-0.1
CATEGORIES=     wm
MASTER_SITES=   http://pkgsrc.saveosx.org/Darwin/distfiles/

MAINTAINER=     yrmt@users.sourceforge.net
HOMEPAGE=       http://github.com/venam/2bwm/
COMMENT=        Fast floating WM written over the XCB library and derived from mcwm
LICENSE=        isc

.include "../../mk/bsd.pkg.mk"
{% endhighlight %}

distinfo:

	
	$NetBSD$

	SHA1 (2bwm-0.1.tar.gz) = e83c862dc1d9aa198aae472eeca274e5d98df0ad
	RMD160 (2bwm-0.1.tar.gz) = d9a93a7d7ae7183f5921f9ad76abeb1401184ef9
	Size (2bwm-0.1.tar.gz) = 38419 bytes

DESCR:

	A fast floating WM, with the particularity of having 2 borders,
	written over the XCB library and derived from mcwm written by
	Michael Cardell. In 2bWM everything is accessible from the keyboard
	but a pointing device can be used for move, resize and raise/lower.

But our PLIST file is still empty.


#### build stage

 Let's try to build the port to see if things work but as soon as the build stage starts, we get this error:

> 2bwm.c:26:10: fatal error: 'xcb/randr.h' file not found

Let's find out which port provides this file ! 

	$ pkgin se xcb 

returns these possible packages: 

	xcb-util-wm-0.3.9nb1  Client and window-manager helpers for ICCCM and EWMH
	xcb-util-renderutil-0.3.8nb1  Convenience functions for the Render extension
	xcb-util-keysyms-0.3.9nb1  XCB Utilities
	xcb-util-image-0.3.9nb1  XCB port of Xlib's XImage and XShmImage
	xcb-util-0.3.9nb1 =  XCB Utilities
	xcb-proto-1.9 =      XCB protocol descriptions (in XML)
	xcb-2.4nb1           Extensible, multiple cut buffers for X

Package content inspection allowed me to find the right port 

	$ pkgin pc libxcb|grep randr.h

So we can add the libxcb `buildlink3.mk` file to the Makefile above the bsd.pkg.mk include: 

	.include "../../x11/libxcb/buildlink3.mk"

This allows the port to link 2bwm against the libxcb port. Let's try to build the port again!

	$ make clean
	$ make

Reports another error !

> 2bwm.c:27:10: fatal error: 'xcb/xcb_keysyms.h' file not found

It looks like this file is provided by xcb-util-keysyms, so let's add:

	.include "../../x11/xcb-util-keysyms/buildlink3.mk"

in our Makefile.

Clean, build again, and add more dependencies until it passes the build stage. Here's how my Makefile ends up looking like:

{% highlight make %}
# $NetBSD$

DISTNAME=       2bwm-0.1
CATEGORIES=     wm
MASTER_SITES=   http://pkgsrc.saveosx.org/Darwin/distfiles/

MAINTAINER=     yrmt@users.sourceforge.net
HOMEPAGE=       http://github.com/venam/2bwm/
COMMENT=        Fast floating WM written over the XCB library and derived from mcwm
LICENSE=        isc

.include "../../x11/libxcb/buildlink3.mk"
.include "../../x11/xcb-util-wm/buildlink3.mk"
.include "../../x11/xcb-util-keysyms/buildlink3.mk"
.include "../../x11/xcb-util/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
{% endhighlight %}


#### install phase

Geat ! We got our program to compile in pkgsrc. Now we must generate the PLIST file so we can actually install the program, but we must `make stage-install` to make sure that it installs in the right place.

	
	$ find /pkgsrc/work/wm/2bwm/work/.destdir/

returns:

	/pkgsrc/work/wm/2bwm/work/.destdir/
	/pkgsrc/work/wm/2bwm/work/.destdir//usr
	/pkgsrc/work/wm/2bwm/work/.destdir//usr/local
	/pkgsrc/work/wm/2bwm/work/.destdir//usr/local/bin
	/pkgsrc/work/wm/2bwm/work/.destdir//usr/local/bin/2bwm
	/pkgsrc/work/wm/2bwm/work/.destdir//usr/local/bin/hidden
	/pkgsrc/work/wm/2bwm/work/.destdir//usr/local/share
	/pkgsrc/work/wm/2bwm/work/.destdir//usr/local/share/man
	/pkgsrc/work/wm/2bwm/work/.destdir//usr/local/share/man/man1
	/pkgsrc/work/wm/2bwm/work/.destdir//usr/local/share/man/man1/2bwm.1
	/pkgsrc/work/wm/2bwm/work/.destdir//usr/local/share/man/man1/hidden.1
	/pkgsrc/work/wm/2bwm/work/.destdir//usr/pkg

This doesn't look right since our `LOCALBASE` is `/usr/pkg`.


	$ make print-PLIST

returns nothing, because 2bwm installs files in the wrong place so we need to fix 2bwm's own Makefile to use the right `DESTDIR` and `PREFIX`, that is set to the right place by pkgsrc. Let's inspect how 2bwm installs:

From 2bwm's Makefile: 

{% highlight make %}
install: $(TARGETS)
        test -d $(DESTDIR)$(PREFIX)/bin || mkdir -p $(DESTDIR)$(PREFIX)/bin
        install -pm 755 2bwm $(DESTDIR)$(PREFIX)/bin
        install -pm 755 hidden $(DESTDIR)$(PREFIX)/bin
        test -d $(DESTDIR)$(MANPREFIX)/man1 || mkdir -p $(DESTDIR)$(MANPREFIX)/man1
        install -pm 644 2bwm.man $(DESTDIR)$(MANPREFIX)/man1/2bwm.1
        install -pm 644 hidden.man $(DESTDIR)$(MANPREFIX)/man1/hidden.1
{% endhighlight %}

This looks fine since it installs in a `DESTDIR`/`PREFIX` but it sets 

> PREFIX=/usr/local

and

> MANPREFIX=$(PREFIX)/share/man

In the beginning of the Makefile. We should remove the first line and edit the man prefix:

> MANPREFIX=${PKGMANDIR}

so pkgsrc can install the program's files in the right place. We have two ways of modifying this file, either patch the Makefile or use `sed` substitution which is a builtin pkgsrc feature that allows you to change lines in files with a sed command before building the port. 

I will show how to do both ways so you can get an introduction on how to generate patch files for pkgsrc.

#### patching the Makefile :

- edit the file you need to modify with `pkgvi`:

	
		$ pkgvi /pkgsrc/work/wm/2bwm/work/2bwm-0.1/Makefile

	which should return:

	> pkgvi: File was modified. For a diff, type:
pkgdiff "/Volumes/Backup/pkgsrc/work/wm/2bwm/work/2bwm-0.1/Makefile"

	and this returns our diff.
	

- create the patch with `mkpatches`, it should create a `patches` directory in the port containing the patch and an original file removed with `mkpatches -c`. 

		$ find patches/*
		patches/patch-Makefile

- now that the patch has been created, we need to add it's hash to distinfo otherwise pkgsrc won't pick it up:

		$ make mdi
you should get this new line:

	> SHA1 (patch-Makefile) = 9f8cd00a37edbd3e4f65915aa666ebd0f3c04e04


- you can now clean and `make patch` and `make stage-install CHECK_FILES=no` since we still haven't generated a proper PLIST. Let's see if 2wm files were installed in the right place this time:

		$ find /pkgsrc/work/wm/2bwm/work/.destdir/

		/pkgsrc/work/wm/2bwm/work/.destdir/
		/pkgsrc/work/wm/2bwm/work/.destdir//usr
		/pkgsrc/work/wm/2bwm/work/.destdir//usr/pkg
		/pkgsrc/work/wm/2bwm/work/.destdir//usr/pkg/bin
		/pkgsrc/work/wm/2bwm/work/.destdir//usr/pkg/bin/2bwm
		/pkgsrc/work/wm/2bwm/work/.destdir//usr/pkg/bin/hidden

	It looks like it is alright ! Let's generate the PLIST:

		$ make print-PLIST > PLIST
	
	containing:

		@comment $NetBSD$
		bin/2bwm
		bin/hidden

	There you have a working port you can install normally with 

		$ make install 


#### using the sed substitution framework

You should be able to fix the prefix error much quicker than with the patching explained above thanks to the sed substitution framework. Here's how it looks like in my port Makefile:

{% highlight make %}
SUBST_CLASSES+=         makefile
SUBST_STAGE.makefile=   pre-build
SUBST_MESSAGE.makefile= Fixing makefile
SUBST_FILES.makefile=   Makefile
SUBST_SED.makefile=     -e 's,/usr/local,${PREFIX},g'
SUBST_SED.makefile+=    -e 's,share/man,${PKGMANDIR},g'
{% endhighlight %}

As you can see, you can do multiple commands on multiple files, it is very useful for very small fixes like this.


#### pkglint

Now that we have a working port, we must make sure it complies to the pkgsrc rules. 

	$ pkglint
	
Returns 

	ERROR: DESCR:4: File must end with a newline.
	ERROR: patches/patch-Makefile:3: Comment expected.
	2 errors and 0 warnings found. (Use -e for more details.)

Fix the things pkglint tells you to do until you get the glorious:

> looks fine.

Then you should do some testing on the program itelf on at least two platforms such as NetBSD, Mac OS X. Other platforms supported by pkgsrc can be found at [pkgsrc.org](http://pkgsrc.org). If you would like to submit your pkgsrc upstream you can either subscribe to pkgsrc-wip or ask a NetBSD developer to add it for you.

You can find the 2bwm port I submitted in [pkgsrc-wip](http://pkgsrc-wip.cvs.sourceforge.net/viewvc/pkgsrc-wip/wip/2bwm/).


## pkgsrc and wip 

If you want to submit your port for others to use you can either subscribe to pkgsrc-wip or ask a NetBSD developer to add it for you which can be tough. Even though there are many IRC channels in which you can find nice developers, you will have to take the time to get to know them. The easiest way for beginners is to submit to pkgsrc-wip so other people can review and test it first. 

pkgsrc-wip is hosted on [sourceforge](https://sourceforge.net/projects/pkgsrc-wip/) and you can easily get cvs access to it if you create an account on there and send an email to NetBSD developer `@wiz` (Thomas Klausner) asking nicely for commit access. I got access fairly quickly and he even fixed a port to show me how to do it properly. 

You can also send me an email or talk to me on IRC so I can submit it for you.


## the options framework

You can create port options with the `options.mk` file, like for `wm/dwm`

	
{% highlight make %}
# $NetBSD: options.mk,v 1.2 2011/06/17 11:59:57 obache Exp $

PKG_OPTIONS_VAR=			PKG_OPTIONS.dwm
PKG_SUPPORTED_OPTIONS=	xinerama
PKG_SUGGESTED_OPTIONS=	xinerama

.include "../../mk/bsd.options.mk"

#
# Xinerama support
#
# If we don't want the Xinerama support we delete XINERAMALIBS and
# XINERAMAFLAGS lines, otherwise the Xinerama support is the default.
#
.if !empty(PKG_OPTIONS:Mxinerama)
.  include "../../x11/libXinerama/buildlink3.mk"
.else
SUBST_CLASSES+=         options
SUBST_STAGE.options=    pre-build
SUBST_MESSAGE.options=  Toggle the Xinerama support
SUBST_FILES.options=    config.mk
SUBST_SED.options+=     -e '/^XINERAMA/d'
.  include "../../x11/libX11/buildlink3.mk"
.endif
{% endhighlight %}

This file should be included in the Makefile:

	.include "options.mk"

If you type `make show-options`, you should see this:

	Any of the following general options may be selected:
	xinerama	 Enable Xinerama support.

	These options are enabled by default:
		xinerama

	These options are currently enabled:
		xinerama

	You can select which build options to use by setting 	PKG_DEFAULT_OPTIONS
	or PKG_OPTIONS.dwm.

Running `make PKG_OPTIONS=""` should build without the `xinerama` dwm option enabled by default.

The options.mk file must contain these variables:

- `PKG_OPTIONS_VAR` sets the options variable name
- `PKG_SUPPORTED_OPTIONS` lists all available options
- `PKG_SUGGESTED_OPTIONS` lists options enabled by default

It allows you to change configure arguments and include other buildlinks, and various other settings.


## hosting a package repo

Now that you've created a few ports, you might want to make
precompiled packages available for testing. You will need pkgsrc's `pkg_install` on the host system. I host my [packages](http://pkgsrc.saveosx.org/) on a FreeBSD server with a bootstrapped pkgsrc.

I use this `zsh` function to :

{% highlight bash %} 
add () {
	# upload the package to remote server
	scp $1 yrmt@saveosx.org:/usr/local/www/saveosx/packages/Darwin/2013Q4/x86_64/All/ 2> /dev/null
	
	# update the package summary
	ssh yrmt@saveosx.org 'cd /usr/local/www/saveosx/packages/Darwin/2013Q4/x86_64/All/;
	        rm pkg_summary.gz;
 	        /usr/pkg/sbin/pkg_info -X *.tgz | gzip -9 > pkg_summary.gz'
	
	# pkgin update
	sudo pkgin update
}
{% endhighlight %}

- upload a package 
- update the package summary, which is an archive containing information about all present packages that will be picked up by pkg_install and pkgin. It looks like this for one package:

		PKGNAME=osxinfo-0.1
		DEPENDS=sqlite3>=3.7.16.2nb1
		COMMENT=Small Mac OS X Info Program
		SIZE_PKG=23952
		BUILD_DATE=2014-06-29 12:45:08 +0200
		CATEGORIES=misc
		HOMEPAGE=http://github.com/yrmt/osxinfo
		LICENSE=isc
		MACHINE_ARCH=x86_64
		OPSYS=Darwin
		OS_VERSION=14.0.0
		PKGPATH=wip/osxinfo
		PKGTOOLS_VERSION=20091115
		REQUIRES=/System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
		REQUIRES=/System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
		REQUIRES=/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
		REQUIRES=/usr/lib/libSystem.B.dylib
		REQUIRES=/usr/pkg/lib/libsqlite3.0.dylib
		FILE_NAME=osxinfo-0.1.tgz
		FILE_SIZE=9710
		DESCRIPTION=Small and fast Mac OS X info program written in C 
		DESCRIPTION=by Youri Mouton.
		DESCRIPTION=
		DESCRIPTION=Homepage:
		DESCRIPTION=http://github.com/yrmt/osxinfo


- update pkgin 


And this shell alias to upload all my built packages, but I still need to run `add()` mentionned above to update the pkg_summary

{% highlight bash %} 
up='rsync -avhz --progress /pkgsrc/packages/ root@saveosx.org:/usr/local/www/saveosx/packages/Darwin/2013Q4/x86_64/'
{% endhighlight %} 

Then you should be able to set the url in repositories.conf to use your packages with pkgin. You can also install them directly with something like `pkg_add http://pkgsrc.saveosx.org/Darwin/2013Q4/x86_64/All/9menu-1.8nb1.tgz` of course. 


## build all packages

Bulk building pkgsrc packages is a topic for another post, see jperkin's excellent blog [posts](http://www.perkin.org.uk/posts/distributed-chrooted-pkgsrc-bulk-builds.html) about this.


## faq

#### what if the port I'm making is a dependency for another one?

You should just generate the buildlink3.mk file we've talked about earlier like this:

	$ createbuildlink > buildlink3.mk

#### what if the program is only hosted on GitHub ?

pkgsrc supports fetching archives from specific git commits on GitHub like this:
{% highlight make %}
PKGNAME=           2bwm-0.1
CATEGORIES=        wm
GHCOMMIT=          52a097ca644eb571b22a135951c945fcca57a25c
DISTNAME=          ${GHCOMMIT}
MASTER_SITES=      https://github.com/venam/2bwm/archive/
DIST_SUBDIR=       2bwm
WRKSRC=            ${WRKDIR}/2bwm-${GHCOMMIT}
{% endhighlight %}

You can then easily update the git commit and the distinfo with it to update the program. 

#### what if the program doesn't have a Makefile

You can do all Makefile operations directly from the port's Makefile like this: 


{% highlight make %}
post-extract:
	${CHMOD} a-x ${WRKSRC}/elementary/apps/48/internet-mail.svg

do-install:
	${INSTALL_DATA_DIR} ${DESTDIR}${PREFIX}/share/icons
	cd ${WRKSRC} && pax -rw -pe . ${DESTDIR}${PREFIX}/share/icons/
{% endhighlight %}

To install, but you can also build programs from the Makefile. This is what qt4-sqlite3 uses:

{% highlight make %}
do-build:
	cd ${WRKSRC}/src/tools/bootstrap && env ${MAKE_ENV} ${GMAKE}
	cd ${WRKSRC}/src/tools/moc && env ${MAKE_ENV} ${GMAKE}
	cd ${WRKSRC}/src/plugins/sqldrivers/sqlite && env ${MAKE_ENV} ${GMAKE}
{% endhighlight %}


You can install the following type of files: 

`INSTALL_PROGRAM_DIR` : directories that contain binaries

`INSTALL_SCRIPT_DIR` : directories that contain scripts

`INSTALL_LIB_DIR` : directories that contain shared and static libraries

`INSTALL_DATA_DIR`: directories that contain data files

`INSTALL_MAN_DIR` : directories that contain man pages

`INSTALL_PROGRAM` : binaries that can be stripped from debugging symbols

`INSTALL_SCRIPT` : binaries that cannot be stripped

`INSTALL_GAME` : game binaries

`INSTALL_LIB` : shared and static libraries

`INSTALL_DATA` : data files

`INSTALL_GAME_DATA` : data files for games

`INSTALL_MAN` : man pages


`INSTALLATION_DIRS` : A list of directories relative to PREFIX that are created by pkgsrc at the beginning of the install phase. The package is supposed to create all needed directories itself before installing files to it and list all other directories here.

#### common errors

1. > Makefile:19: *** missing separator.  Stop.

This means you're not using the right `make`. On most systems, the make installed from the pkgsrc bootstrap is called `bmake`


2. If you have a feeling a port is stuck in the building stage, disable make jobs in your mk.conf

3. Please contribute here :)


## links
- [Jonathan Perkin's excellent blog](http://www.perkin.org.uk/)
- [NetBSD's very extensive pkgsrc guide](http://www.netbsd.org/docs/pkgsrc/)
- [NetBSD's pkgsrc wiki](http://wiki.netbsd.org/pkgsrc/)
- Other blog posts here :)

## where to find me

- yrmt@edgebsd.org 
- irc.oftc.net 
	
	`#saveosx`
