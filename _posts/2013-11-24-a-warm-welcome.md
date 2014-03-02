---
layout: post
title: Introducing Save OS X
author: Calum MacRae
---

Greetings humble reader. You've reached the official blog for the Save OS X project. We'll be posting here regularly with news & tutorials relating to the project, and may also post from time to time about loosely related subjects.

So, enough of that, let's get down to what you're probably all curious about...

####What is Save OS X about?
Save OS X is a hacking and development project for Apple's Operating System; OS X. We're geared towards bringing a wealth of software that's often found on other UNIX derived OS's to OS X and showing the user that they *can* use OS X as a great UNIX based workstation.

####Why?
To put it simply: because OS X is capable of much more than is immediately apparent to the average user. It has a familiar set of underlying utilities, many taken from the NetBSD, FreeBSD & OpenBSD projects. We want to complement these with other tools available.

In my personal opinion, having a monopoly like Apple pay their developers to build a UNIX-like Operating System, that is designed from the core to work in perfect harmony with their hardware, is a wonderful thing. We're not going to spout off and rant about how "Apple are superior", or anything ludicrous like that, we're not trying to promote them or their product in any way. We just want people to understand that OS X is a perfectly viable option for hackers and developers alike.

####How?
We've mostly been working away quietly on this project without much exposure to the community, and throughout this time, the project has been shaped and molded into two main components; a collective of hacks pulled together in scripts and our beefy package repo.

####The hacks
The hacks we've implemented achieve a number of things. The end result will be a system with a seemless X11 implementation (still capable of running the usual Aqua applications), Git and the excellent pkgsrc, with its related tools installed and set up with our package repo.

#### X11
Xorg's X11 has been one of the main areas of focus for our project. We strived to implement it as seemlessly as with other systems like BSD and Linux.

[![screenshot](http://paste.unixhub.net/index.php/QVav/)](http://paste.unixhub.net/index.php/QVav/)

Here's a shot of an OS X desktop utilising our hacks and packages.
We've got a bunch of window managers and desktop environments in our repo ready to install.

####The packages
A great amount of time and wizardry has been spent building our excellent package repository, bringing software that was previously unavailable (at least certainly not in a convenient manner) to OS X users in an easy to use format. 

####pkgsrc
We use NetBSD's [pkgsrc](http://pkgsrc.org/) and its awesome binary package manager; pkgin.
pkgin is a joy to use, and in my personal opinion; this is how package management should be done.
>pkgsrc is a framework for building third-party software on NetBSD and other UNIX-like systems, currently containing over 12000 packages. It is used to enable freely available software to be configured and built easily on supported platforms.

It doesn't come with hefty dependancies, like XCode and it's easy to maintain; no compiling necessary. Also, getting your software into a pkgin package is nice and simple!

Here's a quick video demonstration of the installation of Google's [Go](http://golang.org/) , using pkgin:

<div style="width:500px; margin-left:auto; margin-right:auto;">
<iframe src="//player.vimeo.com/video/80066069" width="500" height="244" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
</div>

It's that easy. No need to go to Apple's developer site, download a hefty installer, no time spent watching things compile. Just search for the package you want, then install it! And hey, if the package you want isn't there, drop us a line on irc or e-mail (contact details listed at the end) and I'm sure we'd be more than happy to get it packaged up for you.


All the binaries available on our repo are 64bit too, [see for yourself!](http://pkgsrc.saveosx.org/Darwin/2013Q2/x86_64/)

Here's the repo capacity at the time of writing (22 November 2013):

{% highlight ruby %}
Packages available: 7462
Total size of packages: 7.85GB
{% endhighlight %}
And it's still growing daily!
 
We have a bunch of notable packages in our repo, including:
 
* gcc
* ghc
* qt4
* sbcl
* gtk
* MPlayer
* ZFS
* XQuartz
* FFmpeg
* Go
 
And that's just to name a a very tiny few. Many of our packages aren't available through other package/ports managers for OS X.
We're also improving and adding features to pkgsrc/pkgin as we go and are commiting the code upstream to contribute back.

For instance, a handy stats screen:
![pkgin stats](http://paste.unixhub.net/index.php/aRZ)

####Okay, so how can I get all this implemented on my system?
Setup scripts for the project are being hosted on my [GitHub](https://github.com/Phyrne/saveosx).

This project only supports the latest OS X release; currently Mavericks.

The hacks have been packed up in a collection of scripts, and conveniently been tied together in a bootstrapper. There are some final, minor tweaks needed on the scripts, mostly cosmetic, and then we'll be releasing info on how to get started!

For now, if you want to try out some packages, use [our pkgin boostrap](http://pkgsrc.saveosx.org/Darwin/bootstrap/bootstrap-x86_64.pkg) and get  testing!
Please send any feedback to myself or Youri:

<a href="mailto:calum0macrae@gmail.com">calum0macrae@gmail.com</a>
<a href="mailto:youri.mout@gmail.com">youri.mout@gmail.com</a>

Or catch us on irc at `#saveosx` on `irc.oftc.net`

####Until next time
We hope you've enjoyed what you've read and are as excited about this project and its future as we are.

**Stay tuned for an upcoming post on who we are and a little history on the project.**
