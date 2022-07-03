import sqlalchemy as db

def connect():
    engine = db.create_engine('sqlite:///:memory:', echo=True)

def init():
    connect()
    print("init")
