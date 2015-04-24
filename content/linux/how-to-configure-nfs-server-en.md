Title: How to configure nfs server
Slug: how-to-configure-nfs-server
Lang: en
Date: 2015-04-24 18:00
Modified: 2015-04-24 18:00
Category: linux
Tags: nfs, howto, networking
Authors: Piergiorgio Faraglia
Summary: Configure nfs server in order to share folders.

In order to share folders among devices you can use NFS (Network File System).
To install an nfs server on linux using apt executes following command:

	# apt-get install nfs-common nfs-kernel-server
	
After you install packages, insert directives to export folder on file
/etc/exports:

	# vi /etc/exports
	
Inside such file each row is referred to a specific folder share. For instance, 
we would like to share folder /media/pippo with 192.168.1.23 pc. To do such
share, you write this line on exports file:

	/media/pippo 192.168.1.23(rw,sync,no_subtree_check)
	
The line indicates the name of shared folder, the address of share receiver,
and the settings that we would like to assign.

Once you insert the directives you should restart your server:

	# /etc/init.d/nfs-kernel-server restart
