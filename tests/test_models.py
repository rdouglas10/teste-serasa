import pytest
from models.produtor_models import Produtor
from validate_docbr import CPF, CNPJ

def test_valid_cpf():
    cpf = "12345678909"
    assert Produtor.is_valid_cpf(cpf)

def test_invalid_cpf():
    cpf = "12345678900"
    assert not Produtor.is_valid_cpf(cpf)

def test_valid_cnpj():
    cnpj = "12345678000195"
    assert Produtor.is_valid_cnpj(cnpj)

def test_invalid_cnpj():
    cnpj = "12345678000196"
    assert not Produtor.is_valid_cnpj(cnpj)
