import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# read data from excel
print("Load data")
data = pd.read_excel('TeslaNumbers.xlsx')
print("Data loaded")
# convert data to json format
earnings = data.to_dict()

# route for data
@app.route('/tesla_earnings', methods=['GET'])
def get_data():
    return jsonify(earnings)

if __name__ == '__main__':
    # Listen on all network interfaces
    print("Start server")
    app.run(host='0.0.0.0', debug=True)
    print("Server running")
    
