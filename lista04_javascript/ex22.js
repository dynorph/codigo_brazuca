function valorAbsoluto(a) {
    if(a < 0) {
        return (a*-1);
    }
    else {
        return a;
    }
}

let a = -15;
console.log(valorAbsoluto(a));