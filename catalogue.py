"""Module catalogue - Squelette à compléter (soirée 17).

Ce fichier fournit la STRUCTURE des fonctions à écrire : nom, paramètres
et contrat (ce qui entre, ce qui sort). Il ne contient AUCUN algorithme.

Les spécifications complètes (comportement attendu, cas limites, exemples)
figurent dans l'énoncé de l'atelier TP, qui fait seul autorité. Remplacez
chaque « raise NotImplementedError » par votre implémentation.

Aucune fonction ne doit modifier la liste reçue en argument.

Fichier distribué aux étudiants - à compléter.

Programmation Orientée Objet - EICPN 2025-2026.
"""

from collections import defaultdict  # noqa: F401 (utile selon votre choix)


# ──────────────────────────────────────────────────────────────────────
# 1. Tris
# ──────────────────────────────────────────────────────────────────────

def trier_par_titre(livres):
    """Trie une liste de Livre par titre croissant.
    Args:
        livres (list): Liste de Livre à trier.

    Returns:
        list: Une nouvelle liste triée (l'originale reste intacte).
    """
    def trier_par_titre(livres):
        
        def obtenir_titre(livre):
         return livre.titre

        return sorted(livres, key=obtenir_titre)


def trier_par_auteur_puis_titre(livres):
    """Trie par auteur, puis par titre à auteur égal.

    Args:
        livres (list): Liste de Livre à trier.

    Returns:
        list: Une nouvelle liste triée.
    """
    return sorted(livres, key=lambda livre: (livre.auteur, livre.titre))
    


def trier_par_annee(livres, recents_dabord=False):
    """Trie par année de publication.

    Args:
        livres (list): Liste de Livre à trier.
        recents_dabord (bool): Si True, les plus récents en premier.

    Returns:
        list: Une nouvelle liste triée.
    """
    return sorted(livres,
                  key=lambda livre: livre.annee,
                  reverse=recents_dabord)


def trier_par_auteur_puis_annee_recente(livres):
    """Trie par auteur croissant, puis par année décroissante.

    Args:
        livres (list): Liste de Livre à trier.

    Returns:
        list: Une nouvelle liste triée.
    """
    return sorted(
        livres,
        key=lambda livre: (livre.auteur, -livre.annee)
    )


# ──────────────────────────────────────────────────────────────────────
# 2. Recherches
# ──────────────────────────────────────────────────────────────────────

def rechercher_par_auteur(livres, auteur):
    """Retourne tous les livres d'un auteur donné.

    Args:
        livres (list): Liste de Livre.
        auteur (str): Nom d'auteur recherché.

    Returns:
        list: Les Livre correspondants (liste éventuellement vide).
    """
    return list(filter(lambda livre: livre.auteur == auteur, livres))
   


def rechercher_par_isbn(livres, isbn):
    """Retrouve un livre par son ISBN en parcourant la liste.

    Args:
        livres (list): Liste de Livre.
        isbn (str): ISBN recherché.

    Returns:
        Livre: Le livre correspondant, ou None s'il est absent.
    """
    for element in livres:
       
        if element.isbn == isbn:
            return element 
            
    
    return None
            

# ──────────────────────────────────────────────────────────────────────
# 3. Ensembles
# ──────────────────────────────────────────────────────────────────────

def compter_distincts(livres):
    """Compte le nombre de livres distincts.

    Args:
        livres (list): Liste de Livre, doublons éventuels.

    Returns:
        int: Nombre de livres distincts.
    """
    uniques = set((l.isbn, l.titre) for l in livres)
    return len(uniques)

def dedoublonner(livres):
    """Supprime les doublons en conservant l'ordre de première apparition.

    Args:
        livres (list): Liste de Livre, doublons éventuels.

    Returns:
        list: Liste sans doublon, ordre de première apparition préservé.
    """
    liste_sans_doublon = []
    cles_vues = set() 
    
    for livre in livres:
        # On crée une clé unique combinant l'ISBN et le titre
        cle_unique = (livre.isbn, livre.titre)
        
        if cle_unique not in cles_vues:
            cles_vues.add(cle_unique)
            liste_sans_doublon.append(livre)
            
    return liste_sans_doublon


# ──────────────────────────────────────────────────────────────────────
# 4. Dictionnaires
# ──────────────────────────────────────────────────────────────────────

def indexer_par_isbn(livres):
    """Construit un index {isbn: livre}.

    Args:
        livres (list): Liste de Livre.

    Returns:
        dict: Dictionnaire {isbn (str): livre (Livre)}.
    """
    raise NotImplementedError("À compléter (voir énoncé TP, exercice 6).")


def regrouper_par_auteur(livres):
    """Regroupe les livres par auteur.

    Args:
        livres (list): Liste de Livre.

    Returns:
        dict: Dictionnaire {auteur (str): [Livre, ...]}.
    """
    raise NotImplementedError("À compléter (voir énoncé TP, exercice 6).")


if __name__ == "__main__":
    print("Squelette non implémenté : complétez les fonctions, "
          "puis lancez la suite de tests.")
