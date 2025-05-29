from database import db

class Reserva(db.Model):
    __tablename__ = 'reserva'

    
    id_sala = db.Column(db.Integer, primary_key=True, nullable=False)
    periodo = db.Column(db.String (100), nullable=False)
    data = db.Column (db.Date, nullable=False)
    tipo_de_sala = db.Column(db.String (100), nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False) #CHAVE ESTRANGEIRA --não sei se tenho que colocar id_turma como está em model_turma
    turma = db.relationship("Turma", backref='reserva', lazy=True) 

    def __init__(self, id_sala, periodo, data, tipo_de_sala, turma_id):
        self.id_sala = id_sala
        self.periodo = periodo
        self.data = data
        self.tipo_de_sala = tipo_de_sala
        self.turma_id = turma_id


#CLASSES
class ReservaJaExiste(Exception):
    def __init__(self, msg="Erro, essa reserva já existe!"):
        self.msg = msg
        super().__init__(self.msg)

class FalhaAoReservar(Exception):
    def __init__(self, msg="Erro, falha ao fazer a reserva"):
        self.msg = msg
        super().__init__(self.msg)

def listar_reserva():
    reserva = Reserva.query.all()
    return reserva


