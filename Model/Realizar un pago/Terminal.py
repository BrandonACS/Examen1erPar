#!/usr/bin/python
#-*- coding: utf-8 -*-

from datetime import date
from pago import pago


class Terminal:
    def __init__(self,num_t,saldo,dueño):
        self.num_t = num_t
        self.saldo = saldo
        self.dueño = dueño

    def corroborar(self ):
        print("corroborando tarjeta")

    def leerTarjeta(self ):
        print("leyendo tarjeta")

    def cobro(self, c):
        return pago(c,date.today(),self.dueño)
        

