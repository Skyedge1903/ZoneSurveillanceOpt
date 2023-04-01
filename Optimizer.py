import numpy as np
import matplotlib.pyplot as plt
import math
import shapely


def place_camera(x, y, angle, distance_de_vue, angle_de_vue):
    # Point d'origine de la caméra
    camera = (x, y)

    # Calcul des coordonnées des points de la caméra
    angle_1 = angle + angle_de_vue / 2
    angle_2 = angle - angle_de_vue / 2
    x1 = x + distance_de_vue * math.cos(math.radians(angle_1))
    y1 = y + distance_de_vue * math.sin(math.radians(angle_1))
    x2 = x + distance_de_vue * math.cos(math.radians(angle_2))
    y2 = y + distance_de_vue * math.sin(math.radians(angle_2))
    point_1 = (x1, y1)
    point_2 = (x2, y2)

    return camera, point_1, point_2


def print_camera(cam):
    # on ajoute la caméra (on utilise la fonction fill)
    # on tire une couleur aléatoire
    color = np.random.rand(3, )
    plt.fill([cam[0][0], cam[1][0], cam[2][0]], [cam[0][1], cam[1][1], cam[2][1]], color=color, alpha=0.5)


def set_axes(x, y):
    # on souhaite que le figure ne soit pas déformée
    plt.axis('equal')
    # on définit les limites des axes
    plt.xlim(x)
    plt.ylim(y)


# mes caméras ont toutes une distance de vue de 10 et un angle de vue de 90
# l'espace que je souhaite surveiller est de 0 à 10 en x et de 0 à 10 en y

distance_de_vue = 25
angle_de_vue = 90

terrain_x, terrain_y = (0, 35), (0, 80)

# position possible des caméras que je veux placer
cam_pos = [(17.5, 15), (17.5, 40), (17.5, 65), (17.5, 15), (17.5, 40), (17.5, 65), (17.5, 15), (17.5, 40), (17.5, 65), (17.5, 40)]
nb_cameras = len(cam_pos)


# on cherche également à trouver quel est le meilleur angle pour chaque caméra
# on va donc chercher à minimiser la surface de l'espace non surveillé
# on utilise la fonction minimize de scipy.optimize

def objective_function(angle):
    # on calcule la surface de l'espace non surveillé
    # on commence par créer un polygone représentant l'espace à surveiller
    terrain = shapely.geometry.Polygon([(terrain_x[0], terrain_y[0]), (terrain_x[0], terrain_y[1]),
                                        (terrain_x[1], terrain_y[1]), (terrain_x[1], terrain_y[0])])
    surface = terrain.area

    for n, i in enumerate(angle):
        # on place les caméras
        cam = place_camera(cam_pos[n][0], cam_pos[n][1], i, distance_de_vue, angle_de_vue)
        # on calcule les coordonnées des points de la caméra
        cam = shapely.geometry.Polygon([(cam[0][0], cam[0][1]), (cam[1][0], cam[1][1]), (cam[2][0], cam[2][1])])
        # on calcule la surface de l'espace non surveillé
        terrain = terrain.difference(cam)

    # on retourne la surface de l'espace non surveillé
    return (terrain.area / surface) * 100


points = [([0] * nb_cameras, objective_function([0] * nb_cameras))]

for n in range(10000):
    for i in range(2):
        # on tire un point aléatoire
        p = np.random.randint(0, len(points))
        # on fait une mutation d'un seul paramètre à la fois
        p = points[p][0]
        for j in range(len(p)):
            new = p.copy()
            new[j] += np.random.randint(-180, 180)
            if j + 1 < len(p):
                new[j + 1] += np.random.randint(-180, 180)
            # on ajoute le nouveau point
            points.append((new, objective_function(new)))

    # on trie les points et on garde 30% des meilleurs
    points = sorted(points, key=lambda x: x[1])
    points = points[:int(len(points) * 0.3)]

    print(points[0])

best_angle = points[0]

# on affiche les caméras
for i, cam in enumerate(cam_pos):
    cam_points = place_camera(cam[0], cam[1], best_angle[0][i], distance_de_vue, angle_de_vue)
    print_camera(cam_points)

# on affiche les numéros des caméras
for i, cam in enumerate(cam_pos):
    plt.text(cam[0], cam[1], str(i), fontsize=20, color='red')
set_axes(terrain_x, terrain_y)
plt.show()
