# Surveillance de zone avec placement de caméras

Ce programme permet de déterminer l'angle optimal pour positionner des caméras de surveillance afin de minimiser la surface non couverte dans une zone donnée.

## Dépendances

Pour utiliser ce programme, vous devez installer les bibliothèques suivantes :
```bash
pip install numpy
pip install matplotlib
pip install Shapely
```
## Fonctionnement

Le script génère un diagramme montrant la position et l'orientation optimales des caméras pour minimiser la surface non surveillée dans une zone donnée. Les caméras sont placées à des positions fixes, mais leurs angles peuvent être ajustés.

## Paramètres

- `distance_de_vue` : distance maximale à laquelle la caméra peut voir (en mètres)
- `angle_de_vue` : angle de vision de la caméra (en degrés)
- `terrain_x et terrain_y` : limites de la zone à surveiller en abscisses et ordonnées (en mètres)
- `cam_pos` : liste des positions des caméras (en coordonnées x, y)

## Fonctions

- `place_camera(x, y, angle, distance_de_vue, angle_de_vue)` : calcule les coordonnées des points de la caméra en fonction de sa position et de son angle.
- `print_camera(cam)` : affiche la caméra sur le graphique.
- `set_axes(x, y)` : définit les limites des axes du graphique.
- `objective_function(angle)` : fonction objectif qui calcule la surface non surveillée en fonction des angles de caméra.

Le programme utilise une approche de recherche aléatoire pour optimiser les angles des caméras en minimisant la surface non couverte. Le résultat est affiché sous forme de graphique, avec les numéros des caméras indiqués en rouge.

## Exécution

Exécutez simplement le script Python pour voir le résultat :
```bash
python surveillance.py
```

Le programme générera un graphique montrant la position et l'orientation optimales des caméras pour minimiser la surface non couverte dans la zone définie.
