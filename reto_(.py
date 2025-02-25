
from collections import namedtuple

class MenuItem():
    def __init__(self, nombre : str, precio : float):
        self.nombre = nombre                           
        self.precio = precio        

    def neto(self):                               
        return self.precio
    
    def mostrar():
        return 
        
# Tupla con nombre para representar un libro    
MenuItems = namedtuple("Menuitems", ["Nombre", "Precio", "Adición"])    

class  Almuerzo(MenuItem):
    def __init__(self, nombre : str, precio : float, adicion: bool):  
        super().__init__(nombre, precio)                        
        if adicion == True:                                        
            self.adicion = 'con sopa'
        elif adicion == False:
            self.adicion = 'sin sopa'
            self.precio = self.precio -500

        self.almuerzo=MenuItems(self.nombre, self.precio, self.adicion)
    

    def mostrar(self):
        return f"Nombre: {self.almuerzo.Nombre}\n Sopa: {self.almuerzo.Adición}\n Precio: {self.almuerzo.Precio}\n\n" 

class Jugo(MenuItem):
    def __init__(self, nombre: str, precio: float, adicion:bool): 
        super().__init__(nombre, precio)                       
        if adicion == True:                                       
            self.adicion = "En agua"
        elif adicion == False:
            self.adicion = "En leche"
            self.precio = self.precio +1500
        bebida=MenuItems(self.nombre, self.precio, self.adicion)
        self.bebida = bebida
    def mostrar(self):
        return f"\nNombre: {self.bebida.Nombre}\n jugo: {self.bebida.Adición}\n Precio: {self.bebida.Precio}\n\n"
        
    
class Postre(MenuItem):
    def __init__(self, nombre:str, precio: float, adicion: bool):   
        super().__init__(nombre, precio)                           
        if adicion == False:                                        
            self.adicion= "promedio"
        elif adicion == True:
            self.adicion = "grande"
            self.precio = self.precio +2000
        postre=MenuItems(self.nombre, self.precio, self.adicion)
        self.postre = postre
    def mostrar(self):

        return f"Nombre: {self.nombre}\n postre: {self.postre.Adición}\n Precio: {self.postre.Precio}\n\n"
 
class Order:
    def __init__(self):                       
        self.lista_cuenta = []
        self.items = []
          
    def añadidura(self, item: "MenuItem" ):
        self.lista_cuenta.append(item)
    
    def mostrar(self):
        return self.lista_cuenta
    
    def cuenta(self):
        self.total = 0                
        
        for item in self.lista_cuenta:
            self.total += item.neto()

        return self.total       
    
    def item(self):
        for item in self.lista_cuenta:
            self.items.append(item.mostrar() )
        lista_items = ( list(map(str, self.items)))
        return ("".join(lista_items))  
    
    def __iter__(self):
        return RegistroEventosIterador(self.lista_cuenta)
  

class RegistroEventosIterador:
  """Implementa un iterador para recorrer eventos registrados."""

  def __init__(self, eventos):
    self.eventos = eventos
    self.indice = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.indice < len(self.eventos):
      evento = self.eventos[self.indice]
      self.indice += 1
      return evento
    else:
      raise StopIteration
    

    
mesa=Order()   
mesa.añadidura(Jugo("maracuya", 5000, False),) 
mesa.añadidura(Almuerzo("corriente", 12000, False))
mesa.añadidura(Postre("fresas", 6000, True))                                          
mesa.añadidura(Jugo("mora", 5000, False))   
mesa.añadidura(Almuerzo("bandeja paisa", 25000, True))
mesa.añadidura(Postre("wafles", 2500, True))                                    
mesa.añadidura(Jugo("mango", 5000, True))   
mesa.añadidura(Almuerzo("corriente", 15000, True))
mesa.añadidura(Postre("brownie", 1000, True))



for evento in mesa:
   item: "MenuItem" = evento
   print(f"{item.mostrar()}  ")