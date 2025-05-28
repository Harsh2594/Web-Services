from flask import Flask,jsonify

#create the app
app = Flask(__name__)

#define a basic route
@app.route('/')
def home():
    return "Welcome to your first Flask API!"


# Define an API route
@app.route('/api/data')
def get_data():
    return jsonify({"name": "John", "language": "Python"})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)