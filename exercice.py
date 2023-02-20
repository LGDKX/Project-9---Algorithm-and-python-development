'''Exercice proposé pour nettoyer des données'''

# Import des librairies dont nous aurons besoin
import pandas as pd
import numpy as np

# On "importe" le jeu de donnée
data = pd.read_csv('operations.csv')

# On corrige le problème de la date
data['date_operation'] = pd.to_datetime(data['date_operation'])

# On créee un nouveau dataframe et on y stocke le dataframe des valeurs manquantes
data_na = data.loc[data['montant'].isnull(),:]

# Pour chaque ligne du dataframe on récupère les index
for index in data_na.index:
    # On calcule le montant à partir des soldes précédentes et actuelles
    data.loc[index, 'montant'] = data.loc[index+1, 'solde_avt_ope'] - data.loc[index, 'solde_avt_ope'] #

# On ajoute la catégorie manquante obtenue par déduction logique
data.loc[data['categ'].isnull(), 'categ'] = 'FACTURE TELEPHONE'

# On supprime la donnée en double
data.drop_duplicates(subset=['date_operation', 'libelle', 'montant', 'solde_avt_ope'], inplace=True, ignore_index=True) #pylint: disable=all

# On remplace la valeur incohérente
data.loc[data['montant']==-15000, 'montant'] = -14.39

print(data)