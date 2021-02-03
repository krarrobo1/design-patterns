/**
 * Patron Adaptader
 * El patrón adaptador se utiliza para transformar una interfaz en otra, de tal modo que una clase que no pueda utilizar la primera haga uso de ella a través de la segunda.
 */

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