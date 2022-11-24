#!/bin/bash
# created by Brewal Guyon
# last modification 24-11-22




a="hello"

for i in {0..8}
do
a=$a$a$a$a$a
done

echo taille de la variable : $(echo $a | wc -c)
# cree une variable assez longue, pour faire varier la memoire

for i in {0..10}
do
echo phase $i/10 du script

echo mise en pause du script pendant 60s 
sleep 60

echo changement de la taille de la variable
a=$a$a
echo taille de la variable : $(echo $a | wc -c)
done

