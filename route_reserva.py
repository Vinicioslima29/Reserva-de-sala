from flask import Blueprint, request, jsonify
import requests
from  model_reserva import Reserva
from database import db

bp_reserva = Blueprint('bp_reserva', __name__)

def validar_turma(turma_id):
    resposta = requests.get(f"http://localhost:5002/turma/{turma_id}")
    return resposta.status_code == 200

@bp_reserva.route('/reserva', methods=['GET'])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([
        {
            "id_sala": res.id_sala,
            "periodo": res.periodo,
            "data": res.data,
            "tipo_de_sala": res.tipo_de_sala,
            "turma_id": res.turma_id,
        } for res in reservas
    ])

@bp_reserva.route('/reserva/<int:id_reserva>', methods=["GET"])
def achar_reserva(id_reserva):
    reserva = Reserva.query.get(id_reserva)
    
    if reserva is None:
        return jsonify({"msg": "Reserva não encontrada!"}), 404
    
    return jsonify([
        {
            "id_sala": res.id_sala,
            "periodo": res.periodo,
            "data": res.data,
            "tipo_de_sala": res.tipo_de_sala,
            "turma_id": res.turma_id,
        } for res in reserva
    ])

@bp_reserva.route("/reserva", methods=["POST"])
def criar_reserva():
    dados = request.json
    turma_id = dados.get("turma_id")

    if not validar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400

    reserva = Reserva(
        id_sala = dados.get("id_sala"),
        periodo = dados.get("periodo"),
        data=dados.get("data"),
        tipo_de_sala = dados.get("tipo_de_sala"),
        turma_id = dados.get("turma_id")
    )

    db.session.add(reserva)
    db.session.commit()

    return jsonify({"msg": "Sua reserva foi criada com sucesso!"}), 201