Ce dossier est composé de 3 sous dossiers : data, notebooks et appli_prediction

data :
Il contient le dataset initial (2016_Building_Energy_Benchmarking.csv) 
et le jeu de données obtenu après apurement (building-energy-apure.csv)

notebooks :
Vous trouverez à l'intérieur de ce dossier 3 notebooks : EDA_cleaning, modelisation_ini, modelisation_EScore

	EDA_cleaning : contient l'ensemble des codes utilisés 
	pour l'analyse exploratoire, l'apurement et le feature ingineering.

	modelisation_ini : contient les différents modèles testés et leurs
	 résultats sans y inclure l'EnergyStarScore.

	modelisation_EScore : contient les différents modèles testés et leurs 
	résultats qui inclue l'EnergyStarScore dans les variables explicatives.

	les 2 modélisation étant effectuée dans le but d'évaluer l’intérêt 
	de l’ENERGY STAR Score pour la prédiction de consommation d’énergie.

appli_prediction :
Il renferme la sauvegarde du modèle final retenu (model.sav) et le code python 
de l'application de prédiction (main.py) avec le modèle retenu en utilisant streamlit.
