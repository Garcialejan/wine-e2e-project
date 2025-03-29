import os
import numpy as np
import pandas as pd
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

from src.wine_e2e_project.pipeline.prediction_pipeline import PredictionPipeline

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# Definimos un modelo de datos utilizando Pydantic para validar los datos
# enviados en el formulario. Recordar que cuando defines un modelo Pydantic
# como parámetro en una ruta, FastAPI automáticamente espera que los datos
# sean enviados en formato JSON
class FormData(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

@app.get("/", response_class=HTMLResponse) # Display homepage
async def home_page(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.get("/train", response_class=HTMLResponse) # Train the pipeline
async def trainning(request:Request):
    try:
        os.system("python main.py") # To execute the main.py as a comand on the CMD
        return "Trainning succesful"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Training failed: {str(e)}")


@app.post("/predict", response_class=HTMLResponse)
async def predict(request:Request, data: FormData):
    try:
        input_data = [
            data.fixed_acidity,
            data.volatile_acidity,
            data.citric_acid,
            data.residual_sugar,
            data.chlorides,
            data.free_sulfur_dioxide,
            data.total_sulfur_dioxide,
            data.density,
            data.pH,
            data.sulphates,
            data.alcohol
            ]
        
        input_data = np.array(input_data).reshape(1, 11)
        
        obj = PredictionPipeline()
        predict = obj.predict(input_data)

        return templates.TemplateResponse(
            "results.html",
            {"request": request,
             "prediction": str(predict)}
            )

    except Exception as e:
        print('The Exception message is: ',e)
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
    

@app.get("/predict", response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)