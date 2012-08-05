---
layout: post
title: "Logging issue with Flask"
tags:
 - python
 - Programming
 - flask
---

While enabling logging for release of rewritten version of SILPA described in my 
[previous post](http://copyninja.info/2012/08/rewriting_silpa_with_flask_microframework.html)
I faced a weird problem. I enabled Logging as described in the Flask documentation but SILPA
won't log anything to the log even though log file is created in whatever location I gave while
configuring the logging. 

Flask documentation suggests following way to use logging 
{% highlight python %}
import logging
from logging.handlers import RequiredHandler
file_handler = RequiredHandler(...)
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)
{% endhighlight %}

After banging my head for some time  I again wanted to look at Python's logging [tutorials](http://docs.python.org/howto/logging.html#logging-advanced-tutorial)
see if I'm doing something wrong and I found this example
{% highlight python %}
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
{% endhighlight %}

So there it is I need to set the logging level even on logger to same level as what I set on my handler.
Now I didn't take time to read the documentation because I wanted to see if my findings really does the
trick so I modified function configuring logging to look something like below (I'm taking the example given
in Flask documentation itself real code can be seen in[ SILPA code on Github](https://github.com/copyninja/Silpa-Flask))

{% highlight python %}
import logging
from logging.handlers import RequiredHandler

file_handler = RequiredHandler(...)
file_handler.setLevel(logging.WARNING)

app.logger.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)
{% endhighlight %}

This actually did the trick and now Flask is happily logging whatever I give to *app.logger.levelname* So I
don't know this was my stupidity or fault in Flask's documentation by forgetting to mention this crucial point.
But in the end all is well :-)

Do comment your thoughts.
