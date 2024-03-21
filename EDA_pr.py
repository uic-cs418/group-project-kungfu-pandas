import pandas as pd
import numpy as np

def get_max(col_name, df):
    map = {}
    temp = df[col_name].to_list()
    for i in temp:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    max = float('-inf')
    key = ''
    for x, y in map.items():
        if y > max:
            max = y
            key = x
    return key

def get_min(col_name, df):
    map = {}
    temp = df[col_name].to_list()
    for i in temp:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    min = float('inf')
    key = ''
    for x, y in map.items():
        if y < min:
            min = y
            key = x
    return key

def get_neighborhood_price_stats(data:pd.DataFrame):
    '''This function will calculate the max, min, average'''
    columns = data.columns.to_list()
    columns = columns[1:] # skip the first index
    print("THE MINIMUM AND MAXIMUM HOUSE PRICES FOR EACH NEIGHBORHOOD AND THE DATES FOR WHEN THESE PRICES OCCURED", end= "\n\n")
    map = {}
    map2 = {}
    min_price_list = []
    max_price_list = []
    min_date_list = []
    max_date_list = []
    avg_price_list = []
    median_price_list = []
    
    for column in columns:
        min_date = data.loc[data[column] == data[column].min(), 'date'].to_list()[0]
        max_date = data.loc[data[column] == data[column].max(), 'date'].to_list()[0]
        min_price_list.append(data[column].min())
        min_date_list.append(min_date)
        max_price_list.append(data[column].max())
        max_date_list.append(max_date)
        avg_price_list.append(data[column].mean())
        median_price_list.append(data[column].median())

    map['Neighborhood'] = columns
    map['Min Price'] = min_price_list
    map['Min Date'] = min_date_list
    map['Max Price'] = max_price_list
    map['Max Date'] = max_date_list

    map2['Neighborhood'] = columns
    map2['Avg Price'] = avg_price_list
    map2['Med Price'] = median_price_list

    df = pd.DataFrame(map)
    df2 = pd.DataFrame(map2)

    df['Min Date'] = pd.to_datetime(df['Min Date'])
    df['Max Date'] = pd.to_datetime(df['Max Date'])

    # df['Min Price'] = df['Min Price'].astype(float)
    # df['Max Price'] = df['Max Price'].astype(float)

    pd.set_option("display.max_rows", None)

    # get the min, max, range, average price for all neighborhoods and their specifications
    print(df.to_string(index=False), end = "\n\n")
    
    # get the avg min price, avg max price for all neighborhoods and their specifications
    print("AVG MIN PRICE: ", df['Min Price'].mean(), "  AVG MAX PRICE: ", df['Max Price'].mean(), end="\n\n")

    # get median min price, median max price for all neighborhoods and their specifications
    print("MEDIAN MIN PRICE: ", df['Min Price'].median(), "  MEDIAN MAX PRICE: ", df['Max Price'].median(), end="\n\n")

    # Most Cheap Neighborhood amongs the min price houses in each neighborhood
    row1 = df.loc[df['Min Price'] == df['Min Price'].min(), ['Neighborhood', 'Min Price', 'Min Date']].iloc[0]

    # Most Expensive Neighborhood amongs the max price houses in each neighborhood
    row2 = df.loc[df['Max Price'] == df['Max Price'].max(), ['Neighborhood', 'Max Price', 'Max Date']].iloc[0]

    print("Cheapest House Price: ",row1.iloc[0], ' $',row1.iloc[1], ' ',row1.iloc[2].date().strftime("%Y-%m-%d"), end="\n\n", sep='')

    print("Expensive House Price: ",row2.iloc[0], ' $',row2.iloc[1], ' ',row2.iloc[2].date().strftime("%Y-%m-%d"), end="\n\n", sep ='')

    avg_Min = df2.loc[df2['Avg Price'] == df2['Avg Price'].min(), ['Neighborhood', 'Avg Price']].iloc[0]
    avg_Max = df2.loc[df2['Avg Price'] == df2['Avg Price'].max(), ['Neighborhood', 'Avg Price']].iloc[0]

    med_min = df2.loc[df2['Med Price'] == df2['Med Price'].min(), ['Neighborhood', 'Med Price']].iloc[0]
    med_max = df2.loc[df2['Med Price'] == df2['Med Price'].max(), ['Neighborhood', 'Med Price']].iloc[0]
    
    print('USING AVERAGE')
    print("\tCheapest Neighborhood: ", avg_Min.iloc[0], ' $',avg_Min.iloc[1], end="\n\n", sep='')
    print("\tExpensive Neighborhood: ", avg_Max.iloc[0], ' $',avg_Max.iloc[1], end="\n\n", sep='')


    print('USING MEDIAN')
    print("\tCheapest Neighborhood: ", med_min.iloc[0], ' $',med_min.iloc[1], end="\n\n", sep='')
    print("\tExpensive Neighborhood: ", med_max.iloc[0], ' $',med_max.iloc[1], end="\n\n", sep='')
    # print(df['Max Date'].info())
    

def get_crime_stats(data:pd.DataFrame):
    # most and least common type of crime
    # neighborhoods with the most and least arrest  # more arrest = active police
    # neighborhoods with the most and least crime   # more crime = less safe
    # most and least common crime location
    # The day with the most crime 
    print('spaceholder')


def main():
    neighborhood_2017_2019 = pd.read_csv('csv_files/neighborhood_data_2017_2019.csv')
    neighborhood_2021_present = pd.read_csv('csv_files/neighborhood_data_2021_present.csv')





    print("HOUSE PRICE BETWEEN 2017-19")
    get_neighborhood_price_stats(neighborhood_2017_2019)
    print("~"*160)
    print("HOUSE PRICE BETWEEN 2021-present")
    get_neighborhood_price_stats(neighborhood_2021_present)

if __name__ == "__main__":
    main()