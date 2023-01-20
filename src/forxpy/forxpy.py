import os
import pandas as pd
import altair as alt
from datetime import datetime

def retrieve_data(export_csv = False):

    """
    Retrieve historical daily currency exchange rates data for Canadian Dollar 
    in CSV format from Bank of Canada website. 
    The function pre-processes and cleans the data to transform it into a more usable format.     
    
    Parameters
    ----------
    export_csv : bool
        If the value is False then only display the data frame, If the value is True then write the file to the current working directory. 

    Returns
    -------
    file :
        cleaned and processed dataframe and csv file that includes historical 
        data on currency exchange rates
        
    >>> retrieve_data(export_csv = False)

    """
    url = 'https://raw.githubusercontent.com/mrnabiz/forx_source/main/data/raw/raw_data_cad.csv'
    # Read CSV file and reset the index
    url = 'https://raw.githubusercontent.com/mrnabiz/forx_source/main/data/raw/raw_data_cad.csv'
    data_raw = (pd.read_csv(url, delimiter="\t")[38:]).reset_index()
    
    # Setting the first row as column names
    data_raw.columns = data_raw.iloc[0]
    data = data_raw.iloc[:, 1:]
    
    # Drop the first row of data
    data = data.drop(data.index[0])
    
    # Drop "FXMYRCAD", "FXTHBCAD", "FXVNDCAD" columns with many NA values
    data = data.drop(labels=["FXMYRCAD", "FXTHBCAD", "FXVNDCAD"], axis=1)
    
    
    # Convert date column to datetime format
    data['date'] = pd.to_datetime(data['date'])
    
    # Creating list of column names
    col_list = data.columns.tolist()
    
    # Remove the date column from the list
    col_list.remove('date')

    # Data cleaning
    data[col_list] = data[col_list].apply(pd.to_numeric)
    data.columns = data.columns.str.replace("FX", "")
    data.columns = data.columns.str.replace("CAD", "")
    data['CAD'] = 1.0

    # Saving dataframe as CSV file
    if export_csv == True:
        data.to_csv("data_raw.csv")
    
    # Convert all columns in the list to numeric data type
    data[col_list] = data[col_list].apply(pd.to_numeric)
    
    # Wrangling column labels
    data.columns = data.columns.str.replace("FX", "")
    data.columns = data.columns.str.replace("CAD", "")
    
    # Add "CAD" column and assign a value of 1.0 to eahc row
    data['CAD'] = 1.0
    
    if output:
        # Saving dataframe as CSV file if output=True
        data.to_csv("data_raw.csv")
    else:
        # Only display dataframe if output=False
        return data

    return data

def fastest_slowest_currency(df):
    """
    This function takes currency exchange rates data as input and returns a 
    list of two strings containing the fastest and slowest growing currency 
    exchange rate in relation to Canadian Dollar.
    The data provided contains currency code in the format FX***CAD, 
    the average exchange rate and the date.
    
    Parameters
    ----------
    df : Pandas DataFrame
        data frame containing currency exchange rates to Canadian Dollars by date
    
    Returns
    -------
    list
        list of strings containing the currency name used to convert 
        to CAD in the format (FX***CAD) and the exchange rates for 
        the fastest and slowest growing currencies
    
    Examples
    >>> fastest_slowest_currency(exchange_data)
    ['FXUSDCAD: 0.857', 'FXTHBCAD: 0.263']
    """ 
    pass

def currency_convert(value, currency1, currency2):
    """
    This function takes a currency value and the currency type 
    to be converted to as input and returns the converted currency 
    value as per the current conversion rate.
    
    Parameters
    ----------
    value: float
        The value of the original currency to be converted

    currency1: str
        The type of currency originally
    
    currency2: str
        The type of currency that the currency1 will be converted to
    
    Returns
    -------
    converted: numeric
        Returns converted numeric currency
    
    Examples
    >>> currency_convert(23, 'USD', 'CAD')
    """
    pass

def plot_historical(start_date, end_date, currency1, currency2):
    """
    Plots the historical rate of the entered currencies within a specific period
    of time.

    Parameters
    ----------
	start_date : string '%YYYY-%mm-%dd'
	    inputted starting date in the format specified '%YYYY-%mm-%dd'
	end_date : string '%YYYY-%mm-%dd'
	    inputted ending date in the format specified '%YYYY-%mm-%dd'
    currency1 : str
        The type of based currency asked for plotting
    currency2 : str
        The type of exchange currency asked for plotting

    Returns
    -------
    plot object
        A plot showing the performance of the currency.

    Examples
    --------
    >>> plot_historical('2020-05-23', '2022-05-30', 'USD', 'CAD')
    """

    # Data filtration
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    ratio = currency1 + '/' + currency2
    data = retrieve_data()
    data[ratio] = data[currency1]/data[currency2]
    data_plt = data[(data['date'] >= start) &
                    (data['date'] <= end)][['date', ratio]]
    
    # Building the base chart
    base_chart = alt.Chart(data_plt).mark_line().encode(
        alt.X('date', title='Date'),
        alt.Y(ratio, scale=alt.Scale(zero=False)),
        tooltip=['date', ratio]).properties(width=900, height=200)
    dot_line_chart = base_chart + base_chart.mark_point(size=2)

    # Building interactivity
    brush = alt.selection_interval(encodings=['x'])
    lower_chart = base_chart.properties(height=60).add_selection(brush)
    upper_chart = dot_line_chart.encode(alt.X('date:T', 
                                            scale=alt.Scale(domain=brush)))

    plt_title = 'How many ' + currency2 + ' does 1 ' + currency1 + ' worth?'
    sbs_plot = (upper_chart & lower_chart).properties(
        title=plt_title
                                        ).configure_title(
        fontSize=18, font='Cambria', anchor='start').configure_axis(
            labelFontSize=10, titleFontSize=10, 
            labelFont='Cambria', titleFont='Cambria'
            )
    
    # Unit tests to test the function input
    assert end >= data['date'].min(), 'The end date is out of the range'
    assert start <= data['date'].max(), 'The start date is out of the range'
    assert currency1 in data.columns.to_list(), 'Currency 1 is not supported'
    assert currency2 in data.columns.to_list(), 'Currency 1 is not supported'

    # Unit tests to test the plot object
    assert base_chart.to_dict()['mark'] == 'line', 'Chart type is not line'
    assert base_chart.to_dict()['encoding']['x']['type'] == 'temporal', 'Datetype is not temporal'
    assert base_chart.to_dict()['encoding']['y']['type'] == 'quantitative', 'Rates are not numeric'
    assert sbs_plot.title == plt_title, 'The final plot has not formed correctly'

    return sbs_plot