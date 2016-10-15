import pandas as pd
import numpy as np
from math import sqrt
from scipy.stats import chi2_contingency


def is_binary(col):
    try:
        valid = col[~np.isnan(col)]
        values = set(valid)
        return len(values) == 2
    except TypeError:
        return False


def filter_binary_cols(df):
    cols = [col for col in df.columns if is_binary(df[col])]
    return cols


def sort_cols(df, cols):
    # Sort columns by number of non-NA entries
    def size(col):
        return sum(~np.isnan(df[col]))
    return sorted(cols, key=size, reverse=True)


def read_data(path):
    return pd.read_csv(path)


def column(m, col):
    return m[col]


def norm(v):
    return sqrt(np.dot(v, v))


def contingency_table(x, y):
    xvals = list(set(x))
    yvals = list(set(y))
    contingency = np.array([np.zeros(len(xvals)) for _ in range(len(yvals))])
    for xv, yv in zip(x, y):
        xi = xvals.index(xv)
        yi = yvals.index(yv)
        contingency[yi][xi] += 1
    return contingency


def corr_str(x, y):
    contingency = contingency_table(x, y)
    chi2, p, dof, expected = chi2_contingency(contingency)
    return 1 - p


def correlation(v1, v2, f=corr_str):
    """v1 v2 are numpy vectors"""
    # Extract indices where they are defined
    validIndex = np.logical_and(~np.isnan(v1), ~np.isnan(v2))
    v1 = v1[validIndex]
    v2 = v2[validIndex]
    # What to do if one is zero?
    return f(v1, v2)


def correlation_matrix(df, cols=None):
    """df is a dataframe"""
    if not cols:
        cols = df.columns
    answer = []
    for col1 in cols:
        row = []
        for col2 in cols:
            if col1 == col2:
                row.append(np.double(0))
            else:
                row.append(correlation(df[col1], df[col2]))
        answer.append(row)
    return answer


def size(v):
    v = v[~np.isnan(v)]
    values = set(v)
    assert values == set([0.0, 1.0])
    return sum(v) / len(v)


def network_layout(corrs, sizes, labels):
    answer = {'nodes': [], 'edges': []}
    for id, size in enumerate(sizes):
        answer['nodes'].append({'id': 'n%s' % id,
                                'size': size,
                                'label': labels[id]})
    counter = 0
    for i, row in enumerate(corrs):
        for j, corr in enumerate(row):
            # Symmetric: only do one direction
            if i < j:
                answer['edges'].append(
                    {'id': 'e%s' % counter,
                     'source': 'n%s' % i,
                     'target': 'n%s' % j,
                     'weight': corr})
                counter += 1
    return answer


def data_network(df, cols, labels=None):
    labels = labels or cols
    df = df[cols]
    corr = correlation_matrix(df)
    sizes = [size(df[col]) for col in cols]
    network = network_layout(corr, sizes, labels)
    return network


def data_tree(df, cols, labels, name="root"):
    "Only use on categorical data"
    if cols:
        col = cols[0]
        rest = cols[1:]

        vals = set(v for v in df[col] if not np.isnan(v))
        children = []
        for val in vals:
            children.append(
                data_tree(df[df[col] == val], rest, labels, labels[col][val]))
        return {'name': name, 'children': children}
    else:
        return {'name':  name, 'size': len(df)}


def decorate_id_tree(tree, id=0):
    tree['id'] = id
    id += 1
    if tree.get('children'):
        for child in tree['children']:
            id = decorate_id_tree(child, id)
    return id


def _assign_attr_default(col, attr, vals):
    # Warning: Type hack
    return vals.get(int(float(attr)), "%s: %s" % (col, attr))
