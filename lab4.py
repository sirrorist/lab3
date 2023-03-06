import streamlit as st
import requests


API_URL = (
  "https://api-inference.huggingface.co/models/KoichiYasuoka/bert-base-russian-upos"
)
headersy = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headersy, json=payload)
    return response.json()


st.write(
    "#Классификация слов в предложении на Русском языке по средством присвоения токенов"
)
user_input = st.text_input("Пожалуйста введите предложение >>: ")


output = query({
    "inputs": str(user_input)
})


# try:
# 	while True:
# 		for o in output:
# 			st.write('Cлово - ', output[i]['word'], ', группа - ', output[i]['entity_group'], '\n')
# 			i = i + 1
# except ValueError:
# 	st.write("Работаем только с предложениями")
a = len(output)
i = 0
if a == 1:
	st.write("Работаем только с предложениями")
else:
	for o in output:
		st.write('Cлово - ', output[i]['word'], ', группа - ', output[i]['entity_group'], '\n')
		i = i + 1
	st.write("Данную работу выполнили Максим Б. и Евгений В.") 
