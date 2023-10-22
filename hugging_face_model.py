import requests
import json

API_URL = (
    "https://api-inference.huggingface.co/models/microsoft/tapex-base-finetuned-wikisql"
)
headers = {"Authorization": "Bearer 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"}


def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


def get_table_answer(question, df):
    output = query(
        {
            "inputs": {"query": f"{question}", "table": f"{df}"},
        }
    )
    return output
