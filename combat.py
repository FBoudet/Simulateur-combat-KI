import numpy as np
import numpy.random as rd

prior_global = False

def Jet(diff, botte_contre=False):
    D = np.arange(-15,21).tolist()
    I = [1,2,3,4,5,7,9,12,15,19,23,28,33,38,44,50,56,61,65,69,72,75,78,81,83,85,87,89,91,93,94,95,96,97,98,99]
    if botte_contre:
        i = 10
    else:
        diff = min(max(-15, diff), 20)
        i = I[D.index(diff)]
    return rd.rand()*100<=i


def RandCombat(Groupe1, Groupe2, dist):
    Round = 0
    mdist = 0
    Log = {'G1':[],'G2':[]}
    while Round<500 and len(Groupe1)>0 and len(Groupe2)>0:
        # print('Round {}, distance {}'.format(Round,dist))
        # print(Groupe1[0].pv,Groupe2[0].pv)

        for cbt in Groupe1:
            if Round == 0 and cbt.chgt_arme:
                if dist > 0:
                    cbt.selected_arme = cbt.arme_dist
                    cbt.mode_combat = 'Distance'
                else:
                    cbt.selected_arme = cbt.arme_contact
                    cbt.mode_combat = 'Contact'
            cbt.select_techniques(dist)

        for cbt in Groupe2:
            if Round == 0 and cbt.chgt_arme:
                if dist > 0:
                    cbt.selected_arme = cbt.arme_dist
                    cbt.mode_combat = 'Distance'
                else:
                    cbt.selected_arme = cbt.arme_contact
                    cbt.mode_combat = 'Contact'
            cbt.select_techniques(dist)

        for cbt in Groupe2:
            if cbt.selected_par != None and cbt.allow_parade:
                cbt.jet_parade()
                #Log['G2'].append(cbt.potentiel_parade)

        for cbt in Groupe1:
            if cbt.selected_par != None and cbt.allow_parade:
                cbt.jet_parade()
                #Log['G1'].append(cbt.potentiel_parade)

        for cbt in Groupe1:
            if cbt.selected_att != None and cbt.allow_att:
                tgt = rd.choice(Groupe2)
                for i in range(cbt.bonus_mult):
#                    Log['G1'].append(cbt.potentiel_technique)
                    if cbt.attaque(tgt):
                        tgt.attaqued_by(cbt)
            Log['G1'].append(cbt.pv)

        for cbt in Groupe2:
            if cbt.selected_att != None and cbt.allow_att:
                tgt = rd.choice(Groupe1)
                for i in range(cbt.bonus_mult):
#                    Log['G2'].append(cbt.potentiel_technique)
                    if cbt.attaque(tgt):
                        tgt.attaqued_by(cbt)
            Log['G2'].append(cbt.pv)

        for cbt in Groupe1:
            mdist += cbt.mod_dist

        for cbt in Groupe2:
            mdist += cbt.mod_dist

        if dist > 0 and mdist < 1000:
            dist -= 1
        #dist = max(0, dist + mod_dist)

        Reset(Groupe1)
        Reset(Groupe2)
        Round += 1


    Result = 'draw'
    if Groupe1 != [] and Groupe2 == []:
        Result = 'Groupe1'
    elif Groupe2 != [] and Groupe1 == []:
        Result =  'Groupe2'

    return Result, Log

def Reset(Groupe):
    for cbt in Groupe:
        cbt.malus_att = 0
        cbt.bonus_att = 0
        cbt.bonus_def = 0
        cbt.bonus_div = 1
        cbt.bonus_mult = 1
        cbt.eff_dist = False
        cbt.eff_contact = False
        cbt.eff_mn = False
        cbt.allow_att = True
        cbt.prior = False
        cbt.bcontre = False
        cbt.mod_dist = 0
        cbt.cdist = False
        cbt.ccont = False
        cbt.cmn = False
        cbt.allow_degats = True
        #if cbt.desarm:
         #   cbt.arme = 0
        cbt.desarm = False
        cbt.allow_parade = True
        cbt.malus_parade = 1
        cbt.malus_armure = 1
        if cbt.bris_armure:
            cbt.armure -= 1
        cbt.bris_armure = False

    # print('snd',cbt.pv, type(cbt.pv))
    if cbt.pv <= 0:
        Groupe.remove(cbt)
