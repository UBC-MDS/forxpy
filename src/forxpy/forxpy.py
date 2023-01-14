def retrieve_data(start_date, output_path):    
	"""
	Retrieve historical daily currency exchange rate data for Canadian Dollars 
    in CSV format from the Bank of Canada website.    
	
	Parameters
	----------
	start_date : string '%YYYY-%mm-%dd'
	    inputted starting date in the format specified '%YYYY-%mm-%dd'
	output_path : path
	    the path where the csv file will get written to
		 
	Returns
	-------
	file
	    csv data file that includes historical data on currency exchange rates
	    
	Examples
	>>> retrieve_data('2022-05-23', 'my_document/currency_exchange.csv')
	"""
	pass
    
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