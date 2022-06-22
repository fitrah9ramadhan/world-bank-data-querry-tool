import constant as c

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

class WorldBankDataTransform:
    all = []
    def __init__(self, filename: dict):
        self.filename = filename

        # Action
        WorldBankDataTransform.all.append(self)
    
    # a variable panel data
    def countries_panel_data(self, key_name: str , country_list: list, save_file=False, filename_save=None):

        if key_name not in self.filename:
            return print(f"{key_name} is not in filename")

        data = pd.read_csv(c.DATA_PATH+self.filename[key_name], skiprows = 3)

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

    # time series data of a country
    def multivar_time_series(self, country: str, save_file=False, filename_save=None):

        dct = self.filename
        new_dict = {}
        lst = []

        for (k, v) in dct.items():
            v = self.countries_panel_data(key_name=k, country_list=[country])
            v = v.rename(columns={country: k})

            new_dict[k] = v
            lst.append(k)
            
        data = new_dict[lst[0]]
        for i in range(len(lst)):
            if i == 0:
                continue
            else:
                data = data.join(new_dict[lst[i]])

        if save_file==True and filename_save != None:
            data.to_csv(c.SAVE_DATA_PATH+filename_save)
            print(f'your csv file has been saved in {c.SAVE_DATA_PATH} as {filename_save}')

        return data

    # cross_section_specific_year
    def multivar_cross_section(self, year, country_list=None, save_file=True, filename_save=None):
        dct = self.filename
        lst = []

        new_dict = {}
        for (k, v) in dct.items():
            v = pd.read_csv(c.DATA_PATH+v, skiprows=3)
            v = v[['Country Name', str(year)]]
            v = v.rename(columns={'Country Name':'Country'})
            if country_list != None:
                v = v[v['Country'].isin(country_list)]
                
            v = v.rename(columns={str(year):k})
            v = v.set_index('Country')

            lst.append(k)
            new_dict[k] = v

        data = new_dict[lst[0]]
        for i in range(len(lst)):
            if i == 0:
                continue
            else:
                data = data.join(new_dict[lst[i]])

        if save_file==True and filename_save != None:
            data.to_csv(c.SAVE_DATA_PATH+filename_save)
            print(f'your csv file has been saved in {c.SAVE_DATA_PATH} as {filename_save}')

        return data

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
            

        
