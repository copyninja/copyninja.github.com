---
layout: post
title: "Note to Self: Telling apt to download specific architecture information only"
date: "2012-12-27 20:32:17 +0530"
tags:
 - Debian
 - multiarch
 - self-notes
---

If you have enabled multi-arch enabled in your system and one of the
third party repository you use in /etc/apt/sources.list is not
providing the foreign arch you have selected then fear not just do the
below for that particular repository line.
    deb [arch=arch1] uri distribution component

In my case mozilla.debian.net doesn't provide binary-armel hence I just did this
    deb [arch=amd64] http://localhost:9999/mdn experimental iceweasel-aurora

and apt stopped complaining about missing foreign arch. Well this is
present in man page of sources.list but I just wrote here so I can
find it easily next time :-).
