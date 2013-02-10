---
layout: post
title: "Multi-Arch based Cross-Compilation"
date: "2013-01-26 21:07:26 +0530"
tags:
- Debian
- multi-arch
- cross-compiling
---

Disclaimer:
----------

I'm not cross-compile expert or have done cross-compilation before
this post is not comparison between normal cross compilation and
multi-arch based cross compilation, this post is purely about how I
achieved cross compilation using Multi-Arch feature introduced by
Debian.

Problem
----------

Get a OS ready for the raspberry-pi computer I purchased recently. No
I don't want to use Raspbian even though it claims as Debian itself. I
want a clean armel based OS with only components what I require. This
is also sort of experiment to improve
[boxer](http://anonscm.debian.org/gitweb/?p=collab-maint/boxer.git;a=summary)
by adding rpi support to it. (Even though Jonas considers rpi as swamp ;-) )

Components need to be compiled:

 1. u-boot
 2. Linux Kernel
 
Architecture: armel

Solution:
----------

The first thing to do is to add the required foreign architecture in
my case *armel*, this can be done using below command.

    dpkg --add-architecture armel
    
Then update package list with whatever package management utility, in
my case I used aptitude. But before doing that we need to add a
repository which provides us GCC cross compiler with gnueabi
support. Yes it is not yet in Debian main and with my discussion with
Jonas what I understood is since Wheezy is first of a kind with
multi-arch capability we can expect cross compiler tool only from
Jessie.

    deb http://emdebian.org/~thibg/repo/ sid main
    
This repository is by emdebian contributor not completely sure about
his name but he hangs in #emdebian with nick ThibG. According to Jonas
repository is bit old but its working where as latest repository from
wookey is broken, though this was told a couple of week back and I
don't know about current status.

Now run *aptitude update* to get package list refreshed after adding
the new repo. Once done we need to install *gcc-4.7-arm-linux-gnueabi*
, run the following command and I suggest you use aptitude because it
will help you resolve dependency mess easily. When dependency
suggestion is given for first time try pressing *e* to enter full
screen aptitude and navigate through the solution provided using *.*
and *,* and select appropriate solution using *!*. Then press *g* to
install the package.

    aptitude install gcc-4.7-arm-linux-gnueabi
    
This scenario showed me real power of the aptitude which till then I
was thinking as nutcase :-).

The above package installs all the cross compilation tools required
beginning with prefix *arm-linux-gnueabi-* but it doesn't create a
required symlink /usr/bin/arm-linux-gnueabi-gcc pointing to
/usr/bin/arm-linux-gnueabi-gcc-4.7 which is required by all tools for
cross compiling just create this symlink manually and you should have
GNU cross compiler ready on your system for
*[armel](http://wiki.debian.org/ArmEabiPort* architecture.

    ln -s /usr/bin/arm-linux-gnueabi-gcc-4.7 /usr/bin/arm-linux-gnueabi
    
Now to cross compile all you need to do is

    export CROSS_COMPILE=arm-linux-gnueabi-
    

Once this package lands to Debian main, cross compiling will be way
more easier.

