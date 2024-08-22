def is_valid_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calculate_digit(cpf, weights):
        return sum(int(digit) * weight for digit, weight in zip(cpf, weights)) % 11

    first_digit = (calculate_digit(cpf[:9], range(10, 1, -1)) % 11) % 10
    second_digit = (calculate_digit(cpf[:10], range(11, 1, -1)) % 11) % 10

    return cpf[-2:] == f"{first_digit}{second_digit}"


def is_valid_cnpj(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))
    
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    def calculate_digit(cnpj, weights):
        return sum(int(digit) * weight for digit, weight in zip(cnpj, weights)) % 11

    first_digit = (calculate_digit(cnpj[:12], range(5, 1, -1)) % 11) % 10
    second_digit = (calculate_digit(cnpj[:13], range(6, 1, -1)) % 11) % 10

    return cnpj[-2:] == f"{first_digit}{second_digit}"

