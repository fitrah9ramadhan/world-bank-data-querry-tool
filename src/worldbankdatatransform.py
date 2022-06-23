import os

import pandas as pd

class WorldBankDataTransform:

    def __init__(self, filename: dict, path:str):
        self.filename = filename
        self.path = path

    # a variable panel data
    def onevar_panel_data(self, key_name: str , country_list: list, save_file=False, path=None, filename_save=None):

        if key_name not in self.filename:
            return print(f"{key_name} is not in filename")

        data = pd.read_csv(self.path+'/'+self.filename[key_name], skiprows = 3)

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
            data.to_csv(path+'/'+filename_save)
            print(f'your csv file has been saved in {path} as {filename_save}')

        return data

    # time series data of a country
    def multivar_time_series(self, country: str, save_file=False, path=None, filename_save=None):

        dct = self.filename
        new_dict = {}
        lst = []

        for (k, v) in dct.items():
            v = self.onevar_panel_data(key_name=k, country_list=[country])
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
            data.to_csv(path+'/'+filename_save)
            print(f'your csv file has been saved in {path} as {filename_save}')

        return data

    # cross_section_specific_year
    def multivar_cross_section(self, year, country_list=None, save_file=True, path=None, filename_save=None):
        dct = self.filename
        lst = []

        new_dict = {}
        for (k, v) in dct.items():
            v = pd.read_csv(self.path+'/'+v, skiprows=3)
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
            data.to_csv(path+'/'+filename_save)
            print(f'your csv file has been saved in {path} as {filename_save}')

        return data

    def multivar_panel_data(self, save_file=False, path=None, filename_save=None):
        dct = self.filename

        new_dict = {}
        lst = []
        for (k, v) in dct.items():
            v = pd.read_csv(self.path+'/'+v, skiprows=3)
            v = v.drop(columns=['Indicator Code','Country Code', 'Indicator Name','Unnamed: 66'])
            v = v.set_index('Country Name').stack(dropna=False)
            v = pd.DataFrame(v)
            v = v.reset_index()
            v = v.rename(columns ={'Country Name':'Country','level_1':'year', 0:k})
            v = v.set_index(['Country','year'])
            
            new_dict[k] = v
            lst.append(k)

        data = new_dict[lst[0]]
        for i in range(len(lst)):
            if i == 0:
                continue
            else:
                data = data.join(new_dict[lst[i]])
        
        if save_file == True and filename_save != None:
            data.to_csv(path+'/'+filename_save)
            print(f'your csv file has been saved in {path} as {filename_save}')

        return data


def get_filename_dict(path):
    filename_list = os.listdir(path)

    filename_dict = {}
    for filename in filename_list:
        filename_dict[filename[:-4]] = filename

    return filename_dict