BART Sébastien / KROL Mikolaï / ELABDALLAH Mohammed

Projet labyrinthe


*---Construire «à la main» des labyrinthes de dimension données------------------------------------------------------------------------------------*

 -script handmade_maze.py

Dans un interpreteur python:
	Utiliser la fonction handmade_maze.
	Elle vous demandera les dimensions de votre labyrinthe, et pour chaque chaque case vous demandera quels murs vous voulez placer, il faudra repondre 'o' pour oui, ou 		'n' pour non.
	La fonction renvoit un objet de type Maze.
Dans un terminal:
	Taper la commande suivante:
	$ python3 handmade_maze.py handmade_maze 
	Même fonctionnement que dans un interpreteur ensuite.


*---Construire des labyrinthes décrits dans des fichiers texte--------------------------------------------------------------------------------------*

 -script txt_to_maze.py

Dans un interpreteur python:
	Utiliser la fonction file_to_maze.
	Cette fonction prend en paramètre une chaine de caractère étant le nom d'un fichier se trouvant dans le dossier txt.
	Exemple: file_to_maze('maze_6_4_1.txt')
	La fonction renvoie un objet de type Maze.


*---Construire des labyrinthes parfaits aléatoires de dimension données------------------------------------------------------------------------------*

 -script perfect_maze.py

Dans un interpreteur python:
	Utiliser la fonction perfect_maze.
	Cette fonction prend en paramètre 2 entiers qui sont respectivement la largeur et la hauteur du labyrinthe souhaité.
	Exemple: perfect_maze(15,10)
	La fonction renvoie un objet de type Maze.


*---Trouver, s’il en existe, un chemin d’un point du labyrinthe à un autre----------------------------------------------------------------------------*

 -méthode solve de la classe Maze

 Exemple: soit maze un objet de type Maze, maze.solve() renverra:
	-l'objet maze avec le chemin affiché s'il il existe (si il y a plusieurs chemins un seul sera aléatoirement affiché)
	-"No solution..." si il n'existe pas de chemin


*---Écrire la description d’un labyrinthe dans un fichier .txt-----------------------------------------------------------------------------------------*

 -méthode to_txt de la classe Maze

 La méthode prend en paramètre une chaine de caractères étant le nom du fichier dans lequel on veut écrire.
 Exemple: soit maze un objet de type Maze, maze.to_txt('essai.txt') va créer un fichier essai.txt et y écrire la description de maze.


*---Interface graphique--------------------------------------------------------------------------------------------------------------------------------*

 -script interface.py

 L'interface permet d'afficher des labyrinthes faits à la main étape par étape ou des labyrinthes parfaits, et afficher si on le souhaite leur solution.
 Dans un terminal:
	taper la commande suivante:
		$ python3 interface.py width height type (en remplaçant width et height par des entiers et type par perfect ou handmade)
	L'interface va se lancer et afficher le labyrinthe, il vous sera alors demandé si vous voulez afficher la solution (dans le terminal)
	Il faudra répondre 'o' pour oui et 'n' pour non.

-------------------------------------------------------------------------------------------------------------------------------------------------------*

Nos fonctions de génèration et construction de labyrinthes fonctionnent pour toutes les dimensions.
Notre fonction de résolution de labyrinthes fonctionne dans les 3 cas:
	-si il y a un chemin unique
	-si il y a plusieurs chemins (un seul sera affiché aléatoirement)
	-si il n'y a pas de solutions
Notre fonction de génèration de labyrinthes à partir de fichiers textes fonctionnent pour tous les fichiers contenues dans l'archive qui nous a été fournie.
Notre fonction qui écrit la description d'un labyrinthe dans un fichier txt fonctionne pour tous les labyrinthes.

Aucun problème à signaler.
