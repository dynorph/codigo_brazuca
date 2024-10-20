function qtdVogais(str) {
    let contador = 0;
    str.split('');
    for(let i = 0; i < str.length; i++) {
        if(str[i] == 'A' || str[i] == 'a' || str[i] == 'E' || str[i] == 'e' || str[i] == 'I' || str[i] == 'i' || str[i] == 'O' || str[i] == 'o' || str[i] == 'U' || str[i] == 'u') {
            contador++;
        }
    }
    return contador;
}

let str = "Ola!";
console.log(qtdVogais(str));