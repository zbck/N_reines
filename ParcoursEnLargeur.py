# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:30:54 2016

@author: emacedegastines
"""
    

from Fonctions import Fonctions

class ParcoursEnLargeur(Fonctions):
        
    def parcoursEnLargeurRec( listeSolution, i, n ):
        ''' fonction récursive pour le parcours en largeur
        - listeSolution : liste de solutions partielles 
        - i : nombre de ligne déjà remplies à l'entrée de la fonction 
        - n : taille de l'échiquier '''
        nouvelleListeSolution = []
        #parcourt la collection des solutions partielles
        for L in listeSolution:
            #pour chaque solution partielle, vérifie si l'ajout d'une reine marche toujours
            for j in range( n ):
                L.append( j )
                if Fonctions.test2( L, i + 1, i ):
                    #Si l'ajout d'une reine marche, l'ajoute a la collection
                    nouvelleListeSolution.append( list(L) )
                L.pop(i)
                
        #Si on n'est pas encore à la dernière ligne, ajoute une nouvelle reine
        if i < n :
            return ParcoursEnLargeur.parcoursEnLargeurRec( nouvelleListeSolution, i + 1, n ) 
        return listeSolution
    
    
        
    def algorithme(n):
        ''' parcourt le graphe en largeur pour chercher les solutions
        - n : taille de l'échiquier '''
        return( ParcoursEnLargeur.parcoursEnLargeurRec( [[]], 0, n ) )

    algorithme = staticmethod(algorithme)
    parcoursEnLargeurRec = staticmethod(parcoursEnLargeurRec)
    
