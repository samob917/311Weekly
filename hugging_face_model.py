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



#NEW MODEL
import requests

API_URL = "https://api-inference.huggingface.co/models/microsoft/tapex-base-finetuned-wikisql"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": {
		"query": "How many stars does the transformers repository have?",
		"table": {
			"Repository": ["Transformers", "Datasets", "Tokenizers"],
			"Stars": ["36542", "4512", "3934"],
			"Contributors": ["651", "77", "34"],
			"Programming language": [
				"Python",
				"Python",
				"Rust, Python and NodeJS"
			]
		}
	},
})