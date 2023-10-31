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
- elles calculent leurs score total,        OK !
- elles affichent leur score total,         OK !
- elles affichent les pions dans l'armée    OK !

"""
class Armee:
    def __init__(self, name, pions):
        self.name = name
        self.pions = pions
        """self.hero = hero
        self.captain = captain
        self.soldier = soldier"""

    def CalculerValeurTotal(self):
        tt = 0
        for i in range(len(self.pions)):
            tt += self.pions[i].nb * self.pions[i].value
        return tt

    def AfficherPionsDansArmee(self):
        txt = ""
        for i in range(len(self.pions)):
            if self.pions[i].nb == 0:
                continue
            texte_descrition = self.pions[i].nb * (self.pions[i].name + ":" + str(self.pions[i].value) + " ")
            txt += texte_descrition
        return txt


# Entités des pions
hero = Unite("Héro", 3, 3)
captain = Unite("Capitaine", 2, 3)
soldier = Unite("Soldat", 1, 1)

# Entités des camps
armee_ordi = Armee("Armée de l'ordi:", [hero, captain, soldier])
armee_joueur = Armee("Armée du joueur:", [])

# lancement des méthodes
score_tt_ordi = armee_ordi.CalculerValeurTotal()
description_pions_ordi = armee_ordi.AfficherPionsDansArmee()
score_tt_joueurs = armee_joueur.CalculerValeurTotal()
description_pions_joueur = armee_joueur.AfficherPionsDansArmee()

# ce qui s'affichera sur le terminal:
print(armee_ordi.name, score_tt_ordi, description_pions_ordi)
print(armee_joueur.name, score_tt_joueurs, description_pions_joueur)
