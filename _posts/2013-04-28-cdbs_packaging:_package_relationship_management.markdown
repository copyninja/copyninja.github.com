---
layout: post
title: "CDBS Packaging: package relationship management"
date: "2013-05-05 17:49:45 +0530"
tags:
- Debian
- cdbs
- packaging
- manual
---

(It took me a while to come up with new CDBS packaging series post not
because I stopped using CDBS just because I was procrastinating myself
as busy)

This is the second post in the CDBS packaging series. In this series
I'm going to talk about package relationship management.

The better example where this feature is useful is packages where
build-depends and run-time dependencies overlap. Most of the Perl
modules which have test suites have build-depend and run-time
dependency intersection. So let me take example of a Perl module. 

First lets see control file of a Perl package which is not using CDBS
and then let me explain how CDBS can help you improve the situation. I
choose *libxml-libxml-perl* lets see part of control file which includes
*Build-Depends Depends Suggests Recommends*.

{% highlight control %}
Source: libxml-libxml-perl
Maintainer: Debian Perl Group <pkg-perl-maintainers@lists.alioth.debian.org>
Uploaders: Jonathan Yu <jawnsy@cpan.org>,
 gregor herrmann <gregoa@debian.org>,
 Chris Butler <chrisb@debian.org>
Section: perl
Priority: optional
Build-Depends: perl (>= 5.12),
 debhelper (>= 9.20120312),
 libtest-pod-perl,
 libxml2-dev,
 libxml-namespacesupport-perl,
 libxml-sax-perl,
 zlib1g-dev
Standards-Version: 3.9.4
Vcs-Browser: http://anonscm.debian.org/gitweb/?p=pkg-perl/packages/libxml-libxml-perl.git
Vcs-Git: git://anonscm.debian.org/pkg-perl/packages/libxml-libxml-perl.git
Homepage: https://metacpan.org/release/XML-LibXML/

Package: libxml-libxml-perl
Architecture: any
Depends: ${shlibs:Depends}, ${misc:Depends}, ${perl:Depends},
 libxml-namespacesupport-perl,
 libxml-sax-perl
Breaks: libxml-libxml-common-perl
Replaces: libxml-libxml-common-perl
Description: Perl interface to the libxml2 library
 XML::LibXML is a Perl interface to the GNOME libxml2 library, which provides
 interfaces for parsing and manipulating XML files. This module allows Perl
 programmers to make use of the highly capable validating XML parser and the
 high performance Document Object Model (DOM) implementation. Additionally, it
 supports using the XML Path Language (XPath) to find and extract information.
{% endhighlight %}

So 2 packages are both in Build-Depends and Depends field

 1. libsax-xml-perl
 2. libxml-namespacesupport-perl

So in this situation there is a possibility that we miss to add one or
both of these packages into Depends field, I'm not saying we will
surely miss but we might after all we are all human beings.

So how can we improve the situation using CDBS? Let me go through step
by step on what we need to do.

1. Create a file called control.in with same above contents but slight
   modification in Build-Depends and Depends section. I will display
   the diff below to avoid re-pasting entire file again and again.

{% highlight udiff %}
--- debian/control      2013-04-28 23:08:11.930082600 +0530
+++ debian/control.in   2013-05-04 20:51:18.849680419 +0530
@@ -5,13 +5,7 @@
  Chris Butler <chrisb@debian.org>
 Section: perl
 Priority: optional
-Build-Depends: perl (>= 5.12),
- debhelper (>= 9.20120312),
- libtest-pod-perl,
- libxml2-dev,
- libxml-namespacesupport-perl,
- libxml-sax-perl,
- zlib1g-dev
+Build-Depends: @cdbs@
 Standards-Version: 3.9.4
 Vcs-Browser: http://anonscm.debian.org/gitweb/?p=pkg-perl/packages/libxml-libxml-perl.git
 Vcs-Git: git://anonscm.debian.org/pkg-perl/packages/libxml-libxml-perl.git
@@ -20,8 +14,7 @@
 Package: libxml-libxml-perl
 Architecture: any
 Depends: ${shlibs:Depends}, ${misc:Depends}, ${perl:Depends},
- libxml-namespacesupport-perl,
- libxml-sax-perl
+ ${cdbs:Depends}
 Breaks: libxml-libxml-common-perl
 Replaces: libxml-libxml-common-perl
 Description: Perl interface to the libxml2 library
@@ -30,4 +23,3 @@
  programmers to make use of the highly capable validating XML parser and the
  high performance Document Object Model (DOM) implementation. Additionally, it
  supports using the XML Path Language (XPath) to find and extract information.
-
{% endhighlight %}

2. Next we need to have something like below in the rule files

{% highlight make %}
#!/usr/bin/make -f

include /usr/share/cdbs/1/rules/debhelper.mk
include /usr/share/cdbs/1/rules/utils.mk
include /usr/share/cdbs/1/rules/upstream-tarball.mk
include /usr/share/cdbs/1/class/perl-makemaker.mk

pkg = $(DEB_SOURCE_PACKAGE)

deps = libxml-libxml-perl libxml-sax-perl
deps-test = libtest-pod-perl

CDBS_BUILD_DEPENDS +=, $(deps), $(deps-test)
CDBS_BUILD_DEPENDS +=, zlib1g-dev, libxml2-dev, perl (>= 5.12)

CDBS_DEPENDS_$(pkg) = , $(deps)

{% endhighlight %}

So basically we moved all Build-Depends and Depends to rules file. The
common ones are placed in deps variable and assigned to both
Build-Depends and Depends. CDBS uses following variables for package
relationship management.

1. CDBS_BUILD_DEPENDS: This variable helps you manage Build-Depends
   field and all you need to do is in your control.in files
   Build-Depends field put place holder @cdbs@
2. CDBS_DEPENDS: This field can be used to manage Depends field of
   binary package for each binary package you need to have one
   CDBS_DEPENDS_pkgname variable with depends assigned to it. And in
   your control.in append ${cdbs:Depends} to Depends field.
3. CDBS_PROVIDES, CDBS_BREAKS, CDBS_RECOMMENDS, CDBS_PREDEPENDS,
   CDBS_SUGGESTS, CDBS_REPLACES: all these does the job what you think
   it does :-).

Other than CDBS_BUILD_DEPENDS all other variables work using substvars
i.e. CDBS will put the respective substitutions in *pkgname.substvars*
file which will be used during deb creation to replace things in
control file.

So to make CDBS generate new control file run the below command

{% highlight console %}
DEB_MAINTAINER_MODE=1 fakeroot debian/rules debian/control
{% endhighlight %}

Basically this command needs to be executed before starting build
process if you miss your changes will not be reflected into
*debian/control*. Additionally this feature is Maintainer Mode helper
tool because Debian policy prohibits change of debian/control during
**normal** package build.

So what is the benefit of using this feature of CDBS? I've listed some
of them which I felt are obvious.

1. When there is intersection in Build-Depends and Depends this
   feature from CDBS is helpful. As I shown above put all intersecting
   dependencies in common variable and appropriately assign them
   wherever it is required. Thus we can avoid possible missing of some
   of run-time dependencies due to human error.
2. It is also possible that newer version of package requires specific
   version of some package (mostly libraries) and we updated build
   dependencies but we might forget to do the same in Depends, by
   using this feature we can make sure we will not miss such minute
   details.
   
One last thing I want to point out is if you are NMUing a CDBS package

> NMUs need not (but are encouraged to) make special use of these tools.
> In particular, the debian/control.in file can be completely ignored.

Before closing down the post, If you find some mistake in the post
please let me know either through comments or through the
[email](http://scr.im/vasudev).

Soon I will be back with new CDBS recipes till then cya.
