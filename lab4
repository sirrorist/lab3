import requests

API_URL = "https://api-inference.huggingface.co/models/KoichiYasuoka/bert-base-russian-upos"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": str(input())
})
i = 0
for o in output:
    print('Cлово - ', output[i]['word'], ', группа - ', output[i]['entity_group'], '\n')
    i = i + 1
