#!/usr/bin/env python

class Persona:

    altura=1.81

    def __init__ (self):
      self.altura=1.80
      self.nombre= "Leo"

    def saludo(self, mensaje):
        print(mensaje)

Leo_ =Persona()

Leo_.saludo("hola, buenos dias")

print(Leo_.nombre)

Leo_.nombre="Leopoldo"

print(Leo_.nombre)

Leo_.apellido= "Garcia"

print(Leo_.apellido)

juan = Persona()

print(juan.apellido)