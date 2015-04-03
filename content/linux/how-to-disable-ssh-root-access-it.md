Title: How to disable ssh root access
Slug: how-to-disable-ssh-root-access
Lang: it
Date: 2015-04-01 15:00
Modified: 2015-04-01 15:00
Category: linux
Tags: ssh, howto, reti, sicurezza
Authors: Piergiorgio Faraglia
Summary: Disabilitare accesso ssh come utente root per aumentare la sicurezza dei tuoi server.

Le librerie SSH installate sulle distribuzioni linux abilitano per default l'accesso dell'utente root sui server ssh.
Sebbene questa impostazione sia di poco conto sulle intranet private o aziendali, essa assume una notevole importanza in termini di sicurezza su server pubblici.
I seguenti passi servono per disabilitare tale accesso.

Per prima cosa, apri il file di configurazione del server ssh con permessi di root

    sudo vi /etc/ssh/ssh_config

Modifica la direttiva PermitRootLogin impostandola a no

    PermitRootLogin no

Salva il file e riavvia il server

    sudo /etc/init.d/ssh restart

Da questo momento in poi non potrai più accedere il server ssh come utente root.
