# Example
# Big four countries
#####################################################

# to start, uncomment and run the code below
from worldbank import WorldBankDataTransform, Visualization 


# in this example, we are going to get an insight from 
# a messy multiple world bank data csv files
# from G4 countries, those are France, Germany, Italy, 
# and the United Kingdom
#####################################################


# Download csv data from data.worldbank.org/indicator
# Get the filename and make it into variable as a string
#####################################################
wb_inflation_filename = 'inflation.csv'
wb_gdp_per_capita_filename = 'gdp-per-capita-constant-US$2015.csv'


# Create filename dictionary
#####################################################
filename = {'inflation': wb_inflation_filename, 'gdp':wb_gdp_per_capita_filename }


# create an object with filename that yv got above
#####################################################
wb_files = WorldBankDataTransform(filename=filename)


# as the object have created, do something that you need
# create G4 country list
#####################################################
big_four_country = ['France', 'Germany', 'Italy', 'United Kingdom']

# create panel data of inflation in G4 countries
#####################################################
panel_big_four_inflation = wb_files.countries_panel_data(key_name='inflation', country_list=big_four_country, save_file=True, filename_save='big_four_inflation.csv')


# create panel data of gdp per capita in G4 countries
#####################################################
panel_big_four_gdp_per_capita = wb_files.countries_panel_data(key_name='gdp', country_list=big_four_country, save_file=True, filename_save='big_four_gdp_per_capita.csv')


# create time series data for a countries with multivariable
# for example: France
#####################################################
ts_inflation_gdp_france = wb_files.multivar_time_series('France', save_file=True, filename_save='france_inflation_and_gdp_ts.csv')


# create cross sectin data for a year with multivariable
# for example: 2018 in all country

cs_2019_all_country = wb_files.multivar_cross_section(year=2018, save_file=True, filename_save='all_country_in_2018.csv')


# create cross section data for a year with multivariable
# for example: 2017 in ASEAN

ASEAN = ['Indonesia', 'Malaysia', 'Singapore', 'Thailand', 'Philippines', 'Myanmar', 'Lao PDR', 'Brunei Darussallam', 'Cambodia']
cs_2017_ASEAN = wb_files.multivar_cross_section(year=2017, country_list=ASEAN, save_file=True, filename_save='ASEAN_in_2017.csv')



# You also can visualize your data that has created from the object above, 
# that is inflation time series data of G4 (France, Germany, Italy, and The United Kingdom)
# there should be csv file generated and the output show you where is the csv file located
# get filename created from above's as a variable
#####################################################
transformed_csv = 'big_four_inflation.csv'


# create a visualization object with its csv files
#####################################################
vis = Visualization(filename=transformed_csv)


# after the below code run, there should be a png file generated, 
# and the output would show you where is the png file located
#####################################################
vis.time_series(size=(10,8), title="Inflation in Big Four (G4) Countries", filename_save='inflation_ts_plot.png')
vis.correlation_map(size=(8,8), title="Inflation Correlation in Big Four (G4) Countries", filename_save='inflation_heatmap.png')
vis.boxplot(size=(20, 8), title="Big Four Inflation Boxplot", filename_save='inflation_boxplot.png')

