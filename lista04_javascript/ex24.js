function divisores(a) {
    let divisores = [];
    for(let i = a; i > 0; i--) {
        if(a % i == 0) {
            divisores.push(i);
        }
    }
    return divisores;
}

let a = 20;
console.log(divisores(a));