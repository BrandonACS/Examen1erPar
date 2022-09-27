#!/usr/bin/python
#-*- coding: utf-8 -*-

class pago:
    def __init__(self,total,fecha,nombre):
        self.total = total
        self.fecha = "",fecha
        self.nom = nombre

    def cobrar(self ):
        print("Cobrando")

    def guardar(self ):
        print("guargo en servidor")

    def mostrar_tiket(self, p):
        print("Su cobro es de:",p)

