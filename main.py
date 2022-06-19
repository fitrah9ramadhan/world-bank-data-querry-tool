from WorldBank import WorldBankDataTransform, Visualization 


big_four_country = ['France', 'Germany', 'Italy', 'United Kingdom']
filename = 'inflation-gdp-deflator-percent.csv'

big_four = WorldBankDataTransform(filename=filename)
ts_big_four = big_four.specific_countries_time_series(big_four_country)

vis = Visualization(ts_big_four)
vis.time_series(size=(10,8), title="Inflation in Big Four (G4) Countries", filename_save='inflation.png')
vis.correlation_map(size=(8,8), title="Inflation Correlation in Big Four (G4) Countries", filename_save='inflation_heatmap.png')
vis.boxplot(size=(20, 8), title="Big Four Inflation Boxplot", filename_save='inflation_boxplot.png')