function verificaPalindromo(str) {
    let strInversa = str.split('').reverse().join('');
    if(str == strInversa) {
        return true;
    }
    return false;
}

let str = "arara";
console.log(verificaPalindromo(str));
