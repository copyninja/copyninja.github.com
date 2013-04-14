---
layout: post
title: "Handling C++ symbols that vary across architectures"
date: "2013-04-14 18:45:25 +0530"
tags:
- Debian
- packaging
- c++
- symbol files
---

Disclaimer
----------

I'm no symbol expert and dealing with symbol files for first time from
the time I started packaging. What I did here is depending on some
suggestions I got in #debian-mentors.

If you think what I did was wrong please enlighten me :-).

Problem
-------

Recently 2 of my library packages *pugixml* and *ctpp2* got accepted
into Debian archive and when buildd tried to build them on remaining
architectures other than one for which I uploaded (amd64) builds
failed. This was expected as symbols file which I generated was for
amd64. As usual I got 2 serious bug reports
[#704718](http://bugs.debian.org/704718) and
[#705135](http://bugs.debian.org/705135).

Solution
--------

First I was not sure how to handle this. I read article on symbols
files handling by rra [1] and tried to use pkgkde-symbolshelper tool
only to quickly figure out that I need to use pkgkde_symbolshelper
addon for dh sequencer. But this was not possible for me as I was
using CDBS for packaging.

I did a quick chat on #debian-mentors and some one suggested me to tag
symbols which vary across architecture with (c++) tag. First I was not
sure but after reading dpkg-gensymbols man page understood that I need
to replace the entire mangled symbols lines with de-mangled version
tagged with (c++) in the beginning.

But this was hectic job searching for each deleted symbols and
replacing it. So I thought of writing a script to do the job and after
struggling for 3 days (yeah I was bit dumb that I didn't read manual
date: "2013-04-14 18:39:20 +0530"
*pugixml* and *ctpp2* package using it, which is now waiting for Jonas
for uploading it.

Here is the script

{% highlight sh %}
#!/bin/bash
set +x

if [ $# -lt 3 ]; then
    echo "Usage: $0 failed_buildlogs_directory symbols_file package_version"
    exit 2
fi
    
BUILD_LOG_DIRECTORY=$1
SYMBOLS_FILE=$2
PACKAGE_VERSION=$3
VERSION_TO_REPLACE=" $PACKAGE_VERSION\""

for LOGFILE in $(ls $BUILD_LOG_DIRECTORY/*.build); do
    for i in $(grep '^-\s_Z' $LOGFILE | perl -pe 's/-//g;'); do
        if [ $i = $PACKAGE_VERSION ];then
            continue
        fi
        demangled_version="\""$(echo $i" "$PACKAGE_VERSION | c++filt)"\""
        tagged_version="(c++)"${demangled_version%$VERSION_TO_REPLACE}"\" "$PACKAGE_VERSION
        escaped_tagged_version=$(echo $tagged_version | sed 's/\&/\\\&/')
        sed -i "s#$i $PACKAGE_VERSION#$escaped_tagged_version#" $SYMBOLS_FILE
   done
done
{% endhighlight %}

So basically to make this work we need all buildlogs to be downloaded
from buildd's again this was easy thanks to rra for developing
*pkgkde-getbuildlogs* :-).

Once you have build logs directory run the above script as follows

<pre>
cppsymbol_replace.sh path_to_buildlogs path_to_symbol_file upstream_version
</pre>
   
After replacing symbols I tried to build package on i386 chroot and
build passed successfully but lintian told me that there are symbols
which have Debian version appended to it and this might lead to
date: "2013-04-14 18:42:42 +0530"
back to mentors :-).

It is this time I really understood concept of mangled names generated
by compiler and why it vary across the architecture ;-).

This time some one by nick *pochu* suggested me to pass option -v with
package version to dpkg-gensymbols to make it generate symbols with
package version and not Debian version.

The following probably needs to be done if package uses dh sequencer
but I'm not sure as I've not tested it. If wrong please correct me.

{% highlight make %}
override_dh_makeshlibs:
    dh_makeshlibs -- -v$PACKAGEVERION #package version needs to be either extracted using parsechangelog or manually fed
{% endhighlight %}

If you are using CDBS this is pretty simple. Just add following to rules

{% highlight make %}
DEB_DH_MAKESHLIBS_ARGS_$(pkgname) += -- -v$(DEB_UPSTREAM_VERSION)
{% endhighlight %}

I noticed that when I provide (c++) tagged de-mangled name
dpkg-gensymbols simply replaces it with proper mangled name but the
deletion doesn't trigger an error in dpkg-gensymbols.

This script me allowed to replace 128 symbols which were very tricky
and long with de-mangled and tagged version in ctpp2, so I hope it
should work across different packages without any problem. Only silly
mistake I did was occurrence of & symbol in function making sed go mad
which I took one full day to debug :facepalm:.

So that's it folks, if you see something wrong in what I did please
let me know through the comments.

[1] [http://www.eyrie.org/~eagle/journal/2012-01/008.html](http://www.eyrie.org/~eagle/journal/2012-01/008.html)
