import requests

API_URL = "https://api-inference.huggingface.co/models/microsoft/tapex-base-finetuned-wikisql"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def get_table_answer(question, df):
    output = query({
        "inputs": {
            "query": f"{question}",
            "table": f"{df}"        
        },
    })
    return output