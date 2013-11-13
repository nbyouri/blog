---
layout: post
title: Create pkgin packages on Mac OS X
author: Youri Mouton
---

## Create a package! 
  
Here we'll take ncurses as an example:

If the package is available on pkgsrc:
Get the package from the pkgsrc/packages directory.

Otherwise, here's how to make it manually:


#### Create the work directory.            

`mkdir -p pkgsrc/devel/ncurses`          

`cd pkgsrc/devel/ncurses`             

#### Create a build-info file.

`pkg_info -X pkg_install \`              
`| egrep '^(MACHINE_ARCH|OPSYS|OS_VERSION|PKGTOOLS_VERSION)' >build-info`            


#### Create a comment file.

The comment file should contain a few words about the package.

#### Create a description file.

same but a much longer description with homepage for description

#### Copy the files provided by a package.

`mkdir files; cd files`                 

and add the files that need to be in the package with complete directory hierarchy from the prefix.

If you're repackaging something from pkgsrc, you can use this command to get all the files at once.

`pkg_info -L ncurses |awk '/^\//{gsub(/\/usr\/pkg\//, "");print "rsync -Ra ", $1, " ."}' | zsh`            


#### Create the contents file.

Put the right prefix first:    

`echo "@cwd /usr/pkg" > contents`             

Then the name-version of the package:      

`echo "@name ncurses-5.9nb2" >> contents`                

You can add dependencies here like this, in example(not needed for ncurses):     

`echo "@pkgdep libevent>=2.0.10" >> contents`      

Add a listing of the files to be installed in the prefix:

`(cd files; find * -type f -or -type l | sort) >> contents`               



#### Create the package.

`pkg_create -B build-info -c comment -d description -f contents -I /usr/pkg -p files -U ncurses-5.9nb2.tgz`                          


Create a package_summary file in your local or remote repo after you uploaded all your packages!

`pkg_info -X *.tgz|gzip -9 > pkg_summary.gz`          



