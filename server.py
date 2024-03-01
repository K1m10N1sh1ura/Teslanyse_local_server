import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Daten aus Excel-Datei lesen
data = pd.read_excel('TeslaNumbers.xlsx')

# Konvertieren Sie die Daten in ein JSON-Format
quartalszahlen = data.to_dict()

# Route für Quartalsdaten
@app.route('/quartalszahlen', methods=['GET'])
def get_quartalszahlen():
    return jsonify(quartalszahlen)

if __name__ == '__main__':
    # Listen on all network interfaces
    app.run(host='0.0.0.0', port=5001, debug=True)