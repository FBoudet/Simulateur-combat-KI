import numpy.random as rd
from combat import Jet
from techniques import styleCombat
from armes import selectArme

class Combattant():
    def __init__(self, pv, carac, chgt_arme, styles=None, niveau=0, armes=None, armure=0, bonus_jet=0, bonus_dgts_perso=0,pnj=True):
        self.pv = pv
        self.carac = carac
        self.chgt_arme = chgt_arme
        self.selected_arme = None
        if chgt_arme:
            self.arme_contact = selectArme(armes[0])
            self.arme_dist = selectArme(armes[1])
            self.parades_contact, self.techniques_contact = styleCombat(styles[0], niveau[0])
            self.parades_dist, self.techniques_dist = styleCombat(styles[1], niveau[1])
        else:
            self.arme = selectArme(armes)
            if self.arme.portee > 0:
                self.arme_dist = self.arme
                self.selected_arme = self.arme_dist
                self.arme_contact = None
                self.parades_dist, self.techniques_dist = styleCombat(styles, niveau)
                self.parades_contact = None
                self.techniques_contact = None
                self.mode_combat = 'Distance'
            else:
                self.arme_contact = self.arme
                self.selected_arme = self.arme_contact
                self.arme_dist = None
                self.parades_contact, self.techniques_contact = styleCombat(styles, niveau)
                self.parades_dist = None
                self.techniques_dist = None
                self.mode_combat = 'Contact'
        self.selected_att = None
        self.selected_par = None
        self.armure = armure
        self.bonus_jet = bonus_jet
        self.bonus_dgts_perso = bonus_dgts_perso
        self.pnj = pnj
        self.malus_att = 0
        self.bonus_att = 0
        self.bonus_def = 0
        self.bonus_div = 1
        self.bonus_mult = 1
        self.eff_dist = False
        self.eff_contact = False
        self.eff_mn = False
        self.allow_att = True
        self.prior = False
        self.bcontre = False
        self.mod_dist = 0
        self.cdist = False
        self.ccont = False
        self.cmn = False
        self.allow_degats = True
        self.desarm = False
        self.allow_parade = True
        self.malus_armure = 1
        self.bris_armure = False
        
    def select_techniques(self, dist):
        if dist > 0:
            if self.mode_combat == 'Distance':
                if dist <= self.selected_arme.portee:
                    self.selected_att = rd.choice(self.techniques_dist)
                    self.allow_parade = self.selected_att.allow_parade
                if self.parades_dist != []:
                    self.selected_par = rd.choice(self.parades_dist)
                    self.allow_att = self.selected_par.allow_att
            else:
                if self.chgt_arme:
                    if self.pnj:
                        self.mode_combat = 'Distance'
                        self.selected_arme = self.arme_dist
                        if dist <= self.selected_arme.portee:
                            self.selected_att = rd.choice(self.techniques_dist)
                            self.allow_parade = self.selected_att.allow_parade
                        if self.parades_dist != []:
                            self.selected_par = rd.choice(self.parades_dist)
                            self.allow_att = self.selected_par.allow_att
                    else:
                        self.mode_combat = 'Distance'
                        self.selected_arme = self.arme_dist

        else:
            if self.mode_combat == 'Contact':
                self.selected_att = rd.choice(self.techniques_contact)
                self.allow_parade = self.selected_att.allow_parade
                if self.parades_contact != []:
                    self.selected_par = rd.choice(self.parades_contact)
                    self.allow_att = self.selected_par.allow_att
            else:
                if self.chgt_arme:
                    if self.pnj:
                        self.mode_combat = 'Contact'
                        self.selected_arme = self.arme_contact
                        self.selected_att = rd.choice(self.techniques_contact)
                        self.allow_parade = self.selected_att.allow_parade
                        if self.parades_contact != []:
                            self.selected_par = rd.choice(self.parades_contact)
                            self.allow_att = self.selected_par.allow_att
                    else:
                        self.mode_combat = 'Contact'
                        self.selected_arme = self.arme_contact
                else:
                    self.selected_att = rd.choice(self.techniques_dist)
                    self.allow_parade = self.selected_att.allow_parade
                    if self.parades_dist != []:
                        self.selected_par = rd.choice(self.parades_dist)
                        self.allow_att = self.selected_par.allow_att
        
        if not self.allow_att and not self.allow_parade:
            self.allow_parade = True


    def jet_parade(self):
        diff = self.carac['INT']
        if self.mode_combat == 'Distance':
            diff += self.carac['CombatDistance']
        else:
            diff += self.carac['CombatContact']
        diff -= (self.selected_par.diff + 5)
        if Jet(diff):
            self.malus_att, self.bonus_def, self.bonus_div, self.eff_dist, self.eff_contact, self.eff_mn, self.prior, self.bcontre, self.mod_dist = \
            self.selected_par.matt, self.selected_par.bdef, self.selected_par.bdiv, self.selected_par.eff_dist, self.selected_par.eff_contact, \
            self.selected_par.eff_mn, self.selected_par.prior, self.selected_par.bcontre, self.selected_par.mod_dist


    def attaque(self, tgt):
        if self.mode_combat == 'Distance':
            diff = self.carac['PER'] + self.carac['CombatDistance'] + self.bonus_jet
        else:
            diff = self.carac['FOR'] + self.carac['CombatContact'] + self.bonus_jet
            
        diff -= (self.selected_arme.malus_jet + self.selected_att.diff + 5)
        
        if self.selected_att.cdist and tgt.eff_dist or self.selected_att.ccont and tgt.eff_contact or self.selected_att.cmn and tgt.eff_mn:
            diff -= self.selected_att.malus_parade*tgt.malus_att
        
        if Jet(diff, tgt.bcontre):
            self.bonus_att, self.malus_armure, self.allow_degats = self.selected_att.bdeg, self.selected_att.malus_armure, self.selected_att.allow_degats
            self.cdist, self.ccont, self.cmn = self.selected_att.cdist, self.selected_att.ccont, self.selected_att.cmn
            tgt.desarm, tgt.bris_armure = self.selected_att.desarm, self.selected_att.bris_armure
            return True
        else:
            return False


    def attaqued_by(self, att):
        if att.allow_degats:
            if att.cdist:
                degats = att.carac['PER']//2 + att.carac['PER']%2
            else:
                degats = att.carac['FOR']
        
                degats += rd.randint(1,4) + att.bonus_att + att.selected_arme.bonus_dgt - att.malus_armure*self.armure
                
                if att.cdist and self.eff_dist or att.ccont and self.eff_contact or att.cmn and self.eff_mn:
                    degats -= self.bonus_def
                            
                degats = degats//self.bonus_div
                degats = max(0,degats)
        else:
            degats = 0
            
        self.pv -= degats


            
            