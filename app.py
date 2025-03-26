from flask import Flask
from flask_jwt_extended import JWTManager
from database.db import init_db
from routes.user_routes import user_bp, cadastro_bp
 
app = Flask(__name__)
app.config.from_pyfile('config.py')
 
jwt = JWTManager(app)
 
init_db()
 
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(cadastro_bp, url_prefix='/cadastro')
 
if __name__ == '__main__':
    app.run(debug=True)