from flask import Flask, request, jsonify
from nodes import data_network, read_data
app = Flask(__name__)

data = read_data('HealthHack2016_Morgana_Data_permuted.csv')


@app.route("/api/network")
def main():
    j = data_network(data, ['fh_food_allergy', 'dog', 'peanut_allergy_1y'])
    return jsonify(j)


# Later we will extract arguments from frontend
@app.route("/test")
def test():
    return jsonify(request.args)

if __name__ == "__main__":
    app.run()
