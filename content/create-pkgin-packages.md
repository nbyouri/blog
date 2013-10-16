Title: Create pkgin packages on Mac OS X.
Date:  2013-10-16 00:00
Category: Mac OS X
Tags: Mac OS X, packages
Slug: pkgin-create
Author: Youri Mouton
Summary: A little guide on how to manually create pkgin packages on Mac OS X!

# Create a package! 
  
Here we'll take ncurses as an example:

##If the package is available on pkgsrc:
Get the package from the pkgsrc/packages directory.

Otherwise, here's how to make it manually:


##Create the work directory.            

> `mkdir -p pkgsrc/devel/ncurses`          

> `cd pkgsrc/devel/ncurses`             

##Create a build-info file.

> `pkg_info -X pkg_install \`              
>  `| egrep '^(MACHINE_ARCH|OPSYS|OS_VERSION|PKGTOOLS_VERSION)' >build-info`            


##Create a comment file.

pkg_info ncurses, copy the comment content.

##Create a description file.

same but for description

##Copy the files provided by a package.

> `mkdir files; cd files`                 

> `pkg_info -L ncurses |awk '/^\//{gsub(/\/usr\/pkg\//, "");print "rsync -Ra ", $1, " ."}' | zsh`            


##Create the contents file.

> `echo "@cwd /usr/pkg" > contents`             

> `echo "@name ncurses-5.9nb2" >> contents`                

You can add dependencies here like this, in example(not needed for ncurses):

> `echo "@pkgdep libevent>=2.0.10" >> contents`      

### Add a listing of the files to be installed in the prefix:

> `(cd files; find * -type f -or -type l | sort) >> contents`               



##Create the package.

> `pkg_create -B build-info -c comment -d description -f contents -I /usr/pkg -p files -U ncurses-5.9nb2.tgz`                          


##Create a package_summary file.

> `pkg_info -X ncurses-5.9nb2.tgz|gzip -9 >pkg_summary.gz`          

##Upload or move to your local repository!


