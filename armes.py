class Arme():
    def __init__(self, bonus_dgt, portee=0, malus_jet=0):
        self.bonus_dgt = bonus_dgt
        self.portee = portee
        self.malus_jet = malus_jet

############## LISTE DES ARMES DISPONIBLES ###############
        
#Contact
Baton = Arme(1)
Couteau = Arme(2)
Epee_Courte = Arme(3)
Hache = Arme(4)
Epee_Longue = Arme(5)
Hallebarde = Arme(6,0,2)
Epee_Magique = Arme(6)
Machette = Arme(2)
Rasoir = Arme(0)
        
#Distance
Fronde = Arme(1,2)
Arc = Arme(2,2)
Arc_Long = Arme(2,3)
Revolver = Arme(3,2)
Fusil = Arme(4,3)
Mitraillette = Arme(5,2,2)
Fusil_de_Chasse = Arme(4,2)
Lance_Roquettes = Arme(6,4)
Lance_Flammes = Arme(4,1)
Fouet = Arme(0,1)

Armes = {
'Bâton' : Baton,
'Couteau' : Couteau,
'Épée Courte' : Epee_Courte,
'Hache' : Hache,
'Épée Longue' : Epee_Longue,
'Hallebarde' : Hallebarde,
'Épée Magique' : Epee_Magique,
'Machette' : Machette,
'Rasoir' : Rasoir,
'Fronde' : Fronde,
'Arc' : Arc,
'Arc Long' : Arc_Long,
'Revolver' : Revolver,
'Fusil' : Fusil,
'Mitraillette' : Mitraillette,
'Fusil de Chasse' : Fusil_de_Chasse,
'Lance-Roquettes' : Lance_Roquettes,
'Lance-Flammes' : Lance_Flammes,
'Fouet' : Fouet
}

def selectArme(name):
    try:
        arme = Armes[name]
    except:
        print("Pas d'arme sous ce nom, #déso !!!")
        raise
    return arme