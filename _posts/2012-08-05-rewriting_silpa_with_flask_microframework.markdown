---
layout: post
title: "Rewriting SILPA with Flask microframework"
tags:
 - python
 - Programming
---

As a introduction on what is SILPA you can read my [previous post](http://copyninja.info/2010/05/silpa-an-indian-language-processing-application.html)
This application was written by Santhosh about 6-7 years ago ( Correct me if I'm wrong Santhosh ;-) ) in Python without using any web framework.
He crafted whole system single handed and with very nice ideas. He wrote all the modules available in it for all possible Indian languages even
though he is only native Malayalam speaker. I joined him 3 years back and I was providing some or other improvements and he ultimately made me
as the *Co-Developer* of SILPA.

Recently I came across the *Flask* microframework and thought of rewriting SILPA to use Flask. You might ask me why Flask? So here are
my reasonings
<pre>
 1. Why reinvent Python webframework when we can use existing?
 2. All Python modules are useful even outside SILPA project why make them dependent on SILPA code?
 3. Templating system used is very old and can't be ported to new Python version lets use something which is new and portable
 4. I was overwhelmed by Flask :P
</pre>

So I proposed about this to Santhosh and he asked me for a POC code. I started working on *April 8 2012 and today by August 5* I can say
I've first stable version of SILPA rewritten using Flask deployable over WSGI on Apache2. It can also be deployed on other servers but
I never tried as I've been using Apache for long time. It took me quite a bit of time but to be frank in the middle I completely had stopped
coding because of some other works. Here is the commit graph and code frequency graphs from Github.

<img src='/images/commit-graph-silpa.png' align="center" caption="Commit Graph"/>
<br/>
<img src='images/code-frequency-silpa.png' align="center" caption="Code Frequency"/>

Changes in New Version
----------------------
Here is some major changes in current version.
<pre>
1. Newly developed framework provides plug and play features for new modules.
2. You need to install the modules which you want to run on it separately using PIP and only minimal code change is required. Only configuration and webbridge.py will be changed. Ofcourse you need to add html file to *templates* folder.
3. This version uses decent routing logic from Flask for page serving.
4. It also provides JSONRPC interface which is compatible with previous version but only with method name changed.
5. This version separates out run time module loading and routing the request to modules.
6. Dynamic module loading now happens only at the beginning of application, so if I want to implement caching for particular services it will be straight forward now.
7. Routing requests to proper module is adapted from old version with few modifications
8. All previous pages are now converted to use *Jinja2* template system.
</pre>

Things Remaining TODO
----------------------
Below is some stuffs still pending before this version can completely replace [http://silpa.org.in](http://silpa.org.in)
<pre>
1. Separate all modules from original SILPA
2. Provide RESTful interface
3. Provide proper LICENSE, AUTHORS file for all modules 
4. Give a Nice UI
5. Find a better name than *SILPA*
...
</pre>

