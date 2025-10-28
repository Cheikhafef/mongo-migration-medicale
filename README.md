#  Migration de données CSV vers MongoDB
Ce projet contient un script Python permettant de migrer des données depuis un fichier CSV vers une base MongoDB locale. Il est conçu pour faciliter l'importation rapide de données tabulaires dans une base NoSQL, en vue d'analyse, de tests ou de prototypage.
##  Objectif de la migration
L'objectif est de transférer des données structurées (CSV) vers MongoDB en respectant les étapes suivantes :
1. **Lecture du fichier CSV** avec `pandas` pour bénéficier de sa robustesse en traitement de données.
2. **Transformation des lignes du CSV** en dictionnaires Python, format compatible avec MongoDB.
3. **Insertion en masse** dans une collection MongoDB via `insert_many`.
Ce processus permet de migrer efficacement des données sans passer par des outils tiers ou des interfaces graphiques.
## Prérequis
- Python 3.13
- MongoDB installé et en cours d'exécution sur `localhost:27017`
- Bibliothèques Python :
  ```bash
  pip install pandas pymongo

## Fonctionnement du script
#Document
Chaque ligne du fichier CSV devient un document JSON dans MongoDB. Un document est une unité de données composée de paires clé-valeur.
#exemple
{
_id:objectID('68fe19539b3006c9e4a1f9e8')
Name:"Bobby JacksOn"
Age:30
Gender:"Male"
Blood Type:"B-"
Medical Condition:"Cancer"
Date of Admission:"2024-01-31"
Doctor:"Matthew Smith"
Hospital:"Sons and Miller"
Insurance Provider:"Blue Cross"
Billing Amount:18856.281305978155
Room Number:328
Admission Type:"Urgent"
Discharge Date:"2024-02-02"
Medication:"Paracetamol"
Test Results:"Normal"}
#Collection (ma_collection)
L'ensemble des 5500 documents est regroupé dans une collection nommée ma_collection. Une collection joue un rôle similaire à une table dans une base de données relationnelle.

#Base de données (ma_base)
=======
#  Migration de données CSV vers MongoDB
Ce projet contient un script Python permettant de migrer des données depuis un fichier CSV vers une base MongoDB locale. Il est conçu pour faciliter l'importation rapide de données tabulaires dans une base NoSQL, en vue d'analyse, de tests ou de prototypage.
##  Objectif de la migration
L'objectif est de transférer des données structurées (CSV) vers MongoDB en respectant les étapes suivantes :
1. **Lecture du fichier CSV** avec `pandas` pour bénéficier de sa robustesse en traitement de données.
2. **Transformation des lignes du CSV** en dictionnaires Python, format compatible avec MongoDB.
3. **Insertion en masse** dans une collection MongoDB via `insert_many`.
Ce processus permet de migrer efficacement des données sans passer par des outils tiers ou des interfaces graphiques.
## Prérequis
- Python 3.13
- MongoDB installé et en cours d'exécution sur `localhost:27017`
- Bibliothèques Python :
  ```bash
  pip install pandas pymongo

## Fonctionnement du script
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

#Document
Chaque ligne du fichier CSV devient un document JSON dans MongoDB. Un document est une unité de données composée de paires clé-valeur.
#exemple
{
_id:objectID('68fe19539b3006c9e4a1f9e8')
Name:"Bobby JacksOn"
Age:30
Gender:"Male"
Blood Type:"B-"
Medical Condition:"Cancer"
Date of Admission:"2024-01-31"
Doctor:"Matthew Smith"
Hospital:"Sons and Miller"
Insurance Provider:"Blue Cross"
Billing Amount:18856.281305978155
Room Number:328
Admission Type:"Urgent"
Discharge Date:"2024-02-02"
Medication:"Paracetamol"
Test Results:"Normal"}
#Collection (ma_collection)
L'ensemble des 5500 documents est regroupé dans une collection nommée ma_collection. Une collection joue un rôle similaire à une table dans une base de données relationnelle.

#Base de données (ma_base)
>>>>>>> 6676fc8 (Initial commit : migration MongoDB + Docker setup)
La collection ma_collection est stockée dans une base de données MongoDB appelée ma_base. Cette base peut contenir plusieurs collections liées à des informations des clients