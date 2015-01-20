Save OS X
=========

About
-----
[Save OS X](http://saveosx.org/) is a hacking and development project for Apple’s Operating System: OS X.
We’re geared towards bringing a wealth of software that’s often found on other UNIX derived OS’s to OS X and showing the user that they can use OS X as a great UNIX based workstation.

Why?
----
To put it simply: because OS X is capable of much more than is immediately apparent to the average user. It has a familiar set of underlying utilities, many taken from the various BSD projects. We want to complement these with other tools available.

We want to show people that OS X is a perfectly viable option for developers, sysadmins, hackers, or just those who like to tinker.

Installation
------------

To get started, grab a copy of the repo (either clone it, or download as a zip).
Open up a Terminal (this must be Apple's 'Terminal.app'), then `cd` to the `scripts` sub-directory and run the `bootstrap` script.

That should get you started.
Simple as that!

Want secure binary package management on OS X fast?
---------------------------------------------------
For a streamlined setup, to get you up and running in under a minute, there's the `quickstrap` script.
Open up a Terminal (this must be Apple's 'Terminal.app'), then `cd` to the `scripts` sub-directory and run the `quickstrap` script.

[Here's a quick demo of the script in action](https://showterm.io/a3ccab391e69016360b98)  
_Note: The time for some of the exeutions in this demo are inaccurate - it is, in fact, a faster process from the shell. This is due to the way [showterm](https://showterm.io) processes text_


So what do these scripts do?
----------------------------
If you follow the steps in the [installation section](#installation), you'll be greeted by an interactive script.
In a nutshell, this script will walk you through the set-up of [pkgsrc](http://pkgsrc.net), [pkgin](http://pkgin.net), set up your PATH & optionally implement [X11](http://www.x.org/wiki/) (using [XQuartz](https://xquartz.macosforge.org/landing/)) in a seamless manner. 

The X11 set-up script also has a revoke flag (`-r`), so you can try out our X11 hacks, and later remove them if you're not a fan.

If you're familiar with shell, peruse through the code, it should be pretty clear what's happening :)

pkgin usage
-----------
Want to find and install a package?

`pkgin search <package name>`

`pkgin install <package name>`

Nice 'n easy!

See [here](http://pkgin.net/#examples) for pkgin's usage examples.

Why choose Save OS X (specifically pkgin) over \<insert package manager here\>?
-----------------------------------------------------------------------------
Here's a list of properties that make [pkgin](http://pkgin.net/) (a binary package manager for pkgsrc) different from other package managers available for OS X:
		Precompiled packages from a trusted source
	- Signed pacakges with GPG
	- Dead simple makefiles
	- A robust multi platform framework
	- Can be bootstrapped without any external dependencies other than a C compiler & a shell
	- Tried and true, with a huge community of BSD developers behind it (and many devs from other communities)
	- A very large collection of packages (up to 15,000)
	- Ultra portable framework for use on many other OS's results in high quality ports
	- Easy creation of new ports/packages
	- Source code & package management are kept separated

Who?
----
[Save OS X](http://saveosx.org/) is a collaborative project between [Calum MacRae](https://github.com/cmacrae) and [Youri Mouton](https://github.com/yrmt)

**E-mail:** [calum0macrae@gmail.com](mailto:calum0macrae@gmail.com) / [youri.mout@gmail.com](mailto:youri.mout@gmail.com)

**IRC**: Come join us at `#saveosx` on `irc.oftc.net`

**Twitter**: [@calumacrae](https://twitter.com/calumacrae) / [@YouriMouton](https://twitter.com/YouriMouton)

License
-------
Use of this source code is governed by an ISC license that can be found in [the LICENSE file](LICENSE)
