// El patron mediador es similar al patron observador, pero con la diferencia de que en lugar de que los objetos se comuniquen entre ellos, se comunican mediante un mediador.
const Emitter = (() => {
    const topics = {}
    const hOP = topics.hasOwnProperty
    return {
        on: (topic, listener) => {
            if (!hOP.call(topics, topic)) topics[topic] = []
            topics[topic].push(listener)
        },
        emit: (topic, info) => {
            if (!hOP.call(topics, topic)) return
            topics[topic].forEach(item => item(info != undefined ? info : {}))
        }
    }
})();

let casaInteligente = (() => {
    Emitter.on('movimiento', sector => console.log(`Encendiendo las luces de ${sector}`));
    Emitter.on('comandoDeVozEncendido', sector => console.log(`Encendiendo las luces de ${sector}`));
    Emitter.on('comandoDeVozApagado', sector => console.log(`Encendiendo las luces de ${sector}`));
})();

Emitter.emit('movimiento', 'garaje');
Emitter.emit('comandoDeVozEncendido', 'sala');
Emitter.emit('comandoDeVozApagado', 'dormitorio');
