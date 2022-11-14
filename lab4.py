import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/KoichiYasuoka/bert-base-russian-upos"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

st.write("# Real Time Sentiment Analysis")
user_input = st.text_input("Please rate our services >>: ")

output = query({
	"inputs": str(user_input)
})
a = output.count()
i = 0
if a == 0:
	st.write("Введите предложение")
else:
	for o in output:
		st.write('Cлово - ', output[i]['word'], ', группа - ', output[i]['entity_group'], '\n')
		i = i + 1
