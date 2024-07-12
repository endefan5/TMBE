function ocultar_festejos() {
    lbl_festejos = document.getElementById("festejos");
    lbl_festejos.style.display = "none"
    eventoEspecial = "No";
}

function mostrar_festejos() {
    lbl_festejos = document.getElementById("festejos");
    lbl_festejos.style.display = "flex"
    eventoEspecial = "Si";
}

// class PH {
//     constructor(pid) {
//         this.p = document.getElementById(pid);
//     }

//     mostrar() {
//         if (this.p.style.display == "flex") {
//             this.p.style.display = "none";
//         } else {
//             this.p.style.display = "flex";
//             this.p.style.backgroundColor = rgba(140, 0, 0, 0);
//         }
//     }
// }

class Platos {
    constructor(id_plato) {
        this.platos = [
            [document.getElementById("comidas"), document.getElementById("SubS1")],
            [document.getElementById("bebidas"), document.getElementById("SubS2")],
            [document.getElementById("postres"), document.getElementById("SubS3")]
        ];

        this.plato = document.getElementById(id_plato);
    }
    mostrar() {

        for (let plat of this.platos) {
            if (plat[0] === this.plato) {
                if (plat[0].style.width == "25%") {
                    plat[0].style.width = "95%";
                    plat[0].style.backgroundColor = "#4e00647a";
                    plat[0].style.color = "yellow";
                    plat[1].style.display = "flex";
                    for (let plat2 of this.platos) {
                        if (plat2[0] !== this.plato) {
                            plat2[0].style.display = "none"

                        }
                    }
                } else {
                    plat[0].style.width = "25%";
                    plat[0].style.backgroundColor = ""
                    plat[0].style.color = "";
                    plat[1].style.display = "none";
                    for (let plat2 of this.platos) {
                        if (plat2[0] !== this.plato) {
                            plat2[0].style.display = "flex"
                            plat2[0].style.flexDirection = "column"
                        }
                    }
                }

            }
        }
    }
}

class elemento_historia {
    static coleccion = []
    constructor(id) {
        this.nombre = "Este es el elemento " + id
        this.contenedor = document.getElementById(id)
        this.parrafo = document.getElementById("p" + id)
        this.flecha = document.getElementById("f" + id)
        this.expandido = false
        elemento_historia.coleccion.push(this)
    }
    
    ocultar_todos() {
        for (let elemento of elemento_historia.coleccion) {
            elemento.contenedor.className = "sectorOculto"
        }
    }

    listar_todos() {
        for (let elemento of elemento_historia.coleccion) {
            console.log(elemento.nombre)
        }
    }

    colapsar_todos() {
        for (let elemento of elemento_historia.coleccion) {
            elemento.expandido = false
            elemento.contenedor.className = "sectorRetraido"
            elemento.parrafo.style.display = "none"
            elemento.flecha.classList.remove("rotate")
        }
    }
    
    expandir() {
        this.contenedor.className = "sectorExpandido"
        this.parrafo.style.display = "flex"
        this.flecha.classList.add("rotate")
    }

    cambiar_estado() {
        if (!this.expandido) {
            this.expandido = true
            this.expandir()
        } else {
            this.expandido = false
            this.colapsar_todos()
        }
    }
}

var eh1 = new elemento_historia("1")
var eh2 = new elemento_historia("2")
var eh3 = new elemento_historia("3")
var eh4 = new elemento_historia("4")
var eh5 = new elemento_historia("5")
var eh6 = new elemento_historia("6")
var eh7 = new elemento_historia("7")



var comm = new Platos("comidas")
var bebb = new Platos("bebidas")
var poss = new Platos("postres")

document.addEventListener('scroll', function () {
    const logo = document.querySelector('.logo');
    const threshold = 100;

    if ((window.innerHeight + window.scrollY) >= (document.body.offsetHeight - threshold)) {
        logo.classList.add('large');
    } else {
        logo.classList.remove('large');
    }
});