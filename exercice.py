'''Exercice about cleaning data'''
#pylint: disable=all 
###################################################
# Import pandas package in order to use csv files #
###################################################
import pandas as pd

class DataCleaner:
    """
    A class that represents a data cleaning tool for CSV files.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)

    def correct_date(self):
        """
        Correct the date format in the data.
        """
        self.data['date_operation'] = pd.to_datetime(self.data['date_operation'])

    def fill_missing_amounts(self):
        """
        Fill missing amounts in the data by calculating them from the previous and current balances.
        """
        data_na = self.data.loc[self.data['montant'].isnull(), :]

        for index in data_na.index:
            self.data.loc[index, 'montant'] = self.data.loc[index + 1, 'solde_avt_ope'] - self.data.loc[index, 'solde_avt_ope']

    def fill_missing_categories(self):
        """
        Fill missing categories in the data by setting them to a default value.
        """
        self.data.loc[self.data['categ'].isnull(), 'categ'] = 'FACTURE TELEPHONE'

    def remove_duplicates(self):
        """
        Remove duplicate rows from the data.
        """
        self.data.drop_duplicates(subset=['date_operation', 'libelle', 'montant', 'solde_avt_ope'], inplace=True, ignore_index=True)

    def replace_inconsistent_values(self):
        """
        Replace inconsistent values in the data.
        """
        self.data.loc[self.data['montant'] == -15000, 'montant'] = -14.39

    def save_data(self, file_path=None):
        """
        Save the cleaned data back to a CSV file.
        """
        if not file_path:
            file_path = self.file_path
        self.data.to_csv(file_path, index=False)


if __name__ == '__main__':
    # Example usage
    cleaner = DataCleaner('operations.csv')
    cleaner.correct_date()
    cleaner.fill_missing_amounts()
    cleaner.fill_missing_categories()
    cleaner.remove_duplicates()
    cleaner.replace_inconsistent_values()
    cleaner.save_data('cleaned_operations.csv')
