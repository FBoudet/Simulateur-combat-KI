from combattant import Combattant

# Malabar = Combattant(40,{'FOR':4,'PER':3,'INT':2,'CombatMainsNues':4,'CombatContact':2,'CombatDistance':2},True,('Lutteur','Base Distance'),(3,0),('Arc'),1)
# Ecuyer = Combattant(40,{'FOR':4,'PER':2,'INT':2,'CombatMainsNues':2,'CombatContact':4,'CombatDistance':2},True,('Lame Rapide','Base Distance'),(2,0),('Épée Courte','Arc'),2,1)
# Homme_de_main = Combattant(35,{'FOR':3,'PER':4,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':4},True,('Base Contact',"Tireur d'Élite"),(0,2),('Couteau','Arc'),1)
# Coiffeur = Combattant(25,{'FOR':2,'PER':3,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},False,'Lame Défensive',1,('Couteau'),0)
# Apprenti = Combattant(25,{'FOR':2,'PER':2,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},True,('Base Contact','Base Distance'),(0,0),('Bâton','Fronde'),0)
# Majordome = Combattant(25,{'FOR':2,'PER':4,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},False,'Lutteur',1,None,0)
# Geek = Combattant(25,{'FOR':2,'PER':3,'INT':4,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},False,"Tireur d'Élite",1,('Fronde'),0)
# Confesseur = Combattant(25,{'FOR':2,'PER':3,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},False,'Arts Martiaux',1,None,0)
# Infirmier = Combattant(30,{'FOR':3,'PER':2,'INT':4,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},False,'Lutteur',1,None,0)
# Garde_du_Corps = Combattant(45,{'FOR':5,'PER':3,'INT':3,'CombatMainsNues':5,'CombatContact':3,'CombatDistance':3},True,('Lame Défensive','Base Distance'),(3,0),('Hache','Revolver'),2)
# Maitre_d_Armes = Combattant(50,{'FOR':5,'PER':3,'INT':3,'CombatMainsNues':2,'CombatContact':5,'CombatDistance':5},True,('Lame Précise','Base Distance'),(4,0),('Épée Longue','Arc Long'),3,1)
# Partisan = Combattant(30,{'FOR':3,'PER':3,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},True,('Lutteur','Base Distance'),(1,0),('Arc'),1)
# Secretaire = Combattant(30,{'FOR':3,'PER':3,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},False,'Base Mains Nues',0,None,0)
# Terroriste = Combattant(35,{'FOR':3,'PER':5,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},True,('Lame Rapide','Base Distance'),(1,0),('Couteau','Revolver'),1)
# Complice = Combattant(30,{'FOR':3,'PER':5,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},True,('Lutteur','Base Distance'),(1,0),('Arc'),1)
# Medium = Combattant(30,{'FOR':3,'PER':3,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},False,'Base Mains Nues',0,None,0)
# Erudit = Combattant(30,{'FOR':3,'PER':3,'INT':5,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},False,'Base Mains Nues',0,None,0)
# Styliste = Combattant(30,{'FOR':3,'PER':3,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},False,'Base Mains Nues',0,None,0)
# Cuistot = Combattant(25,{'FOR':2,'PER':2,'INT':2,'CombatMainsNues':1,'CombatContact':1,'CombatDistance':1},False,'Lame Précise',1,('Couteau'),0)
# Clown = Combattant(25,{'FOR':2,'PER':2,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},False,'Base Mains Nues',0,None,0)
# Garde_Malade = Combattant(25,{'FOR':2,'PER':2,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},False,'Base Mains Nues',0,None,0)
# Valet = Combattant(25,{'FOR':2,'PER':2,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},False,'Base Contact',0,('Bâton'),0)
# Esclave = Combattant(25,{'FOR':2,'PER':2,'INT':2,'CombatMainsNues':1,'CombatContact':1,'CombatDistance':1},False,'Lutteur',1,None,0)
# Robot_de_Compagnie = Combattant(25,{'FOR':2,'PER':2,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},False,'Base Mains Nues',0,None,0)
# Robot_Menager = Combattant(25,{'FOR':2,'PER':2,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2},False,'Base Mains Nues',0,None,0)
# Milicien = Combattant(45,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},True,('Lame Précise','Base Distance'),(3,0),('Épée Courte','Arc'),2,1)
# Franc_Tireur = Combattant(45,{'FOR':5,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,3),('Épée Courte','Revolver'),2)
# Emeutier = Combattant(45,{'FOR':5,'PER':5,'INT':3,'CombatMainsNues':4,'CombatContact':5,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(3,0),('Épée Courte','Arc'),2,1)
# Sectateur = Combattant(45,{'FOR':5,'PER':5,'INT':3,'CombatMainsNues':4,'CombatContact':5,'CombatDistance':3},True,('Lame Défensive','Base Distance'),(3,0),('Épée Courte','Arc'),2,1)
# Paramilitaire = Combattant(45,{'FOR':5,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(3,0),('Épée Courte','Arc'),2)
# Policier = Combattant(40,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(3,0),('Couteau','Arc'),2,1)
# Policier_d_Elite = Combattant(50,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(4,0),('Hache','Revolver'),3,1)
# Soldat = Combattant(45,{'FOR':5,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3},True,('Lame Précise','Base Distance'),(3,0),('Épée Courte','Arc'),2,1)
# Soldat_d_Elite = Combattant(50,{'FOR':5,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3},True,('Lame Précise','Base Distance'),(3,0),('Épée Longue','Revolver'),3,1)
# Tank = Combattant(60,{'FOR':5,'PER':4,'INT':3,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,5),('Hache','Lance-Roquettes'),4,1)
# Clone = Combattant(45,{'FOR':5,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(3,0),('Épée Courte','Arc'),2,1)
# Guerrière_Slavone = Combattant(50,{'FOR':5,'PER':6,'INT':5,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(3,0),('Hache','Revolver'),2,1)
# Patrouilleur = Combattant(50,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,2),('Épée Courte','Revolver'),2,1)
# Fregate = Combattant(60,{'FOR':5,'PER':5,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,4),('Hache','Fusil'),3,1)
# Destroyer = Combattant(70,{'FOR':6,'PER':6,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,4),('Hache','Lance-Roquettes'),5,1)
# Croiseur = Combattant(80,{'FOR':7,'PER':7,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,6),('Épée Longue','Lance-Roquettes'),5,1)
# Porte_Avions = Combattant(70,{'FOR':6,'PER':8,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,4),('Hache','Lance-Roquettes'),5,1)
# Bombardier = Combattant(50,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,4),('Épée Courte','Lance-Roquettes'),3,1)
# Coleoptère = Combattant(50,{'FOR':3,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,4),('Épée Courte','Revolver'),3,1)
# Galère_Imperiale = Combattant(50,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,2),('Hallebarde','Arc Long'),3,1)
# Limousine_Plaquee_Or = Combattant(50,{'FOR':3,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,3),('Épée Courte','Revolver'),3,1)
# Papamobile = Combattant(50,{'FOR':3,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,3),('Épée Courte','Revolver'),3,1)
# Petit_Poney = Combattant(40,{'FOR':2,'PER':5,'INT':4,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(3,0),('Couteau','Arc Long'),2,1)
# Palanquin_sur_Sbleune = Combattant(50,{'FOR':5,'PER':5,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3},True,('Lame Défensive','Base Distance'),(4,0),('Hache','Arc Long'),3)
# Avion_Presidentiel = Combattant(50,{'FOR':3,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,4),('Épée Courte','Revolver'),3,1)
# Carrosse = Combattant(50,{'FOR':3,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,3),('Épée Longue','Arc Long'),3,1)
# Limousine = Combattant(50,{'FOR':3,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,3),('Épée Courte','Revolver'),3,1)
# Brigand = Combattant(30,{'FOR':3,'PER':3,'INT':2,'CombatMainsNues':1,'CombatContact':1,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(2,0),('Épée Courte','Arc'),1)
# Assassin = Combattant(40,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':3,'CombatDistance':4},True,('Lame Rapide','Base Distance'),(3,0),('Épée Longue','Arc Long'),2)
# Soldat_Deserteur = Combattant(55,{'FOR':5,'PER':5,'INT':3,'CombatMainsNues':4,'CombatContact':5,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(4,0),('Hache','Revolver'),2,1)
# Chef_Rebelle = Combattant(65,{'FOR':6,'PER':5,'INT':4,'CombatMainsNues':5,'CombatContact':6,'CombatDistance':4},True,('Lame Rapide','Base Distance'),(5,0),('Épée Longue','Fusil'),4,1)
# Mille_Pattes_Accro = Combattant(20,{'FOR':2,'PER':3,'INT':3,'CombatMainsNues':2,'CombatContact':1,'CombatDistance':1},True,('Base Distance','Base Distance'),(0,0),('Fronde'),1)
# Champignonz = Combattant(30,{'FOR':4,'PER':3,'INT':3,'CombatMainsNues':2,'CombatContact':1,'CombatDistance':1},True,('Base Distance','Base Distance'),(0,0),('Fronde'),2)
# Champignonz_Mutant = Combattant(45,{'FOR':6,'PER':6,'INT':3,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},True,('Base Distance','Base Distance'),(0,0),('Fronde'),2)
# Le_Rêveur = Combattant(60,{'FOR':5,'PER':7,'INT':5,'CombatMainsNues':3,'CombatContact':3,'CombatDistance':2},True,('Lame Rapide','Base Distance'),(4,0),('Épée Longue','Revolver'),4)
# Chapardeur = Combattant(30,{'FOR':3,'PER':3,'INT':2,'CombatMainsNues':1,'CombatContact':1,'CombatDistance':1},True,('Lame Précise','Base Distance'),(1,0),('Couteau','Arc'),1)
# Bishônen_Assassin = Combattant(50,{'FOR':5,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':3,'CombatDistance':5},True,('Lame Précise','Base Distance'),(4,0),('Épée Longue','Revolver'),2)
# Bishônen_Magicien = Combattant(55,{'FOR':6,'PER':4,'INT':4,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},True,('Lame Précise','Base Distance'),(3,0),('Épée Courte','Arc'),2)
# Prince_Bishônen = Combattant(70,{'FOR':6,'PER':5,'INT':4,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':4},True,('Lame Précise','Base Distance'),(6,0),('Épée Magique','Fusil'),4)
# Aigle_Geant = Combattant(30,{'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Lutteur',2,None,0)
# Ange_Vengeur = Combattant(35,{'FOR':4,'PER':5,'INT':3,'CombatMainsNues':2,'CombatContact':3,'CombatDistance':2},True,('Lame Rapide','Base Distance'),(1,0),('Épée Courte','Arc'),1)
# Archange_Vengeur = Combattant(50,{'FOR':5,'PER':6,'INT':4,'CombatMainsNues':3,'CombatContact':3,'CombatDistance':2},True,('Lame Rapide','Base Distance'),(2,0),('Épée Longue','Arc Long'),2)
# Poing_de_la_Grande_Deesse = Combattant(90,{'FOR':10,'PER':9,'INT':5,'CombatMainsNues':8,'CombatContact':8,'CombatDistance':8},True,('Lame Rapide','Base Distance'),(6,0),('Épée Magique','Mitraillette'),4)
# Demon_Mineur = Combattant(35,{'FOR':4,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Lame Précise','Base Distance'),(2,0),('Bâton','Fronde'),1)
# Demon_Majeur = Combattant(55,{'FOR':6,'PER':5,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},True,('Lame Précise','Base Distance'),(3,0),('Épée Courte','Arc'),2)
# Rejeton_de_Naar = Combattant(65,{'FOR':7,'PER':6,'INT':4,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3},True,('Lame Précise','Base Distance'),(4,0),('Épée Longue','Revolver'),3)
# Œil_de_Naar = Combattant(90,{'FOR':10,'PER':9,'INT':5,'CombatMainsNues':8,'CombatContact':8,'CombatDistance':8},True,('Lame Précise','Base Distance'),(6,0),('Épée Magique','Mitraillette'),4)
# Chien_du_Desert = Combattant(30,{'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Lutteur',2,None,0)
# Araignee_du_Desert = Combattant(40,{'FOR':4,'PER':4,'INT':4,'CombatMainsNues':3,'CombatContact':3,'CombatDistance':4},False,'Lutteur',3,None,1)
# Chameau_Leclerc = Combattant(55,{'FOR':6,'PER':5,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},False,'Lutteur',4,None,2)
# Liane_Tueuse = Combattant(30,{'FOR':3,'PER':3,'INT':3,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Arts Martiaux',2,None,0)
# Loup = Combattant(35,{'FOR':3,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},False,'Lutteur',3,None,0)
# Gorille_Geant = Combattant(50,{'FOR':5,'PER':4,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},False,'Lutteur',4,None,1)
# Monstre_des_Forêts = Combattant(60,{'FOR':6,'PER':5,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},False,'Lutteur',5,None,2)
# Kanard_Hostile = Combattant(30,{'FOR':2,'PER':3,'INT':3,'CombatMainsNues':3,'CombatContact':1,'CombatDistance':2},False,'Arts Martiaux',2,None,0)
# Kanard_Pittopatte = Combattant(45,{'FOR':4,'PER':4,'INT':4,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},False,'Arts Martiaux',4,None,1)
# Homard_Geant = Combattant(30,{'FOR':3,'PER':3,'INT':3,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Lutteur',2,None,2)
# Tortue_Blindee = Combattant(40,{'FOR':4,'PER':3,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},False,'Lutteur',3,None,4)
# Requin_Volant = Combattant(55,{'FOR':6,'PER':6,'INT':3,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},False,'Lutteur',4,None,2)
# Ping_Pong = Combattant(25,{'FOR':2,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Arts Martiaux',1,None,0)
# Troll = Combattant(45,{'FOR':5,'PER':5,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},False,'Lame Rapide',3,('Épée Courte'),1)
# Guerrier_Hologramme = Combattant(55,{'FOR':5,'PER':6,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},True,('Lame Précise','Base Distance'),(4,0),('Hache','Arc'),0)
# Cube_de_Logique_Brute = Combattant(30,{'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Lutteur',1,None,0)
# Pieuvre_de_Logique_Brute = Combattant(40,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},False,'Lutteur',2,None,1)
# Logipieuvre = Combattant(55,{'FOR':5,'PER':4,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},True,('Lame Précise','Base Distance'),(3,0),('Épée Courte','Fronde'),2)
# Grand_Calculateur = Combattant(65,{'FOR':5,'PER':5,'INT':6,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3},True,('Lame Précise','Base Distance'),(5,0),('Épée Longue','Arc'),3)
# Invocateur_de_Magmor = Combattant(30,{'FOR':2,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,2),('Bâton','Arc'),0)
# Rejeton_de_Magmor = Combattant(50,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},True,('Lame Défensive','Base Distance'),(4,0),('Hache','Fronde'),1)
# Magmor_le_Polymorphe = Combattant(80,{'FOR':9,'PER':8,'INT':3,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3},True,('Lame Défensive','Base Distance'),(6,0),('Épée Magique','Fusil'),4)
# Poisson_Bouffe_Tout = Combattant(25,{'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Base Mains Nues',0,None,0)
# Requin = Combattant(40,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},False,'Lutteur',2,None,1)
# Pieuvre_des_Profondeurs = Combattant(50,{'FOR':5,'PER':6,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},False,'Lutteur',3,None,1)
# Pirate = Combattant(30,{'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(2,0),('Épée Courte','Arc'),2)
# Capitaine_Pirate = Combattant(45,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(4,0),('Épée Longue','Revolver'),3)
# Barbe_Mauve = Combattant(60,{'FOR':6,'PER':5,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(6,0),('Épée Magique','Fusil'),4)
# Rapace_Temeraire = Combattant(30,{'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Lutteur',2,None,0)
# Bâtard_du_Geant_des_Montagnes = Combattant(40,{'FOR':4,'PER':3,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},True,('Lame Défensive','Base Distance'),(3,0),('Hache','Arc'),1)
# Geant_des_Montagnes = Combattant(65,{'FOR':7,'PER':5,'INT':4,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3},True,('Lame Défensive','Base Distance'),(5,0),('Hallebarde','Arc Long'),2)
# Dragonneau = Combattant(35,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Arts Martiaux',1,None,0)
# Dragon = Combattant(55,{'FOR':6,'PER':5,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(3,0),('Épée Courte','Arc'),1)
# Ancalagon_le_Noir = Combattant(75,{'FOR':7,'PER':6,'INT':5,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(6,0),('Épée Longue','Arc'),2)
# Squelette = Combattant(30,{'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Lame Défensive',1,('Bâton'),0)
# Zombie = Combattant(40,{'FOR':4,'PER':4,'INT':2,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},False,'Lame Défensive',2,('Couteau'),0)
# Momie = Combattant(50,{'FOR':5,'PER':5,'INT':2,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},False,'Lame Défensive',3,('Épée Courte'),1)
# Liche = Combattant(65,{'FOR':6,'PER':6,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},True,('Lame Défensive','Base Distance'),(5,0),('Épée Longue','Arc'),2)
# Dragon_Chenille = Combattant(20,{'FOR':2,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Base Mains Nues',0,None,0)
# Hyène_Mutante = Combattant(40,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},False,'Lutteur',2,None,1)
# Super_Guerrier = Combattant(55,{'FOR':6,'PER':5,'INT':3,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},True,('Lame Précise','Base Distance'),(4,0),('Épée Longue','Revolver'),2)
# Ectoplasme = Combattant(25,{'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Base Distance','Base Distance'),(0,0),('Fronde'),0)
# Guerrier_Fantôme = Combattant(45,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(3,0),('Couteau','Arc'),1)
# Mysti = Combattant(65,{'FOR':5,'PER':3,'INT':4,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(5,0),('Épée Longue','Revolver'),3)
# Mouton = Combattant(20,{'FOR':2,'PER':2,'INT':1,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Base Mains Nues',0,None,0)
# Vache = Combattant(25,{'FOR':3,'PER':2,'INT':1,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Base Mains Nues',0,None,0)
# Paysanne_Effarouchee = Combattant(25,{'FOR':2,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Lame Précise',1,('Bâton'),0)
# Voleur_de_Betail = Combattant(40,{'FOR':4,'PER':4,'INT':2,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},True,('Lame Précise','Base Distance'),(3,0),('Couteau','Fronde'),0)
# Druidesse = Combattant(55,{'FOR':5,'PER':5,'INT':4,'CombatMainsNues':2,'CombatContact':1,'CombatDistance':1},True,('Lame Précise','Base Distance'),(3,0),('Bâton','Fronde'),0)
# Cheval = Combattant(20,{'FOR':2,'PER':2,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Base Mains Nues',0,None,0)
# Pingouin_à_Roulettes = Combattant(25,{'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Base Mains Nues',0,None,0)
# Piquosaure = Combattant(40,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},False,'Lutteur',2,None,3)
# Ver_de_Glace = Combattant(45,{'FOR':5,'PER':5,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},False,'Lutteur',3,None,1)
# Nounours_Polaire = Combattant(55,{'FOR':6,'PER':5,'INT':3,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},False,'Lutteur',4,None,2)
# Père_Noël = Combattant(35,{'FOR':2,'PER':4,'INT':3,'CombatMainsNues':1,'CombatContact':1,'CombatDistance':2},True,('Lame Précise','Base Distance'),(3,0),('Couteau','Arc'),0)
# Sbleune_Rouge = Combattant(30,{'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Lame Défensive',2,('Couteau'),2)
# Sbleune_Vert = Combattant(40,{'FOR':4,'PER':4,'INT':2,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},False,'Lame Défensive',3,('Épée Courte'),2)
# Sbleune_Jaune = Combattant(50,{'FOR':5,'PER':5,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},False,'Lame Défensive',4,('Hache'),3)
# Araignee_Eboueuse = Combattant(30,{'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Lutteur',1,None,0)
# Fourmi_Geante = Combattant(40,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},False,'Lutteur',2,None,1)
# Salamandre_de_la_Mort = Combattant(55,{'FOR':6,'PER':6,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},False,'Lutteur',4,None,1)
# Teteux_Parasite = Combattant(30,{'FOR':3,'PER':3,'INT':3,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Lame Précise','Base Distance'),(1,0),('Couteau','Fronde'),0)
# Teteux_Noir = Combattant(40,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},True,('Lame Précise','Base Distance'),(3,0),('Épée Courte','Arc'),1)
# Helène_Nipournicontre = Combattant(60,{'FOR':6,'PER':6,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},True,('Lame Précise','Base Distance'),(5,0),('Épée Longue','Revolver'),2)
# Cape_Vampire = Combattant(30,{'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},False,'Lutteur',1,None,0)
# Vampire_Mineur = Combattant(40,{'FOR':4,'PER':3,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3},True,('Lame Précise','Base Distance'),(2,0),('Épée Courte','Arc'),0)
# Vampire_Majeur = Combattant(55,{'FOR':6,'PER':4,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},True,('Lame Précise','Base Distance'),(4,0),('Hache','Revolver'),1)
# Primitif_Elmerien = Combattant(30,{'FOR':3,'PER':3,'INT':1,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Lame Défensive','Base Distance'),(2,0),('Épée Courte','Arc'),0)
# Primitif_Elmerien_Guerrier = Combattant(50,{'FOR':5,'PER':5,'INT':1,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},True,('Lame Défensive','Base Distance'),(4,0),('Hache','Revolver'),2)
# Primitif_Elmerien_Mage = Combattant(50,{'FOR':5,'PER':6,'INT':2,'CombatMainsNues':2,'CombatContact':1,'CombatDistance':1},True,('Lame Défensive','Base Distance'),(3,0),('Hache','Revolver'),1)
# Elemental_d_Eau = Combattant(50,{'FOR':5,'PER':4,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(2,0),('Épée Courte','Arc'),1)
# Elemental_d_Air = Combattant(50,{'FOR':5,'PER':5,'INT':2,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(3,0),('Épée Courte','Arc'),2)
# Elemental_de_Terre = Combattant(55,{'FOR':6,'PER':4,'INT':3,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(4,0),('Hache','Revolver'),2)
# Elemental_de_Feu = Combattant(55,{'FOR':5,'PER':5,'INT':4,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(4,0),('Épée Longue','Revolver'),2)
# Bourgeois_Decadent = Combattant(40,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,2),('Épée Courte','Arc'),1)
# Esclave_Rebelle = Combattant(40,{'FOR':4,'PER':4,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Lame Précise','Base Distance'),(3,0),('Épée Courte','Arc'),1)
# Greviste_Casseur = Combattant(40,{'FOR':4,'PER':4,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Lame Défensive','Base Distance'),(2,0),('Épée Courte','Arc'),1)
# Commando_Frigide = Combattant(40,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(2,0),('Épée Courte','Arc'),1)
# Militant_Carnivore = Combattant(40,{'FOR':4,'PER':4,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Lame Précise','Base Distance'),(2,0),('Épée Courte','Arc'),1)
# Grammairien_Vindicatif = Combattant(40,{'FOR':4,'PER':4,'INT':4,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Lame Défensive','Base Distance'),(2,0),('Épée Courte','Arc'),1)
# Poudre_en_Colère = Combattant(40,{'FOR':4,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Lame Précise','Base Distance'),(2,0),('Épée Courte','Arc'),1)
# Paysan_en_Revolte = Combattant(40,{'FOR':4,'PER':4,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Lame Défensive','Base Distance'),(2,0),('Épée Courte','Arc'),1)
# Loubard_Tatoue = Combattant(45,{'FOR':6,'PER':5,'INT':4,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3},True,('Lame Rapide','Base Distance'),(2,0),('Épée Courte','Arc'),1)
# Extraterrestre = Combattant(55,{'FOR':7,'PER':6,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,3),('Épée Courte','Arc'),2)
# Grand_Extraterrestre = Combattant(55,{'FOR':4,'PER':4,'INT':4,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3},True,('Base Contact',"Tireur d'Élite"),(0,5),('Hache','Revolver'),3)

Malabar = {'pv': 40 ,'carac': {'FOR':4,'PER':3,'INT':2,'CombatMainsNues':4,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'True', 'styles': ('Lutteur','Base Distance'), 'niveau': (3,0), 'armes': ('Arc'), 'armure': 1}
Ecuyer = {'pv': 40 ,'carac': {'FOR':4,'PER':2,'INT':2,'CombatMainsNues':2,'CombatContact':4,'CombatDistance':2}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (2,0), 'armes': ('Épée Courte','Arc'), 'armure': 2, 'bonus_jet': 1}
Homme_de_main = {'pv': 35 ,'carac': {'FOR':3,'PER':4,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':4}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,2), 'armes': ('Couteau','Arc'), 'armure': 1}
Coiffeur = {'pv': 25 ,'carac': {'FOR':2,'PER':3,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Lame Défensive', 'niveau': '1', 'armes': ('Couteau'), 'armure': 0}
Apprenti = {'pv': 25 ,'carac': {'FOR':2,'PER':2,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'True', 'styles': ('Base Contact','Base Distance'), 'niveau': (0,0), 'armes': ('Bâton','Fronde'), 'armure': 0}
Majordome = {'pv': 25 ,'carac': {'FOR':2,'PER':4,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '1', 'armes': 'None', 'armure': 0}
Geek = {'pv': 25 ,'carac': {'FOR':2,'PER':3,'INT':4,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Tireur d\'Élite', 'niveau': '1', 'armes': ('Fronde'), 'armure': 0}
Confesseur = {'pv': 25 ,'carac': {'FOR':2,'PER':3,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Arts Martiaux', 'niveau': '1', 'armes': 'None', 'armure': 0}
Infirmier = {'pv': 30 ,'carac': {'FOR':3,'PER':2,'INT':4,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '1', 'armes': 'None', 'armure': 0}
Garde_du_Corps = {'pv': 45 ,'carac': {'FOR':5,'PER':3,'INT':3,'CombatMainsNues':5,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Défensive','Base Distance'), 'niveau': (3,0), 'armes': ('Hache','Revolver'), 'armure': 2}
Maitre_d_Armes = {'pv': 50 ,'carac': {'FOR':5,'PER':3,'INT':3,'CombatMainsNues':2,'CombatContact':5,'CombatDistance':5}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (4,0), 'armes': ('Épée Longue','Arc Long'), 'armure': 3, 'bonus_jet': 1}
Partisan = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'True', 'styles': ('Lutteur','Base Distance'), 'niveau': (1,0), 'armes': ('Arc'), 'armure': 1}
Secretaire = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Base Mains Nues', 'niveau': '0', 'armes': 'None', 'armure': 0}
Terroriste = {'pv': 35 ,'carac': {'FOR':3,'PER':5,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (1,0), 'armes': ('Couteau','Revolver'), 'armure': 1}
Complice = {'pv': 30 ,'carac': {'FOR':3,'PER':5,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'True', 'styles': ('Lutteur','Base Distance'), 'niveau': (1,0), 'armes': ('Arc'), 'armure': 1}
Medium = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Base Mains Nues', 'niveau': '0', 'armes': 'None', 'armure': 0}
Erudit = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':5,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Base Mains Nues', 'niveau': '0', 'armes': 'None', 'armure': 0}
Styliste = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':3,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Base Mains Nues', 'niveau': '0', 'armes': 'None', 'armure': 0}
Cuistot = {'pv': 25 ,'carac': {'FOR':2,'PER':2,'INT':2,'CombatMainsNues':1,'CombatContact':1,'CombatDistance':1}, 'chgt_arme': 'False', 'styles': 'Lame Précise', 'niveau': '1', 'armes': ('Couteau'), 'armure': 0}
Clown = {'pv': 25 ,'carac': {'FOR':2,'PER':2,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Base Mains Nues', 'niveau': '0', 'armes': 'None', 'armure': 0}
Garde_Malade = {'pv': 25 ,'carac': {'FOR':2,'PER':2,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Base Mains Nues', 'niveau': '0', 'armes': 'None', 'armure': 0}
Valet = {'pv': 25 ,'carac': {'FOR':2,'PER':2,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Base Contact', 'niveau': '0', 'armes': ('Bâton'), 'armure': 0}
Esclave = {'pv': 25 ,'carac': {'FOR':2,'PER':2,'INT':2,'CombatMainsNues':1,'CombatContact':1,'CombatDistance':1}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '1', 'armes': 'None', 'armure': 0}
Robot_de_Compagnie = {'pv': 25 ,'carac': {'FOR':2,'PER':2,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Base Mains Nues', 'niveau': '0', 'armes': 'None', 'armure': 0}
Robot_Menager = {'pv': 25 ,'carac': {'FOR':2,'PER':2,'INT':2,'CombatMainsNues':2,'CombatContact':2,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Base Mains Nues', 'niveau': '0', 'armes': 'None', 'armure': 0}
Milicien = {'pv': 45 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Courte','Arc'), 'armure': 2, 'bonus_jet': 1}
Franc_Tireur = {'pv': 45 ,'carac': {'FOR':5,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,3), 'armes': ('Épée Courte','Revolver'), 'armure': 2}
Emeutier = {'pv': 45 ,'carac': {'FOR':5,'PER':5,'INT':3,'CombatMainsNues':4,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Courte','Arc'), 'armure': 2, 'bonus_jet': 1}
Sectateur = {'pv': 45 ,'carac': {'FOR':5,'PER':5,'INT':3,'CombatMainsNues':4,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Défensive','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Courte','Arc'), 'armure': 2, 'bonus_jet': 1}
Paramilitaire = {'pv': 45 ,'carac': {'FOR':5,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Courte','Arc'), 'armure': 2}
Policier = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (3,0), 'armes': ('Couteau','Arc'), 'armure': 2, 'bonus_jet': 1}
Policier_d_Elite = {'pv': 50 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (4,0), 'armes': ('Hache','Revolver'), 'armure': 3, 'bonus_jet': 1}
Soldat = {'pv': 45 ,'carac': {'FOR':5,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Courte','Arc'), 'armure': 2, 'bonus_jet': 1}
Soldat_d_Elite = {'pv': 50 ,'carac': {'FOR':5,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Longue','Revolver'), 'armure': 3, 'bonus_jet': 1}
Tank = {'pv': 60 ,'carac': {'FOR':5,'PER':4,'INT':3,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,5), 'armes': ('Hache','Lance-Roquettes'), 'armure': 4, 'bonus_jet': 1}
Clone = {'pv': 45 ,'carac': {'FOR':5,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Courte','Arc'), 'armure': 2, 'bonus_jet': 1}
Guerrière_Slavone = {'pv': 50 ,'carac': {'FOR':5,'PER':6,'INT':5,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (3,0), 'armes': ('Hache','Revolver'), 'armure': 2, 'bonus_jet': 1}
Patrouilleur = {'pv': 50 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,2), 'armes': ('Épée Courte','Revolver'), 'armure': 2, 'bonus_jet': 1}
Fregate = {'pv': 60 ,'carac': {'FOR':5,'PER':5,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,4), 'armes': ('Hache','Fusil'), 'armure': 3, 'bonus_jet': 1}
Destroyer = {'pv': 70 ,'carac': {'FOR':6,'PER':6,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,4), 'armes': ('Hache','Lance-Roquettes'), 'armure': 5, 'bonus_jet': 1}
Croiseur = {'pv': 80 ,'carac': {'FOR':7,'PER':7,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,6), 'armes': ('Épée Longue','Lance-Roquettes'), 'armure': 5, 'bonus_jet': 1}
Porte_Avions = {'pv': 70 ,'carac': {'FOR':6,'PER':8,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,4), 'armes': ('Hache','Lance-Roquettes'), 'armure': 5, 'bonus_jet': 1}
Bombardier = {'pv': 50 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,4), 'armes': ('Épée Courte','Lance-Roquettes'), 'armure': 3, 'bonus_jet': 1}
Coleoptère = {'pv': 50 ,'carac': {'FOR':3,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,4), 'armes': ('Épée Courte','Revolver'), 'armure': 3, 'bonus_jet': 1}
Galère_Imperiale = {'pv': 50 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,2), 'armes': ('Hallebarde','Arc Long'), 'armure': 3, 'bonus_jet': 1}
Limousine_Plaquee_Or = {'pv': 50 ,'carac': {'FOR':3,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,3), 'armes': ('Épée Courte','Revolver'), 'armure': 3, 'bonus_jet': 1}
Papamobile = {'pv': 50 ,'carac': {'FOR':3,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,3), 'armes': ('Épée Courte','Revolver'), 'armure': 3, 'bonus_jet': 1}
Petit_Poney = {'pv': 40 ,'carac': {'FOR':2,'PER':5,'INT':4,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (3,0), 'armes': ('Couteau','Arc Long'), 'armure': 2, 'bonus_jet': 1}
Palanquin_sur_Sbleune = {'pv': 50 ,'carac': {'FOR':5,'PER':5,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Défensive','Base Distance'), 'niveau': (4,0), 'armes': ('Hache','Arc Long'), 'armure': 3}
Avion_Presidentiel = {'pv': 50 ,'carac': {'FOR':3,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,4), 'armes': ('Épée Courte','Revolver'), 'armure': 3, 'bonus_jet': 1}
Carrosse = {'pv': 50 ,'carac': {'FOR':3,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,3), 'armes': ('Épée Longue','Arc Long'), 'armure': 3, 'bonus_jet': 1}
Limousine = {'pv': 50 ,'carac': {'FOR':3,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,3), 'armes': ('Épée Courte','Revolver'), 'armure': 3, 'bonus_jet': 1}
Brigand = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':2,'CombatMainsNues':1,'CombatContact':1,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (2,0), 'armes': ('Épée Courte','Arc'), 'armure': 1}
Assassin = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':3,'CombatDistance':4}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Longue','Arc Long'), 'armure': 2}
Soldat_Deserteur = {'pv': 55 ,'carac': {'FOR':5,'PER':5,'INT':3,'CombatMainsNues':4,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (4,0), 'armes': ('Hache','Revolver'), 'armure': 2, 'bonus_jet': 1}
Chef_Rebelle = {'pv': 65 ,'carac': {'FOR':6,'PER':5,'INT':4,'CombatMainsNues':5,'CombatContact':6,'CombatDistance':4}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (5,0), 'armes': ('Épée Longue','Fusil'), 'armure': 4, 'bonus_jet': 1}
Mille_Pattes_Accro = {'pv': 20 ,'carac': {'FOR':2,'PER':3,'INT':3,'CombatMainsNues':2,'CombatContact':1,'CombatDistance':1}, 'chgt_arme': 'True', 'styles': ('Base Distance','Base Distance'), 'niveau': (0,0), 'armes': ('Fronde'), 'armure': 1}
Champignonz = {'pv': 30 ,'carac': {'FOR':4,'PER':3,'INT':3,'CombatMainsNues':2,'CombatContact':1,'CombatDistance':1}, 'chgt_arme': 'True', 'styles': ('Base Distance','Base Distance'), 'niveau': (0,0), 'armes': ('Fronde'), 'armure': 2}
Champignonz_Mutant = {'pv': 45 ,'carac': {'FOR':6,'PER':6,'INT':3,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Distance','Base Distance'), 'niveau': (0,0), 'armes': ('Fronde'), 'armure': 2}
Le_Rêveur = {'pv': 60 ,'carac': {'FOR':5,'PER':7,'INT':5,'CombatMainsNues':3,'CombatContact':3,'CombatDistance':2}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (4,0), 'armes': ('Épée Longue','Revolver'), 'armure': 4}
Chapardeur = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':2,'CombatMainsNues':1,'CombatContact':1,'CombatDistance':1}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (1,0), 'armes': ('Couteau','Arc'), 'armure': 1}
Bishônen_Assassin = {'pv': 50 ,'carac': {'FOR':5,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':3,'CombatDistance':5}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (4,0), 'armes': ('Épée Longue','Revolver'), 'armure': 2}
Bishônen_Magicien = {'pv': 55 ,'carac': {'FOR':6,'PER':4,'INT':4,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Courte','Arc'), 'armure': 2}
Prince_Bishônen = {'pv': 70 ,'carac': {'FOR':6,'PER':5,'INT':4,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':4}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (6,0), 'armes': ('Épée Magique','Fusil'), 'armure': 4}
Aigle_Geant = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '2', 'armes': 'None', 'armure': 0}
Ange_Vengeur = {'pv': 35 ,'carac': {'FOR':4,'PER':5,'INT':3,'CombatMainsNues':2,'CombatContact':3,'CombatDistance':2}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (1,0), 'armes': ('Épée Courte','Arc'), 'armure': 1}
Archange_Vengeur = {'pv': 50 ,'carac': {'FOR':5,'PER':6,'INT':4,'CombatMainsNues':3,'CombatContact':3,'CombatDistance':2}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (2,0), 'armes': ('Épée Longue','Arc Long'), 'armure': 2}
Poing_de_la_Grande_Deesse = {'pv': 90 ,'carac': {'FOR':10,'PER':9,'INT':5,'CombatMainsNues':8,'CombatContact':8,'CombatDistance':8}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (6,0), 'armes': ('Épée Magique','Mitraillette'), 'armure': 4}
Demon_Mineur = {'pv': 35 ,'carac': {'FOR':4,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (2,0), 'armes': ('Bâton','Fronde'), 'armure': 1}
Demon_Majeur = {'pv': 55 ,'carac': {'FOR':6,'PER':5,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Courte','Arc'), 'armure': 2}
Rejeton_de_Naar = {'pv': 65 ,'carac': {'FOR':7,'PER':6,'INT':4,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (4,0), 'armes': ('Épée Longue','Revolver'), 'armure': 3}
Œil_de_Naar = {'pv': 90 ,'carac': {'FOR':10,'PER':9,'INT':5,'CombatMainsNues':8,'CombatContact':8,'CombatDistance':8}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (6,0), 'armes': ('Épée Magique','Mitraillette'), 'armure': 4}
Chien_du_Desert = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '2', 'armes': 'None', 'armure': 0}
Araignee_du_Desert = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':4,'CombatMainsNues':3,'CombatContact':3,'CombatDistance':4}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '3', 'armes': 'None', 'armure': 1}
Chameau_Leclerc = {'pv': 55 ,'carac': {'FOR':6,'PER':5,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '4', 'armes': 'None', 'armure': 2}
Liane_Tueuse = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':3,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Arts Martiaux', 'niveau': '2', 'armes': 'None', 'armure': 0}
Loup = {'pv': 35 ,'carac': {'FOR':3,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '3', 'armes': 'None', 'armure': 0}
Gorille_Geant = {'pv': 50 ,'carac': {'FOR':5,'PER':4,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '4', 'armes': 'None', 'armure': 1}
Monstre_des_Forêts = {'pv': 60 ,'carac': {'FOR':6,'PER':5,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '5', 'armes': 'None', 'armure': 2}
Kanard_Hostile = {'pv': 30 ,'carac': {'FOR':2,'PER':3,'INT':3,'CombatMainsNues':3,'CombatContact':1,'CombatDistance':2}, 'chgt_arme': 'False', 'styles': 'Arts Martiaux', 'niveau': '2', 'armes': 'None', 'armure': 0}
Kanard_Pittopatte = {'pv': 45 ,'carac': {'FOR':4,'PER':4,'INT':4,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Arts Martiaux', 'niveau': '4', 'armes': 'None', 'armure': 1}
Homard_Geant = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':3,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '2', 'armes': 'None', 'armure': 2}
Tortue_Blindee = {'pv': 40 ,'carac': {'FOR':4,'PER':3,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '3', 'armes': 'None', 'armure': 4}
Requin_Volant = {'pv': 55 ,'carac': {'FOR':6,'PER':6,'INT':3,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '4', 'armes': 'None', 'armure': 2}
Ping_Pong = {'pv': 25 ,'carac': {'FOR':2,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Arts Martiaux', 'niveau': '1', 'armes': 'None', 'armure': 0}
Troll = {'pv': 45 ,'carac': {'FOR':5,'PER':5,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lame Rapide', 'niveau': '3', 'armes': ('Épée Courte'), 'armure': 1}
Guerrier_Hologramme = {'pv': 55 ,'carac': {'FOR':5,'PER':6,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (4,0), 'armes': ('Hache','Arc'), 'armure': 0}
Cube_de_Logique_Brute = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '1', 'armes': 'None', 'armure': 0}
Pieuvre_de_Logique_Brute = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '2', 'armes': 'None', 'armure': 1}
Logipieuvre = {'pv': 55 ,'carac': {'FOR':5,'PER':4,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Courte','Fronde'), 'armure': 2}
Grand_Calculateur = {'pv': 65 ,'carac': {'FOR':5,'PER':5,'INT':6,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (5,0), 'armes': ('Épée Longue','Arc'), 'armure': 3}
Invocateur_de_Magmor = {'pv': 30 ,'carac': {'FOR':2,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,2), 'armes': ('Bâton','Arc'), 'armure': 0}
Rejeton_de_Magmor = {'pv': 50 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Défensive','Base Distance'), 'niveau': (4,0), 'armes': ('Hache','Fronde'), 'armure': 1}
Magmor_le_Polymorphe = {'pv': 80 ,'carac': {'FOR':9,'PER':8,'INT':3,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Défensive','Base Distance'), 'niveau': (6,0), 'armes': ('Épée Magique','Fusil'), 'armure': 4}
Poisson_Bouffe_Tout = {'pv': 25 ,'carac': {'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Base Mains Nues', 'niveau': '0', 'armes': 'None', 'armure': 0}
Requin = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '2', 'armes': 'None', 'armure': 1}
Pieuvre_des_Profondeurs = {'pv': 50 ,'carac': {'FOR':5,'PER':6,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '3', 'armes': 'None', 'armure': 1}
Pirate = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (2,0), 'armes': ('Épée Courte','Arc'), 'armure': 2}
Capitaine_Pirate = {'pv': 45 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (4,0), 'armes': ('Épée Longue','Revolver'), 'armure': 3}
Barbe_Mauve = {'pv': 60 ,'carac': {'FOR':6,'PER':5,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (6,0), 'armes': ('Épée Magique','Fusil'), 'armure': 4}
Rapace_Temeraire = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '2', 'armes': 'None', 'armure': 0}
Bâtard_du_Geant_des_Montagnes = {'pv': 40 ,'carac': {'FOR':4,'PER':3,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Défensive','Base Distance'), 'niveau': (3,0), 'armes': ('Hache','Arc'), 'armure': 1}
Geant_des_Montagnes = {'pv': 65 ,'carac': {'FOR':7,'PER':5,'INT':4,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Défensive','Base Distance'), 'niveau': (5,0), 'armes': ('Hallebarde','Arc Long'), 'armure': 2}
Dragonneau = {'pv': 35 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Arts Martiaux', 'niveau': '1', 'armes': 'None', 'armure': 0}
Dragon = {'pv': 55 ,'carac': {'FOR':6,'PER':5,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Courte','Arc'), 'armure': 1}
Ancalagon_le_Noir = {'pv': 75 ,'carac': {'FOR':7,'PER':6,'INT':5,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (6,0), 'armes': ('Épée Longue','Arc'), 'armure': 2}
Squelette = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lame Défensive', 'niveau': '1', 'armes': ('Bâton'), 'armure': 0}
Zombie = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':2,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lame Défensive', 'niveau': '2', 'armes': ('Couteau'), 'armure': 0}
Momie = {'pv': 50 ,'carac': {'FOR':5,'PER':5,'INT':2,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lame Défensive', 'niveau': '3', 'armes': ('Épée Courte'), 'armure': 1}
Liche = {'pv': 65 ,'carac': {'FOR':6,'PER':6,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Défensive','Base Distance'), 'niveau': (5,0), 'armes': ('Épée Longue','Arc'), 'armure': 2}
Dragon_Chenille = {'pv': 20 ,'carac': {'FOR':2,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Base Mains Nues', 'niveau': '0', 'armes': 'None', 'armure': 0}
Hyène_Mutante = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '2', 'armes': 'None', 'armure': 1}
Super_Guerrier = {'pv': 55 ,'carac': {'FOR':6,'PER':5,'INT':3,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (4,0), 'armes': ('Épée Longue','Revolver'), 'armure': 2}
Ectoplasme = {'pv': 25 ,'carac': {'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Distance','Base Distance'), 'niveau': (0,0), 'armes': ('Fronde'), 'armure': 0}
Guerrier_Fantôme = {'pv': 45 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (3,0), 'armes': ('Couteau','Arc'), 'armure': 1}
Mysti = {'pv': 65 ,'carac': {'FOR':5,'PER':3,'INT':4,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (5,0), 'armes': ('Épée Longue','Revolver'), 'armure': 3}
Mouton = {'pv': 20 ,'carac': {'FOR':2,'PER':2,'INT':1,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Base Mains Nues', 'niveau': '0', 'armes': 'None', 'armure': 0}
Vache = {'pv': 25 ,'carac': {'FOR':3,'PER':2,'INT':1,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Base Mains Nues', 'niveau': '0', 'armes': 'None', 'armure': 0}
Paysanne_Effarouchee = {'pv': 25 ,'carac': {'FOR':2,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lame Précise', 'niveau': '1', 'armes': ('Bâton'), 'armure': 0}
Voleur_de_Betail = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':2,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (3,0), 'armes': ('Couteau','Fronde'), 'armure': 0}
Druidesse = {'pv': 55 ,'carac': {'FOR':5,'PER':5,'INT':4,'CombatMainsNues':2,'CombatContact':1,'CombatDistance':1}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (3,0), 'armes': ('Bâton','Fronde'), 'armure': 0}
Cheval = {'pv': 20 ,'carac': {'FOR':2,'PER':2,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Base Mains Nues', 'niveau': '0', 'armes': 'None', 'armure': 0}
Pingouin_à_Roulettes = {'pv': 25 ,'carac': {'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Base Mains Nues', 'niveau': '0', 'armes': 'None', 'armure': 0}
Piquosaure = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '2', 'armes': 'None', 'armure': 3}
Ver_de_Glace = {'pv': 45 ,'carac': {'FOR':5,'PER':5,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '3', 'armes': 'None', 'armure': 1}
Nounours_Polaire = {'pv': 55 ,'carac': {'FOR':6,'PER':5,'INT':3,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '4', 'armes': 'None', 'armure': 2}
Père_Noël = {'pv': 35 ,'carac': {'FOR':2,'PER':4,'INT':3,'CombatMainsNues':1,'CombatContact':1,'CombatDistance':2}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (3,0), 'armes': ('Couteau','Arc'), 'armure': 0}
Sbleune_Rouge = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lame Défensive', 'niveau': '2', 'armes': ('Couteau'), 'armure': 2}
Sbleune_Vert = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':2,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lame Défensive', 'niveau': '3', 'armes': ('Épée Courte'), 'armure': 2}
Sbleune_Jaune = {'pv': 50 ,'carac': {'FOR':5,'PER':5,'INT':3,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lame Défensive', 'niveau': '4', 'armes': ('Hache'), 'armure': 3}
Araignee_Eboueuse = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '1', 'armes': 'None', 'armure': 0}
Fourmi_Geante = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '2', 'armes': 'None', 'armure': 1}
Salamandre_de_la_Mort = {'pv': 55 ,'carac': {'FOR':6,'PER':6,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '4', 'armes': 'None', 'armure': 1}
Teteux_Parasite = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':3,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (1,0), 'armes': ('Couteau','Fronde'), 'armure': 0}
Teteux_Noir = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme':'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Courte','Arc'), 'armure': 1}
Helène_Nipournicontre = {'pv': 60 ,'carac': {'FOR':6,'PER':6,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (5,0), 'armes': ('Épée Longue','Revolver'), 'armure': 2}
Cape_Vampire = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'False', 'styles': 'Lutteur', 'niveau': '1', 'armes': 'None', 'armure': 0}
Vampire_Mineur = {'pv': 40 ,'carac': {'FOR':4,'PER':3,'INT':3,'CombatMainsNues':4,'CombatContact':3,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (2,0), 'armes': ('Épée Courte','Arc'), 'armure': 0}
Vampire_Majeur = {'pv': 55 ,'carac': {'FOR':6,'PER':4,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (4,0), 'armes':('Hache','Revolver'), 'armure': 1}
Primitif_Elmerien = {'pv': 30 ,'carac': {'FOR':3,'PER':3,'INT':1,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Défensive','Base Distance'), 'niveau': (2,0), 'armes': ('Épée Courte','Arc'), 'armure': 0}
Primitif_Elmerien_Guerrier = {'pv': 50 ,'carac': {'FOR':5,'PER':5,'INT':1,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Défensive','Base Distance'), 'niveau': (4,0), 'armes': ('Hache','Revolver'), 'armure': 2}
Primitif_Elmerien_Mage = {'pv': 50 ,'carac': {'FOR':5,'PER':6,'INT':2,'CombatMainsNues':2,'CombatContact':1,'CombatDistance':1}, 'chgt_arme': 'True', 'styles': ('Lame Défensive','Base Distance'), 'niveau': (3,0), 'armes': ('Hache','Revolver'), 'armure': 1}
Elemental_d_Eau = {'pv': 50 ,'carac': {'FOR':5,'PER':4,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (2,0), 'armes': ('Épée Courte','Arc'), 'armure': 1}
Elemental_d_Air = {'pv': 50 ,'carac': {'FOR':5,'PER':5,'INT':2,'CombatMainsNues':5,'CombatContact':4,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Courte','Arc'), 'armure': 2}
Elemental_de_Terre = {'pv': 55 ,'carac': {'FOR':6,'PER':4,'INT':3,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (4,0), 'armes': ('Hache','Revolver'), 'armure': 2}
Elemental_de_Feu = {'pv': 55 ,'carac': {'FOR':5,'PER':5,'INT':4,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (4,0), 'armes': ('Épée Longue','Revolver'), 'armure': 2}
Bourgeois_Decadent = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,2), 'armes': ('Épée Courte','Arc'), 'armure': 1}
Esclave_Rebelle = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (3,0), 'armes': ('Épée Courte','Arc'), 'armure': 1}
Greviste_Casseur = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Défensive','Base Distance'), 'niveau': (2,0), 'armes': ('Épée Courte','Arc'), 'armure': 1}
Commando_Frigide = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (2,0), 'armes': ('Épée Courte','Arc'), 'armure': 1}
Militant_Carnivore = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (2,0), 'armes': ('Épée Courte','Arc'), 'armure': 1}
Grammairien_Vindicatif = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':4,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Défensive','Base Distance'), 'niveau': (2,0), 'armes': ('Épée Courte','Arc'), 'armure': 1}
Poudre_en_Colère = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':3,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Précise','Base Distance'), 'niveau': (2,0), 'armes': ('Épée Courte','Arc'), 'armure': 1}
Paysan_en_Revolte = {'pv': 40 ,'carac': {'FOR':4,'PER':4,'INT':2,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Défensive','Base Distance'), 'niveau': (2,0), 'armes': ('Épée Courte','Arc'), 'armure': 1}
Loubard_Tatoue = {'pv': 45 ,'carac': {'FOR':6,'PER':5,'INT':4,'CombatMainsNues':3,'CombatContact':2,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Lame Rapide','Base Distance'), 'niveau': (2,0), 'armes': ('Épée Courte','Arc'), 'armure': 1}
Extraterrestre = {'pv': 55 ,'carac': {'FOR':7,'PER':6,'INT':4,'CombatMainsNues':6,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,3), 'armes': ('Épée Courte','Arc'), 'armure': 2}
Grand_Extraterrestre = {'pv': 55 ,'carac': {'FOR':4,'PER':4,'INT':4,'CombatMainsNues':7,'CombatContact':5,'CombatDistance':3}, 'chgt_arme': 'True', 'styles': ('Base Contact','Tireur d\'Élite'), 'niveau': (0,5), 'armes': ('Hache','Revolver'), 'armure': 3}


PNJ = {
"Aigle Géant" : Aigle_Geant,
"Ancalagon le Noir" : Ancalagon_le_Noir,
"Ange Vengeur" : Ange_Vengeur,
"Apprenti" : Apprenti,
"Araignée du Désert" : Araignee_du_Desert,
"Araignée-Éboueuse" : Araignee_Eboueuse,
"Archange Vengeur" : Archange_Vengeur,
"Assassin" : Assassin,
"Avion Présidentiel" : Avion_Presidentiel,
"Barbe-Mauve" : Barbe_Mauve,
"Bâtard du Géant des Montagnes" : Bâtard_du_Geant_des_Montagnes,
"Bishônen Assassin" : Bishônen_Assassin,
"Bishônen Magicien" : Bishônen_Magicien,
"Bombardier" : Bombardier,
"Bourgeois Décadent" : Bourgeois_Decadent,
"Cape-Vampire" : Cape_Vampire,
"Capitaine Pirate" : Capitaine_Pirate,
"Carrosse" : Carrosse,
"Chameau Leclerc" : Chameau_Leclerc,
"Champignonz" : Champignonz,
"Champignonz Mutant" : Champignonz_Mutant,
"Chapardeur" : Chapardeur,
"Chef Rebelle" : Chef_Rebelle,
"Cheval" : Cheval,
"Chien du Désert" : Chien_du_Desert,
"Clone" : Clone,
"Clown" : Clown,
"Coiffeur" : Coiffeur,
"Coléoptère" : Coleoptère,
"Commando Frigide" : Commando_Frigide,
"Complice" : Complice,
"Confesseur" : Confesseur,
"Croiseur" : Croiseur,
"Cube de Logique Brute" : Cube_de_Logique_Brute,
"Cuistot" : Cuistot,
"Démon Majeur" : Demon_Majeur,
"Démon Mineur" : Demon_Mineur,
"Destroyer" : Destroyer,
"Dragon" : Dragon,
"Dragon-Chenille" : Dragon_Chenille,
"Dragonneau" : Dragonneau,
"Druidesse" : Druidesse,
"Ectoplasme" : Ectoplasme,
"Écuyer" : Ecuyer,
"Élémental d'Air" : Elemental_d_Air,
"Élémental de Feu" : Elemental_de_Feu,
"Élémental de Terre" : Elemental_de_Terre,
"Élémental d'Eau" : Elemental_d_Eau,
"Émeutier" : Emeutier,
"Érudit" : Erudit,
"Esclave" : Esclave,
"Esclave Rebelle" : Esclave_Rebelle,
"Extraterrestre" : Extraterrestre,
"Fourmi Géante" : Fourmi_Geante,
"Franc-Tireur" : Franc_Tireur,
"Frégate" : Fregate,
"Galère Impériale" : Galère_Imperiale,
"Garde du Corps" : Garde_du_Corps,
"Garde-Malade" : Garde_Malade,
"Géant des Montagnes" : Geant_des_Montagnes,
"Geek" : Geek,
"Gorille Géant" : Gorille_Geant,
"Grammairien Vindicatif" : Grammairien_Vindicatif,
"Grand Calculateur" : Grand_Calculateur,
"Grand Extraterrestre" : Grand_Extraterrestre,
"Gréviste Casseur" : Greviste_Casseur,
"Guerrier Fantôme" : Guerrier_Fantôme,
"Guerrier Hologramme" : Guerrier_Hologramme,
"Guerrière Slavone" : Guerrière_Slavone,
"Hélène Nipournicontre" : Helène_Nipournicontre,
"Homard Géant" : Homard_Geant,
"Homme de main" : Homme_de_main,
"Hyène Mutante" : Hyène_Mutante,
"Infirmier" : Infirmier,
"Invocateur de Magmor" : Invocateur_de_Magmor,
"Kanard Hostile" : Kanard_Hostile,
"Kanard Pittopatte" : Kanard_Pittopatte,
"Le Rêveur" : Le_Rêveur,
"Liane Tueuse" : Liane_Tueuse,
"Liche" : Liche,
"Limousine" : Limousine,
"Limousine Plaquée Or" : Limousine_Plaquee_Or,
"Logipieuvre" : Logipieuvre,
"Loubard Tatoué" : Loubard_Tatoue,
"Loup" : Loup,
"Magmor le Polymorphe" : Magmor_le_Polymorphe,
"Maître d'Armes" : Maitre_d_Armes,
"Majordome" : Majordome,
"Médium" : Medium,
"Milicien" : Milicien,
"Militant Carnivore" : Militant_Carnivore,
"Mille-Pattes Accro" : Mille_Pattes_Accro,
"Momie" : Momie,
"Monstre des Forêts" : Monstre_des_Forêts,
"Mouton" : Mouton,
"Mysti" : Mysti,
"Nounours Polaire" : Nounours_Polaire,
"Œil de Naar" : Œil_de_Naar,
"Palanquin sur Sbleune" : Palanquin_sur_Sbleune,
"Papamobile" : Papamobile,
"Paramilitaire" : Paramilitaire,
"Partisan" : Partisan,
"Patrouilleur" : Patrouilleur,
"Paysan en Révolte" : Paysan_en_Revolte,
"Paysanne Effarouchée" : Paysanne_Effarouchee,
"Père Noël" : Père_Noël,
"Petit Poney" : Petit_Poney,
"Pieuvre de Logique Brute" : Pieuvre_de_Logique_Brute,
"Pieuvre des Profondeurs" : Pieuvre_des_Profondeurs,
"Pingouin à Roulettes" : Pingouin_à_Roulettes,
"Ping-Pong" : Ping_Pong,
"Piquosaure" : Piquosaure,
"Pirate" : Pirate,
"Poing de la Grande Déesse" : Poing_de_la_Grande_Deesse,
"Poisson Bouffe-Tout" : Poisson_Bouffe_Tout,
"Policier d'Élite" : Policier_d_Elite,
"Porte-Avions" : Porte_Avions,
"Poudré en Colère" : Poudre_en_Colère,
"Primitif Elmérien" : Primitif_Elmerien,
"Primitif Elmérien Guerrier" : Primitif_Elmerien_Guerrier,
"Primitif Elmérien Mage" : Primitif_Elmerien_Mage,
"Prince Bishônen" : Prince_Bishônen,
"Rapace Téméraire" : Rapace_Temeraire,
"Rejeton de Magmor" : Rejeton_de_Magmor,
"Rejeton de Naar" : Rejeton_de_Naar,
"Requin" : Requin,
"Requin Volant" : Requin_Volant,
"Robot de Compagnie" : Robot_de_Compagnie,
"Robot Ménager" : Robot_Menager,
"Salamandre de la Mort" : Salamandre_de_la_Mort,
"Sbleune Jaune" : Sbleune_Jaune,
"Sbleune Rouge" : Sbleune_Rouge,
"Sbleune Vert" : Sbleune_Vert,
"Secrétaire" : Secretaire,
"Sectateur" : Sectateur,
"Soldat" : Soldat,
"Soldat d'Élite" : Soldat_d_Elite,
"Soldat Déserteur" : Soldat_Deserteur,
"Squelette" : Squelette,
"Styliste" : Styliste,
"Super-Guerrier" : Super_Guerrier,
"Tank" : Tank,
"Terroriste" : Terroriste,
"Téteux Noir" : Teteux_Noir,
"Téteux Parasite" : Teteux_Parasite,
"Tortue Blindée" : Tortue_Blindee,
"Troll" : Troll,
"Vache" : Vache,
"Valet" : Valet,
"Vampire Majeur" : Vampire_Majeur,
"Vampire Mineur" : Vampire_Mineur,
"Ver de Glace" : Ver_de_Glace,
"Voleur de Bétail" : Voleur_de_Betail,
"Zombie" : Zombie
}

def getPNJ(name):
    try:
        params = PNJ[name]
    except:
        print("Pas de PNJ sous ce nom, #déso !!!")
        raise
    pnj = Combattant(**params)
    return pnj

#Employes = {
#"Écuyer" : Ecuyer,
#"Homme de main" : Homme_de_main,
#"Coiffeur" : Coiffeur,
#"Apprenti" : Apprenti,
#"Majordome" : Majordome,
#"Geek" : Geek,
#"Confesseur" : Confesseur,
#"Infirmier" : Infirmier,
#"Garde du Corps" : Garde_du_Corps,
#"Maître d'Armes" : Maitre_d_Armes,
#"Partisan" : Partisan,
#"Secrétaire" : Secretaire,
#"Terroriste" : Terroriste,
#"Complice" : Complice,
#"Médium" : Medium,
#"Érudit" : Erudit,
#"Styliste" : Styliste,
#"Cuistot" : Cuistot,
#"Clown" : Clown,
#"Garde-Malade" : Garde_Malade,
#"Valet" : Valet,
#"Esclave" : Esclave,
#"Robot de Compagnie" : Robot_de_Compagnie,
#"Robot Ménager" : Robot_Menager,
#"Milicien" : Milicien,
#"Franc-Tireur" : Franc_Tireur,
#"Émeutier" : Emeutier,
#"Sectateur" : Sectateur,
#"Paramilitaire" : Paramilitaire
#}
#
#Employes_Fonction = {
#"Policier d'Élite" : Policier_d_Elite,
#"Soldat" : Soldat,
#"Soldat d'Élite" : Soldat_d_Elite,
#"Tank" : Tank,
#"Clone" : Clone,
#"Guerrière Slavone" : Guerrière_Slavone,
#"Patrouilleur" : Patrouilleur,
#"Frégate" : Fregate,
#"Destroyer" : Destroyer,
#"Croiseur" : Croiseur,
#"Porte-Avions" : Porte_Avions,
#"Bombardier" : Bombardier,
#"Coléoptère" : Coleoptère,
#"Galère Impériale" : Galère_Imperiale,
#"Limousine Plaquée Or" : Limousine_Plaquee_Or,
#"Papamobile" : Papamobile,
#"Petit Poney" : Petit_Poney,
#"Palanquin sur Sbleune" : Palanquin_sur_Sbleune,
#"Avion Présidentiel" : Avion_Presidentiel,
#"Carrosse" : Carrosse,
#"Limousine" : Limousine
#}
#
#Monstres = {
#"Assassin" : Assassin,
#"Soldat Déserteur" : Soldat_Deserteur,
#"Chef Rebelle" : Chef_Rebelle,
#"Mille-Pattes Accro" : Mille_Pattes_Accro,
#"Champignonz" : Champignonz,
#"Champignonz Mutant" : Champignonz_Mutant,
#"Le Rêveur" : Le_Rêveur,
#"Chapardeur" : Chapardeur,
#"Bishônen Assassin" : Bishônen_Assassin,
#"Bishônen Magicien" : Bishônen_Magicien,
#"Prince Bishônen" : Prince_Bishônen,
#"Aigle Géant" : Aigle_Geant,
#"Ange Vengeur" : Ange_Vengeur,
#"Archange Vengeur" : Archange_Vengeur,
#"Poing de la Grande Déesse" : Poing_de_la_Grande_Deesse,
#"Démon Mineur" : Demon_Mineur,
#"Démon Majeur" : Demon_Majeur,
#"Rejeton de Naar" : Rejeton_de_Naar,
#"Œil de Naar" : Œil_de_Naar,
#"Chien du Désert" : Chien_du_Desert,
#"Araignée du Désert" : Araignee_du_Desert,
#"Chameau Leclerc" : Chameau_Leclerc,
#"Liane Tueuse" : Liane_Tueuse,
#"Loup" : Loup,
#"Gorille Géant" : Gorille_Geant,
#"Monstre des Forêts" : Monstre_des_Forêts,
#"Kanard Hostile" : Kanard_Hostile,
#"Kanard Pittopatte" : Kanard_Pittopatte,
#"Homard Géant" : Homard_Geant,
#"Tortue Blindée" : Tortue_Blindee,
#"Requin Volant" : Requin_Volant,
#"Ping-Pong" : Ping_Pong,
#"Troll" : Troll,
#"Guerrier Hologramme" : Guerrier_Hologramme,
#"Cube de Logique Brute" : Cube_de_Logique_Brute,
#"Pieuvre de Logique Brute" : Pieuvre_de_Logique_Brute,
#"Logipieuvre" : Logipieuvre,
#"Grand Calculateur" : Grand_Calculateur,
#"Invocateur de Magmor" : Invocateur_de_Magmor,
#"Rejeton de Magmor" : Rejeton_de_Magmor,
#"Magmor le Polymorphe" : Magmor_le_Polymorphe,
#"Poisson Bouffe-Tout" : Poisson_Bouffe_Tout,
#"Requin" : Requin,
#"Pieuvre des Profondeurs" : Pieuvre_des_Profondeurs,
#"Pirate" : Pirate,
#"Capitaine Pirate" : Capitaine_Pirate,
#"Barbe-Mauve" : Barbe_Mauve,
#"Rapace Téméraire" : Rapace_Temeraire,
#"Bâtard du Géant des Montagnes" : Bâtard_du_Geant_des_Montagnes,
#"Géant des Montagnes" : Geant_des_Montagnes,
#"Dragonneau" : Dragonneau,
#"Dragon" : Dragon,
#"Ancalagon le Noir" : Ancalagon_le_Noir,
#"Squelette" : Squelette,
#"Zombie" : Zombie,
#"Momie" : Momie,
#"Liche" : Liche,
#"Dragon-Chenille" : Dragon_Chenille,
#"Hyène Mutante" : Hyène_Mutante,
#"Super-Guerrier" : Super_Guerrier,
#"Ectoplasme" : Ectoplasme,
#"Guerrier Fantôme" : Guerrier_Fantôme,
#"Mysti" : Mysti,
#"Mouton" : Mouton,
#"Vache" : Vache,
#"Paysanne Effarouchée" : Paysanne_Effarouchee,
#"Voleur de Bétail" : Voleur_de_Betail,
#"Druidesse" : Druidesse,
#"Cheval" : Cheval,
#"Pingouin à Roulettes" : Pingouin_à_Roulettes,
#"Piquosaure" : Piquosaure,
#"Ver de Glace" : Ver_de_Glace,
#"Nounours Polaire" : Nounours_Polaire,
#"Père Noël" : Père_Noël,
#"Sbleune Rouge" : Sbleune_Rouge,
#"Sbleune Vert" : Sbleune_Vert,
#"Sbleune Jaune" : Sbleune_Jaune,
#"Araignée-Éboueuse" : Araignee_Eboueuse,
#"Fourmi Géante" : Fourmi_Geante,
#"Salamandre de la Mort" : Salamandre_de_la_Mort,
#"Téteux Parasite" : Teteux_Parasite,
#"Téteux Noir" : Teteux_Noir,
#"Hélène Nipournicontre" : Helène_Nipournicontre,
#"Cape-Vampire" : Cape_Vampire,
#"Vampire Mineur" : Vampire_Mineur,
#"Vampire Majeur" : Vampire_Majeur,
#"Primitif Elmérien" : Primitif_Elmerien,
#"Primitif Elmérien Guerrier" : Primitif_Elmerien_Guerrier,
#"Primitif Elmérien Mage" : Primitif_Elmerien_Mage,
#"Élémental d'Eau" : Elemental_d_Eau,
#"Élémental d'Air" : Elemental_d_Air,
#"Élémental de Terre" : Elemental_de_Terre,
#"Élémental de Feu" : Elemental_de_Feu,
#"Bourgeois Décadent" : Bourgeois_Decadent,
#"Esclave Rebelle" : Esclave_Rebelle,
#"Gréviste Casseur" : Greviste_Casseur,
#"Commando Frigide" : Commando_Frigide,
#"Militant Carnivore" : Militant_Carnivore,
#"Grammairien Vindicatif" : Grammairien_Vindicatif,
#"Poudré en Colère" : Poudre_en_Colère,
#"Paysan en Révolte" : Paysan_en_Revolte,
#"Loubard Tatoué" : Loubard_Tatoue,
#"Extraterrestre" : Extraterrestre,
#"Grand Extraterrestre" : Grand_Extraterrestre
#}
