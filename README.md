# RaspberyCode
La carte de développement Pico Breadboard
La carte de développement Pico Breadboard de la société SB Components est une carte polyvalente composée d'une plaquette à trous pour du cablâge, d'un buzzer, de 4 LED et de 4 boutons-poussoirs. SB Components a développé ce kit pour aider les utilisateurs à prototyper des projets avec le Raspberry Pi Pico de manière efficace. Le schéma électrique de cette carte est disponible [ici](schema.pdf).


[1)](codage_en_4bit.py) On utilise 3 LED câblées (LED2 à LED4) et un bouton-poussoir. Réaliser un programme afin que lorsqu'on appuie sur le bouton-poussoir, on obtienne le nombre d'appuis en binaire sur les 3 LED. Le nombre binaire est remis à 0 au 8ème appui. Une temporisation est utilisée pour ignorer le phénomène de rebond de l'interrupteur.

[2)]() On désire réaliser un programme permettant de faire clignoter une LED, à diverses fréquences. Les autres diodes sont éteintes. Le programme démarre sur un appui d'un bouton-poussoir et la diode clignote à 1 Hz pendant 3 secondes. Un second appui sur le même bouton-poussoir, la diode clignote à 2 Hz pendant 3 secondes. Un troisième appui, la diode clignote à la fréquence de 4 Hz pendant 3 secondes. Un quatrième appui, la diode clignote à la fréquence de 8 Hz pendant 3 secondes. Un cinquième appui, on revient à la situation de départ où la diode clignote à 1 Hz pendant 3 secondes, et ainsi de suite... Le temps où la diode est allumée est égal au temps où la diode est éteinte. Une temporisation est utilisée pour ignorer le phénomène de rebond de l'interrupteur.

[3)]() En utilisant les 4 LED, réaliser un chenillard qui démarre dès le début du programme de la droite vers la gauche, et retour pour recommencer. L'appui sur un bouton-poussoir provoque un changement du sens de rotation, maintenant de la gauche vers la droite et retour. Un nouvel appui sur le bouton-poussoir provoque un changement de sens, de la droite vers la gauche et retour. Et ainsi de suite …
Bref à chaque appui sur le bouton-poussoir, le sens de décalage change! Une diode reste allumée 500 ms, et le changement de sens se fait à la fin d'une séquence de décalage soit sur le passage de LED4 à LED1 ou sur le passage de LED1 à LED4, avant de redémarrer dans le nouveau sens.

[4]() Réaliser un programme permettant de réaliser 3 fonctions logiques. F1, F2 et F3 sont visualisées respectivement sur les LED1, LED2 et LED3. LED4 reste éteinte. Les 2 variables binaires a et b sont réalisées grâce à 2 boutons-poussoirs. F1 est un ET logique, F2 est un OU logique et F3 est un OU exclusif inversé.
