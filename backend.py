from flask import Flask, jsonify, request
from nodes import data_network, read_data, data_tree, filter_binary_cols, sort_cols
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
    name = row['name']
    attribute = float(row['value'])
    var_attr_name[variable][attribute] = name
var_attr_name = dict(var_attr_name)


# Filter down to the good columns
cols = filter_binary_cols(data)
cols = [col for col in cols if col in var_attr_name]
cols = sort_cols(data, cols)


@app.route("/api/network")
def network(cols=cols, exclude=None, limit=None):
    limit = request.args.get('limit')
    exclude = request.args.get('exclude')
    if exclude:
        cols = [col for col in cols if col not in exclude]
    if limit:
        limit = int(limit)
        cols = cols[:limit]

    j = data_network(data, cols, [var_map[col] for col in cols])
    return jsonify(j)


@app.route("/api/sunburst")
def sunburst(cols=cols):
    limit = request.args.get('limit') or 5
    exclude = request.args.get('exclude')
    if exclude:
        cols = [col for col in cols if col not in exclude]
    if limit:
        limit = int(limit)
        cols = cols[:limit]
    j = data_tree(data, cols, var_attr_name)
    return jsonify(j)

if __name__ == "__main__":
    app.run()
