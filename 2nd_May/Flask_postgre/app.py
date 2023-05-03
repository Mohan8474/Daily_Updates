from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:mohan8474@localhost:5432/flasksql"
db = SQLAlchemy(app)
app.app_context().push()
#migrate = Migrate(app, db)

class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"
    
class BikesModel(db.Model):
    __tablename__ = 'bikes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())


    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        

    def __repr__(self):
        return f"<Car {self.name}>"

class BikesandcarsModel(db.Model):
    __tablename__ = 'bikesandcars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())


    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        

    def __repr__(self):
        return f"<Car {self.name}>"

if __name__ == "__main__":
    db.create_all()
    db.session.commit()
    app.run(debug=True)