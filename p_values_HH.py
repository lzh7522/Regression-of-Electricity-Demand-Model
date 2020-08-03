import csv
import numpy as np
import statsmodels.api as sm

filename = 'p_values_hh.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    contents = dict([(k, []) for k in header_row])
    for row in reader:
        i = 0
        for key in contents:
            contents[key].append(float(row[i]))
            i += 1

y = contents.pop(header_row[0])
x = []
for key in contents:
    x.append(contents[key])


def reg_y(y, x):
    ones = np.ones(len(x[0]))
    X = sm.add_constant(np.column_stack((x[0], ones)))
    for ele in x[1:]:
        X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results


x_temp = ['const']
for key in header_row[1:]:
    x_temp.append(key)
x_temp.reverse()

max_p_value = 1

while max_p_value > 0.05:
    results = reg_y(y, x)
    print(results.summary(xname=x_temp))
    p_values = results.pvalues
    p_values_list = p_values.tolist()
    max_p_value = max(p_values_list[:-1])
    min_p_value = min(p_values_list[:-1])
    max_index = p_values_list.index(max_p_value)
    del x[len(x)-max_index-1]
    del x_temp[max_index]
