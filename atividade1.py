class Calculadora:
    
    def __init__(self, nome):
        self.nome = nome
        self.historico = []


    def soma(self, operador1, operador2):
        return operador1 + operador2
    

    def subtracao(self, operador1, operador2):
        return operador1 - operador2
    
    
    def multiplicacao(self, operador1, operador2):
        return operador1 * operador2
    

    def divisao(self, operador1, operador2):
        if operador2 == 0:
            print("Não pode, pois não existe divisão por zero.")
            return None
        return operador1 / operador2
    

    def adicionar_ao_historico(self, operacao, operador1, operador2, resultado):
        if resultado is not None:
            self.historico.append(f"{operacao} de {operador1} e {operador2}: {resultado}")


    def exibir_historico(self):
        if not self.historico:
            print("Nenhuma operação realizada.")
        else:
            print("\nHistórico de operações:")
            for h in self.historico:
                print(h)


    def iniciar(self):
        while True:
            print("\n(1) Soma\n(2) Subtração\n(3) Multiplicação\n(4) Divisão")
            operacao = input("Escolha uma operação [1 a 4]: ")
            if operacao not in ['1', '2', '3', '4']:
                self.exibir_historico()
                break
            else:
                operador1 = float(input("Digite o primeiro valor: "))
                operador2 = float(input("Digite o segundo valor: "))
                
                if operacao == '1':
                    resultado = self.soma(operador1, operador2)
                    self.adicionar_ao_historico("Soma", operador1, operador2, resultado)
                elif operacao == '2':
                    resultado = self.subtracao(operador1, operador2)
                    self.adicionar_ao_historico("Subtração", operador1, operador2, resultado)
                elif operacao == '3':
                    resultado = self.multiplicacao(operador1, operador2)
                    self.adicionar_ao_historico("Multiplicação", operador1, operador2, resultado)
                elif operacao == '4':
                    resultado = self.divisao(operador1, operador2)
                    if resultado is not None:
                        self.adicionar_ao_historico("Divisão", operador1, operador2, resultado)

                if resultado is not None:
                    print(f"Resultado: {resultado}")

nome = str(input("Digite o seu nome: "))
calcul = Calculadora(nome)
calcul.iniciar()
