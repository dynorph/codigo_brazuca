function fibonacci(a) {
    let sequencia = [];
    sequencia[0] = 0;
    if(a > 1) {
        sequencia[1] = 1;
    }
    for(let i = 2; i < a; i++) {
        sequencia[i] = sequencia[i-1] + sequencia[i-2];
    }
    return sequencia;
}

let a = 10;
console.log(fibonacci(a));