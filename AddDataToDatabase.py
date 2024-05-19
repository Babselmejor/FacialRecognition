import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://projetia-754d3-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "852741":
        {
            "Nom": "Emily Blunt",
            "Discipline": "Génie Civil",
            "Première_année": 2021,
            "Assiduité": 12,
            "Note": "B",
            "Année": 1,
            "Dernière_Présence": "2022-12-11 00:54:34"
        },
"963852":
        {
            "Nom": "Elon Musk",
            "Discipline": "Mécanique",
            "Première_année": 2020,
            "Assiduité": 7,
            "Note": "G",
            "Année": 2,
            "Dernière_Présence": "2022-12-11 00:54:34"
        },
"1":
    {
            "Nom": "Marc Zuck",
            "Discipline": "Gestion",
            "Première_année": 2020,
            "Assiduité": 7,
            "Note": "G",
            "Année": 2,
            "Dernière_Présence": "2022-12-11 00:54:34"
        },
"2":
        {
            "Nom": "Aziz Gueye",
            "Discipline": "Informatique",
            "Première_année": 2021,
            "Assiduité": 7,
            "Note": "G",
            "Année": 2,
            "Dernière_Présence": "2022-12-11 00:54:34"
        },
"3":
        {
            "Nom": "Jordan",
            "Discipline": "Informatique",
            "Première_année": 2021,
            "Assiduité": 7,
            "Note": "G",
            "Année": 2,
            "Dernière_Présence": "2022-12-11 00:54:34"
        },
"4":
        {
            "Nom": "Babacar Sene",
            "Discipline": "Technicien Sup",
            "Première_année": 2022,
            "Assiduité": 7,
            "Note": "G",
            "Année": 2,
            "Dernière_Présence": "2022-12-11 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)