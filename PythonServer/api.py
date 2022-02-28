from fastapi import FastAPI
import os
import copy_bert_sentiment_predict
from copy_bert_sentiment_predict import MyModel

app = FastAPI()
model = MyModel()

@app.get("/text/{text}")
async def text(text):
	MyModel()
	return model.predict(text)
