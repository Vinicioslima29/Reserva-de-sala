from database import db

class Reserva(db.Model):
    id_sala = db.Column(db.Integer, primary_key=True, nullable=False)
    periodo = db.Column(db.String (100), nullable=False)
    data = db.Column (db.Date, nullable=False)
    tipo_de_sala = db.Column(db.String (100), nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False) #CHAVE ESTRANGEIRA --não sei se tenho que colocar id_turma como está em model_turma
  

