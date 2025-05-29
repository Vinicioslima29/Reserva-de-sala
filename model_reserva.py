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

class ReservaNaoEncontrada(Exception):
    def __init__(self, msg="Erro, esta reserva já existe!"):
        self.msg = msg
        super().__init__(self.msg)



#FUNÇÕES
def listar_reserva():
    reserva = Reserva.query.all()
    return reserva


def criar_reserva(nova_reserva):
    nova_reserva = Reserva(
        id_sala=nova_reserva['id_sala'], 
        periodo=nova_reserva['periodo'], 
        data=nova_reserva['data'], 
        tipo_de_sala=nova_reserva['tipo_de_sala'], 
        turma_id=nova_reserva['turma_id']

    )

    db.session.add(nova_reserva)
    db.session.commit()
    return {"Reserva criada com sucesso!"}, 200
