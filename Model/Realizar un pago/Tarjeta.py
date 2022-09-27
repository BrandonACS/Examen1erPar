#!/usr/bin/python
#-*- coding: utf-8 -*-

class Tarjeta:
    def __init__(self,num,fecha,cvv):
        self.num_tar = num
        self.Fecha_vencimiento = fecha
        self.cvv = cvv

    def getNumT(self):
        return self.num_tar

    def getDate(self):
        return self.Fecha_vencimiento

    def getCvv(self):
        return self.cvv

