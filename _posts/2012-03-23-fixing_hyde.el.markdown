---
layout: post
title: "Fixing hyde.el"
---

Recently after changing my blog to use jekyll and Github I came across the
*hyde.el* an emacs plugin which allows to maintain a jekyll powered blog from
emacs. You can find the post by author [here](http://nibrahim.net.in/2010/11/11/hyde_%3A_an_emacs_mode_for_jekyll_blogs.html)
and source code [here on Github](https://github.com/nibrahim/Hyde).

At first site I was very happy about plugin and started using it but I could successfully
use it only once properly then whenever I launch the plugin I get error message

<blockquote>*zsh:cd blog path no such directory*</blockquote>

***(Note: I'm a zsh user not sure if this error is particular to zsh only. If you face 
same error on other shell please let me know) ***

After error *hyde mode* never showed jekyll blog properly. Looking at the source code
I saw all the statements which were commands were executed using *shell-command* elisp
function similar to following

{% highlight elisp %}
let (
(cmd (format "cd '%s' && git diff-files --quiet '%s' > /dev/null" repo file))
)
    (= (shell-command cmd) 1))
{% endhighlight%}

The cd command in the string was failing some how spoiling all other stuff!.. Probably the *~* in 
the path to blog was not properly expanded by *shell-command*, So I thought why not use elisp in
built *cd* function instead and bingo the hyde mode works perfectly fine now!.. 

I've raised a [pull request](https://github.com/nibrahim/Hyde/pull/5) as I don't like to maintain
a fork. Hope author will consider merging my changes. Hope this fix helps others too. Cya.
