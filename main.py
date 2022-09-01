# Imports
import shutil
import os
from pathlib import Path
from tkinter import *
from tkinter.filedialog import askdirectory


# Funções
def get_path():
    """Função que ira pegar o caminho da pasta selecionada para a organização"""
    global path  # Torna o caminho acessível por todo o código
    path = askdirectory()  # Abre a janela de seleção do arquivo
    path = Path(path)  # Transforma o arquivo para um caminho, exemplo: C:Usuarios/Downloads...)
    text_label.configure(text=f'Path: {path}', fg='#00FF1F')  # Muda o que esta escrito na text_label e a cor
    return path  # Retorna o Caminho da pasta selecionado


def organize():
    """Função que irá realizar a organização da pasta selecionada"""
    files = path.iterdir()  # files(arquivos) = path(caminho).iterdir()- Seleciona todos os arquivos
    for file in files:  # Percorre todos os arquivos dentro do caminho selecionado
        file_name, file_extension = os.path.splitext(
            file)  # Separa os arquivos em 2(duas) partes: nome_do_arquivo, extensao_do_arquivo

        if file_extension != '':  # Pastas, por padrão, não possuem extensão, assim conseguindo separar as pastas criadas (Evitando o programa de tentar mover uma das pastas de organização para dentro dela mesma) 
            if (path / Path(
                    file_extension.upper())).exists():  # Checa se no caminho selecionado existe uma pasta com o nome da extensão da mesma, se retornar True:
                shutil.move(file, Path(
                    path / file_extension.upper()))  # Move o arquivo para dentro da pasta que possue o nome de sua extensão

            if not (path / Path(file_extension.upper())).exists():  # Caso não possua uma pasta com o nome da extensão:
                Path(path / file_extension.upper()).mkdir()  # Cria uma pasta com o nome da extensão em maiúsculo
                shutil.move(file, Path(
                    path / file_extension.upper()))  # Move o arquivo para a pasta que possue o nome de sua extensão

        elif file_extension == '':  # Caso o arquivo seja uma pasta:
            pass  # Ignora


# Tkinter, interface gráfica
# Janela
root = Tk()  # Cria a janela
root.title('File organizer')  # Coloca um título
root.configure(bg='#515151')  # Muda a cor de fundo da janela

# Items
text_label = Label(root, text='Click there to select the file -->',
                   bg='#969696')  # Label: Utilizada para exibir textos.

path_button = Button(root, text='There', command=get_path, width=20,
                     bg='#969696')  # Button: Botão que executa a função get_path
organize_button = Button(root, text='Organizer', command=organize,
                         bg='#969696')  # Button: Botão que executa a função organize

# Grid
text_label.grid(row=0, column=0, padx=10, pady=10)  # Grid da label

path_button.grid(row=0, column=1, padx=10, pady=10)  # Grid do botão1
organize_button.grid(row=1, column=0, columnspan=2, padx=20)  # Grid do botão2

# Mainloop
root.mainloop()  # 'Looping' padrão do Tkinter que permite com que a 'interface' gráfica seja mostrada
