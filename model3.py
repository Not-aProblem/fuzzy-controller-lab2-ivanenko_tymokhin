var_use = {
    "Small_Breeds": [(0, 15, 0.1), (0, 20, 0.1), (0, 11, 0.1)],
    "Medium_Breeds": [(0, 20, 0.1), (0, 40, 0.1), (0, 11, 0.1)],
    "Large_Breeds": [(0, 28, 0.1), (0, 70, 0.1), (0, 11, 0.01)],
}


input_lvs = [
    {
        "X": (0, 10.1, 0.1),
        "name": "Age",
        "terms": {
            "puppy": {
                "umf": ("trapmf", 0, 0, 0.55, 4.61),
                "lmf": ("trapmf", 0, 0, 0.09, 1.15, 1),
            },
            "young": {
                "umf": ("trapmf", 0.42, 2.25, 4.00, 5.41),
                "lmf": ("trapmf", 2.79, 3.21, 3.21, 0.34, 3.71),
            },
            "adult": {
                "umf": ("trapmf", 3.38, 5.50, 7.25, 9.02),
                "lmf": ("trapmf", 5.79, 6.28, 6.28, 0.33, 6.67),
            },
            "senior": {
                "umf": ("trapmf", 7.37, 9.36, 10, 10),
                "lmf": ("trapmf", 8.68, 9.91, 10, 10, 1),
            },
        },
    },
    {
        "X": (0, 10.1, 0.1),
        "name": "Weight",
        "terms": {
            "low": {
                "umf": ("trapmf", 0, 0, 0.55, 4.61),
                "lmf": ("trapmf", 0, 0, 0.09, 1.15, 1),
            },
            "litle low": {
                "umf": ("trapmf", 0.42, 2.25, 4.00, 5.41),
                "lmf": ("trapmf", 2.79, 3.21, 3.21, 0.34, 3.71),
            },
            "litle high": {
                "umf": ("trapmf", 3.38, 5.50, 7.25, 9.02),
                "lmf": ("trapmf", 5.79, 6.28, 6.28, 0.33, 6.67),
            },
            "high": {
                "umf": ("trapmf", 7.37, 9.36, 10, 10),
                "lmf": ("trapmf", 8.68, 9.91, 10, 10, 1),
            },
        },
    },
    {
        "X": (0, 10.1, 0.1),
        "name": "Nutrition",
        "terms": {
            "bed": {
                "umf": ("trapmf", 0, 0, 0.55, 4.61),
                "lmf": ("trapmf", 0, 0, 0.09, 1.15, 1),
            },
            "less normal": {
                "umf": ("trapmf", 0.42, 2.25, 4.00, 5.41),
                "lmf": ("trapmf", 2.79, 3.21, 3.21, 0.34, 3.71),
            },
            "more normal": {
                "umf": ("trapmf", 3.38, 5.50, 7.25, 9.02),
                "lmf": ("trapmf", 5.79, 6.28, 6.28, 0.33, 6.67),
            },
            "extra good": {
                "umf": ("trapmf", 7.37, 9.36, 10, 10),
                "lmf": ("trapmf", 8.68, 9.91, 10, 10, 1),
            },
        },
    },
]

output_lv = {
    "X": (0, 10.1, 0.1),
    "name": "Attractive level",
    "terms": {
        "none to very little": {
            "umf": ("trapmf", 0, 0, 0.59, 3.95),
            "lmf": ("trapmf", 0, 0, 0.09, 1.32, 1),
        },
        "very low": {
            "umf": ("trapmf", 0.28, 2.00, 3.00, 5.22),
            "lmf": ("trapmf", 1.79, 2.37, 2.37, 2.71, 0.48),
        },
        "low": {
            "umf": ("trapmf", 0.98, 2.75, 4.00, 5.41),
            "lmf": ("trapmf", 2.79, 3.30, 3.30, 3.71, 0.42),
        },
        "medium": {
            "umf": ("trapmf", 2.38, 4.50, 6.00, 8.18),
            "lmf": ("trapmf", 4.79, 5.12, 5.12, 5.35, 0.27),
        },
        "above medium": {
            "umf": ("trapmf", 4.02, 5.65, 7.00, 8.41),
            "lmf": ("trapmf", 5.89, 6.34, 6.34, 6.81, 0.40),
        },
        "high": {
            "umf": ("trapmf", 4.38, 6.50, 7.75, 9.62),
            "lmf": ("trapmf", 6.79, 7.25, 7.25, 7.91, 0.47),
        },
        "extremely high": {
            "umf": ("trapmf", 5.21, 8.27, 10, 10),
            "lmf": ("trapmf", 7.66, 9.82, 10, 10, 1),
        },
    },
}


rule_base = [
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
