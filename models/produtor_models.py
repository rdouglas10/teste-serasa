from . import db
from validate_docbr import CPF, CNPJ

class Produtor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpf_cnpj = db.Column(db.String(18), nullable=False)
    nome_produtor = db.Column(db.String(100), nullable=False)
    nome_fazenda = db.Column(db.String(100), unique=True, nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    area_total = db.Column(db.Float, nullable=False)
    area_agricultavel = db.Column(db.Float, nullable=False)
    area_vegetacao = db.Column(db.Float, nullable=False)
    culturas = db.Column(db.String, nullable=False)

    def validate(self):
        cpf_validator = CPF()
        cnpj_validator = CNPJ()

        if len(self.cpf_cnpj) <= 11:
            if not cpf_validator.validate(self.cpf_cnpj):
                return False, 'CPF inválido'
        else:
            if not cnpj_validator.validate(self.cpf_cnpj):
                return False, 'CNPJ inválido'

        # Usar comparação direta com floats
        if int(self.area_agricultavel) + int(self.area_vegetacao) > int(self.area_total):
            return False, 'A soma das áreas agricultável e de vegetação não pode exceder a área total'
        return True, ''

    @staticmethod
    def is_valid_cpf(cpf):
        cpf_validator = CPF()
        return cpf_validator.validate(cpf)

    @staticmethod
    def is_valid_cnpj(cnpj):
        cnpj_validator = CNPJ()
        return cnpj_validator.validate(cnpj)
