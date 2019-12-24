import numpy as np
from combat import RandCombat
from pnj import getPNJ


def Sample_Combat_PNJ(C1, C2, n_test):
    for i in range(n_test):
        P1 = getPNJ(C1)
        P2 = getPNJ(C2)
        Result, Log = RandCombat([P1],[P2],0)
        E.append(Result)
        result = np.array(E)
        g1=np.sum(result=='Groupe1')
        g2=np.sum(result=='Groupe2')
    return g1,g2

N_test = 1000
list_pnj = getPNJ('all')
N_pnj = len(list_pnj)
A = np.zeros((N_pnj,N_pnj))
D = np.zeros((N_pnj,N_pnj))
for i, pnj_i in enumerate(list_pnj):
    #print('a',pnj_i,getPNJ(pnj_i))
    for j, pnj_j in enumerate(list_pnj):
        #print('b',pnj_j)
        if j>i:
            E = []
            #print('c', PNJ_j.armes)
            print('{} vs {}'.format(pnj_i, pnj_j))
            g1, g2 = Sample_Combat_PNJ(pnj_i, pnj_j, N_test)
            A[i,j] = g1
            A[j,i] = g2

np.save('battle_matrix',A)
