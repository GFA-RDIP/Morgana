import pandas as pd
import numpy as np
from math import sqrt
from scipy.stats import chi2_contingency
from functools import reduce


def is_binary(col):
    return is_categorical(col, 2)


def is_categorical(col, cats=5):
    try:
        valid = col[~np.isnan(col)]
        values = set(valid)
        return len(values) <= cats
    except TypeError:
        return False


def filter_binary_cols(df):
    return filter_categorical_cols(df, 2)


def filter_categorical_cols(df, cats=5):
    cols = [col for col in df.columns if is_categorical(df[col], cats)]
    return cols


def sort_cols(df, cols):
    # Sort columns by number of non-NA entries
    return sorted(cols, key=lambda x: length(df[x]), reverse=True)


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


def correlation_matrix(df, cols=None, binop=correlation):
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
                row.append(binop(df[col1], df[col2]))
        answer.append(row)
    return answer


def size(v):
    v = v[~np.isnan(v)]
    values = set(v)
    if 0.0 in values:
        return sum(v[v != 0.0]) / len(v)
    else:
        # Not numeric; just ignore the first thing seen for
        # demo purposes
        return sum(v[v != v[0]]) / len(v)


def length(v, w=None):
    if w is None:
        w = v
    vt = ~np.isnan(v)
    wt = ~np.isnan(w)
    valid = np.logical_and(vt, wt)
    return sum(valid)


def network_layout(corrs, sizes, labels, l):
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
                     'num': float(l[i][j]),
                     'weight': corr})
                counter += 1
    return answer


def data_network(df, cols, labels=None):
    labels = labels or cols
    df = df[cols]
    corr = correlation_matrix(df, cols)
    l = correlation_matrix(df, cols, length)
    sizes = [size(df[col]) for col in cols]
    network = network_layout(corr, sizes, labels, l)
    return network


def data_tree(df, cols, labels, name="root", variable=None, value=None):
    "Only use on categorical data"
    if cols:
        col = cols[0]
        rest = cols[1:]

        vals = set(v for v in df[col] if not np.isnan(v))
        children = []
        for val in vals:
            children.append(
                data_tree(df[df[col] == val], rest, labels, labels[col][val], col, val))
        ans = {'name': name, 'children': children}
        if variable:
            ans['_variable'] = variable
        if value:
            ans['_value'] = value
        return ans
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
