---
title: "TP : Algorithmes génétiques"
author: Pierre VASLIN
date: 5 janvier 2021
geometry: margin=2.5cm
output: 
    pdf_document:
        fig_caption: yes
header-includes:
- | 
    ```{=latex}
    \usepackage{amsmath,amsfonts,euscript,tikz,fancyhdr,float}
    \floatplacement{figure}{H}
    ```
---

## Introduction
Pour résoudre le problème de recherche de mot de passe, j'ai réalisé une 3 implémentations différentes comportant des variante dans la manière de résolution du problème. Chaque partie décrira chaque implémentation en parallèle et la dernière partie analysera les différence entre les différentes implémentations avec leurs hyper-paramètre.
Un individu correspond à une tentative de mot de passe, son phénotype étant une chaîne de de 12 à 18 chiffre et lettres majuscules

## Codage du génotype
Pour génotype de la première implémentation, j'ai choisi d'utiliser un codage des caractères en nombres binaires. Le nombre de caractère à encoder en binaire est de 36 caractères soit les caractères de A à Z, de 0 à 9 et le caractère vide. La présence du caractère vide est justifié pour faire varier le nombre de caractère composant le mot de passe dans notre cas le mot de passe est composé entre 12 et 18 caractères. On encode les caractères avec 6 bits. Pour la conversion en phénotype, on utilisera donc une table d'équivalence.

Pour l'implémentation 2, le génotype est un tableau contenant les caractères composant un mot de passe c'est à dire les lettres de A à Z, de 0 à 9 et le caractère vide. Pour passer du génotype au phénotype, on fera une conversion de la liste de caractère en chaine de caractère.

Le génotype de l'implémentation 3 est une variante de celui de l'implémentation 2, on enlève seulement le caractère vide parmi les valeur possible dans le tableau de caractère. Nous verrons par la suite que le nombre de caractère composant un mot de passe variera par mutation.

## La sélection (et la présence ou non d'élitisme)
Pour les différentes implémentation, il est possible d'exécuter le l'algorithme génétique avec le programme avec une sélection:
* linéaire par le rang, sans élitisme
* exponentielle par le rang
En faisant varier C on peut avoir une sélection plus ou moins élitiste. La variable C fera donc partie des hyper-paramètres des l'algorithme génétique implémentés. Pour les trois implémentations, on utilisera la sélection exponentielle par le rang qui offrira plus de paramétrage.

## Les mutations
Pour la première implémentation, la fonction de mutation change la valeur d'un bit présent dans un génotype aléatoirement de 0 à 1 ou de 1 à 0. Chaque bit à une probabilité $\mu$ de muter et on réalise une seule mutation par génotype.

La seconde implémentation, possède une fonction de mutation qui fait changer la valeur d'un caractère en un caractère aléatoire parmi ceux potentiellement présent dans le mot de passe soit les caractères de A à Z, de 0 à 9 et le caractère vide.

La troisième implémentation possède 7 fonctions différentes de mutation. Pour chaque génotype on réalise une mutation avec une probabilité de $mu$.
On va maintenant énumérer les différentes mutations et leur probabilité:
1. Mutation aléatoire (probabilité 2/8): On change la valeur d'un caractère aléatoirement.
2. Mutation réduction de taille du génotype (probabilité 1/8): On enlève aléatoirement un caractère dans le génotype si le nombre de caractère est supérieur à 12 caractères.
3. Mutation agrandissement (probabilité 1/8): On ajoute un caractère aléatoire à une position aléatoire.
4. Mutation échange (probabilité 1/8): Intervertie de place deux caractères aléatoirement présent dans le génotype.
5. Mutation replace (probabilité 1/8): On retire aléatoirement une élément dans le génotype et on ajoute un caractère à une position aléatoire.
6. Mutation décalage à droite (probabilité 1/8): On supprime le génome situé à la fin du génotype et on rajoute un caractère aléatoire en première position.
7. Mutation décalage à gauche (probabilité 1/8): On supprime le génome situé au début du génotype et on rajoute un caractère aléatoire en dernière position.

## Le cross-over
Pour la première et la seconde implémentation un cross-over se fait par caractère de 1 à N-1 caractères par cross-over.

Pour l'implémentation 2 et 3, on échange un nombre de caractère aléatoire entre deux parents.

## Les valeurs des hyper-paramètre (nombre d'individu, taux de mutation, etc.)
### Étude de la première implémentation
La première exécution, on obtient :

![nb agent:100, nb gen:50, proba co:0.6, proba mutation:0.5](./img/version1.png){width=75%}

![nb agent:100, nb gen:50, proba co:0.2, proba mutation:0.4](./img/version1_b.png){width=75%}

On constate avec c'est deux graphiques que les agents ne tendent pas vers une solution proche ou égale au mot de passe cherché. En réalisant plusieurs autres exécutions en faisant varier les paramètres, on ne temps pas plus vers une solution stable, dû peut-être à une probabilité de mutation trop haute.

![nb agent:100, nb gen:100, proba co:0.3, proba mutation:0.2](./img/version1_c.png){width=75%}

Après implémentation de la sélection exponentiel par rang, on n'a pas de meilleur résultat comme peut nous le monter le graphique suivant.

![nb agent:1000, nb gen:100, proba co:0.2, proba mutation:0.8, c:0.5](./img/version1_dE.png){width=75%}

Les résultats ne sont pas bon, c'est pourquoi j'ai réalisé une seconde implémentation avec un génotype différent décrit précédemment.

### Étude de la seconde implémentation





#### Note personnel
Une classe individu
    -def mutation
    -def evaluation

le phénotype est une chaine de caractère entre 12 et 18 caractères
le génotype contient une chaine de caractère codé

codage en code ascii

operateur de mutation

cross over

pc =  proba cross over
$\mu$ = proba mutation by bit

codage de gray pour les 




Après

* plusieurs cross-over et plusieurs mutation
* random sur les mutations
* Pas gerer les caractères vide, le faire qu'a la création
* lors du cross-over faire des changements d'ordre
* faire une mutation qui enlève ou supprime un caractère
* Au pire : Après avoir atteind 0.90, on selectionne le mdp qui atteind 0.90, on peut faire du brut force

Implementation 1:
500,1500,0.1,0.4,0.99,5

Implementation 
good param 500,1500,0.1,0.1,0.98,5
Implementation 2:
good param 500,1500,0.1,0.2,0.98,5
500,1500,0.2,0.2,0.98,5

Implementaion 3:
500,1500,0.1,0.4,0.98,5s

Pour le numéo étudiant 11914433,  le mdp est XDLEV31N4RD32
