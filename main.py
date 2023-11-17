import random
import model
import t2_mandani_inference

t2_mandani_inference.preprocessing(model.input_lvs, model.output_lv)

for _ in range(100):
    crisp_values = (random.randint(17, 100), random.randint(130, 200), random.randint(15, 50), random.randint(1000, 50000))
    result = t2_mandani_inference.process(model.input_lvs, model.output_lv, model.rule_base, crisp_values)
    print(result)