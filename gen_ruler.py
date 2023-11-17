import numpy as np


import pandas as pd
import itertools

import streamlit as st
import pandas as pd
import numpy as np

# init Table

# df = pd.DataFrame(
#     {
#         "Age": [10],
#         "Height": [10],
#         "Nutrition": [10],
#         "metrick": ["cof"],
#         "Value": [5.200000000000001],
#         "term": ["medium"],
#     }
# )


# df.to_csv("data.csv", index=False)


data = {
    "Age": ["puppy", "young", "adult", "senior"],
    "Weight": ["low", "litle low", "litle high", "high"],
    "Nutrition": ["bed", "less normal", "more normal", "extra good"],
}


value = {
    "Age": lambda x: 8 + x * -2,
    "Weight": lambda x: np.abs(round((-2 + x))),
    "Nutrition": lambda x: x * 3 - 1 * max(0, x - 1),
}
p = [
    "none to very little",
    "very low",
    "low",
    "medium",
    "above medium",
    "high",
    "extremely high",
]
rez = []
rez2 = []
for tupl in tuple(itertools.product(*[data[i] for i in data])):
    t = 0
    for index, param in enumerate(data):
        t += value[param](data[param].index(tupl[index]))
    rez2.append(t)
    t2 = (tupl, "low")
    t = min(max(t // 2 - 1, 0), len(p) - 1)

    t2 = (tupl, p[t])

    rez.append((t2))


print(rez)


number_count = {}
for num in rez2:
    if num in number_count:
        number_count[num] += 1
    else:
        number_count[num] = 1
rez = []
for i in number_count:
    rez.append(number_count[i])


chart_data = pd.DataFrame(rez, columns=["a"])


st.bar_chart(chart_data)


# from model3 import input_lvs


# data = {}
# for i in input_lvs:
#     data[i["name"]] = []
#     for i2 in i["terms"]:
#         data[i["name"]].append(i2)
# print(data)


# from model3 import output_lv

# data = []
# for i2 in output_lv["terms"]:
#     data.append(i2)

# # print(data)


[
    (("puppy", "low", "bed"), "above medium"),
    (("puppy", "low", "less normal"), "high"),
    (("puppy", "low", "more normal"), "extremely high"),
    (("puppy", "low", "extra good"), "extremely high"),
    (("puppy", "litle low", "bed"), "medium"),
    (("puppy", "litle low", "less normal"), "high"),
    (("puppy", "litle low", "more normal"), "extremely high"),
    (("puppy", "litle low", "extra good"), "extremely high"),
    (("puppy", "litle high", "bed"), "medium"),
    (("puppy", "litle high", "less normal"), "above medium"),
    (("puppy", "litle high", "more normal"), "high"),
    (("puppy", "litle high", "extra good"), "extremely high"),
    (("puppy", "high", "bed"), "medium"),
    (("puppy", "high", "less normal"), "high"),
    (("puppy", "high", "more normal"), "extremely high"),
    (("puppy", "high", "extra good"), "extremely high"),
    (("young", "low", "bed"), "medium"),
    (("young", "low", "less normal"), "above medium"),
    (("young", "low", "more normal"), "high"),
    (("young", "low", "extra good"), "extremely high"),
    (("young", "litle low", "bed"), "low"),
    (("young", "litle low", "less normal"), "above medium"),
    (("young", "litle low", "more normal"), "high"),
    (("young", "litle low", "extra good"), "extremely high"),
    (("young", "litle high", "bed"), "low"),
    (("young", "litle high", "less normal"), "medium"),
    (("young", "litle high", "more normal"), "above medium"),
    (("young", "litle high", "extra good"), "high"),
    (("young", "high", "bed"), "low"),
    (("young", "high", "less normal"), "above medium"),
    (("young", "high", "more normal"), "high"),
    (("young", "high", "extra good"), "extremely high"),
    (("adult", "low", "bed"), "low"),
    (("adult", "low", "less normal"), "medium"),
    (("adult", "low", "more normal"), "above medium"),
    (("adult", "low", "extra good"), "high"),
    (("adult", "litle low", "bed"), "very low"),
    (("adult", "litle low", "less normal"), "medium"),
    (("adult", "litle low", "more normal"), "above medium"),
    (("adult", "litle low", "extra good"), "high"),
    (("adult", "litle high", "bed"), "very low"),
    (("adult", "litle high", "less normal"), "low"),
    (("adult", "litle high", "more normal"), "medium"),
    (("adult", "litle high", "extra good"), "above medium"),
    (("adult", "high", "bed"), "very low"),
    (("adult", "high", "less normal"), "medium"),
    (("adult", "high", "more normal"), "above medium"),
    (("adult", "high", "extra good"), "high"),
    (("senior", "low", "bed"), "very low"),
    (("senior", "low", "less normal"), "low"),
    (("senior", "low", "more normal"), "medium"),
    (("senior", "low", "extra good"), "above medium"),
    (("senior", "litle low", "bed"), "none to very little"),
    (("senior", "litle low", "less normal"), "low"),
    (("senior", "litle low", "more normal"), "medium"),
    (("senior", "litle low", "extra good"), "above medium"),
    (("senior", "litle high", "bed"), "none to very little"),
    (("senior", "litle high", "less normal"), "very low"),
    (("senior", "litle high", "more normal"), "low"),
    (("senior", "litle high", "extra good"), "medium"),
    (("senior", "high", "bed"), "none to very little"),
    (("senior", "high", "less normal"), "low"),
    (("senior", "high", "more normal"), "medium"),
    (("senior", "high", "extra good"), "above medium"),
]
