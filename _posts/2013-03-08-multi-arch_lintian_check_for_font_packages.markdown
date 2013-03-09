---
layout: post
title: "Multi-Arch lintian check for font packages"
date: "2013-03-08 20:44:50 +0530"
tags:
- Debian
- lintian
- packaging
- multi-arch
---

I've provided a new patch for lintian to warn about font packages that
are not marked as *Multi-Arch foreign or allowed*. Its already
included in the lintian by *Neils Thykier* and will be part of version
*2.5.12*. The following tag has been implemented

    font-package-not-multi-arch-foreign
    
A Bit of History for this implementation is as follows:

We got a bug report on one of the fonts in pkg-fonts team that its not
been installed in i386 architecture on a amd64 multi-arch system
[#694864](http://bugs.debian.org/694864). We were first confused but
[Daniel Kahn Gillmor](http://debian-administration.org/users/dkg)
[pointed](http://lists.alioth.debian.org/pipermail/pkg-fonts-devel/2012-December/011392.html)
that we indeed need to mark all font packages as Multi-Arch
foreign. He proposed that we should write a lintian check for this
which I volunteered to do and then forgot!. Recently I was checking my
QA page and landed into Ubuntu's page of my package where I saw they
were patching imported font package and marking them as Multi-Arch:
foreign and I suddenly remembered my promise! and this patch was the
result of same enlightenment :-).

Since there is huge number of font packages maintained by pkg-fonts
devel we targeted this for Jessie release. 

> Here by I request all font package maintainers to consider marking
> their packages as Multi-Arch foreign. I also request people to join us
> on pkg-fonts-devel and help us doing this for all font packages
> maintained by the team, we really lack people in the team.
