from database import db_serv

class Reservas (db_serv.Model):
    id_sala = db_serv.Column(db_serv.Integer, primary_key=True, nullable=False)
    periodo = db_serv.Column(db_serv.String (100), nullable=False)
    data = db_serv.Column (db_serv.Date, nullable=False)
    tipo_de_sala = db_serv.Column(db_serv.String (100), nullable=False)
    turma_id = db_serv.Column(db_serv.Integer, db_serv.ForeignKey('turma.id'), nullable=False) #CHAVE ESTRANGEIRA --não sei se tenho que colocar id_turma como está em model_turma
    turma = db_serv.relationship("Turma", back_populates="alunos") 


    def __init__(self, id_sala, periodo, data, tipo_de_sala, turma_id):
        self.id_sala = id_sala
        self.periodo = periodo
        self.data = data
        self.tipo_de_sala = tipo_de_sala
        self.turma_id = turma_id

#CLASSE PARA AS EXCEÇÕES
class ReservaJaExiste(Exception):
    def __init__(self, msg="Erro, essa reserva já existe!"):
        self.msg = msg
        super().__init__(self.msg)

class FalhaAoReservar(Exception):
    def __init__(self, msg="Erro, falha ao fazer a reserva"):
        self.msg = msg
        super().__init__(self.msg)

#FUNÇÕES
def listar_reserva():
    reserva = Reservas.query.all()
    return reserva

def criar_reserva(): #VINI VAI FAZER
    # gera_reserva = Reservas(
    #     id_sala =
    #)
    pass

