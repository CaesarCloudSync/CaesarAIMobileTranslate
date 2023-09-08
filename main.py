#https://thepythoncode.com/article/translate-text-in-python?utm_content=cmp-true
import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any, Dict, AnyStr, List, Union

from CaesarTranslate.caesarmobiletranslate import CaesarMobileTranslate

app = FastAPI()
caesamobiletrans = CaesarMobileTranslate()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class CaesarMobileTranslateReq(BaseModel):
    text:str
    dest:str

JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]
@app.get("/") # POST # allow all origins all methods.
async def home():
    return "Hello world to Caesar Mobile Translate."  
@app.post("/caesarmobiletranslate") # POST # allow all origins all methods.
async def caesarmobiletranslate(data : JSONStructure = None):  
    try:
        data = dict(data)#request.get_json()
        print(data)
        translation,dest,original,src = caesamobiletrans.translate(data["text"],data["dest"])

        return {"translation":translation,"dest":dest,"original":original,"src":src}
    except Exception as ex:
        return {"error":f"{type(ex)}-{ex}"}

async def main():
    config = uvicorn.Config("main:app", port=7860, log_level="info",host="0.0.0.0",reload=True) # Local
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())