from flask import Flask,jsonify

#create the app:
app = Flask(__name__)

#Define a basic route:
@app.route('/')
def homepage():
  return "Welcome to my first API"

#Define an API route:
@app.route('/api/data')
def get_data():
  return jsonify({
  "name": "Alice",
  "email": "alice@example.com"
  })

#Run the app:
if __name__ == '__main__':
  app.run(debug=True)
