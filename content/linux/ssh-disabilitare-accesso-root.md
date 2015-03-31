Title: SSH, disabilitare l'accesso di root
Slug: ssh-disabilitare-accesso-root
Date: 2015-03-31 15:00
Modified: 2015-03-31 15:00
Category: Linux
Tags: ssh
Authors: Piergiorgio Faraglia
Summary: Disabilitare l'accesso con l'utente di root su un server tramite ssh.

Le librerie ssh installabili sulle distribuzioni linux per default abilitano
l'accesso tramite l'utente root. Sebbene su una intranet privata o aziendale
questa impostazione può risultare sufficiente, non è la stessa cosa in termini
di sicurezza sui server pubblici. 
Di seguito vi indico i passi da seguire per disabilitare l'accesso come utente root.

In primo luogo occorre aprire il file di configurazione di ssh:

    sudo vi /etc/ssh/ssh_config

All'interno del file modificare la direttiva PermitRootLogin:

    PermitRootLogin no

Salvare il file e riavviare il server ssh:

    sudo /etc/init.d/ssh restart

Da questo momento in poi non sarà più possibile accedere come root sul server.
