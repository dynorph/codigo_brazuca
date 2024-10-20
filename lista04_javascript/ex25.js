function vogaisToAsterisk(str) {
    stringSeparada = str.split('');
    for(let i = 0; i < str.length; i++) {
        if(str[i] == 'A' || str[i] == 'a' || str[i] == 'E' || str[i] == 'e' || str[i] == 'I' || str[i] == 'i' || str[i] == 'O' || str[i] == 'o' || str[i] == 'U' || str[i] == 'u') {
            stringSeparada[i] = '*';
        }
    }
    return stringSeparada.join('');
}

let str = "Ola mundo!";
console.log(vogaisToAsterisk(str));