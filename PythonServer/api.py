from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/text/{text}")
async def text(text):
	stream = os.popen('python bert_sentiment_predict.py "' + text + '"')
	output = stream.read()
	output = output.rstrip("\n")
	output = output.split(",")
	return {"predicted" : output[0], "accuracy" : output[1]}
