Title: Come configurare un server nfs
Slug: come-configurare-server-nfs
Lang: it
Date: 2015-04-24 18:00
Modified: 2015-04-24 18:00
Category: linux
Tags: nfs, howto, reti
Authors: Piergiorgio Faraglia
Summary: Come configurare un server nfs per condividere cartelle in rete.

Per poter condividere una cartella mediante NFS è necessario installare sul 
computer dal quale esportare la cartella i seguenti pacchettri:

	# apt-get install nfs-common nfs-kernel-server
	
Una volta installati i pacchetti inserire le direttive per esportare la cartella
nel file /etc/exports

	# vi /etc/exports
	
Nel file ogni riga corrisponde all'intenzione di voler condividere una cartella,
ad esempio volendo condividere la cartella /media/pippo con il pc 192.168.1.23 la 
riga da inserire nel file sarà:

	/media/pippo 192.168.1.23(rw,sync,no_subtree_check)
	
Ossia bisogna inserire il nome della cartella da condividere, l'indirizzo del 
destinatario della condivisione e le impostazione che vogliamo assegnare alla
condivisione.

Una volta inserite le direttive necessarie occorre riavviare il server affinchè 
esse siano effettivamente attive

	# /etc/init.d/nfs-kernel-server restart
	
