# créer un repo GIT pour faire mes tests
# réparer les bug générer en créant la class Armee

""" MEGA TEST DE REPO GIT"""

class Unite:
    def __init__(self, name, value, nb):
        self.name = name
        self.value = value
        self.nb = nb


class Armee:
    def __init__(self, name):
        self.name = name

    def InitialiserCampOrdi(self):
        for j in range(len(unites)):
            for i in range(0, unites[j].nb):
                camp_ordi.append(unites[i].name)

    def CalculerValeurTotal(self):
        tt = 0
        for i in range(len(unites)):
            tt += unites[i].nb * unites[i].value
        return tt

    def AfficherCampInitial(self):
        txt = ""
        for i in range(len(unites)):
            if unites[i].nb == 0:
                continue
            texte_descrition = unites[i].nb * (unites[i].name + ":" + str(unites[i].value) + " ")
            txt += texte_descrition
        return txt


hero = Unite("Héro", 3, 3)
captain = Unite("Capitaine", 2, 3)
soldier = Unite("Soldat", 1, 1)
armee_ordi = Armee("Armée initial")

armee_ordi.InitialiserCampOrdi()

unites = [hero, captain, soldier]
camp_ordi = []
camp_joueur = []



'''initialiser_camp_ordi(unites)

print(afficher_camp_initial(unites))
valeur_tt_camp_init = calculer_valeur_total(unites)'''
print("la valeur total :", valeur_tt_camp_init)
print("la valeur du joueur :", sum(camp_joueur))
print("l'ordi", len(camp_ordi))
print("joueur", len(camp_joueur))






#fonctionnalité du jeu
def interchanger_les_listes(l1, l2, rep_joueur):
    l2.append(l1[int(rep_joueur)])
    del l1[int(rep_joueur)]
#interchanger_les_listes(camp_ordi, camp_joueur, "1")











'''#pour créer le camp de l'ordi
def initialiser_camp_ordi(uni):
    for j in range(len(uni)):
        for i in range(0, uni[j].nb):
            camp_ordi.append(uni[i].name)


#pour calculer le 16
def calculer_valeur_total(uni):
    tt = 0
    for i in range(len(uni)):
        tt += uni[i].nb * uni[i].value
    return tt


#pour afficher: Héro:3 Héro:3 Capitaine:2 ...
def afficher_camp_initial(unites):
    txt = ""
    for i in range(len(unites)):
        if unites[i].nb == 0:
            continue
        texte_descrition = unites[i].nb * (unites[i].name + ":" + str(unites[i].value) + " ")
        txt += texte_descrition
    return txt'''