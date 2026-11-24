from fastapi import FastAPI,Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration,T5Tokenizer
import torch
import re
from fastapi.templating import Jinja2Templates #ui part
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

#initialize our fastapi app
app=FastAPI(title="Text Summarization App",description="text summarization using t5",version="1.0")

#load model and tokenizer
model=T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
tokenizer=T5Tokenizer.from_pretrained("./saved_summary_model")

#define device
if torch.backends.mps.is_available():
    device=torch.device("mps")
elif torch.cuda.is_available():
    device=torch.device("cuda")
else:
    device=torch.device("cpu")

model.to(device)

#templating
templates=Jinja2Templates(directory=".")

#input schema for dialogue=>string
class DialogueInput(BaseModel):
    dialogue:str


def clean_data(text):
    text=re.sub(r"\r\n"," ",text) #lines
    text=re.sub(r"\s+"," ",text) #spaces
    text=re.sub(r"<.*?>"," ",text) #html tags <p> <h1>
    text=text.strip().lower()
    return text


def summarize_dialogue(dialogue:str) -> str:
    dialogue=clean_data(dialogue) #clean

    #tokenize
    inputs=tokenizer(
        dialogue,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    ).to(device)
    

    #generate summary =>it will generate token ids
    model.to(device)
    targets=model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=150,
        num_beams=4,
        early_stopping=True
    )

    # token ids => convert to text(decoding)
    summary=tokenizer.decode(targets[0],skip_special_tokens=True) # in case of false some special tokems such as tags or\n will also print
    return summary


#API endpoints
@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):
    summary=summarize_dialogue(dialogue_input.dialogue)
    return {"summary":summary}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

