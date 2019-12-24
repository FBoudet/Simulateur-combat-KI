import numpy as np

def _compute_power_path(D):
    """
    On calcule la matrice des chemins de puissance d'après la matrice des confrontations
    Entrée: D matrice NxN des confrontations bilatérales
    Sortie: P dict. P[V,W] force du chemin le plus fort entre deux candidats V et W
    """

    N = D.shape[0]
    P = np.zeros((N,N))
    for u in range(N):
        for v in range(N):
            if u != v:
                strength = D[u,v]
                if strength > D[v,u]:
                    P[u,v] = strength

    for u in range(N):
        for v in range(N):
            if u != v:
                for w in range(N):
                    if w not in [u,v]:
                        dum = P[v,w]
                        dum2 = min(P[v,u],P[u,w])
                        if dum2 > dum:
                            P[v,w] = dum2
    return P

def compute_rankings(D):
    P = _compute_power_path(D)
    N = P.shape[0]
    wins = np.zeros(N,)
    for u in range(N):
        num_wins = 0
        for v in range(N):
            if u == v:
                continue
            score_u = P[u,v]
            score_v = P[v,u]
            if score_u > score_v:
                num_wins += 1
            wins[u] = num_wins
    s = np.argsort(wins)
    return s
