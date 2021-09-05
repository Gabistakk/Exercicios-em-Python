valor = float(input("Digite o valor da casa: R$"))

salario = float(input("\nDigite o valor do seu salário: R$"))

tempo = float(input("\nDigite em quantos anos pretende pagar: R$"))

porcensalario = salario * 0.3

prestaçao = valor / (tempo * 12)

if prestaçao >= porcensalario:
    print("\nO emprestimo foi negado!")

else:
    print("\nO emprestimo foi aceito!")
