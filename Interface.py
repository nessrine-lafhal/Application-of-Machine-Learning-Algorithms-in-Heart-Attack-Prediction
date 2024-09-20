import pandas as pd
from sklearn.svm import SVC
from tkinter import *

# Charger les données CSV
data = pd.read_csv(r"C:\Users\Nessrine\Desktop\IA_project\heart.csv")

# Diviser les données en features (X) et target (y)
X = data.drop(columns=['output'])
y = data['output']

# Entraîner un modèle SVM
model = SVC(kernel='linear')
model.fit(X, y)

# Fonction pour faire des prédictions
def predict():
    age = int(age_entry.get())
    sex = int(sex_entry.get())
    cp = int(cp_entry.get())
    trtbps = int(trtbps_entry.get())
    chol = int(chol_entry.get())
    fbs = int(fbs_entry.get())
    restecg = int(restecg_entry.get())
    thalachh = int(thalachh_entry.get())
    exng = int(exng_entry.get())
    oldpeak = float(oldpeak_entry.get())
    slp = int(slp_entry.get())
    caa = int(caa_entry.get())
    thall = int(thall_entry.get())

    # Faire une prédiction
    prediction = model.predict([[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]])
    
    if prediction[0] == 1:
        result_label.config(text="Risque de maladie cardiaque.", fg="red")
    else:
        result_label.config(text="Pas de risque de maladie cardiaque.", fg="green")

# Créer l'interface utilisateur
root = Tk()
root.title("Prédiction de maladie cardiaque")

# Définir une taille de fenêtre plus grande
root.geometry("800x600")

# Ajouter un titre et un paragraphe d'introduction avec une taille de police plus grande
title_label = Label(root, text="Prédiction de maladie cardiaque", font=("Helvetica", 36, "bold"), fg="blue")
title_label.grid(row=0, columnspan=2)

intro_text = "Bienvenue dans notre application de prédiction de maladie cardiaque. Veuillez saisir les informations requises ci-dessous pour obtenir une prédiction."
intro_label = Label(root, text=intro_text, wraplength=700, justify="center", font=("Helvetica", 18))
intro_label.grid(row=1, columnspan=2)

# Labels et entries pour chaque feature avec une taille de police plus grande
features = ['Age', 'Sex', 'Cp', 'Trtbps', 'Chol', 'Fbs', 'Restecg', 'Thalachh', 'Exng', 'Oldpeak', 'Slp', 'Caa', 'Thall']
for i, feature in enumerate(features):
    Label(root, text=feature, font=("Helvetica", 16)).grid(row=i+2, column=0)
    Entry(root, width=10, justify='center').grid(row=i+2, column=1)

# Bouton pour faire la prédiction avec une taille de police plus grande
predict_button = Button(root, text="Prédire", command=predict, font=("Helvetica", 18))
predict_button.grid(row=len(features)+2, columnspan=2)

# Label pour afficher le résultat avec une taille de police plus grande
result_label = Label(root, text="", font=("Helvetica", 20))
result_label.grid(row=len(features)+3, columnspan=2)

# Récupérer les entries
age_entry = root.grid_slaves(row=2, column=1)[0]
sex_entry = root.grid_slaves(row=3, column=1)[0]
cp_entry = root.grid_slaves(row=4, column=1)[0]
trtbps_entry = root.grid_slaves(row=5, column=1)[0]
chol_entry = root.grid_slaves(row=6, column=1)[0]
fbs_entry = root.grid_slaves(row=7, column=1)[0]
restecg_entry = root.grid_slaves(row=8, column=1)[0]
thalachh_entry = root.grid_slaves(row=9, column=1)[0]
exng_entry = root.grid_slaves(row=10, column=1)[0]
oldpeak_entry = root.grid_slaves(row=11, column=1)[0]
slp_entry = root.grid_slaves(row=12, column=1)[0]
caa_entry = root.grid_slaves(row=13, column=1)[0]
thall_entry = root.grid_slaves(row=14, column=1)[0]

root.mainloop()
