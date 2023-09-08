from cpf_cnpj import Documento
import re

'''
cpf_um = "11111111112"
#exemplo_cnpj = "35379838000112"
#exemplo_cpf = "11111111112"
documento = Documento.cria_documento(cpf_um)
print(documento)
'''

padrao = "\w{5,50}@[a-z]{3,10}.com.br"
texto = "aaabbbcc rodrigo123@gmail.com.br ccbbbaaa"
resposta = re.search(padrao, texto)

print(resposta.group())





