const auto = {
    modelo: 'Ford f150',
    tipo: 'camioneta',
    manejar: function () {
        console.log("Manejando...");
    },
    frenar: function (){
        console.log('Frenando...')
    }
}

const ford = Object.create(auto);
console.log(ford.modelo)

ford.modelo = 'Ford ranger';
ford.cilindraje = '2000cc';