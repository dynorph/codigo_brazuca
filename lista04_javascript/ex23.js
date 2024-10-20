function raizQuadrada(a) {
    if(a<0) {
        return "error";
    }
    else {
        return a ** 0.5;
    }
}

let a = 25;
if(raizQuadrada(a) != "error") {
    console.log(raizQuadrada(a));
}