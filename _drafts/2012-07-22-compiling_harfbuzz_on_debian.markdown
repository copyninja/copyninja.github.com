---
layout: post
title: "Compiling Harfbuzz on Debian"
tags:
- Debian
- Harfbuzz
---

Harfbuzz (more correctly harfbuzz-ng) is a Text Layout/shaping engine. Mostly supporting rendering
of Text including complex scripts. A quote taken from Wikipedia which describes [harfbuzz](https://en.wikipedia.org/wiki/HarfBuzz#HarfBuzz)
<blockquote>
HarfBuzz (in Persian: حرف‌باز) is a layout/shaping engine for OpenType fonts. Its purpose is to standardize text layout in FOSS; its code originally started as part of the FreeType project, was then developed separately in Qt and Pango, and finally merged back into a common repository. Both Qt and Pango currently use HarfBuzz; other standalone users include Firefox and Chromium, the open source project behind Google Chrome.
</blockquote>

Coming directly to the point. You can get Harfbuzz from its Git repository hosted on[ Freedesktop](http://cgit.freedesktop.org/harfbuzz).
It requires following library and binary compilation
<pre>
    1. ragel: Finite state machine code compiler
    2. libglib2.0-dev: Glib Development files
    3. libcairo2-dev : Cairo 2D graphics library development files
    4. libicu-dev: Development components for International components for Unicode
    5. libgraphite2-dev: Development files for libgraphite2
    6. libfreetype6-dev: Freetype 2 library development files
</pre>

Once you install all the above package. Follow following commands to build the harfbuzz.
{% highlight bash %}
./autogen.sh
./configure --prefix=/usr
make
sudo make install
{% endhighlight %}

You can skip make install if you don't like it to be installed on system.I actually wanted to work on the Debian package
of Harfbuzz but since there is some one already working on [it](http://lists.alioth.debian.org/pipermail/pkg-fonts-devel/2012-July/010867.html).
Probably I will wait till the guy completes package.

I will write on testing the text rendering of your language using harfbuzz in my next post. Till then Cya.
