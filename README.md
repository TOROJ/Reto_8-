# Reto 8!
uff ya casi llegando a la recta final...
bueno ahora si.
En este reto veremos una manera diferente del reto del restaurante, para recorrer las ordenes en dos momentos, el primer momento sera el que se crea una lista con el cuál tiene el
objetivo de guardar la información, mientras la segunda recorre a la primera y le da la funcion **mostrar()** esta hara posible al usuario dejar ver lo que se creó.

Todo en tan poco como esto:
```python
for evento in mesa:
   item: "MenuItem" = evento
   print(f"{item.mostrar()}  ")
```
se los voy a explicar:
```python
mesa=Order()    # Objeto hereda a clase.
mesa.añadidura(Jugo("maracuya", 5000, False),)  # funciones y datos, de los cuales usa mesa de Order()
```
```python
class Order:
    def __init__(self):                       
        self.lista_cuenta = []
        self.items = []
          
    def añadidura(self, item: "MenuItem" ):
        self.lista_cuenta.append(item)
        
    def __iter__(self):
        return RegistroEventosIterador(self.lista_cuenta)
    ....
```
Entre muchas cosas, aqui en order tenemos una función  imortante, que es la añadidura, esta en pocas palabras es la que tiene la información de la cuenta y lo guarda en esta misma,
El problema de esta, es que la guarda mas no es legible a simple vista( se los explico, guarda la info del objeto mas no de lo que se hace con el... osea aparece el <main_jugoetcetc.393993)
así, que usamos el __ _iter_ __ el cual sera el que pase uno a uno de los elementos:
```python
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
```
(se que esto parece sospechoso, sin embargo viendo que cumplia la misma función y viendo que me servia, lo use :P)

Principalmente aquí es donde permitira pasar dato por dato.

Y por último, la parte de impresion. 
Esta fue la que ya vimos de primeras, de las cuales usa un for, para ir a todos los elementos de la lista donde se guarda todo, toma item por item y al final, usa el metodo mostrar(),
el cual dara el resultado impreso.
```python
for evento in mesa:
   item: "MenuItem" = evento
   print(f"{item.mostrar()}  ")
```
Y ya con esto se puede imprimir de la misma manera muchas veces más hasta llegar al final.
## Conclución:
La verdad me gusto la clase que vimos, ya que no sabia de partes como zip o lambda que me llamaron la atención, fue interesante y también me gusto hacer lo mismo pero de otro modo distinto
la verdad... solo estoy asustado por que mañana es el examen.... y vaya, aparenta estar dificil.... hablamos en el ultimo reto :b 
