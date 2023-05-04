from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
from sqlalchemy.dialects.postgresql import insert

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:mohan8474@localhost:5432/upsertsql"
db = SQLAlchemy(app)
app.app_context().push()
#migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

@app.route('/users', methods=['POST'])
def upsert_user():
    user_data = request.get_json()

    stmt = insert(User).values(
        name=user_data['name'],
        email=user_data['email'])
    
    stmt =stmt.on_conflict_do_update(
        index_elements=['name'],
        set_={'email': user_data['email']}
    )

    db.session.execute(stmt)
    db.session.commit()

    return 'User upserted successfully'
if __name__ == "__main__":
    db.create_all()
    db.session.commit()
    app.run(debug=True)



