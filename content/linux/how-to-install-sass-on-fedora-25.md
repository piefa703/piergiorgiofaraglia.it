Title: How to install sass on fedora 25
Slug: how-to-install-sass-on-fedora-25
Lang: en
Date: 2017-11-04 08:00
Modified: 2017-11-04 08:00
Category: linux
Tags: nfs, howto, networking, sass, css
Authors: Piergiorgio Faraglia
Summary: How to install sass on fedora 25.

I need sass for one of my projects and then I install it on my fedora 25. I will show the steps to do that.

You need to install gem on your system:

  # sudo dnf install rubygems
  
You need to update your gem

  # sudo gem update --system
  
Then install sass

  # sudo gem install sass --pre
