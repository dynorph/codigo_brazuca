programa {
  funcao inicio() {
    inteiro num, contador = 0
    para(inteiro i = 0; i < 5; i++) {
      escreva("Insira um numero: ")
      leia(num)
      se(num > 0) {
        contador++
      }
    }
    escreva("Voc� escreveu ", contador, " numeros positivos")
  }
}
