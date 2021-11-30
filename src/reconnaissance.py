from image import Image


def lecture_modeles(chemin_dossier):
    fichiers = ['_0.png', '_1.png', '_2.png', '_3.png', '_4.png', '_5.png', '_6.png',
                '_7.png', '_8.png', '_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    #Binarisation + Localisation + Sauvegardes 
    im_2 = image.binarisation(S)
    im_2_located = im_2.localisation()
    x = 0
    index = 0
    #Parcours d'une liste d’images modèles et sauvegarde de la similitude maximale ainsi l’indice de l’image avec la similitude.
    for i in range(len(liste_modeles)):
        result = im_2_located.resize(liste_modeles[i].H,liste_modeles[i].W)
        if result.similitude(liste_modeles[i])>x: 
            x=result.similitude(liste_modeles[i])
            index=i
    return index