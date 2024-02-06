import pickle
import streamlit as st
import pandas as pd

# Chargement du modèle XGBoost retenu
f = open('model.sav', 'rb')
model = pickle.load(f)

# Fonction de prédiction
def prediction(X_encode):
    prediction = model.predict(X_encode)
    print(prediction)
    return prediction

def main():

    # image
    st.image(r".\seattle.jpg", width=700, use_column_width=False)

    # Code HTML
    html = """
        <style>
            .center {
                text-align: center;
            }
            .custom-font {
                font-family: 'Bodoni MT', serif;
            }
            .small-font {
                font-size: 40px;  /* Ajustez la taille de la police selon vos besoins */
            }
        </style>
        <h1 class="center custom-font small-font" style="color: black;">Prédiction de la consommation annuelle d'énergie des propriétés de la ville de SEATTLE</h1>
         """
    # Affichage de la mise en forme
    st.markdown(html, unsafe_allow_html=True)

        # Petite description de la page
    st.divider()
    texte = """
    Bienvenue dans notre outil de prédiction de la consommation annuelle
    d'énergie des bâtiments non destinés à l’habitation de la ville de Seattle.
    Cet outil a été conçu pour anticiper et optimiser vos actions
    visant à maintenir une consommation énergétique efficiente.
    Veuillez renseigner les informations suivantes relatives aux propriétés
    pour voir les prédictions du modèle (Assurez-vous de remplir tous les champs).
    """

    # Ajouter du style CSS pour centrer le texte
    css_code = """
        <style>
            .justified-text {
                text-align: justify;
            }
        </style>
    """

    # Affichage du texte avec le style CSS
    st.markdown(css_code, unsafe_allow_html=True)
    st.markdown(f'<p class="justified-text">{texte}</p>', unsafe_allow_html=True)
    st.divider()

    # Créer les champs pour entrer les données recquis pour la prédiction
    # Utilisation principale
    type_prop = ['Hotel', 'Other', 'Mixed Use Property', 'University',
                'Small- and Mid-Sized Office', 'Self-Storage Facility',
                'Warehouse', 'K-12 School', 'Large Office',
                'Senior Care Community', 'Medical Office', 'Retail Store',
                'Hospital', 'Residence Hall', 'Distribution Center',
                'Worship Facility', 'Supermarket / Grocery Store', 'Laboratory',
                'Refrigerated Warehouse', 'Restaurant', 'Office']
    PrimaryPropertyType = st.sidebar.selectbox("Sélectionnez l'utilisation principale de la propriété",
                                               type_prop, index =0)
    # Quartier
    neigh = ['DOWNTOWN', 'NORTHEAST', 'EAST', 'LAKE UNION', 'GREATER DUWAMISH',
             'BALLARD', 'NORTHWEST', 'MAGNOLIA / QUEEN ANNE', 'CENTRAL',
             'SOUTHWEST', 'SOUTHEAST', 'NORTH', 'DELRIDGE']
    Neighborhood = st.sidebar.selectbox("Sélectionnez le quartier du Bâtiment", neigh, index=0)

    # Nombre de bâtiments
    NumberofBuildings = st.number_input("Le nombre de bâtiments dans la propriété", min_value=0, max_value=100)

    # Nombre d'étages
    NumberofFloors = st.number_input("Le nombre d'étages dans la propriété", min_value=0)

    # Superficie totale
    PropertyGFATotal = st.number_input("Superficie totale de la propriété (GFA)", min_value=0)

    # Utilisation de la vapeur (en kBtu)
    SteamUse = st.number_input("Quantité annuelle de vapeur consommée (en kBtu)", min_value=0)

    # Électricité (en kBtu)
    Electricity = st.number_input("Quantité annuelle d'electricité consommée (en kBtu)", min_value=0)

    # Gaz naturel (en kBtu)
    NaturalGas = st.number_input("Quantité annuelle de Gaz naturel consommée (en kBtu)", min_value=0)

    # Émissions totales de gaz à effet de serre
    TotalGHGEmissions = st.number_input("Émissions totales de gaz à effet de serre", min_value=0)

    # Type d'utilisation (Nombre)
    UseTypeNumber = st.number_input("Nombre de types d'utilisation de la propriété", min_value=0)

    # Âge du bâtiment
    Age_building = st.number_input("Âge du bâtiment", min_value=0)

    # Pourcentage de la superficie du plus grand sous-bâtiment par rapport à la superficie totale
    proplargestUseGFA = st.number_input("Pourcentage de la superficie du plus grand "
                                        "sous-bâtiment par rapport à la superficie totale.", min_value=0)

    # Effectuer la prédiction avec la fonction définie plus haut (prediction)
    # objet pour stocker le résultat
    pred =""
    # Créer le bouton 'Prédiction'
    if st.button("Prédiction") :
        # s'assurer que les champs sont tous remplis
        if (
                PrimaryPropertyType != "" and
                Neighborhood != "" and
                NumberofBuildings != "" and
                NumberofFloors != "" and
                PropertyGFATotal != "" and
                SteamUse != "" and
                Electricity != "" and
                NaturalGas != "" and
                TotalGHGEmissions != "" and
                UseTypeNumber != "" and
                Age_building != "" and
                proplargestUseGFA != ""
        ):
            # Récupérer les champs remplie dans la matrice X
            X = pd.DataFrame({
                'PrimaryPropertyType': [PrimaryPropertyType],
                'Neighborhood': [Neighborhood],
                'NumberofBuildings': [NumberofBuildings],
                'NumberofFloors': [NumberofFloors],
                'PropertyGFATotal': [PropertyGFATotal],
                'SteamUse(kBtu)': [SteamUse],
                'Electricity(kBtu)': [Electricity],
                'NaturalGas(kBtu)': [NaturalGas],
                'TotalGHGEmissions': [TotalGHGEmissions],
                'UseTypeNumber': [UseTypeNumber],
                'Age_building': [Age_building],
                'proplargestUseGFA': [proplargestUseGFA]
            })
            # Transformer les variables catégorielles en dummy
            categorical_features = X.select_dtypes(include="object").columns
            X_encode = pd.get_dummies(data=X,
                                      columns=categorical_features,
                                      drop_first=True
                                      )
            # Effectuer la prédiction avec le modèle
            pred = prediction(X)
            st.success("**Consommation d'énergie annuelle prédite (en kBtu) :**")
            st.success(pred, icon="✅")
        else:
            st.success("Assurez-vous que tous les champs sont remplis.")
if __name__=='__main__':
    main()
