class ArbreBinaire:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfant_gauche = None
        self.enfant_droit = None

    def insert_gauche(self, valeur):
        if self.enfant_gauche == None:
            self.enfant_gauche = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
            new_node.enfant_gauche = self.enfant_gauche
            self.enfant_gauche = new_node

    def insert_droit(self, valeur):
        if self.enfant_droit == None:
            self.enfant_droit = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
            new_node.enfant_droit = self.enfant_droit
            self.enfant_droit = new_node

    def get_valeur(self):
        return self.valeur

    def get_gauche(self):
        return self.enfant_gauche

    def get_droit(self):
        return self.enfant_droit


#######fin de la classe########

######début de la construction de l'arbre binaire###########

racine = ArbreBinaire(15)
racine.insert_gauche(6)
racine.insert_droit(18)

b_node = racine.get_gauche()
b_node.insert_gauche(3)
b_node.insert_droit(7)

c_node = b_node.get_gauche()
c_node.insert_gauche(2)
c_node.insert_droit(4)

d_node = b_node.get_droit()
d_node.insert_droit(13)

e_node = d_node.get_droit()
e_node.insert_gauche(9)

f_node = racine.get_droit()
f_node.insert_gauche(17)
f_node.insert_droit(20)


######fin de la construction de l'arbre binaire###########

######debut###############
def affiche(T):
    if T is not None:
        return (T.get_valeur(), affiche(T.get_gauche()), affiche(T.get_droit()))


def hauteur(T):
    if T is not None:
        if T.get_droit() is not None and T.get_gauche() is not None:
            return 1 + max(hauteur(T.get_gauche()), hauteur(T.get_droit()))
        elif T.get_droit() is not None:
            return 1 + hauteur(T.get_droit())
        elif T.get_gauche() is not None:
            return 1 + hauteur(T.get_gauche())
        else:
            return 1


def taille(T):
    if T is not None:
        if T.get_droit() is not None and T.get_gauche() is not None:
            return 1 + taille(T.get_gauche()) + taille(T.get_droit())
        elif T.get_droit() is not None:
            return 1 + taille(T.get_droit())
        elif T.get_gauche() is not None:
            return 1 + taille(T.get_gauche())
        else:
            return 1


def parcours_infixe(T):
    if T is not None:
        if T.get_gauche() is not None:
            parcours_infixe(T.get_gauche())
        if T.get_valeur() is not None:
            print(T.get_valeur())
        if T.get_droit() is not None:
            parcours_infixe(T.get_droit())


def parcours_prefixe(T):
    if T is not None:
        if T.get_valeur() is not None:
            print(T.get_valeur())
        parcours_prefixe(T.get_gauche())
        parcours_prefixe(T.get_droit())


def parcours_suffixe(T):
    if T is not None:
        parcours_suffixe(T.get_gauche())
        parcours_suffixe(T.get_droit())
        if T.get_valeur() is not None:
            print(T.get_valeur())


def parcours_largeur(T):
    f = [T]
    while len(f) > 0:
        x = f.pop(0)
        if x is not None:
            print(x.get_valeur())
        if x.get_gauche() is not None:
            Tg = x.get_gauche()
            f.append(Tg)
        if x.get_droit() is not None:
            Td = x.get_droit()
            f.append(Td)


def arbre_recherche(T, k):
    if T is None:
        return False
    if k == T.get_valeur():
        return True
    if k < T.get_valeur():
        return arbre_recherche(T.get_gauche(), k)
    else:
        return arbre_recherche(T.get_droit(), k)


def arbre_recherche_ite(T, k):
    if T is not None:
        x = T
        while T is not None and k != x.get_valeur():
            x = T
            if k < x.get_valeur():
                T = x.get_gauche()
            else:
                T = x.get_droit()
        if k == x.get_valeur():
            return True
        else:
            return False


def arbre_insertion(T, y):
    if T is not None and y is not None:
        x = T
        while T is not None:
            x = T
            if y < x.get_valeur():
                T = x.get_gauche()
            else:
                T = x.get_droit()
        if y < x.get_valeur():
            x.insert_gauche(y)
        else:
            x.insert_droit(y)


print(parcours_largeur(racine))
