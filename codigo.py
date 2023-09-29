import pyautogui
import time
import pandas

# Passo 1: Entrar no sistema da empresa

# tempo de cada tarefa
pyautogui.PAUSE = 0.5

# abrir o navegdor
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("Enter")
# acessar o link do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")

time.sleep(3) # tempo para carregar a pagina

# Passo 2: Fazer Login
pyautogui.click(x=547, y=391) # coordenadas do click do mouse para selecionar o campo email
pyautogui.write("meuemail@outlook.com")
pyautogui.press("tab") # esta ação é para ir ao campo senha
pyautogui.write("minhasenha")
# Esta ação é para ir no botão para fazer login no sistema apos inserir o email e senha.
pyautogui.press("tab")
pyautogui.press("Enter")

# Passo 3: Importar a base de dados de produtos

#foi criado uma variavel para importar o arquivo, assim facilita o uso quando for utilizar o loop
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar os produtos

# loop para cadastrar todos os itens do arquivo
for linha in tabela.index:

    
    #selecionar o primeiro campo
    pyautogui.click(x=518, y=277)
    
    #preesncher os campos
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # variavel criada para o if
    obs = tabela.loc[linha, "obs"]
    #este if para verificar se o obs não esta vazio para escrever no campo
    if not pandas.isna(obs):
        pyautogui.write(obs)   
        

    #apertar o botão enviar
    pyautogui.press("tab")
    pyautogui.press("Enter")
    
    # voltar ao topo da tela
    pyautogui.scroll(10000)

# Passo 5: Repitir o cadastro para todos os produtos