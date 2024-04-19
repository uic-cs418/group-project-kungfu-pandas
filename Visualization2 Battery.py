import pandas as pd
import plotly.express as px

def visualization_battery():
    crime_data = pd.read_csv('csv_files/Crimes_2021_to_Present.csv')
    battery_data = crime_data[crime_data['Primary Type'] == 'BATTERY']
    
    battery_count = battery_data.groupby('RegionName').size().reset_index(name='CrimeCount')
    
    housing_data = pd.read_csv('csv_files/neighborhood_data_2017_2019.csv')
    housing_data_long = housing_data.melt(id_vars=['date'], var_name='Neighborhood', value_name='HousingPrice')
    housing_data_long['date'] = pd.to_datetime(housing_data_long['date'])
    
    avg_housing_prices = housing_data_long.groupby('Neighborhood')['HousingPrice'].mean().reset_index()
    
    merged_data_battery = battery_count.merge(avg_housing_prices, left_on='RegionName', right_on='Neighborhood')
    merged_data_battery['CrimeQuartile'] = pd.qcut(merged_data_battery['CrimeCount'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

    fig = px.box(merged_data_battery, x='CrimeQuartile', y='HousingPrice',
                 title='<b>Boxplot of Housing Prices by Battery Crime Rate Quartile</b>',
                 labels={'CrimeQuartile': 'Battery Crime Rate Quartile', 'HousingPrice': 'Average Housing Price ($)'},
                 color='CrimeQuartile', color_discrete_sequence=px.colors.qualitative.Pastel)
    
    fig.update_layout(showlegend=True)
    fig.show()

def main():
    visualization_battery()

if __name__ == '__main__':
    main()
