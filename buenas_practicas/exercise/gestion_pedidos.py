import itertools
from collections import Counter
from enum import Enum

class EstadoPedido(Enum):
    PENDIENTE = "Pendiente"
    ENVIADO = "Enviado"
    ENTREGADO = "Entregado"

class SistemaPedidos:
    _id_generador = itertools.count(1)

    def __init__(self):
        self.pedidos = {}
        self.contador_productos = Counter()

    def crear_pedido(self, productos: list[str]):
        pedido_id = next(self._id_generador)
        # normalizar productos a minúsculas
        productos = [p.lower() for p in productos]
        self.pedidos[pedido_id] = {
            "productos": productos,
            "estado": EstadoPedido.PENDIENTE.value,
        }
        self.contador_productos.update(productos)
        return pedido_id

    def cambiar_estado(self, pedido_id: int, nuevo_estado: EstadoPedido):
        if pedido_id in self.pedidos:
            self.pedidos[pedido_id]["estado"] = nuevo_estado.value
        else:
            print(f"❌ Pedido {pedido_id} no encontrado")

    def obtener_pedido(self, pedido_id: int):
        return self.pedidos.get(pedido_id, "❌ Pedido no encontrado")

    def mostrar_contador(self):
        return dict(self.contador_productos)

    def mostrar_pedido(self, pedido_id: int):
        pedido = self.obtener_pedido(pedido_id)
        if isinstance(pedido, dict):
            productos = ", ".join(pedido["productos"])
            return f"📦 Pedido {pedido_id} | Estado: {pedido['estado']} | Productos: [{productos}]"
        return pedido


# -------------------
# Ejemplo de uso
# -------------------
sistema = SistemaPedidos()

pedido1 = sistema.crear_pedido(['Laptop', 'Audifonos', 'Mouse'])
pedido2 = sistema.crear_pedido(['Impresora', 'Cargador', 'Television'])

print(sistema.mostrar_pedido(pedido1))
print(sistema.mostrar_pedido(pedido2))

print("Cambiando estado 💱")
sistema.cambiar_estado(pedido1, EstadoPedido.ENVIADO)

print(sistema.mostrar_pedido(pedido1))
print(sistema.mostrar_pedido(pedido2))

print("📊 Contador de productos:", sistema.mostrar_contador())
