ODS API Management
==================

Outils permettant d'interragir avec l'API Management du portail.
Les éléments principaux sont les classes cOds et cOdMEL.
Ils sont complétés de plusieurs scripts qui utilisent ces classes pour effectuer des traitements sur le portail Open data.

# Classes
## COds
Classe avec un ensemble de méthodes permettant d'interragir avec le portail Open data.
La classe est commentée avec les docstrings utiles permettant de comprendre comment fonctionne chaque méthode.

## cOdMEL
Classe avec un ensemble de méthodes plus spécifiques au portail de la Métropole Européenne de Lille.

# Scripts

## transfertDataset
Permet de transférer un jeu de données d'un portail ODS vers un autre portail.

**Attention, les 2 portails doivent avoir exactement les mêmes métadonnées**

Script créé pour utilisation d'un domaine de test avant passage du dataset en production.

## transfertPage
Permet le transfert d'une page d'un portail ODS vers un autre portail

## transfertList
Fichier de paramétrage des jeux de données et pages à transférer.

## transfertParam
Paramètre des portail ODS à utiliser comme source et destination ainsi que les clé API pour ces 2 portails.

**Attention, les clé API doivent disposer des droits pour l'API Manager ODS**

## utils
Un lot de fonctions utiles. Par exemple pour l'accès à des fichiers

## ftpFunctions
Un lot de fonctions permettant l'accès à un répertoire FTP et la récupération/envoi de fichier vers un FTP.

