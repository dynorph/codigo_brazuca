function par_impar(a) {
    if(a % 2 == 0) {
        return "Par";
    }
    else {
        return "Impar";
    }
}

let a = 3;
console.log(par_impar(a));