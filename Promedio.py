# -*- coding: iso-8859-15 -*-
# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	print "Hola, esta es una calculadora"
	print "Dime la cantidad de datos"
	n = float(raw_input())
	acum = 0
	for i in range(1,n+1):
		print "Dime el dato",1,":"
		dato = float(raw_input())
		acum = acum+dato
	prom = acum/n
	print "El promedio es: ",prom

