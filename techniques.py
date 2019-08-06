import numpy.random as rd

class Parade():
    def __init__(self, diff, bdef, matt, bdiv, eff_dist, eff_contact, eff_mn, allow_att=True, prior=False, bcontre=False, mod_dist=0):
        self.diff = diff
        self.bdef = bdef
        self.matt = matt
        self.bdiv = bdiv
        self.eff_dist = eff_dist
        self.eff_contact = eff_contact
        self.eff_mn = eff_mn
        self.allow_att = allow_att
        self.prior = prior #seuls ceux qui ont réussi cette parade peuvet attaquer
        self.bcontre = bcontre #les 10% de la botte de contre
        self.mod_dist = mod_dist


class Technique():
    def __init__(self, diff, bdeg, bmult, cdist, ccont, cmn, allow_degats=True, desarm=False, allow_parade=True, malus_parade=1, malus_armure=1, bris_armure=False, mod_dist=0):
        self.diff = diff
        self.bdeg = bdeg
        self.bmult = bmult
        self.cdist = cdist
        self.ccont = ccont
        self.cmn = cmn
        self.allow_degats = allow_degats
        self.desarm = desarm
        self.allow_parade = allow_parade
        self.malus_parade = malus_parade
        self.malus_armure = malus_armure
        self.bris_armure = bris_armure

############## LISTE DES STYLES DISPONIBLES ###############

#Mains nues
Coup_de_Poing = Technique(0,0,1,False,False,True)
Encaissement = Parade(0,0,0,2,False,True,True)
Lutte = Technique(2,2,1,False,False,True)
Esquive = Parade(0,0,5,1,False,True,False)
Prise_Desarmante = Technique(8,0,1,False,False,True,False,True)
Defense_Totale = Parade(4,0,0,4,False,True,True,False)
Fureur = Technique(-2,5,1,False,False,True,True,False,False)
Projection = Technique(4,0,1,False,False,True,False,False,True,1,1,False,3) #Augmente la distance au round suivant, dégâts = 0, pnj font pas
Rapidite_MN = Technique(8,-2,2,False,False,True)
Recul = Parade(2,0,0,1,False,True,True,True,False,False,1) #Met la distance à 1 au round suivant
Point_Vital = Technique(10,8,1,False,False,True)

#Contact
Coup = Technique(0,0,1,False,True,False)
Parade_ = Parade(2,4,0,1,False,True,True)
Rapidite_Contact = Technique(8,-2,2,False,True,False)
Feinte = Parade(2,0,6,1,False,True,False)
Frenesie = Technique(-2,3,1,False,True,False,True,False,False)
Botte_Feinte = Parade(10,0,100,1,False,True,False)
Botte_Eclair = Technique(8,0,1,False,True,False,True,False,True,0)
Coup_Precis = Technique(5,5,1,False,True,False)
Desarmement = Technique(6,0,1,False,True,False,False,True)
Botte_Perforante = Technique(10,0,1,False,True,False,True,False,True,1,0)
Riposte = Technique(2,0,1,False,True,False) #Change de cible ==> PAS RÉGLÉ
Botte_Contre = Parade(10,0,0,1,False,True,True,True,False,True)
Botte_Riposte = Technique(10,0,1,False,True,False) #Attaque jusqu'à 3 adversaire qui l'ont visé en plus de la cible ==> PAS RÉGLÉ
Charge = Technique(3,0,1,False,True,False,True,False,True,1,1,False,-1) #Réduis la distance de 2 au lieu de 1 + porte un coup si dist = 0 + parades mn/contact adversaire impossibles ==> PAS RÉGLÉ
Intimidation = Parade(5,0,0,1,False,True,True) #Les adversaires changent de cible si possible. Pas spécifié si fonctionne à distance ==> PAS RÉGLÉ
Bris_Armure = Technique(14,0,1,False,True,False,False,False,True,1,1,True)
Deculottage = Technique(3,0,1,False,True,False)
Tour_Chauffe = Parade(5,0,0,1,False,True,True,True,True) #Seules les personnes ayant réussi tour de chauffe peuvent attaquer, uniquement au 1er round
Botte_Elegante = Technique(10,3,1,False,True,False)

#Distance
Tir = Technique(0,0,1,True,False,False)
Camouflage = Parade(0,0,4,1,True,False,False)
Tir_Instinctif = Technique(-4,-3,1,True,False,False)
Parade_Maladroite = Parade(3,3,0,1,False,True,True)
Precision = Technique(5,5,1,True,False,False)
Maintien_Distance = Parade(8,0,0,1,True,False,False,True,False,False,1000)
Rapidite_Tir = Technique(8,-2,2,True,False,False)
Harcelement = Technique(10,0,1,True,False,False) #Uniquement au 1er round. Met fin au combat après le round ==> PAS RÉGLÉ
Couverture = Parade(6,0,2,1,True,True,True) #Ajoute un malus de 2 supplémentaire à tous les adversaires sur tous les membres du groupe ==> PAS RÉGLÉ
Tete_Brulee = Technique(-2,4,1,True,False,False,True,False,False)
Degainer = Technique(0,0,1,False,False,False,True,False,False) #Permet de changer d'arme et de donner un coup normal. Annule la parade ==> PAS RÉGLÉ
Plus_Vite_Que_Son_Ombre = Parade(5,0,0,1,True,True,True,True,True) #Seules les personnes ayant réussi la même parade peuvent attaquer, uniquement au 1er round


Styles = {
"Lutteur" : ([Encaissement, Esquive, Defense_Totale], [Coup_de_Poing, Lutte, Prise_Desarmante, Fureur]),
"Arts Martiaux" : ([Esquive, Encaissement, Recul], [Coup_de_Poing, Projection, Rapidite_MN, Point_Vital]),
"Lame Rapide" : ([Parade_, Feinte, Botte_Feinte], [Coup, Rapidite_Contact, Frenesie, Botte_Eclair]),
"Lame Précise" : ([Parade_, Feinte, Botte_Feinte], [Coup, Coup_Precis, Desarmement, Botte_Perforante]),
"Lame Défensive" : ([Parade_, Feinte, Botte_Contre], [Coup, Riposte, Desarmement, Botte_Riposte]),
"Lame Violente" : ([Parade_, Feinte, Intimidation], [Coup, Charge, Frenesie, Bris_Armure]),
"Lame avec Panache" : ([Parade_, Feinte, Tour_Chauffe], [Coup, Charge, Deculottage, Botte_Elegante]),
"Tireur d'Élite" : ([Camouflage, Parade_Maladroite, Maintien_Distance], [Tir, Tir_Instinctif, Precision, Rapidite_Tir]),
"Guérilla" : ([Camouflage, Parade_Maladroite, Couverture], [Tir, Tir_Instinctif, Harcelement, Tete_Brulee]),
"Desperado" : ([Camouflage, Parade_Maladroite, Plus_Vite_Que_Son_Ombre], [Tir, Tir_Instinctif, Degainer, Rapidite_Tir]),
"Base Mains Nues" : ([], [Coup_de_Poing]),
"Base Contact" : ([], [Coup]),
"Base Distance" : ([], [Tir]),
"Test_Distance" : ([Parade_Maladroite], [Precision])
}

def styleCombat(name, niveau):
    i = niveau//2
    j = niveau%2
    try:
        style = Styles[name]
    except:
        print("Pas de style sous ce nom, #déso !!!")
        raise
    return style[0][:i+j], style[1][:1+i]
