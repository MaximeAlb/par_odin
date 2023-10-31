# créer un repo GIT pour faire mes tests
# réparer les bug générer en créant la class Armee

"Enfin le git push et pull fonctionnent !"

class Unite:
    def __init__(self, name, value, nb):
        self.name = name
        self.value = value
        self.nb = nb


"""
Il va y avoir 2 armées qui reprenne certaines fonctions:
- les 2 armées auront un nom,               OK !
- elles calculent leurs score total,        
- elles affichent leur score total,         OK !
- elles affichent les pions dans l'armée    OK !

"""
class Armee:

    def __init__(self, name, pions):
        self.LISTE_PIONS = []
        self.liste_valeurs = []
        self.name = name
        self.pions = pions


    def AfficherPionsDansArmee(self):
        txt = ""
        for i in range(len(self.pions)):
            if self.pions[i].nb == 0:
                continue
            texte_descrition = self.pions[i].nb * (self.pions[i].name + ":" + str(self.pions[i].value) + " ")
            txt += texte_descrition
        return txt

    def CreationListePion(self):
        if len(self.pions) == 0:
            for i in range(0, 7):
                self.LISTE_PIONS.append("     ")
        for pion in self.pions:
            for i in range(pion.nb):
                self.LISTE_PIONS.append(pion.name)
        return self.LISTE_PIONS

    def CreationListeValeursDesPions(self):
        for pion in self.pions:
            for i in range(pion.nb):
                self.liste_valeurs.append(pion.value)
        return self.liste_valeurs



def transfert_pion_armee(lo, lj, rep_pj):
    lo[int(rep_pj) - 1], lj[int(rep_pj) - 1] = lj[int(rep_pj) - 1], lo[int(rep_pj) - 1]


def CalculerValeurTotal(l):
    tt = 0
    for valeur in l:
        tt += valeur
    return tt


# Entités des pions
hero = Unite("Héro", 3, 3)
captain = Unite("Capitaine", 2, 3)
soldier = Unite("Soldat", 1, 1)

# Entités des camps
armee_ordi = Armee("Armée de l'ordi:", [hero, captain, soldier])
armee_joueur = Armee("Armée du joueur:", [])

# variables
liste_pions_armee_ordi = armee_ordi.CreationListePion()
liste_pions_armee_joueur = armee_joueur.CreationListePion()

# lancement des méthodes
score_tt_ordi = CalculerValeurTotal(armee_ordi.CreationListeValeursDesPions())
description_pions_ordi = armee_ordi.AfficherPionsDansArmee()
score_tt_joueurs = CalculerValeurTotal(armee_joueur.CreationListeValeursDesPions())
description_pions_joueur = armee_joueur.AfficherPionsDansArmee()

# ce qui s'affichera sur le terminal:
print(armee_ordi.name, score_tt_ordi, description_pions_ordi)
print(armee_joueur.name, score_tt_joueurs, description_pions_joueur)

# ce qui ne s'affiche pas mais que je souhaite voir pour visualiser
print(armee_joueur.CreationListeValeursDesPions())
print(liste_pions_armee_ordi)
print(liste_pions_armee_joueur)

# lancement boucle infini du jeu
while True:
    print()
    retour_joueur = input("entre un nombre du pav num: ")
    transfert_pion_armee(liste_pions_armee_ordi, liste_pions_armee_joueur, retour_joueur)
    print(CalculerValeurTotal(armee_ordi.CreationListeValeursDesPions()), liste_pions_armee_ordi)
    print(CalculerValeurTotal(armee_joueur.CreationListeValeursDesPions()), liste_pions_armee_joueur)
    print(armee_joueur.CreationListeValeursDesPions())
    if retour_joueur == str(0):
        break
