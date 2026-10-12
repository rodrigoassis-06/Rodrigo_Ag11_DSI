from colorama import Fore, Style, init

# Inicializa o colorama
init()

# Funcao para definir a cor de acordo com o nivel informado
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Lista com os niveis, situacoes e mensagens do reservatorio
reservatorio = [
    {
        "nivel": 1,
        "situacao": "Muito baixo (critico)",
        "mensagem": "Nivel critico! Risco de falta de agua."
    },
    {
        "nivel": 2,
        "situacao": "Baixo",
        "mensagem": "Nivel baixo. Economize agua."
    },
    {
        "nivel": 3,
        "situacao": "Medio",
        "mensagem": "Nivel normal. Operacao estavel."
    },
    {
        "nivel": 4,
        "situacao": "Alto",
        "mensagem": "Nivel alto. Atencao ao reservatorio."
    },
    {
        "nivel": 5,
        "situacao": "Muito alto (alerta)",
        "mensagem": "Nivel maximo atingido! Risco de transbordamento."
    }
]

# Exibindo as mensagens no terminal
print("=== MONITORAMENTO DO RESERVATORIO DE AGUA ===\n")

for item in reservatorio:
    cor = definir_cor(item["nivel"])
    print(cor + f"Nivel {item['nivel']} - {item['situacao']}")
    print(cor + f"Alerta: {item['mensagem']}")
    print(Style.RESET_ALL + "---------------------------------------------")

# Restaura o estilo padrao do terminal
print(Style.RESET_ALL + "\nMonitoramento finalizado.")
