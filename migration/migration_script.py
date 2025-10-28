<<<<<<< HEAD

```python
import pandas as pd
from pymongo import MongoClient
# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ma_base"]
collection = db["ma_collection"]
# Lecture du fichier CSV
df = pd.read_csv("C:/Users/cheik/Downloads/archive/healthcare_dataset.csv")
#  Transformation en dictionnaires
documents = df.to_dict(orient="records")
# Insertion dans MongoDB
collection.insert_many(documents)

