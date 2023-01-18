import os
import pandas as pd

def retrieve_data(output):
    """
    Retrieve historical daily currency exchange rates data for Canadian Dollar 
    in CSV format from Bank of Canada website. 
    The function pre-processes and cleans the data to transform it into a more usable format.     
    
    Parameters
    ----------
    output : bool
        if the value is False then only display the data frame, if the value is True then write the file to the current working directory 
        
    Returns
    -------
    file :
        cleaned and processed csv data file that includes historical data on currency exchange rates
        
    Examples
    >>> retrieve_data(output=True)
    """
    url = 'https://raw.githubusercontent.com/mrnabiz/forx_source/main/data/raw/raw_data_cad.csv'
    # Read CSV file and reset the index
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

def plot_historical(start_date, end_date, currency):
    """
    Plots the historical rate of the entered currencies within a specific period
    of time.

    Parameters
    ----------
	start_date : string '%YYYY-%mm-%dd'
	    inputted starting date in the format specified '%YYYY-%mm-%dd'
	end_date : string '%YYYY-%mm-%dd'
	    inputted ending date in the format specified '%YYYY-%mm-%dd'
    currency : str
        The type of currency asked for plotting

    Returns
    -------
    plot object
        A plot showing the performance of the currency.

    Examples
    --------
    >>> plot_historical('2022-05-23', '2022-05-30', 'USD')
    """
    pass