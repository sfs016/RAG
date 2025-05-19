from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from morphik import Morphik
import os
import traceback

# initialize client as you already have
morphik = Morphik(uri=os.environ["MORPHIK_URI"])
app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
def query_endpoint(req: QueryRequest):
    try:
        # synchronous call
        resp = morphik.query(req.question)
        # extract the generated text and sources correctly
        return {
            "answer": resp.completion,
            "sources": resp.sources
        }
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
