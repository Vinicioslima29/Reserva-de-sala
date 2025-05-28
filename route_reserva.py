from flask import Blueprint, request, jsonify
import requests
from  model_reserva import Reserva
from database import db

bp_reserva = Blueprint('bp_reserva', __name__)

def validar_turma(id_turma):
    resposta = requests.get(f"http://localhost:5002/turma/{id_turma}")
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
