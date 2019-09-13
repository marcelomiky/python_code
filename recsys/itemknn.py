import pandas as pd
import numpy as np

database_file = 'database.csv'

database_set = pd.read_csv(database_file, sep='\t', header=None, encoding="utf-8-sig")
rows, cols = database_set.shape


def adj_cos(list_i, list_j):

    if len(list_i) != len(list_j):
        print("The lists must have the same length!")
        return 0

    numerator = 0
    new_list_1 = list()
    new_list_2 = list()

    for i in range(len(list_i)):
        numerator += list_i[i] * list_j[i]
        new_list_1.append(list_i[i] ** 2)
        new_list_2.append(list_j[i] ** 2)

    denominator = np.sqrt(sum(new_list_1) * sum(new_list_2))

    if denominator != 0:
        return numerator/denominator


def matrix_adj_cos(database_set):
    num_users, num_items = database_set.shape
    list_mean_rating = list()

    for i in range(num_users):
        temp_list = np.array(database_set.loc[i])
        list_mean_rating.append(temp_list[~np.isnan(temp_list)].mean())

    for i in range(num_users):
        database_set.loc[i] = database_set.loc[i] - list_mean_rating[i]

    return database_set


matrix_adj_cos = matrix_adj_cos(database_set)

i = 0
j = 2

list_i = matrix_adj_cos.loc[:, i]
list_j = matrix_adj_cos.loc[:, j]

# print("list_i:\n", list_i)
# print("list_j:\n", list_j)

index_nan_i = list(list_i.index[list_i.apply(np.isnan)])
index_nan_j = list(list_j.index[list_j.apply(np.isnan)])

index_all = list(set(index_nan_i + index_nan_j))

print(index_all)

for i in index_all:
    del list_i[i]
    del list_j[i]

list_i = list(list_i)
list_j = list(list_j)

# print("list_i:\n", list_i)
# print("list_j:\n", list_j)

print(adj_cos(list_i, list_j))
