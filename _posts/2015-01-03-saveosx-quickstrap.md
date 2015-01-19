---
layout: post
title: A Streamlined Bootstrapper for Save OS X
author: Calum MacRae
tags: pkgsrc, saveosx
---
__Editors Note: This is a cross-post from Calum's personal blog: [http://cmacr.ae](http://cmacr.ae)__

[Youri](https://twitter.com/YouriMouton) and I have been working on [Save OS X](https://github.com/cmacrae/saveosx) on and off for quite some time now. It's grown and matured into something we're very proud of, but sadly, we're not the best at advocacy. This is something we'll be working on.

I won't be going into detail about the project at large in this post. I wanted to write about a specific script I threw together the other day, and my motives behind writing it.

What the people want!
---------------------
So far, whilst writing the bootstrap scripts for [Save OS X](https://github.com/cmacrae/saveosx), I've approached it in such a way that assumes the user is completely unfamiliar with all the underlying technologies. The [`bootstrap`](https://github.com/cmacrae/saveosx/blob/master/scripts/bootstrap) script, which is intended as the only script the user needs to run, is completely interactive. It provides some fancy title screens per _section_, detailing what that part of the project is, and what it's used for.

I tried out [Homebrew](http://brew.sh) for the first time in a while the other day. It ended in frustration, and actually broke itself - something I wasn't expecting. But, I'm not writing about brew to bash it: I really liked how simple the install was. With the suggestion of piping from curl to ruby ([relevant](http://curlpipesh.tumblr.com)) aside, it was a pleasant set-up, and running in no time. This is something we didn't offer.
It was nice, as a user who already knew what it was, and knew what they wanted, to have a hassle free, fast install.

So, I stripped out all the mish-mash of `case`s nested in `while` loops from the `bootstrap` script, and [`quickstrap`](https://github.com/cmacrae/saveosx/blob/master/scripts/quickstrap) was born. I didn't bother including the functionality of the [`x-setup`](https://github.com/cmacrae/saveosx/blob/master/scripts/x-setup) script, if people want it, they can just run that script on its own :)

Yeah... so?
-----------
Well, now you can get secure, 64bit binary package management, with GPG verification, running on OS X in under a minute. I hope that's as nice to other people as it seems to me.

[`pkgsrc`](http://pkgsrc.net) has been supported on OS X for a very long time, and [`pkgin`](http://pkgin.net) has always been dead simple to set up, so this isn't radically new.
Though, we are bringing GPG signed packages to the table, thanks to the excellent work from [@khorben](https://twitter.com/khorben) of the [EdgeBSD](https://edgebsd.org) project, and [Youri](https://twitter.com/YouriMouton)'s relentless work on the packages. Along with this, you don't have to worry about setting up OS X's PATH/MANPATH evaluation, and GPG is handled for you.

A quick demo
------------
I decided to throw a demo up, using [showterm.io](https://showterm.io/a3ccab391e69016360b98).  

_Note: The time for some of the exeutions in this demo are inaccurate - it is, in fact, a faster process from the shell. This is due to the way [showterm](https://showterm.io) processes text_

Go grab it
----------
You can get the `quickstrap` script from my GitHub:
[https://github.com/cmacrae/saveosx](https://github.com/cmacrae/saveosx)  

So, have at it people. Let us know what you think!

We'll keep you posted!
----------------------
We're working on various improvements to the project at the moment.
We'll be updating [saveosx.org](http://saveosx.org) with a more intuitive & informative layout.
Also, [Youri](https://twitter.com/YouriMouton)'s cooking up new packages as I type!
