function saoMultiplos(a,b) {
    if(a % b == 0 || b % a == 0) {
        return true;
    }
    return false;
}

let a = 3;
let b = 6;
console.log(saoMultiplos(a,b));