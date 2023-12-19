from flask import Flask, jsonify

app = Flask(__name__)

# Airport database (ICAO code as the key)
airport_db = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    # Add more airports as needed
}

@app.route('/airport/<string:icao>', methods=['GET'])
def get_airport_info(icao):
    airport_info = airport_db.get(icao.upper())  # Convert ICAO code to uppercase for case-insensitivity

    if airport_info:
        response = {"ICAO": icao.upper(), "Name": airport_info["Name"], "Location": airport_info["Location"]}
        return jsonify(response)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
