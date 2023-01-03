import toml
from pathlib import Path
import subprocess

categorias = toml.load('./vars/config.toml')
ids_categorias = categorias['categorias']['a_arquivar']

arquivamento = toml.load('./vars/config.toml')
arquivar_em = arquivamento['categorias']['arquivar_em']
