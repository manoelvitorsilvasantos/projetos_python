import random
from faker import Faker

class Validar:

    @staticmethod
    def getGerarCPF():
        novo_cpf = [random.randint(0, 9) for _ in range(9)]
        cpf = ''.join(filter(str.isdigit, novo_cpf))
    
    @staticmethod
    def verifica_cpf(cpf):
        # Remove quaisquer caracteres que não sejam dígitos
        cpf = ''.join(filter(str.isdigit, cpf))

        # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11:
            return False

        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False

        # Calcula o primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = soma % 11
        if resto < 2:
            digito1 = 0
        else:
            digito1 = 11 - resto

        # Verifica se o primeiro dígito verificador é válido
        if digito1 != int(cpf[9]):
            return False

        # Calcula o segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = soma % 11
        if resto < 2:
            digito2 = 0
        else:
            digito2 = 11 - resto

        # Verifica se o segundo dígito verificador é válido
        if digito2 != int(cpf[10]):
            return False

        # Se chegou aqui, o CPF é válido
        return True


    @staticmethod
    def getGerarCPF():
        novo_cpf = str([random.randint(0, 9) for _ in range(9)])
        cpf = ''.join(filter(str.isdigit, novo_cpf))
        lista = list(cpf)
        #print(lista)
        ncpf = [int(x) for x in lista]

        # calcular primeiro digito verificador
        soma = sum([i * v for i, v in enumerate(ncpf[::-1], start=2)])
        primeiro_digito = 11 - (soma % 11)
        if primeiro_digito > 9:
            primeiro_digito = 0
        ncpf.append(primeiro_digito)

        # calcula o segundo digito verificador
        soma = sum([i * v for i, v in enumerate(ncpf[::-1], start=2)])
        segundo_digito = 11 - (soma % 11)
        if segundo_digito > 9:
            segundo_digito = 0
        ncpf.append(segundo_digito)

        # formata o CPF com string
        novo_cpf = f'{ncpf[0:3]}.{ncpf[3:6]}.{ncpf[6:9]}-{ncpf[9:]}'
        frm = ''.join(filter(str.isdigit, novo_cpf))
        cpf_formatado = f'{frm[0:3]}.{frm[3:6]}.{frm[6:9]}-{frm[9:]}'
        return cpf_formatado
        

    @staticmethod
    def getRG(self, rg):
        # Remover pontos e traços do número de RG
        rg = rg.replace(".", "").replace("-", "")
    
        # Verificar se o número de RG tem 9 dígitos
        if len(rg) != 9:
            return False
    
        # Verificar se o número de RG contém apenas dígitos
        if not rg.isdigit():
            return False
    
        # Verificar se os dois primeiros dígitos são válidos
        uf_rg = int(rg[:2])
        if uf_rg < 1 or uf_rg > 28:
            return False
    
        # Verificar o dígito verificador
        soma = 0
        for i in range(8):
            soma += int(rg[i]) * (2 + i)
        dv = (11 - soma % 11) % 10
        if dv != int(rg[8]):
            return False
    
        # Se o número de RG passar por todas as verificações, é válido
        return True

    
    @staticmethod
    def menu():
        print("Validação de RG\n")
        while True:
            print("Escolha uma opção:")
            print("1. Validar número de RG")
            print("2. Gerar CPF válido")
            print("3. Verificar CPF é valido")
            print("0. Sair")
            opcao = input("Opção: ")
            if opcao == "1":
                rg = input("Digite o número de RG a ser validado: ")
                if Validar.getRG(rg):
                    print(f"O número de RG {rg} é válido.\n")
                else:
                    print(f"O número de RG {rg} é inválido.\n")
            elif opcao == "2":
                print(Validar.getGerarCPF())
            elif opcao == "3":
                meu_cpf = input("Digite o seu cpf {xxx.xxx.xxx-xx} >> ")
                if Validar.verifica_cpf(meu_cpf):
                    print("CPF Válido")
                else:
                    print("CPF Inválido")
                    
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    app = Validar()
    app.menu()
