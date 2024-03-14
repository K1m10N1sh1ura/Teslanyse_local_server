import os
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Funktion zum Lesen der Daten aus einer Excel-Datei und Konvertieren in JSON
def read_excel_to_json(filename):
    data = pd.read_excel(filename)
    return data.to_dict()

# Route für Tesla Earnings
@app.route('/tesla_earnings', methods=['GET'])
def get_tesla_earnings():
    data = read_excel_to_json('TeslaNumbers.xlsx')
    return jsonify(data)

# Neue Route für wöchentliche Verkäufe in China
@app.route('/china_weekly_sales/2022', methods=['GET'])
def get_china_sales_2022():
    data = read_excel_to_json('TeslaChinaInsuredUnits2022.xlsx')
    return jsonify(data)
# Neue Route für wöchentliche Verkäufe in China
@app.route('/china_weekly_sales/2023', methods=['GET'])
def get_china_sales_2023():
    data = read_excel_to_json('TeslaChinaInsuredUnits2023.xlsx')
    return jsonify(data)
# Neue Route für wöchentliche Verkäufe in China
@app.route('/china_weekly_sales/2024', methods=['GET'])
def get_china_sales_2024():
    data = read_excel_to_json('TeslaChinaInsuredUnits2024.xlsx')
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
