# World Bank Data Querry Tool
* Multi csv files
* Transform and Visualize World Bank Data Indicator
  * Panel Data
  * Time Series Data (multi variables)
* Time Series Plot
* Boxplot
* Heatmap
## Requirements
* python 3.9.12
* pandas 1.4.2
* matplotlib 3.5.1
* seaborn 0.11.2

## WorldBankDataTransform

Standard data.worldbank.org/indicator data form

![image1](assets/readme_pictures/wb_standard_data_form.PNG)

#### .countries_panel_data(key_name, country_list, save_file=False, filename_save=None )

transformed to:

![image2](assets/readme_pictures/panel_data.PNG)

#### .multivar_time_series(country, save_file=False, filename_save=None)

transformed to:

![image 3](assets/readme_pictures/time_series_data.PNG)

## Read example.py!
