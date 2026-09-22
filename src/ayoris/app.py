from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI(title='Ayoris',version='0.1.0')
class Health(BaseModel): status:str; service:str
@app.get('/health',response_model=Health)
def health(): return Health(status='ok',service='ayoris')
