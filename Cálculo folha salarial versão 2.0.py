# Constantes
SALARIO_MINIMO = 1320
CATEGORIAS = ["G", "O"]  # G = Gerente, O = Operário
TURNOS = ["M", "V", "N"]  # M = Matutino, V = Vespertino, N = Noturno
PORCENTAGENS = {
    "G": {"N": 0.10, "M": 0.15, "V": 0.15},
    "O": {"N": 0.09, "M": 0.14, "V": 0.14},
}

# Função para validação de entrada
def obter_entrada(mensagem, opcoes=None):
    while True:
        entrada = input(mensagem).strip().upper()
        if opcoes and entrada not in opcoes:
            print(f"Valor inválido! Escolha entre {opcoes}.")
        elif not entrada:
            print("O valor não pode ser vazio.")
        else:
            return entrada

# Função principal para cálculo do salário
def calcular_salario():
    nome = input("Digite o nome do funcionário: ").strip()
    if not nome:
        print("O nome não pode ser vazio.")
        return

    try:
        horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas no mês: "))
        if horas_trabalhadas <= 0:
            print("O número de horas deve ser positivo.")
            return
    except ValueError:
        print("Por favor, insira um número válido.")
        return

    turno = obter_entrada("Qual é o turno de trabalho? (M = Matutino, V = Vespertino, N = Noturno): ", TURNOS)
    categoria = obter_entrada("Qual é a categoria? (G = Gerente, O = Operário): ", CATEGORIAS)

    valor_hora = PORCENTAGENS[categoria][turno] * SALARIO_MINIMO
    salario_total = valor_hora * horas_trabalhadas

    print(f"{nome}, o seu salário é de R$ {salario_total:.2f}.")

# Execução
calcular_salario()
