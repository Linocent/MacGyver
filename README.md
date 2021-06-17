# MacGyver
***

## Cahier des charges

### Fonctionnalités:
* Il n'y a qu'un seul niveau. La structure (départ, emplacement des murs, arrivée), devra être enregistrée dans un fichier pour la modifier facilement au besoin.
* MacGyver sera contrôlé par les touches directionnelles du clavier.
* Les objets seront répartis aléatoirement dans le labyrinthe et changeront d’emplacement si l'utilisateur ferme le jeu et le relance.
* La fenêtre du jeu sera un carré pouvant afficher 15 sprites sur la longueur.
* MacGyver devra donc se déplacer de case en case, avec 15 cases sur la longueur de la fenêtre !
* Il récupèrera un objet simplement en se déplaçant dessus.
* Le programme s'arrête uniquement si MacGyver a bien récupéré tous les objets et trouvé la sortie du labyrinthe. S'il n'a pas tous les objets et qu'il se présente devant le garde, il meurt (la vie est cruelle pour les héros).
* Le programme sera standalone, c'est-à-dire qu'il pourra être exécuté sur n'importe quel ordinateur.

### Livrables:
* Programme hébergé par Github,
* Document texte expliquant votre démarche et comprenant le lien vers votre code source (sur Github). Développez notamment le choix de l'algorithme. Expliquez également les difficultés rencontrées et les solutions trouvées. Le document doit être en format pdf et ne pas excéder 2 pages A4.

### Contraintes:
* Vous versionnerez votre code en utilisant Git et le publierez sur Github pour que votre mentor puisse le commenter,
* Vous respecterez les bonnes pratiques de la PEP 8 et développerez dans un environnement virtuel utilisant Python 3,
* Votre code devra être écrit en anglais : nom des variables, commentaires, fonctions...

## Comment jouer?

* D'abord il faut cloner et télécharger le repo.
* Construire un environnement virtuel et installer les modules du fichier requirements.txt à l'aide de la commande suivante:
_pip install -r requirements.txt_
* Lancer game.py et amusez-vous!
