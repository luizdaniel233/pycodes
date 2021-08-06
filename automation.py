import pandas as pd
import json
def escrever_json(lista):
    with open('meu_arquivo.json', 'w',encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)
data = pd.read_excel('/home/luiz/Desktop/git/umbrella/plan_test.xlsx',sheet_name='MONITORIA PREVENTIVA LANE M')
new = []
dict = {}
#new.append(dict)
for i in data:
    for j in data[i]:
        if i != "NaN":
            if j != "NaN":
                dict.update({i:j})
                new.append(dict)
escrever_json(new)