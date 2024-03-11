import os
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# read data from excel
data = pd.read_excel('TeslaNumbers.xlsx')
# convert data to json format
earnings = data.to_dict()

# route for data
@app.route('/tesla_earnings', methods=['GET'])
def get_data():
    return jsonify(earnings)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
