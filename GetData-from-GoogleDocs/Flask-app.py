from flask import Flask, jsonify
from flask_cors import CORS
from extractor import get_data_google_docs

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    df = get_data_google_docs()
    datos = df.to_dict(orient='records')
    return jsonify(datos)


if __name__ == '__main__':
    app.run(debug=True)
