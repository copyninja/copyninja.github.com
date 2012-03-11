---
layout: post
title: "ttf-indic-fonts to fonts-indic transition complete!"
tags:
- Debian
- news
---

We in Debian-IN team where maintaining ttf-indic-fonts a set of fonts for all 
Indian language fonts from various origin. This package used to build around 7
to 10 binary package of different Indian language. The source package ttf-indic-fonts
was itself a mess. It was a native package it was mixing all fonts with active
upstream and inactive upstream together which was hard to maintain. Last April
I transitioned this package from old packaging style (which version I don't remember)
to *dh7* standard. At the same time **bubulle** asked me it would be great if I
can rename the package to  [Fonts team new packaging policy](http://wiki.debian.org/Fonts/PackagingPolicy)
Even though I was just beginning with Debian packaging I dared to propose a [draft](http://lists.alioth.debian.org/pipermail/debian-in-workers/2011-May/001587.html)
:) Well it was in May and now its March 2012 almost one year over and We have 
successfully finished the transition and [Kartik](http://0x1f1f.wordpress.com/)
uploaded all packages to Debian. Now Debian-IN team maintains 62 packages and
me? Yeah my package count jumped from 12 to 38! Almost close to close to number
of packages Kartik is maintaining :)

Please do the testing report any bugs! Cya
