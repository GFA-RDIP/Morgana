from flask import Flask, jsonify, request
from nodes import data_network, read_data, data_tree, filter_categorical_cols, sort_cols, decorate_id_tree
import pickle
import csv
from collections import defaultdict
app = Flask(__name__)

# To run locally (cross site scripting hack)
from flask_cors import CORS
cors = CORS(app)

data = read_data('HealthHack2016_Morgana_Data_permuted.csv')

# Variable, name
with open('variables.csv') as f:
    variables = [row for row in csv.DictReader(f)]
var_map = {r['variable']: r['name'] for r in variables}

# Variable, Value, Name, Shortname
with open('attributes.csv') as f:
    attributes = [row for row in csv.DictReader(f)]


var_attr_name = defaultdict(dict)
for row in attributes:
    variable = row['variable']
    name = row['shortname']
    # Hack to deal with pandas type conversion
    try:
        attribute = float(row['value'])
    except (TypeError, ValueError):
        pass
    var_attr_name[variable][attribute] = name
var_attr_name = dict(var_attr_name)


# Filter down to the good columns
cols = filter_categorical_cols(data)
cols = [col for col in cols if col in var_attr_name]
cols = sort_cols(data, cols)
data = data[['id'] + cols]


try:
    with open('network.dat', 'rb') as f:
        network_memo = pickle.load(f)
except FileNotFoundError:
    network_memo = {}


@app.route("/api/network")
def network(cols=cols, exclude=None, limit=None):
    limit = request.args.get('limit') or 40
    exclude = request.args.get('exclude')
    if exclude:
        cols = [col for col in cols if col not in exclude]
    if limit:
        limit = int(limit)
        cols = cols[:limit]

    if tuple(cols) not in network_memo:
        network_memo[tuple(cols)] = data_network(
            data, cols, [var_map[col] for col in cols])
        with open('network.dat', 'wb') as f:
            pickle.dump(network_memo, f)
    j = network_memo[tuple(cols)]
    return jsonify(j)

try:
    with open('sun.dat', 'rb') as f:
        sun_memo = pickle.load(f)
except FileNotFoundError:
    sun_memo = {}


@app.route("/api/sunburst")
def sunburst(cols=cols):
    limit = request.args.get('limit') or 5
    exclude = request.args.get('exclude')
    if exclude:
        cols = [col for col in cols if col not in exclude]
    if limit:
        limit = int(limit)
        cols = cols[:limit]
    if tuple(cols) not in sun_memo:
        sun_memo[tuple(cols)] = data_tree(data, cols, var_attr_name)
        with open('sun.dat', 'wb') as f:
            pickle.dump(sun_memo, f)
    j = sun_memo[tuple(cols)]
    return jsonify(j)


@app.route("/api/patient", methods=['GET', 'POST'])
def patient():
    selector = request.get_json(force=True)
    out_data = data[['id'] + selector.keys())]

    for var, val in selector.items():
        if val != "*":
            out_data=out_data[out_data[var] == val]
    with open('data.csv', 'w') as f:
        out_data.to_csv(f)

    # return jsonify(out_data)
    return jsonify({'url': 'http://localhost:8000/data.csv'})


if __name__ == "__main__":
    app.run()
