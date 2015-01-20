#### Installing the required files for running pkgin:

The packages are built on Mac OS X Yosemite using the pkgsrc framework from the NetBSD Foundation.

[Download](http://pkgsrc.saveosx.org/Darwin/bootstrap/bootstrap-x86_64-2014Q4.tar.gz) the archive needed to install pkgsrc and pkgin (8MB)

Extract it with

`$ sudo tar -C / -xzf bootstrap-x86_64-2014Q4.tar.gz`

Have a [look](http://pkgsrc.saveosx.org/Darwin/2014Q4/x86_64/All/) our latest packages, they're 64bit and PGP signed!

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

Install a package       

`$ sudo pkgin in tmux`      

List available packages     

`$ pkgin avail`      

List installed packages      

`$ pkgin list`      

Package statistics

`$ pkgin stats`

More features are available, remember to read the man page !

For info about creating packages and helping out, check the [blog](blog)!

#### Repository status: 

        Number of repositories: 1
        Packages available: 11494
        Total size of packages: 11G
