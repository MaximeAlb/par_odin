# créer un repo GIT pour faire mes tests
# réparer les bug générer en créant la class Armee

"Enfin le git push et pull fonctionnent !"

class Unite:
    def __init__(self, name, val):
        self.name = name
        self.val = val


"""
Il va y avoir 2 armées qui reprenne certaines fonctions:
- les 2 armées auront un nom,               OK !
- elles calculent leurs score total,        OK !
- elles affichent leur score total,         OK !
- elles affichent les pions dans l'armée    OK !

"""
class Armee:

    def __init__(self, name, pions):
        self.LISTE_PIONS = []
        self.name = name
        self.pions = pions
        self.tt = 0
        self.dico = {}

    def CreationDicoPions(self):
        for pion in self.pions:
            self.dico[pion.name] = pion.val
        return self.dico

    def AfficherPionsDansArmee(self):
        txt = ""
        for pion in self.pions:
            if len(self.pions) == 0:
                txt = "VIDE"
                continue
            texte_descrition = pion.name + ":" + str(pion.val) + ", "
            txt += texte_descrition
        return txt

    def CreationListePion(self):
        if len(self.pions) == 0:
            for i in range(0, 7):
                self.LISTE_PIONS.append(vide.name)
        for pion in self.pions:
            self.LISTE_PIONS.append(pion.name)
        return self.LISTE_PIONS


def transfert_pion_armee(lo, lj, rep_pj):
    lo[int(rep_pj) - 1], lj[int(rep_pj) - 1] = lj[int(rep_pj) - 1], lo[int(rep_pj) - 1]


def calcul_pts(l, dico):
    tt = 0
    for e in l:
        if e == "Vide":
            continue
        tt += dico[e]
    return tt



# Entités des pions
vide = Unite("Vide", 0)
hero = Unite("Héro", 3)
captain = Unite("Capitaine", 2)
soldier = Unite("Soldat", 1)

# Entités des camps
armee_ordi = Armee("Armée de l'ordi:", [hero, hero, hero, captain, captain, captain, soldier])
armee_joueur = Armee("Armée du joueur:", [])

# variables
liste_pions_armee_ordi = armee_ordi.CreationListePion()
liste_pions_armee_joueur = armee_joueur.CreationListePion()

# lancement des méthodes
creat_dico_pions_ordi = armee_ordi.CreationDicoPions()
description_pions_ordi = armee_ordi.AfficherPionsDansArmee()
creat_dico_pions_pj = armee_ordi.CreationDicoPions()
description_pions_joueur = armee_joueur.AfficherPionsDansArmee()

# ce qui s'affichera sur le terminal:
print(armee_ordi.name, description_pions_ordi)
print(armee_joueur.name, description_pions_joueur)

# ce qui ne s'affiche pas mais que je souhaite voir pour visualiser
print("création du dico ordi", creat_dico_pions_ordi)
print("création du dico pj", creat_dico_pions_pj)
print("création de la l ordi", liste_pions_armee_ordi)
print("création de la l pj", liste_pions_armee_joueur)

# lancement boucle infini du jeu
while True:
    print(calcul_pts(liste_pions_armee_ordi, creat_dico_pions_ordi))
    print(calcul_pts(liste_pions_armee_joueur, creat_dico_pions_pj))
    retour_joueur = input("entre un nombre du pav num: ")
    transfert_pion_armee(liste_pions_armee_ordi, liste_pions_armee_joueur, retour_joueur)
    if retour_joueur == str(0):
        break
