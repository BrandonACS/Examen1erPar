from Tarjeta import Tarjeta
from Terminal import Terminal

tar=Tarjeta("5111312568916326","26/03",511)
term=Terminal("9133162432659961",5000,"Brandon")

print("ingresando su tarjeta")
term.leerTarjeta()
term.corroborar()
print("Su tarjeta es:",tar.getNumT(),"\n Su fecha de vencimiento:",tar.getDate(),"\n cvv:",tar.getCvv())
p=term.cobro(300)
print("datos de terminal\n num_tarjeta:",term.num_t,"\n saldo:",term.saldo,"\n dueño:",term.dueño)
p.cobrar()
p.guardar()
p.mostrar_tiket(300)
