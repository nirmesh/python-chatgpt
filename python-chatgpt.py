import requests
api_endpoint="https://api.openai.com/v1/completions"
api_secret="xxx"
request_headers={
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+api_secret
}
request_data ={
    "model":"text-davinci-003",
    "prompt":"Write python script to get today's date. Write only code,no text",
    "max_tokens":100,
    "temperature":0.5


}
response = requests.post(api_endpoint,headers=request_headers,json=request_data)
if response.status_code ==200:
    print(response.json()["choices"][0]["text"])
else:
    print(f"Request failed with status code::{str(response.status_code)}")
    
