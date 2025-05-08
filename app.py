from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

DATABASE = 'sql_murder_mystery.db'

# Helper function to get a database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# API endpoint to execute player SQL queries
@app.route('/api/execute-query', methods=['POST'])
def execute_query():
    data = request.get_json()
    query = data.get('query', '')

    # Basic validation: only allow SELECT queries
    if not query.strip().lower().startswith('select'):
        return jsonify({'error': 'Only SELECT queries are allowed.'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.execute(query)
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        results = [dict(zip(columns, row)) for row in rows]
        conn.close()
        return jsonify({'results': results})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# API endpoint to check the player's solution
@app.route('/api/check-solution', methods=['POST'])
def check_solution():
    data = request.get_json()
    murderer_id = data.get('murdererId')

    # The actual murderer is Laura White with PersonID 6
    if murderer_id == 6 or murderer_id == '6':
        return jsonify({'correct': True, 'message': 'Congratulations! You have solved the case!'}), 200
    else:
        return jsonify({'correct': False, 'message': 'Incorrect. Keep investigating!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
