from urllib3 import Retry
import constant as c

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

class WorldBankDataTransform:
    all = []
    def __init__(self, filename: str):
        self.filename = filename

        # Action
        WorldBankDataTransform.all.append(self)
    
    def specific_countries_time_series(self, country_list: list, save_file=False, filename_save=None):

        data = pd.read_csv(c.DATA_PATH+self.filename, skiprows = 3)

        data.drop(columns = ["Country Code", "Indicator Code", "Indicator Name"], inplace = True)
        data = data[data["Country Name"].isin(country_list)]
        data = data.rename(columns={'Country Name':'Year'})
        data = data.transpose()
        new_header = data.iloc[0]
        data = data[1:]
        data.columns = new_header
        data = data.dropna()
        data = data.astype(float)
        data.index = pd.to_datetime(data.index)

        if save_file==True and filename_save != None:
            data.to_csv(c.SAVE_DATA_PATH+filename_save)
            print(f'your csv file has been saved in {c.SAVE_DATA_PATH} as {filename_save}')

        return data
    
    def specific_year_cross_section():
        pass

    def __repr__(self):
        return f"WorldBankDataTransform('{self.filename}')"

class Visualization:
    all = []
    def __init__(self, filename):
        self.filename = filename

        # Action
        Visualization.all.append(self)

    def time_series(self, size: tuple, title: str, filename_save=None):

        data = pd.read_csv(c.SAVE_DATA_PATH+self.filename, index_col='Unnamed: 0', parse_dates=True)

        fig, ax = plt.subplots(figsize=size)
        sns.lineplot(data = data)
        ax.set_title(title)

        if filename_save != None:
            fig.savefig(c.SAVE_FIG_PATH+filename_save)
            return print(f"your pic has been saved in {c.SAVE_FIG_PATH} as {filename_save}")

    def correlation_map(self, size: tuple, title: str, filename_save=None):

        data = pd.read_csv(c.SAVE_DATA_PATH+self.filename, index_col='Unnamed: 0', parse_dates=True)

        fig, ax = plt.subplots(figsize=size)
        corr = data.corr()
        mask = np.triu(corr)
        sns.heatmap(corr, annot=True, mask=mask)
        ax.set_title(title)
        ax.set_xlabel('')
        ax.set_ylabel('')

        if filename_save != None:
            fig.savefig(c.SAVE_FIG_PATH+filename_save)
            return print(f"your pic has been saved in {c.SAVE_FIG_PATH} as {filename_save}")
    
    def boxplot(self, size: tuple, title: str, filename_save=None):

        data = pd.read_csv(c.SAVE_DATA_PATH+self.filename, index_col='Unnamed: 0', parse_dates=True)

        fig, ax = plt.subplots(figsize=size)
        sns.boxplot(data = data)
        ax.set_title(title)
        ax.set_ylabel('')
        ax.set_xlabel('')

        if filename_save != None:
            fig.savefig(c.SAVE_FIG_PATH+filename_save)
            return print(f"your pic has been saved in {c.SAVE_FIG_PATH} as {filename_save}")

    def __repr__(self):
        return f"Visualization('{self.filename}')"
            

        
