from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ
#cpf_um = Cpf("15316267454")
#print(cpf_um)
exemplo_cnpj = "35379838000112"
exemplo_cpf = "11111111112"
#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))
documento = CpfCnpj(exemplo_cpf, 'cpf')
print(documento)

