from datetime import timedelta
import datetime
from time import sleep, strptime



"""
#trabajo practico algoritmos universidad
#EJERCICIO 1-A

#fecha y hora actual
hoy = datetime.datetime.now()
print(f'fecha y hora actual: {hoy}')

#anio actual
anio= datetime.datetime.now()
print(f'Anio actual: {anio.year}')

#mes
mes= datetime.datetime.now()
print(f'Mes del anio: {mes.month}')

#número de semana del año
semana= datetime.datetime.now()
print(f'Semana del anio: {semana.isocalendar()[1]}')

#día de la semana
dia_semana = datetime.datetime.now()
print(f'Dia de la semana: {dia_semana.weekday()}')

#día del año
dia_semana = datetime.datetime.now()
print(f"Dia del anio: {dia_semana.strftime('%j')}")

#día del mes
dia_semana = datetime.datetime.now()
print(f"Dia del mes: {dia_semana.strftime('%d')}")
"""
"""
#EJERCICIO B
#CALCULAR DIFERENCIA CON FECHAS
# Consulta como obtener solo la fecha ya que es un datetime.delta? 
# Y me aparece 0:00:00 detras de la fecha datetime.date retorna las fechas

import locale
locale.setlocale(locale.LC_ALL, 'es-ES')

hoy = datetime.date.today()
parcial = datetime.date(2022, 7, 23)
diferencia = (hoy - parcial)


dia = str(diferencia)
dia = dia.replace('days', 'dias')
dia = dia.replace('0:00:00', '')
print(f'Faltan {dia}para el 2 parcial')
"""

"""
#EJERCICIO 1C
for i in range(5):
    string = 'Hola soy cristian'
    print(string)
    sleep(3)
"""

"""
#EJERCICIO 2
#A)
from datetime import datetime
class Persona:
    lista_mascotas = []
    
    def __init__(self, nombre, apellido, fecha_de_nacimiento, direccion, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.email = email 
    
    def age(self):
        cuenta = datetime.today() - datetime.strptime( self.fecha_de_nacimiento, '%Y-%m-%d')
        anios = str(cuenta / 365)
        reemplazo = anios.replace('days', 'anios')
        ree = reemplazo[0:8]
        return f'{self.nombre} tiene {ree}'
    
    def agregar_mascota(self):
        self.mascota = input('Ingrese una mascota: ')
        self.lista = self.lista_mascotas.append(self.mascota)
        return self.lista
    
    def mostrar_lista(self):
        return self.lista_mascotas
        
    
        
    
yo = Persona('cristian', 'villagra','1983-03-14','cala 97 Solano', 1165391958, 'cristian83villagra@gmail.com')
print(yo.agregar_mascota())
print(yo.agregar_mascota())
print(yo.agregar_mascota())
print(yo.mostrar_lista())

"""

"""
#EJERCICIO 3
#3A y B
class Mascota:

    def __init__(self, nombre):
        self.nombre = nombre
        
    def pata_saluda(self):
        return print(f'{self.nombre}, saluda con la pata')

mi_perro = Mascota('oliver')
print(mi_perro.pata_saluda())        
"""
