'''Exercice about cleaning data'''

###################################################
# Import pandas package in order to use csv files #
###################################################
import pandas as pd

# Importing data set
data = pd.read_csv('operations.csv')

# Correcting date problem
data['date_operation'] = pd.to_datetime(data['date_operation'])

# Creating new dataframe in order to stock missing values's dataframe
data_na = data.loc[data['montant'].isnull(),:]

# We get the index for every dataframe's lines
for index in data_na.index:
    # Amount is calculated from the previous and current balances
    data.loc[index, 'montant'] = data.loc[index+1, 'solde_avt_ope'] - data.loc[index, 'solde_avt_ope'] #

# Adding missing categorie by deduction
data.loc[data['categ'].isnull(), 'categ'] = 'FACTURE TELEPHONE'

# Deleting double data
data.drop_duplicates(subset=['date_operation', 'libelle', 'montant', 'solde_avt_ope'], inplace=True, ignore_index=True) #pylint: disable=all

# Replacing inconsistent value
data.loc[data['montant']==-15000, 'montant'] = -14.39

# Printing data
print(data)