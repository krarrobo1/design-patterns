# Patrones de Diseño
Los patrones de diseño son un conjunto de técnicas utilizadas para resolver un problema en específico. Dentro del mundo del desarrollo de software, nos sirven para poder refinar componentes de un sistema de software, facilitando así la reutilización, mantenimiento y calidad del código.

Hoy en día existen un sin numero de patrones de diseño, debido a la necesidad de organizarlos se pueden clasificar en tres categorias principales: 

(1) **Creacionales**, estos guían en la creación de objetos. 

(2) **Estructurales:** describen como organizar objetos para trabajar en conjunto. 

(3) **De comportamiento:** para organizar de mejor manera el comportamiento de los objetos.

Acontinuación detallaremos cada uno de ellos junto con ejemplos de los patrones más comunes en su categoría

# Patrones Creacionales

Los patrones creacionales proporcionan varios mecanismos de creación de objetos que incrementan la flexibilidad y la reutilización del código existente.

### Patrón Factory 

Este patrón proporciona una interfaz para la creación de objetos en una superclase, mientras permite a las subclases alterar el tipo de objetos que se crearán:

**Ejemplo:**

Queremos crear una fabrica de errores de manera en la cúal se pueda instanciar un error de acuerdo al tipo de error que le pidamos.

    class ErrorFactory():
	    @staticmethod
		def get_error(type):
		    if type == 'notfound':
			   return NotFoundError()
		    elif type == 'unauthorized':
			   return UnauthorizedError()

En este caso si le decimos a ErrorFactory que necesitamos un error de tipo 'notfound' nos devolverá una instancia del siguiente error:

    class  NotFoundError(IError):
	    def __init__(self):
		    self.message = "Resource not found!"
		def print_message(self):
			print(self.message)
			return

Para ver la implementación completa puedes revisar el archivo: ***python/factory.py***  en el repositorio.

## Patrón prototype

Este patrón nos permite copiar objetos existentes sin que el código dependa de sus clases.

**Ejemplo:**
En este caso hemos creado el objeto camioneta con sus respectivos metodos.

    const camioneta = {
	    modelo: 'Ford f150',
	    tipo: 'camioneta',
	    manejar: function () {
	    console.log("Manejando...");
	    },
		frenar: function (){
		    console.log('Frenando...')
	    }
    }
    const ford = Object.create(camioneta);
    console.log(ford.modelo)
    
    ford.modelo = 'Ford ranger';
    console.log(ford.modelo);

Mediante el método `Object.create` podemos clonar instancias de ese objeto de manera fácil en Javascript. Y también nos permite cambiar o crear nuevos atributos sin afectar al objeto original.

Para ver la implementación completa puedes revisar el archivo: ***javascript/prototype.js***  en el repositorio.

# Patrones estructurales

Estos patrones explican cómo ensamblar objetos y clases en estructuras más grandes, mientras se mantiene la flexibilidad y eficiencia de la estructura.

## Patrón Adapter

Adapter es un patrón de diseño estructural que permite la colaboración entre objetos con interfaces incompatibles.

Ejemplo:

Imaginemos que tenemos 2 Apis en nuestro proyecto, por alguna razon que ignoramos por simplicidad el  equipo de desarrollo decide dar de baja la "Api 1" y empezar a utilizar "Api 2". Resulta que tenemos muchos lugares en nuestra aplicación que llaman o utilizan métodos de la "Api 1", por lo que si queremos cambiar a "Api 2" nos tocaría cambiarla en todos los lugares que lo necesiten.

Para resolver esta problemática crearemos un adaptador que nos permita envolver la Api 2

```
// Api 1
class Api {
    constructor() {
        this.operations = function (url, opts, verb) {
            switch (verb) {
                case 'get':
                    // return fetch ...
                    break;
                case 'post':
                    // return fetch ...
                    break;
                default:
                    return
            }
        }
    }
}

// Clase Api2
class Api2 {
    constructor() {
        this.get = function (url, opts) {
            // return axios.get..
        };
        this.post = function (url, opts) {
            // return axios.post..
        }
    }
}

// Adaptador
class ApiAdapter {
    constructor() {
        const api2 = new Api2();
        this.operations = function (url, opts, verb) {
            switch (verb) {
                case 'get':
                    return api2.get(url, opts);
                case 'post':
                    return api2.post(url, opts);
                default:
                    break;
            }
        }
    }
};


const api = new Api();
api.operations('www.google.com', { q: 1 }, 'get');

const api2 = new Api2();
api2.get('www.google.com', { q: 1 });

// En este caso estamos usando el método 2 por debajo de la implementación del adaptador para poder llamar a las funciones de la misma manera que el api1 pero por debajo estaremos usando la api2.
const adapter = new ApiAdapter();
adapter.operations('www.google.com', { q: 1 }, 'get');
```

## Patrón Facade

El patrón Facade disminuye la complejidad general de la aplicación, al mismo tiempo que ayuda a mover dependencias no deseadas a un solo lugar.

**Ejemplo:**

Supongamos que tenemos una aplicacion de pedidos a domicilio, tenemos un servicio que se encarga de notificar al restaurante la orden del cliente. Asi mismo tenemos otro servicio que se encarga de registrar la orden del cliente y otro que se encarga de generar la factura y enviarsela al correo y otro de notificar al repartidor acerca de un nuevo pedido.

En este proceso de realizar un pedido tenemos la participación de 3 servicios. Que colaboran entre sí para cumplir con la solicitud.

En este caso con el patrón Facade ,podemos crear una fachada la cual se encargará de gestionar los 3 servicios y delegar las acciones que debe realizar cada servicio.

```
class Facade:
    def __init__(self, servicio_pedidos, servicio_facturacion, servicio_notificacion):
      self.servicio_pedidos = servicio_pedidos
      self.servicio_facturacion = servicio_facturacion
      self.servicio_notificacion = servicio_notificacion
    
    def hacer_pedido(self):
        servicio_pedidos.registrar_pedido()
        servicio_facturacion.generar_factura()
        servicio_notificacion.enviar_notificacion_repartidor()
		return 


class Pedidos:
	"""
    Este servicio se encarga de gestionar los pedidos
    """
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
```

# Patrones de comportamiento

Estos patrones tratan con algoritmos y la asignación de responsabilidades entre objetos.

## Patrón Mediator

Mediator es un patrón de diseño de comportamiento que te permite reducir las dependencias caóticas entre objetos. El patrón restringe las comunicaciones directas entre los objetos, forzándolos a colaborar únicamente a través de un objeto mediador.

**Ejemplo:**

Supongamos que tenemos una casa inteligente, la cual se encarga de realizar ciertas acciones dependiendo de la informacion que les envian los sensores, para que la casa y los sensores se puedan comunicar efectivamente lo hacen a traves del mediador quien se encargara de notificar a la casa cuando un sensor se active o alguien realice un comando de voz.
```
// En lugar de que los objetos se comuniquen entre ellos, se comunican mediante un mediador **Emitter**.

let casaInteligente = (() => {
    Emitter.on('movimiento', sector => console.log(`Encendiendo las luces de ${sector}`));
    Emitter.on('comandoDeVozEncendido', sector => console.log(`Encendiendo las luces de ${sector}`));
    Emitter.on('comandoDeVozApagado', sector => console.log(`Encendiendo las luces de ${sector}`));
})();

// El sensor del garaje detecto un movimiento
Emitter.emit('movimiento', 'garaje');
// El gestor de comandos detecto un nuevo comando de voz
Emitter.emit('comandoDeVozEncendido', 'sala'); 
Emitter.emit('comandoDeVozApagado', 'dormitorio');
```

## Patron comando

Command es un patrón de diseño de comportamiento que convierte solicitudes u operaciones simples en objetos.

La conversión permite la ejecución diferida de comandos, el almacenamiento del historial de comandos, etc.

Ejemplo:

Supongamos que tenemos una calculadora, la cual depende de lo que presionemos realiza un comando en especifico
cuando presionamos calcular. va a llamar a los comandos de CalculoComplejo el cual realizara los calculos.
Luego se llama el metodo imprimir para que se visualice el resultado en pantalla. 

La ventaja de este patron es que si queremos extender la funcionalidad de nuestra calculadora a futuro.

Simplemente debemos crear una nueva clase que herede de Command y programar el nuevo compotamiento que queremos.

```
from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):
    """ Interfaz comando """
    @abstractmethod
    def execute(self):
        pass

class ComandoImprimir(Command):
    def __init__(self, payload):
        self._payload = payload
    def execute(self):
        print(self._payload)


class ComandoCalculoComplejo(Command):
    def __init__(self, receiver):
        self.receiver = receiver
    def execute(self):
        print('Realizando calculo complejo...')
        self.receiver.calculate_a()
        self.receiver.calculate_b()
    
class Calculador:
    def calculate_a(self):
        print('Calculando a...')

    def calculate_b(self):
        print('Calculando b...')

class Calculadora:
    _on_start = None
    _on_finish = None

    """
    Initialize commands.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def realizar_calculos(self):
        
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        if isinstance(self._on_finish, Command):
            self._on_finish.execute()

if __name__ == '__main__':
    calculadora = Calculadora()
    calculador = Calculador()
    calculadora.set_on_start(ComandoCalculoComplejo(calculador))
    calculadora.set_on_finish(ComandoImprimir("La respuesta esta en tu corazon ...."))
    calculadora.realizar_calculos()
    ```