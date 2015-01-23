---
layout: post
title: Using pkgin on Mac OS X
author: Youri Mouton
---

#### Installing the required files for running pkgin:

See the [install instructions](http://saveosx.org/download-and-install/) to get started.

#### Getting ready:     

Update pkgin with the new repositories information     

`$ sudo pkgin -y update`

Add /usr/pkg/bin and /usr/pkg/sbin to your $PATH   

`$ PATH=/usr/pkg/bin:/usr/pkg/sbin:$PATH`     

Add /usr/pkg/man to your $MANPATH    

`$ MANPATH=/usr/pkg/man:$MANPATH`    

You might want to add this to your shell configuration.

#### Using pkgin:

Search for a package       

`$ pkgin search tmux`  

Or, using a regular expression:

`$ pkgin se "clang|gcc4[45]"`

Install a package       

`$ sudo pkgin in tmux`      

List available packages     

`$ pkgin avail`      

List installed packages      

`$ pkgin list`      

#### Available options

	Commands and shortcuts:
	list                (ls  ) -  List installed packages.
	avail               (av  ) -  List available packages.
	install             (in  ) -  Perform packages installation or upgrade.
	update              (up  ) -  Create and populate the initial database.
	remove              (rm  ) -  Remove packages and depending packages.
	upgrade             (ug  ) -  Upgrade main packages to their newer versions.
	full-upgrade        (fug ) -  Upgrade all packages to their newer versions.
	show-deps           (sd  ) -  Display direct dependencies.
	show-full-deps      (sfd ) -  Display dependencies recursively.
	show-rev-deps       (srd ) -  Display reverse dependencies recursively.
	show-category       (sc  ) -  Show packages belonging to category.
	show-pkg-category   (spc ) -  Show package's category.
	show-all-categories (sac ) -  Show all categories.
	keep                (ke  ) -  Mark package as "non auto-removable".
	unkeep              (uk  ) -  Mark package as "auto-removable".
	show-keep           (sk  ) -  Display "non auto-removable" packages.
	show-no-keep        (snk ) -  Display "auto-removable" packages.
	search              (se  ) -  Search for a package.
	clean               (cl  ) -  Clean packages cache.
	autoremove          (ar  ) -  Autoremove orphan dependencies.
	export              (ex  ) -  Export "non auto-removable" packages to stdout.
	import              (im  ) -  Import "non auto-removable" package list from file.
	provides            (prov) -  Show what files a package provides.
	requires            (req ) -  Show what files a package requires.
	pkg-content         (pc  ) -  Show remote package's content.
	pkg-descr           (pd  ) -  Show remote package's long-description.
	pkg-build-defs      (pbd ) -  Show remote package's build definitions.
	stats               (st  ) -  Packages statistics.

### [Read the pkgin man page!](http://saveosx.org/man/)     

