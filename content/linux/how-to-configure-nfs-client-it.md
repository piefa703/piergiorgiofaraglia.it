Title: Come configurare un server nfs
Slug: come-configurare-server-nfs
Lang: it
Date: 2015-04-24 18:00
Modified: 2015-04-24 18:00
Category: linux
Tags: nfs, howto, networking
Authors: Piergiorgio Faraglia
Summary: Configure nfs server and client sides.
Status: draft

nfs client
------------

Colui che vuole condividere una cartella di un server che precedentemente ha 
autorizzato tale condivisione dovrà in prima instanza creare una cartella nel
proprio file system che utilizzerà per montare la cartella remota.

Per poter utilizzare partizioni remote bisogna aver installato il pacchetto:

	# apt-get install nfs-common

Ad esempio supponiamo che la cartella si chiami remota e sarà creata 
all''interno della cartella media:

	$ mkdir /media/remota
	
Una volta creata la cartella bisogna modificare il file fstab per poter inserire 
la volontà di condividere una cartella remota.

	# vi /etc/fstab
	
Nel file inserire una riga così composta:

	192.168.1.99:/media/pippo 		  /media/remota		nfs 	rw,rsize=4096,wsize=4096,users,noauto,exec	0	0 
	
In questa riga è stato ipotizzato che il server remoto abbia un ip 192.168.1.99,
che la cartella remota da condividere sia /media/pippo e che la cartella locale 
sia /media/remota

A questo punto salvare il file e montare la cartella:

	$ mount /media/remota
	
Il gioco è fatto!

nfs client
------------

Colui che vuole condividere una cartella di un server che precedentemente ha 
autorizzato tale condivisione dovrà in prima instanza creare una cartella nel
proprio file system che utilizzerà per montare la cartella remota.

Per poter utilizzare partizioni remote bisogna aver installato il pacchetto:

	# apt-get install nfs-common

Ad esempio supponiamo che la cartella si chiami remota e sarà creata 
all''interno della cartella media:

	$ mkdir /media/remota
	
Una volta creata la cartella bisogna modificare il file fstab per poter inserire 
la volontà di condividere una cartella remota.

	# vi /etc/fstab
	
Nel file inserire una riga così composta:

	192.168.1.99:/media/pippo 		  /media/remota		nfs 	rw,rsize=4096,wsize=4096,users,noauto,exec	0	0 
	
In questa riga è stato ipotizzato che il server remoto abbia un ip 192.168.1.99,
che la cartella remota da condividere sia /media/pippo e che la cartella locale 
sia /media/remota

A questo punto salvare il file e montare la cartella:

	$ mount /media/remota
	
Il gioco è fatto!
