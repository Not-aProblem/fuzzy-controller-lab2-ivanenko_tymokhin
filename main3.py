import random
import model3
import t2_mandani_inference
import streamlit as st
import pandas as pd
import t2_fuzzifier
import t2_plot
import t2_model_of_words

crisp = []  # [22, 185, 20, 50_000]

begin = {"Age": 14, "Weight": 19, "Nutrition": 10}


for i in ["Age", "Weight", "Nutrition"]:
    crisp.append(float(st.text_input(i, begin[i])))

type_pet = st.selectbox(
    "What type of pat?", ("Small_Breeds", "Medium_Breeds", "Large_Breeds")
)

metrick = st.selectbox("metrick type?", ("cog", "fom", "lom", "mom"))


crisp = [
    min(10, t2_fuzzifier.__normalization(v, model3.var_use[type_pet][i]))
    for i, v in enumerate(crisp)
]


if not "U" in model3.input_lvs[0].keys():
    t2_mandani_inference.preprocessing(model3.input_lvs, model3.output_lv)

val, word, x, fp1, EK4 = t2_mandani_inference.process(
    model3.input_lvs, model3.output_lv, model3.rule_base, crisp, metrick
)
st.title((val, word))

t2_plot.draw_t2_fuzzy_set(x, *EK4)
t2_plot.draw_t_1_fuzzy_area(x, fp1)
# t2_plot.draw_lv(model3.output_lv)
# t2_plot.draw_lv(model3.input_lvs)

t2_plot.draw_words_model(model3.output_lv)
t2_plot.draw_words_model(model3.input_lvs[0])
