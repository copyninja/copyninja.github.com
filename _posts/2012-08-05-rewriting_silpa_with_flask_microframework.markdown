---
layout: post
title: "Rewriting SILPA with Flask microframework"
tags:
 - python
 - Programming
 - SILPA
---

As a introduction on what is SILPA you can read my [previous post](http://copyninja.info/2010/05/silpa-an-indian-language-processing-application.html)
This application was written by Santhosh <strike>about 6-7 years ago</strike> in May <strike>2010</strike> 2009 ( <strike> Correct me if I'm wrong Santhosh ;-)</strike> Thanks to Santhosh for correcting me ) in Python without using any web framework.
He crafted whole system single handed and with very nice ideas. He wrote all the modules available in it for all possible Indian languages even
though he is native Malayalam speaker. I joined him 3 years back and I was providing some or other improvements and he ultimately made me
as the *Co-Developer* of SILPA.

Recently I came across the *Flask* microframework and thought of rewriting SILPA to use Flask. You might ask me why Flask? So here are
my reasonings
<pre>
 1. Why reinvent Python webframework when we can use existing? Besides maintaining a not so well known framework code which is not written by you will be difficult    and time consuming.
 2. All Python modules are useful even outside SILPA project why make them dependent on SILPA code?
 3. Templating system used is very old and can't be ported to new Python version lets use something which is new and portable
 4. If new contributor wanted to add a module he need to understand SILPA framework to write and integrate it. This might be discouraging new
    contributions so lets use pure python module and make integration with SILPA straight forward.
 5. I was overwhelmed by Flask :P
</pre>

I had previously tried bottle microframework but for some reason I couldn't crack it so choosing of Flask is not because it was better among other available microframework or something like that. I choose it because I could easily understand it and it suited my needs better.

So I proposed about this to Santhosh and he asked me for a POC code. I started working on *April 8 2012 and today by August 5* I can say
I've first stable version of SILPA rewritten using Flask deployable over WSGI on Apache2. It can also be deployed on other servers supporting
WSGI interface. 

It took me quite a bit of time but to be frank in the middle I completely had stopped coding because of some other works. Here is the commit graph
and code frequency graphs from Github.
<br/>
<img class="post" src='/images/commit-graph-silpa.png' align="center" caption="Commit Graph"/>
<br/>
<img class="post" src='images/code-frequency-silpa.png' align="center" caption="Code Frequency"/>

Changes in New Version
----------------------
Here is some major changes in current version.
<pre>
1. Newly developed framework provides plug and play features for new modules.
2. You need to install the modules which you want to run on it separately using PIP and only minimal code change is required. Only configuration and webbridge.py 
   will be changed. Ofcourse you need to add html file to *templates* folder.
3. This version uses decent routing logic from Flask for page serving.
4. It also provides JSONRPC interface which is compatible with previous version but only with method name changed.
5. This version separates out run time module loading and routing the request to modules.
6. Dynamic module loading now happens only at the beginning of application, so if I want to implement caching for particular services it will be straight forward
   now.
7. Routing requests to proper module is adapted from old version with few modifications
8. All previous pages are now converted to use *Jinja2* template system.
</pre>

Things Remaining TODO
----------------------
Below is some stuffs still pending before this version can completely replace [http://silpa.org.in](http://silpa.org.in)
<pre>
1. Separate all modules from original SILPA and get it uploaded to pypi
2. Provide RESTful interface
3. Provide proper LICENSE, AUTHORS file for all modules 
4. Prepare a Nice UI
5. Find a better name than *SILPA*
...
</pre>

Update
------
<pre>
Forgot to provide the github link and demo link for the new version of SILPA. Thanks to Aravinda for pointing
it out. Here it goes
Github: <a href="http://github.com/copyninja/Silpa-Flask">http://github.com/copyninja/Silpa-Flask</a>
Demo: <a href="http://flasksilpa-indic.rhcloud.com">http://flasksilpa-indic.rhcloud.com</a>
</pre>
