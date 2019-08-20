#!/bin/python3

from random import choice

#crea una lista de jugadores desde un archivo
jugadores = []
file = open('jugadores.txt', 'r')
jugadores = file.read().splitlines()
print('Jugadores:', jugadores)

#crea una lista de nombres de equipo desde un archivo
nombresEquipos = []
file = open('nombresEquipos.txt', 'r')
nombresEquipos = file.read().splitlines()
print('Nombres equipos:', nombresEquipos)

#crea listas de equipos vacías
equipoA = []
equipoB = []

#el bucle se ejecuta hasta que no queden jugadores
while len(jugadores) > 0:
  
  #elige un jugador aleatorio para el equipo A
  jugadorA = choice(jugadores)
  equipoA.append(jugadorA)
  #elimina el jugador de la lista de jugadores
  jugadores.remove(jugadorA)
  
  #sal del bucle si no quedan jugadores
  if jugadores == []: 
    break
  
  #elige un jugador aleatorio para el equipo B
  jugadorB = choice(jugadores)
  equipoB.append(jugadorB)
  #elimina el jugador de la lista de jugadores
  jugadores.remove(jugadorB)

#elige al azar los nombres para los 2 equipos
nombreEquipoA = choice(nombresEquipos)
nombresEquipos.remove(nombreEquipoA)
nombreEquipoB = choice(nombresEquipos)
nombresEquipos.remove(nombreEquipoB)

#imprime los equipos
print('\nAqui tienes tus equipos:\n')
print(nombreEquipoA, equipoA)
print(nombreEquipoB, equipoB)