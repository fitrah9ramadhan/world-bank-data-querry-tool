# World Bank Data Query Tool

* Multi .csv Files 
* Transform World Bank Data Indicator
  * One Variable Panel Data
  * MultiVariable Time Series Data
  * MultiVariable Cross Section Data
  * MultiVariable Panel Data **(New!)**

## Requirements
* python 3.xx 
* pandas 1.4.2

## How to Install

```python: 
pip install worldbankdatatransform
```

## How to Use

 ```python:
 from worldbankdatatransform import get_filename_dict, WorldBankDataTransform
```

download csv files that you want at data.worldbank.org/indicator and 
you csv files must stored in a folder with appropriate filename, i.e inflation.csv, constant-gdp.csv

 ```python:
 your_path = 'your csv folder path' ## i.e D:/world-bank/data
 filename = get_filename_dict(path=your_path)
 
 # Create an object
 wb_files = WorldBankDataTransform(filename=filename, path=your_path)
```

### One Variable Panel Data

Transform world bank csv files into

| year | country_1 | country_2 | ... | country_n |
|------|-----------|-----------|-----|-----------|
|      |           |           |     |           |

for example:
```python:
G4_countries = ['United Kingdom', 'France', 'Germany', 'Italy']
inflation = "inflation" # csv file name of the variable you want, without '.csv'

G4_countries_inflation = wb_files.onevar_panel_data(key_name=inflation, 
                                                    country_list=G4_countries, 
                                                    save_file=False,
                                                    path=None,
                                                    filename_save=None)
```
```G4_countries_inflation``` is a pandas DataFrame

### Multivariable Time Series Data

Transform world bank csv files into specific country's multivariable:

| year | variable_1 | variable_2 | ... | variable_n |
|------|-----------|-----------|-----|-----------|
|      |           |           |     |           |


```python:

country = "Vanuatu"
vanuatu_time_series = wb_files.multivar_time_series(country=country, 
                                                    save_file=False,
                                                    path=None,
                                                    filename_save=None)
```

```vanuatu_time_series``` is a pandas DataFrame

### Multivariable Cross Section Data

Transform world bank csv files into specific year multivariable of countries:

| country | variable_1 | variable_2 | ... | variable_n |
|------|-----------|-----------|-----|-----------|
|      |           |           |     |           |


world_in_2019 = wb_files.multivar_cross_section(year=2019, 
                                                country_list=None, 
                                                save_file=False,
                                                path=None,
                                                filename_save=None)

you can also specify country list included in the DataFrame
i.e 
asean_5 = ['Indonesia', 'Malaysia', 'Singapore', 'Thailand', 'Philippines']
and store into ```country_list``` parameter


### Multivariable Panel Data

Transform world bank csv files into specific year multivariable of countries:

| country | year | variable_1 | variable_2 | .... |variable_n|
|------|-----------|-----------|-----|-----------|-----------|
|      |           |           |     |           |           |


all_countries_panel_data = wb_files.multivar_panel_data(save_file=False,
                                                        path=None,
                                                        filename_save=None)


## How to Save into csv Files

Set the ```save_file=True,```
        ```path='your save file folder path',```
        ```filename_save='your_data_filename.csv'```

