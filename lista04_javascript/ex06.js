function soma_1a100() {
    let soma = 0;
    for(let i = 1; i <= 100; i++) {
        soma += i;
    }
    return soma;
}

console.log(soma_1a100());