def convert(currency1,currency2):
    """
    Convert Currency 1 to Currency 2.
def convert(currency1,currency2):
    """
    Convert Currency 1 to Currency 2.

    The conversion rate is based on the average exchange rate 
    by the 4:00 pm ET of the closest business day

    Parameters
    ----------
    currency1: str
    currency1: str
        The type of currency to be converted
    
    currency2: str
    currency2: str
        The type of currency that the currency1 will be converted to

    Returns
    -------
    float
        The amount of currency 2 that the currency 1 equals to 

    Examples
    --------
    >>> convert("CAD","USD")
    """
    pass

def retrieve_data(start_date, output_path):
	    
	"""
	Retrieve historical daily currency exchange rate data for Canadian Dollars 
    in CSV format from the Bank of Canada website.    
	
	Parameters
	----------
	start_date : string "%YYYY-%mm-%dd"
	    inputted starting date in the format specified "%YYYY-%mm-%dd"
	output_path : path
	    the path where the csv file will get written to
		 
	Returns
	-------
	file
	    csv data file that includes historical data on currency exchange rates
	    
	Examples
	>>> retrieve_data("2022-05-23", "my_document/currency_exchange.csv")
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
    This function takes currency exchange rates data as input and returns a list of two strings containing the fastest and slowest growing currency exchange rate in relation to Canadian Dollar.
    The data provided contains currency code in the format FX***CAD, the average exchange rate and the date.
    
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