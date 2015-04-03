Title: How to disable ssh root access
Slug: how-to-disable-ssh-root-access
Lang: en
Date: 2015-04-01 15:00
Modified: 2015-04-01 15:00
Category: linux
Tags: ssh, howto, networking, security
Authors: Piergiorgio Faraglia
Summary: Disable ssh root access to increase security of your servers.

SSH libraries installed on linux distributions enabled by default root user access.
Although on private or business intranet network such a feature could be sufficient in terms of security, on internet is better to disable ssh root access.

Following the steps below to disable it.

First of all, open ssh configuration file with root permissions:

    sudo vi /etc/ssh/ssh_config

Inside the file updates PermitRootLogin directive:

    PermitRootLogin no

Save file and restart ssh server:

    sudo /etc/init.d/ssh restart

From that moment you can't access your server as root user directly from outside the machine.
