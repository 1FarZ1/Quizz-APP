import requests  
parameters={
    "amount" : 10,
    "type" : "boolean"
}
response=requests.get("https://opentdb.com/api.php?",params=parameters)
response.raise_for_status()
Data=response.json()
question_data=Data["results"]
