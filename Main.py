import pyrebase
import os
import json
from colorama import Fore, Back, Style, init
import re
import subprocess
import sys
init(autoreset=True)

path_Main = ""
dados = None
version = "1,0"

# Obtém o caminho para o diretório do executável (geralmente criado pelo PyInstaller)
exe_dir = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)

# Define o caminho completo para o arquivo "data.json"
caminho_json = os.path.join(exe_dir, "data.json")

def main():
    global version
    aviso = F"""
    {Fore.YELLOW}AVISO LEGAL{Style.RESET_ALL}
    
    Este script é confidencial e contém informações proprietárias. Ele   é    fornecido
    apenas para uso interno e não deve ser compartilhado com  terceiros sem autorização 
    prévia. O uso deste script está sujeito     aos termos e    condições estabelecidos 
    pelo criador. Ao executar este script, você concorda   em   cumprir todos os termos 
    e condições aplicáveis.
"""
    print(aviso)
    print("Ao continuar, você aceita os termos de uso.\n")

    # Configuração do Firebase (use as credenciais do seu projeto)
    config = {
        "apiKey": "...",
        "authDomain": "...",
        "databaseURL": "...",
        "projectId": "...",
        "storageBucket": "...",
        "messagingSenderId": "...",
        "appId": "..."
    }

    #dirFinder()

    while True:
        try:
            firebase = pyrebase.initialize_app(config)

            # Acesse o banco de dados
            db = firebase.database()

            # Verifique se a versão atual do programa está na lista de versões permitidas
            versoes_permitidas = db.child("allowed_versions").get().val()

            if versoes_permitidas.get(version) == True:
                # print(f"A versão {version} é permitida. Você pode continuar.")
                jsonCheck()
                break
            else:
                tempV = version.replace(",", ".")
                confirm = input(f"A versão {tempV} não está na lista de versões permitidas.\n\n{Back.RED}Acesso negado.{Style.RESET_ALL}")

            break  # Sair do loop após uma execução bem-sucedida
        except Exception as e:
            confirm = input(Back.RED+"Não foi possível conectar ao servidor. Tente novamente mais tarde."+Style.RESET_ALL)
            # Você pode adicionar mais manipulação de erro aqui, se necessário
            break

    

def jsonCheck():
    global path_Main
    global dados
    global caminho_json

    if not os.path.exists(caminho_json):
        dados = {
            "Regional": {"CO":"REGIONAL CO", "LESTE":"REGIONAL LESTE", "NE":"REGIONAL NORDESTE", "NO":"REGIONAL NORTE", "SPMG":"REGIONAL SPMG", "SUL":"REGIONAL SUL"}, 
            "Cliente": {
                "REGIONAL CO": [{"cliente1":"cliente1","cliente2":"cliente2"}], 
                "REGIONAL LESTE": [{"cliente1":"cliente1","cliente2":"cliente2"}], 
                "REGIONAL NORDESTE": [{"cliente1 ":"cliente1","cliente2":"cliente2"}], 
                "REGIONAL NORTE": [{"cliente1":"cliente1","cliente2":"cliente2"}], 
                "REGIONAL SPMG": [{"cliente1":"cliente1","cliente2":"cliente2"}], 
                "REGIONAL SUL": [{"cliente1":"cliente1","cliente2":"cliente2"}]
            },
            "Investimento": {"Combos":"Combos", "Estrutural":"Execução Estrutural", "Metas":"Plano de Metas", "TTI":"TTI", "Ypióca":"Ypioca"}, 
            "Ano": {"F24":"FY24"}, 
            "Dia": {"Q1":"P03", "Q2":"P06", "Q3":"P09", "P1":"P01", "P2":"P02", "P3":"P03", "P4":"P04", "P5":"P05", "P6":"P06", "P7":"P07", "P8":"P08", "P9":"P09", "P10":"P10", "P11":"P11", "P12":"P12"}, 
            "dirBase": ""
        }

        # Cria e escreve o JSON no arquivo
        with open(caminho_json, 'w', encoding='utf-8') as json_file:
            json.dump(dados, json_file, ensure_ascii=False)
        
    else:
        with open(caminho_json, 'r', encoding='utf-8') as json_file:
            dados = json.load(json_file)
    
    path_Main = dados["dirBase"]
    menu()

def menu():
    global path_Main

    os.system("cls" if os.name == "nt" else "clear")

    search_text = """

███████ ██ ███    ██ ██████  ███████ ██████  
██      ██ ████   ██ ██   ██ ██      ██   ██ 
█████   ██ ██ ██  ██ ██   ██ █████   ██████  
██      ██ ██  ██ ██ ██   ██ ██      ██   ██ 
██      ██ ██   ████ ██████  ███████ ██   ██ 
"""
    intro = """
       _   _                         _______                 _     
      | | | |                       |__   __|               | |    
      | | | |__     ___    _ __        | |      ___    ___  | |__  
  _   | | | '_ \\   / _ \\  | '_ \\       | |     / _ \\  / __| | '_ \\ 
 | |__| | | | | | | (_) | | | | |      | |    |  __/ | (__  | | | |
  \\____/  |_| |_|  \\___/  |_| |_|      |_|     \\___|  \\___| |_| |_| v1.0 BETA
    """

    print("#" * 67)
    print(intro)
    print("#" * 67 + "\n")

    menu_Text = """
 [ 1 ] Procurar directórios.
 [ 2 ] Definir pasta base.
 [ 3 ] Sair.
"""
    print(Fore.YELLOW + menu_Text)

    if path_Main == "":
        print(Fore.RED + "Sem pasta base" + Style.RESET_ALL )
    else:
        print(Fore.GREEN + "Pasta base definida!" + Style.RESET_ALL )

    while True:
        try:
            print("\n")
            option = int(input("Escolha uma opção do menu: "))

            if option == 1:
                os.system("cls" if os.name == "nt" else "clear")
                print(search_text)
                dirFinder()
                break
            elif option == 2:
                mainFolder()
                break
            elif option == 3:
                break  # Define a variável de controle para False e sai do loop
            else:
                print(Fore.RED + "Por favor, escolha uma opção válida.")
        except:
            print(Fore.RED + "Por favor, escolha uma opção válida.")



def mainFolder():
    global path_Main
    global dados
    os.system("cls" if os.name == "nt" else "clear")

    intro = """
       _   _                         _______                 _     
      | | | |                       |__   __|               | |    
      | | | |__     ___    _ __        | |      ___    ___  | |__  
  _   | | | '_ \\   / _ \\  | '_ \\       | |     / _ \\  / __| | '_ \\ 
 | |__| | | | | | | (_) | | | | |      | |    |  __/ | (__  | | | |
  \\____/  |_| |_|  \\___/  |_| |_|      |_|     \\___|  \\___| |_| |_| v1.0 BETA
    """
    print("#" * 67)
    print(intro)
    print("#" * 67 )

    message = Fore.YELLOW+"Necessário definir caminho base."

    print("\n")
    if path_Main != "":
        message = Fore.GREEN+"Pasta base definida!"
    print(message)
    print("\nVocê pode definir copiando e colando o directório de destino,\nexemplo: C:\\User\\Downloads\\pasta-desejada")
    print("\n")
    print("Caminho atual: "+path_Main)
    print("\n")

    while True:
        print("Insira", Fore.YELLOW+ "[ 3 ]"+ Style.RESET_ALL +" para voltar ao menu.")
        search_dir = input("Ou defina o caminho base: ").strip()

        if search_dir == "3":
            menu()
            break
        
        if not search_dir:
            print("\n"+Fore.RED +"O campo não pode ficar vazio.")
            continue

        if not os.path.exists(search_dir):
            print("\n"+Fore.RED +"Caminho especificado não existe.")
            continue
        
        confirm = input("\nQuer definir " + Fore.YELLOW + search_dir + Style.RESET_ALL + " como pasta base? (S/N): ").strip()
        if confirm.upper() == "S":
            path_Main = search_dir

            dados["dirBase"] = path_Main

            # Salve o JSON modificado de volta no arquivo
            with open('data.json', 'w', encoding='utf-8') as json_file:
                json.dump(dados, json_file, ensure_ascii=False)

            menu()
            break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("#" * 67)
            print(intro)
            continue
        

def dirFinder():
    global dados

    while True:

        # Entrada
        input_str = input(Style.BRIGHT+Fore.BLUE+"\nDigite o texto da planilha, ou [ X ] para sair: "+Style.RESET_ALL )

        if input_str.lower() == 'x':
            menu()
            break

        # Substitua os caracteres especiais por espaços em branco
        input_str = re.sub(r'[/]', '', input_str)
        input_str = re.sub(r'[\\\n:]', ' ', input_str)

        input_words = input_str.lower().split()
        keywords = set(input_words)

        # Inicialize as variáveis
        regional = None
        cliente = None
        investimento = None
        anos = None
        dias = None

        # Verifica a correspondência da regional
        for key, values in dados["Regional"].items():
            if key.lower() in keywords:
                regional = values
                break

        # Verifica a correspondência do cliente
        if regional and regional in dados["Cliente"]:
            for cliente_info in dados["Cliente"][regional]:
                for key, values in cliente_info.items():
                    if key.lower() in keywords:
                        cliente = values
                        break

        # Verifica a correspondência de investimento, ano e dia
        for key, values in dados.items():
            #print(key)
            if key.lower() in ["investimento", "ano", "dia"]:
                for original_word, value in values.items():
                    if original_word.lower() in keywords:
                        if key == "Investimento":
                            investimento = value
                        elif key == "Ano":
                            anos = value
                        elif key == "Dia":
                            dias = value

        if regional is None or cliente is None or investimento is None or anos is None or dias is None:
            print(Fore.RED + "\nAlgum dos valores abaixo está incompleto, ou sem informações")
            
            valores = f"""
        Regional     :    {format_value(regional,"Nenhum")}
        Cliente      :    {format_value(cliente,"Nenhum")}
        Investimento :    {format_value(investimento,"Nenhum")}
        Ano          :    {format_value(anos,"Nenhum")}
        Dia          :    {format_value(dias,"Nenhum")}
            """
            print(valores)
            #dirFinder()
            continue

        else:

            # Montar o diretório com base nas variáveis
            directory = f'{path_Main}\\{regional}\\{cliente}\\{investimento}\\{anos}\\{dias}'

            if not os.path.exists(directory):
                print("\n" + Fore.RED + "Caminho base especificado não existe!")
                print("\n" + Fore.YELLOW + "\nCaminho: " + directory)
                #dirFinder()
                continue
            else:
                search(directory)
                break

# Defina os valores padrão e aplique a formatação de cor
def format_value(value, default_value):
    if value is None:
        formatted_value = f"{Fore.YELLOW}{default_value}{Style.RESET_ALL}"
    else:
        formatted_value = value
    return formatted_value


def search(dir):
    # print("\nProcurando pastas com arquivos no destino indicado.\n") COMBOS CLIENTE2 SUL P2 F24
    for root, dirs, files in os.walk(dir):
        if any(files):
            print("\n")
            print(Fore.GREEN + "Pasta com arquivos encontrada:", root)
            print("\n")
            

            if any(dirs):
                print(Fore.YELLOW+"PASTA(s)"+Style.RESET_ALL)
                for item in dirs:
                    #prefix = Fore.YELLOW+" < pasta > "+Style.RESET_ALL
                    #print(prefix + item)
                    print("   "+item)
            print("\n"+Fore.YELLOW+"ARQUIVO(s)"+Style.RESET_ALL)

            for item in files:
                #prefix = Fore.YELLOW+" < pasta > "+Style.RESET_ALL if item in dirs else Fore.YELLOW+" <<< arquivo >>> "+Style.RESET_ALL
                #print(prefix + item)
                print("   "+item)

            print("\n")
            print("Digite [ X ] para abrir o directório")
            confirm = input("Ou pressione Enter para continuar : ")
            
            if confirm.lower() == "x":
                subprocess.Popen(['explorer', dir])
                print("\n" + "#" * 67 )
                dirFinder()
                break
            
            else:
                print("\n" + "#" * 67 )
                dirFinder()
                break
        else:
            print("\n")
            print(Fore.YELLOW + "Nenhum arquivo encontrado no destino: ", root)

            print("\n" + "#" * 67 )
            dirFinder()

#Inicialize o main
if __name__ == "__main__":
    main()

