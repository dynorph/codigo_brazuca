function media(lista) {
    let soma = 0;
    for(let i = 0; i < lista.length; i++) {
        soma += lista[i];
    }
    return soma/lista.length;
}

let lista = [2, 3, 4, 5, 6, 7, 8];
console.log(media(lista));