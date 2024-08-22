from flask import Blueprint, jsonify
from models.produtor_models import db, Produtor

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/produtor/<string:cpf_cnpj>/totais', methods=['GET'])
def get_totais(cpf_cnpj):
    total_fazendas = Produtor.query.where(Produtor.cpf_cnpj == cpf_cnpj).count()
    total_area = db.session.query(db.func.sum(Produtor.area_total)).where(Produtor.cpf_cnpj == cpf_cnpj).scalar()
    return jsonify({
        'total_fazendas': total_fazendas,
        'total_area_hectares': total_area
    })
