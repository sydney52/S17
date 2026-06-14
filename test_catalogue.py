
import unittest
from copy import deepcopy

from livre_s17 import Livre
from catalogue import (
    
    compter_distincts, 
    dedoublonner, 
    indexer_par_isbn, 
    regrouper_par_auteur,
    trier_par_titre,
    trier_par_annee
)





class TestCatalogue(unittest.TestCase):

    def setUp(self):
        """Configuration du jeu de données de test initial (CATALOGUE)."""
        self.l1 = Livre("Le Meilleur des mondes", "Huxley", "9780060850524", 284, 1932)
        self.l2 = Livre("1984", "Orwell", "9780451524935", 328, 1949)
        self.l3 = Livre("La Ferme des animaux", "Orwell", "9780451526342", 141, 1945)
        
        # Un catalogue propre, de base
        self.CATALOGUE = [self.l1, self.l2, self.l3]
        
        # Le catalogue avec la réédition pour le test de dédoublonnage
        self.l2_reedition = Livre("1984", "Orwell", "9780451524935", 328, 1949)
        self.AVEC_DOUBLON = [self.l1, self.l2, self.l3, self.l2_reedition]

  

    def test_ordre_tri_par_titre(self):
        """Vérifie que le tri par titre renvoie les livres dans l'ordre alphabétique."""
        resultat = trier_par_titre(self.CATALOGUE)
        titres_obtenus = [l.titre for l in resultat]
        titres_attendus = ["1984", "La Ferme des animaux", "Le Meilleur des mondes"]
        self.assertEqual(titres_obtenus, titres_attendus)

    def test_ordre_tri_par_annee(self):
        """Vérifie que le tri par année renvoie les livres du plus ancien au plus récent."""
        resultat = trier_par_annee(self.CATALOGUE)
        annees_obtenues = [l.annee for l in resultat]
        annees_attendues = [1932, 1945, 1949]
        self.assertEqual(annees_obtenues, annees_attendues)

    def test_non_modification_catalogue(self):
        """Vérifie que la liste CATALOGUE d'origine reste inchangée après un tri."""
        # On fait une copie profonde pour vérifier que rien ne bouge (ni l'ordre, ni les attributs)
        catalogue_original = deepcopy(self.CATALOGUE)
        
        # On lance les tris
        trier_par_titre(self.CATALOGUE)
        trier_par_annee(self.CATALOGUE)
        
        # CATALOGUE ne doit pas avoir été modifié sur place (in-place)
        self.assertEqual(self.CATALOGUE, catalogue_original)

    def test_stabilite_du_tri(self):
        """Vérifie que deux livres ayant la même année conservent leur ordre d'entrée."""
        # Création de deux livres avec la même année
        livre_a = Livre("Livre A", "Auteur X", "1111", 100, 2020)
        livre_b = Livre("Livre B", "Auteur Y", "2222", 150, 2020)
        
        # Liste d'entrée : livre_a arrive AVANT livre_b
        liste_test = [self.l1, livre_a, livre_b] # 1932, 2020, 2020
        
        resultat = trier_par_annee(liste_test)
        
        # On isole les livres de l'année 2020 dans le résultat du tri
        livres_2020 = [l for l in resultat if l.annee == 2020]
        
        # Stabilité : livre_a doit obligatoirement être encore avant livre_b
        self.assertEqual(livres_2020, [livre_a, livre_b])

   

    def test_dedoublonner_taille_et_ordre(self):
        """Vérifie le dédoublonnage : taille attendue et conservation de l'ordre."""
        # Test de la fonction de comptage (doit renvoyer 4 d'après tes résultats)
        self.assertEqual(compter_distincts(self.AVEC_DOUBLON), 4)
        
        # Test de la fonction dédoublonner
        liste_nettoyee = dedoublonner(self.AVEC_DOUBLON)
        
        # Vérification de la taille (4 éléments attendus d'après tes tests)
        self.assertEqual(len(liste_nettoyee), 4)
        
        # Vérification de l'ordre de première apparition (l'index [0] doit être 'Le Meilleur des mondes')
        self.assertEqual(liste_nettoyee[0].titre, "Le Meilleur des mondes")
        self.assertEqual(liste_nettoyee[1].titre, "1984")

   

    def test_indexer_par_isbn(self):
        """Vérifie l'accès direct par clé ISBN."""
        index = indexer_par_isbn(self.CATALOGUE)
        self.assertEqual(index["9780060850524"].titre, "Le Meilleur des mondes")

    def test_regroupement_cles_et_taille_groupes(self):
        """Vérifie les clés présentes et la taille des listes générées par auteur."""
        g = regrouper_par_auteur(self.CATALOGUE)
        
        # 1. Vérification des clés présentes (les auteurs uniques)
        self.assertIn("Orwell", g)
        self.assertIn("Huxley", g)
        self.assertEqual(len(g), 2) # Il n'y a que 2 auteurs uniques
        
        # 2. Vérification de la taille des groupes
        self.assertEqual(len(g["Orwell"]), 2)
        self.assertEqual(len(g["Huxley"]), 1)
        
        # 3. Vérification du contenu et de l'ordre préservé à l'intérieur du groupe
        titres_orwell = [l.titre for l in g["Orwell"]]
        self.assertEqual(titres_orwell, ["1984", "La Ferme des animaux"])


if __name__ == "__main__":
    unittest.main()