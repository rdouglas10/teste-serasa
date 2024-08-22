from flask import Blueprint, request, jsonify
from models.produtor_models import db, Produtor
from schemas.produtor_schemas import ProdutorSchema


produtor_bp = Blueprint('produtor_bp', __name__)
produtor_schema = ProdutorSchema()
produtores_schema = ProdutorSchema(many=True)


@produtor_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"message": "Hello word!"}), 200


@produtor_bp.route('/produtores', methods=['POST'])
def add_produtor():
    try:
        data = request.get_json()
        produtor = Produtor(
            cpf_cnpj=data['cpf_cnpj'],
            nome_produtor=data['nome_produtor'],
            nome_fazenda=data['nome_fazenda'],
            cidade=data['cidade'],
            estado=data['estado'],
            area_total=data['area_total'],
            area_agricultavel=data['area_agricultavel'],
            area_vegetacao=data['area_vegetacao'],
            culturas=data['culturas']
        )
        
        valid, message = produtor.validate()
        if not valid:
            return jsonify({'error': message}), 400
        db.session.add(produtor)
        db.session.commit()        
        result = produtor_schema.dump(produtor)
        return jsonify(result), 201
    except Exception as e:
        return {"Error": str(e)}

@produtor_bp.route('/produtores/<int:id>', methods=['PUT'])
def update_produtor(id):
    produtor = Produtor.query.get_or_404(id)
    data = request.get_json()
    produtor.cpf_cnpj = data.get('cpf_cnpj', produtor.cpf_cnpj)
    produtor.nome_produtor = data.get('nome_produtor', produtor.nome_produtor)
    produtor.nome_fazenda = data.get('nome_fazenda', produtor.nome_fazenda)
    produtor.cidade = data.get('cidade', produtor.cidade)
    produtor.estado = data.get('estado', produtor.estado)
    produtor.area_total = data.get('area_total', produtor.area_total)
    produtor.area_agricultavel = data.get('area_agricultavel', produtor.area_agricultavel)
    produtor.area_vegetacao = data.get('area_vegetacao', produtor.area_vegetacao)
    produtor.culturas = data.get('culturas', produtor.culturas)
    valid, message = produtor.validate()
    if not valid:
        return jsonify({'error': message}), 400
    db.session.commit()
    result = produtor_schema.dump(produtor)

    return jsonify(result), 200

@produtor_bp.route('/produtores/<int:id>', methods=['DELETE'])
def delete_produtor(id):
    produtor = Produtor.query.get_or_404(id)
    db.session.delete(produtor)
    db.session.commit()
    return '', 204

@produtor_bp.route('/produtor/<int:id>', methods=['GET'])
def get_produtor(id):
    produtor = Produtor.query.get_or_404(id)
    result = produtor_schema.dump(produtor)

    return jsonify(result), 200
