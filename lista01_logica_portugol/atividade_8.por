programa {
  funcao inicio() {
    inteiro ano
    escreva("Insira um ano: ")
    leia(ano)
    se(ano % 4 == 0) {
      se(ano % 100 == 0) {
        se(ano % 400 == 0) {
          escreva("O ano � bissexto")
        }
        senao {
          escreva("O ano n�o � bissexto")
        }
      }
      senao {
        escreva("O ano � bissexto")
      }
    }
    senao {
      escreva("O ano n�o � bissexto")
    }
  }
}
