from fastapi import FastAPI, UploadFile, File
import json
import pandas as pd
import requests
from PIL import Image, ImageOps
import numpy as np
import random
from keras.models import load_model
import random
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload_image")
async def create_file(file: UploadFile=File(...)):
    file2store = await file.read()
    f = open("input.png", "wb")
    f.write(file2store)    
    image_path = "input.png"
    model = load_model('keras_model.h5')
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_path).convert('RGB')
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    class_names = ['French Fries', 'Ice Cream', 'Pizza', 'Sushi', 'Curry', 'Fried Rice']
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    return {'class_name': class_name, "estimated_calories": random.randint(200,700)}

