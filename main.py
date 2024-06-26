from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import RedirectResponse, JSONResponse
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from typing import List, Dict, Tuple
from nltk import download, ne_chunk

app = FastAPI()

download('punkt')
download('averaged_perceptron_tagger')
download('maxent_ne_chunker')
download('words')

    
@app.post("/tokenize/")
async def tokenize(text_input: Dict[str, str] = Body(...), tokenize_type: str = "word") -> Dict[str, List[str]]:
    
    """
    tokenize_type can be word or sent
    """
    
    try:
        
        text = " ".join(text_input.values())

        
        if tokenize_type == "word":
                        
            word_tokens = word_tokenize(text)
            
            return JSONResponse(content={
                "result": word_tokens
                })
            
        elif tokenize_type == "sent":
            
            sent_tokens = sent_tokenize(text_input.values())
            
            return JSONResponse(content={
                "result": sent_tokens
                })
        
        else:
            raise ValueError("tokenize_type must be word or sent!")
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{str(e)}")

@app.post("/postag/")
async def postag(text_input:  Dict[str, str]) -> Dict[str, Tuple]:
    try:
        
        text = " ".join(text_input.values())

        word_tokens = word_tokenize(text)

        postag_data = pos_tag(word_tokens, tagset='universal') 
        
        return JSONResponse(content={
            "result": postag_data
        })
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{str(e)}")


@app.post("/ner/")
async def ner(text_input:  Dict[str, str]) -> Dict[str, Tuple]:
    try:
        
        text = " ".join(text_input.values())
        
        word_tokens = word_tokenize(text)

        postag_data = pos_tag(word_tokens, tagset='universal') 
        
        entities = ne_chunk(postag_data)
        
        return JSONResponse(content={
            "result": entities
        })
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{str(e)}")

@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)