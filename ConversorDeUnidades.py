def metros_para_quilometros(metros):
    """
    Converte metros para quilômetros.
    
    Args:
        metros (float): Valor em metros.
    
    Returns:
        float: Valor em quilômetros.
    """
    return metros / 1000

def celsius_para_fahrenheit(celsius):
    """
    Converte Celsius para Fahrenheit.
    
    Args:
        celsius (float): Valor em Celsius.
    
    Returns:
        float: Valor em Fahrenheit.
    """
    return (celsius * 9/5) + 32

def quilogramas_para_libras(quilogramas):
    """
    Converte quilogramas para libras.
    
    Args:
        quilogramas (float): Valor em quilogramas.
    
    Returns:
        float: Valor em libras.
    """
    return quilogramas * 2.20462

def main():
    print("Conversor de Unidades")
    print("---------------------")
    
    while True:
        print("Opções:")
        print("1. Metros para Quilômetros")
        print("2. Celsius para Fahrenheit")
        print("3. Quilogramas para Libras")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            metros = float(input("Digite o valor em metros: "))
            quilometros = metros_para_quilometros(metros)
            print(f"{metros} metros é igual a {quilometros} quilômetros.")
        elif opcao == "2":
            celsius = float(input("Digite o valor em Celsius: "))
            fahrenheit = celsius_para_fahrenheit(celsius)
            print(f"{celsius} Celsius é igual a {fahrenheit} Fahrenheit.")
        elif opcao == "3":
            quilogramas = float(input("Digite o valor em quilogramas: "))
            libras = quilogramas_para_libras(quilogramas)
            print(f"{quilogramas} quilogramas é igual a {libras} libras.")
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()