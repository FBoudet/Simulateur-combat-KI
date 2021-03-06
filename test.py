import numpy as np
from combat import RandCombat
from combattant import Combattant
from pnj import getPNJ

#Combattant(PV,caracs={FOR,PER,INT,CombatContact,CombatDistance},Chgt d'arme?,(Style contact,Style dist),(niv contact,niv dist),(arme contact,arme dist),armure,pnj?)
E = []
n_test = 10000

for i in range(n_test):
    Reiz = Combattant(30,{'PER':9,'INT':8,'CombatDistance':7},chgt_arme=False,styles='Test_Distance',niveau=2,armes='Fusil',armure=4,bonus_jet=0,bonus_dgts_perso=0,pnj=False)
    Reiz2 = Combattant(30,{'PER':9,'INT':8,'CombatDistance':7},chgt_arme=False,styles='Test_Distance',niveau=2,armes='Fusil',armure=4,bonus_jet=0,bonus_dgts_perso=0,pnj=False)    
    C2 = Combattant(65,{'FOR':7,'PER':5,'INT':4,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3},True,('Lame Défensive','Base Distance'),(5,0),('Hallebarde','Arc Long'),2)
    Daven = Combattant(pv=30,carac={'FOR':4,'INT':3,'CombatMainsNues':4},chgt_arme=False,styles='Arts Martiaux',niveau=1,armes=None,armure=4,bonus_jet=0,bonus_dgts_perso=0,pnj=False)
    GrosBill = Combattant(pv=50,carac={'FOR':12,'INT':10,'CombatContact':8},chgt_arme=False,styles='Lame Rapide',niveau=6,armes='Épée Magique',armure=5,bonus_jet=1,bonus_dgts_perso=0,pnj=False)
    C4 = getPNJ('Élémental de Terre')
    C5 = getPNJ('Élémental de Feu')
    C6 = getPNJ('Poing de la Grande Déesse')

    Result, Log = RandCombat([Reiz],[C4],3)
    E.append(Result)
    # if Result == 'Groupe1':
    #     print(Log)


result = np.array(E)
g1=np.sum(result=='Groupe1')
g2=np.sum(result=='Groupe2')
dr=np.sum(result=='draw')


print("Victoire du combattant 1 : {}/{}".format(g1,n_test))
print("Victoire du combattant 2 : {}/{}".format(g2,n_test))
print("Match nul, très très nul: {}/{}".format(dr,n_test))
