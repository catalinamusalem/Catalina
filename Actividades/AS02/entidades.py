from copy import copy


class Producto:
    def __init__(self, id_, nombre, categoria, precio, disponible, descuento_oferta):
        self.id_ = id_
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible
        self.descuento_oferta = descuento_oferta

    def __repr__(self):
        return self.nombre


class Cliente:
    def __init__(self, id_, nombre, carrito):
        self.id_ = id_
        self.nombre = nombre
        self.carrito = carrito


class IterableOfertones:
    def __init__(self, productos):
        self.productos = productos

    def __iter__(self):
        return IteradorOfertones(self)


class IteradorOfertones:
    def __init__(self, iterable):
        self.iterable = copy(iterable)
        self.ordenados = sorted(self.iterable.productos, key = lambda x: x.descuento_oferta)
        self.actual = len(self.iterable.productos)-1

    def __iter__(self):
        # Completar
        return self

    def __next__(self):
        # Completar
        if self.actual == 0:
            raise StopIteration("Llegamos al final")
        else:
            valor= self.actual
            self.actual -= 1
            producto = self.ordenados[valor]
            producto.precio = producto.precio * (1-(producto.descuento_oferta / 100))
            return self.ordenados[valor]
