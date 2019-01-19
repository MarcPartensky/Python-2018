import socket

hote = "MBA13New"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

msg_recu = b""
while msg_recu != b"fin":

    """ #Envoi
    msg_a_envoyer = input("> ")
    msg_a_envoyer = msg_a_envoyer.encode()
    connexion_avec_serveur.send(msg_a_envoyer) """

    #Réception
    msg_recu = connexion_avec_serveur.recv(1024)
    msg_recu=msg_recu.decode()
    if msg_recu[0]=="/":
        print("Exécution de: "+msg_recu[1:])
        eval(msg_recu[1:])
    else:
        print(msg_recu)

print("Fermeture de la connexion")
connexion_avec_serveur.close()
