---
layout: post
title: "Packaging Falcon Programming Language for Debian"
tags:
 - Debian
 - packaging
---
[Falcon](http://falconpl.org/) is a programming language which is not yet packaged for
Debian. I saw that the ITP[#460591](http://bugs.debian.org/460591) is owned by my Debian
mentor and good friend [Kartik Mistry](http://0x1f1f.wordpress.com/). So I jumped in to
help him finish this package.

Ok enough of introduction now directly to point. We thought its better to base
the Debian package on upstream Git repository itself so we can do snapshot release like *Go Language*
package is doing. So in this post I'm going to give steps we used to do this and also guidelines
on future packaging of Falcon.

<ol>
1. First step we need to clone the upstream Falcon's git repo. Then duplicate *master* branch into
  *upstream* branch.
  {% highlight bash %}
  git clone http://git.falconpl.org/falcon.git
  git checkout -b upstream
  {% endhighlight %}

2. Now by staying on *upstream* branch we made it track the upstream's git repo using following commands
   {% highlight bash %}
   git remote add upstream-falcon http://git.falconpl.org/falcon.git
   git branch --set-upstream upstream-falcon
   {% endhighlight %}

3. We made the master branch point to origin which is our collab-maint git repository.
   {% highlight bash %}
   git checkout master
   git remote set-url origin git.debian.org:/git/collab-maint/falconpl.git
   {% endhighlight %}

4. Next is creating the pristine-tar branch so that it will be easy for us to build using *git-buildpackage*
   tools. We just took snapshot of upstream's head and created a tarball and then used *pristine-tar* utility
   to commit it. Then we tagged upstream version
   {% highlight bash %}
   git checkout upstream
   git archive --format=tar HEAD | gzip -9 > ../falconpl_0.9.6.8-git20120403.orig.tar.gz
   git tag upstream/0.9.6.8-git20120403
   pristine-tar commit ../falconpl_0.9.6.8-git20120403.orig.tar.gz
   {% endhighlight%}
   
5. And finally we copied **debian** directory from Ubuntu's falconpl package into our master branch and modified
   the debian changelog to match our new snapshot version. To release a new version all we need to do is follow 
   step 4 and then additionally merge the upstream with master

</ol>

So our repo is now in proper shape to be built using git-buildpackage. But we are left with many things to clean
and fix. So things which are currently pending are


1. *Make copyright file in Debian copyright format 1.0*
2. *Separate out each module falcon builds into separate package. Looks like Ubuntu doesn't install any of modules*
3. *Last but not the least upload it to Debian ( Kartik's task :-) )*


Even though I'm packaging Falcon for Debian I'm not a Falcon programmer so if there are any Falcon programmer reading this
post and want to help you are always welcome :-).
