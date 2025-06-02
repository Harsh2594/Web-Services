#(Main Entry File):
from flask import Flask
from users.routes import users_bp

app = Flask(__name__)

#Ragister the Blueprint:

app.register_blueprint(users_bp)

if __name__ == '__main__':
  app.run(debug=True)

  
