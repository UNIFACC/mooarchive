import toml
from pathlib import Path
import subprocess

categorias = toml.load('./vars/config.toml')
ids_categorias = categorias['categorias']['a_arquivar']

arquivamento = toml.load('./vars/config.toml')
arquivar_em = arquivamento['categorias']['arquivar_em']

def lista_disciplinas(categoria: int):
    cmd = f'sudo moosh -n course-list -c {str(categoria)} -i'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    saida = output.decode("utf-8")
    disciplinas = saida.split("\n")
    disciplinas = disciplinas[ : -1]
    return disciplinas