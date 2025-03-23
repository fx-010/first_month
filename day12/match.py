lists = [
    "fnd17_oxlcxspebg", "fnd17_shsoutbs", "fnd28_value_05191q",
    "fnd28_value_05301q", "fnd28_value_05302q", "fnd17_pehigh",
    "fnd17_pelow", "fnd17-priceavg150day", "fnd17-priceavg200day",
    "fnd17_priceavg50day", "fnd17-pxedra", "fnd28_newa3_value_18191a",
    "fnd28_value_02300a", "mdl175_ebitda", "mdl175_pain"
]

# 公式模版
template = "ts_regression(ts_zscore({}, 500), ts_zscore({}, 500),500)"

# 存储所有生成公式
formulas = []

for i in range(len(lists)):
    for j in range(len(lists)):
        if i != j:       # 防止重复
            formula = template.format(lists[i],lists[j])
            formulas.append(formula)

print(f"共生成{len(formulas)}个公式：")

for formula in formulas:
    print(f"{formulas}")