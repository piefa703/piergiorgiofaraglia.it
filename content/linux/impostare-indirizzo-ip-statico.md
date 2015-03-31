Title: Impostare un indirizzo ip statico
Slug: impostare-indirizzo-ip-statico
Date: 2015-03-31 15:30
Modified: 2015-03-31 15:30
Category: Linux
Tags: networking
Authors: Piergiorgio Faraglia
Summary: Passaggi per impostare un indirizzo ip statico ad un server linux.

Le distribuzioni linux attuali sono configurate per poter assegnare indirizzi
ip dinamici ai pc una volta collegati alla rete.

Risulta comodo, soprattutto nella configurazioni di sottoreti, assegnare ad una
macchina un ip statico. Nel post si supponga di voler assegnare l'indirizzo ip
statico 192.168.1.10 all'interfaccia eth0.
Per impostare l'indirizzo ip statico seguire i seguenti passi.

Aprire il file delle interfacce di rete con permessi di root

    sudo vi /etc/network/interfaces

Inserire le direttive per l'interfaccia che si vuole configurare

    auto eth0
    iface eth0 inet static
        address     192.68.1.10
        network     192.168.1.0
        netmask     255.255.255.0
        broadcast   192.168.1.255
        gateway     192.168.1.1

Riavviare l'interfaccia di rete (con permessi di root)

    sudo ifconfig eth0 down
    sudo ifconfig eth0 up
    sudo /etc/init.d/networking stop
    sudo /etc/init.d/networking start
