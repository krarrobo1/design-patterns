class Facade:
    def __init__(self, servicio_pedidos, servicio_facturacion, servicio_notificacion):
      self.servicio_pedidos = servicio_pedidos
      self.servicio_facturacion = servicio_facturacion
      self.servicio_notificacion = servicio_notificacion
    
    def hacer_pedido(self):
        print('Nuevo pedido!!')
        servicio_pedidos.registrar_pedido()
        print("Pedido registrado...")
        servicio_facturacion.generar_factura()
        print("Facturacion realizada..")
        servicio_notificacion.enviar_notificacion_repartidor()
        print("Notificacion enviada al repartidor..")

        pass


class Pedidos:
    def registrar_pedido(self):
            pass

    # ...

    def cancelar_pedido(self):
        pass


class Notificacion:
    """
    Este servicio se encarga de enviar notificaciones tanto al cliente como al repartidor y al restaurante
    """

    def enviar_notificacion_cliente(self):
        pass

    # ...

    def enviar_notificacion_repartidor(self):
        pass

class Facturacion:
    """
    Este servicio se encarga de calcular el total de la factura y generar un archivo de la factura.
    """
    def generar_factura(self):
        pass
    
    def calcular_total(self):
        pass



if __name__ == '__main__':
    servicio_pedidos = Pedidos()
    servicio_facturacion = Facturacion()
    servicio_notificacion = Notificacion()
    facade = Facade(servicio_pedidos, servicio_facturacion, servicio_notificacion)
    facade.hacer_pedido()
    