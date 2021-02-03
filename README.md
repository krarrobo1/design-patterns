# Patrones de Diseño
Los patrones de diseño son un conjunto de técnicas utilizadas para resolver un problema en específico. Dentro del mundo del desarrollo de software, nos sirven para poder refinar componentes de un sistema de software, facilitando así la reutilización, mantenimiento y calidad del código.

Hoy en día existen un sin numero de patrones de diseño, debido a la necesidad de organizarlos se pueden clasificar en tres categorias principales: 

(1) **Creacionales**, estos guían en la creación de objetos. 

(2) **Estructurales:** describen como organizar objetos para trabajar en conjunto. 

(3) **De comportamiento:** para organizar de mejor manera el comportamiento de los objetos.

Acontinuación detallaremos cada uno de ellos junto con ejemplos de los patrones más comunes en su categoría

## Patrones Creacionales

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

Ejemplo:
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