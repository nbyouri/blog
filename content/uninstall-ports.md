Title: Uninstalling package managers on Mac OS X
Date: 2013-10-09 20:27
Category: Mac OS X
Tags: Mac OS X, packages
Slug: uninstall-pm
Author: Youri Mouton
Summary: A little guide on how to uninstall package managers.

This can be a pain sometimes when you want to start over or if you're 
just tired of your package manager's complexity and if it's just broken.

## MacPorts:

> Uninstall the installed ports      
`$ sudo port -fp uninstall installed`          

> Then delete all the files     
`sudo rm -rf   \  `
    `/opt/local \             `
    `/Applications/DarwinPorts \`        
    `/Applications/MacPorts \          `
    `/Library/LaunchDaemons/org.macports.* \          `
    `/Library/Receipts/DarwinPorts*.pkg \           `
    `/Library/Receipts/MacPorts*.pkg \            `
    `/Library/StartupItems/DarwinPortsStartup \        `
    `/Library/Tcl/darwinports1.0 \          `
    `/Library/Tcl/macports1.0 \         ` 
    `~/.macports`         

## Homebrew

>Delete all the files     

`$ cd /usr/local`         

`$ rm -rf Cellar`         

`$ brew prune`       

`$ git ls-files|xargs rm -rf`        

`$ rm -r Library/Homebrew Library/Aliases Library/Formula Library/Contributions`     

`$ rm -rf .git`     

`$ rm -rf ~/Library/Caches/Homebrew`     

## Install a good package manager! Like [pkgin](http://saveosx.org/pkgsrc-osx.html) :) 
