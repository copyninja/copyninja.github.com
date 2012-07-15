---
layout: post
title: "Note to Self: Deleting Remote Branches and Tags in Git"
tags:
 - git
 - programming
---

Its been a while I'm using Git as a version control system for my various work whether
it is FOSS related or my professional work. Every time I stumble into a case where I
need to delete an accidentally pushed branch or tag on remote and every time I forget
how I did it last time. Today I did it again and I had to search it again to find a
method. So here it goes this is a note to myself so I won't forget it next time

Deleting a remote branch
    git push origin :branchname
    
Deleting a remote tag
    git push origin :refs/tags/tagname
    
Where origin can be replaced by proper remote if you are using multiple remote for mirroring
purpose.

If you want to delete locally use following code
    git branch -d branchname
    git tag -d tagname
    
Note: To delete tag remotes you need to delete it locally first and then push it. 

That's it hope it helps others too :-)
