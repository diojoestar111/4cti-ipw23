def valida_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")  # remove os pontos e traços do CPF

    if len(cpf) != 11 or not cpf.isdigit():  # verifica se o CPF tem 11 dígitos e se todos são numéricos
        return False

    # calcula o primeiro dígito verificador
    soma = 0
    for i in range(0, 9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # calcula o segundo dígito verificador
    soma = 0
    for i in range(0, 10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    # verifica se os dígitos verificadores são iguais aos do CPF
    if cpf[-2:] == str(digito1) + str(digito2):
        return True
    else:
        return False
