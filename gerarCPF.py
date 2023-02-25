import random

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

if __name__ == "__main__":
    print(getGerarCPF())
