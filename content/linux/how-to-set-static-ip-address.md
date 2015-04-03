Title: How to set static ip address on linux
Slug: how-to-set-static-ip-address-linux
Lang: en
Date: 2015-03-31 15:30
Modified: 2015-03-31 15:30
Category: linux
Tags: howto, networking
Authors: Piergiorgio Faraglia
Summary: Steps to set static ip address on a linux machine.

Current linux distributions are configured to assign dynamic ip addresses when a machine is connected to net.

It's useful, overall on subnet configurations, to assign a static ip address
to a specific machine. With the following instructions I explain how to assign
that specific address.

Suppose you want to assign an ip address 192.168.1.10 to the interface eth0. The steps are:

Open interfaces configuration file with root privileges:

    sudo vi /etc/network/interfaces

Insert interface directives to the target interface:

    auto eth0
    iface eth0 inet static
        address     192.68.1.10
        network     192.168.1.0
        netmask     255.255.255.0
        broadcast   192.168.1.255
        gateway     192.168.1.1

Restart network interface with root privileges:

    sudo ifconfig eth0 down
    sudo ifconfig eth0 up
    sudo /etc/init.d/networking stop
    sudo /etc/init.d/networking start
