from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow Streamlit to communicate with the API

# Sample data - in a real app, this might come from a database
data = {
    'values': [10, 20, 30, 40, 50],
    'labels': ['A', 'B', 'C', 'D', 'E']
}

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/api/process', methods=['POST'])
def process_data():
    input_data = request.json
    # Process the data (example: multiply values by 2)
    result = {
        'processed_values': [val * 2 for val in input_data.get('values', [])],
        'original_labels': input_data.get('labels', [])
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
