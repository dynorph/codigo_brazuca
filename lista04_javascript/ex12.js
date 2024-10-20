function fatorial(a) {
    if(a <= 1) {
        return 1;
    }
    else {
        return a * fatorial(a-1);
    }
}

let a = 5;
console.log(fatorial(a));