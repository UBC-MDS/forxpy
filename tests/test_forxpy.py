import pytest
from forxpy.forxpy import *
from datetime import datetime

def test_retrieve_data():

    data = retrieve_data(export_csv = False)

    """ Test whether the first row has been dropped. """
    assert data.index[0] == 1, "First row is not dropped"
    
    """ Test whether the required columns have been dropped. """
    assert 'FXMYRCAD' not in data.columns, "FXMYRCAD column is not dropped"
    assert 'FXTHBCAD' not in data.columns, "FXTHBCAD column is not dropped"
    assert 'FXVNDCAD' not in data.columns, "FXVNDCAD column is not dropped"
    
    """ Test whether the output is pandas DataFrame data type. """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Output is not pd.DataFrame data type")


def test_plot_historical():
    sbs_plot = plot_historical('2020-05-23', '2022-05-30', 'USD', 'CAD')
    plt_objs = sbs_plot.to_dict()

    """ Test whether the final plot has been formed """
    plt_title = 'How many CAD does 1 USD worth?'
    assert sbs_plot.title == plt_title, 'The final plot has not formed correctly'
    
    """ Test whether the subplot has been formed correctly """
    assert plt_objs['vconcat'][0]['layer'][0]['mark'] == 'line', 'Chart type is not line'
    assert plt_objs['vconcat'][0]['layer'][0]['encoding']['x']['field'] == 'date', 'The X axis is not date'
    assert plt_objs['vconcat'][0]['layer'][0]['encoding']['y']['field'] == 'USD/CAD', 'Rates are not numeric'

def test_fastest_slowest_currency():
    start_date = '2019-05-23'
    end_date = '2022-05-30'

    res = fastest_slowest_currency(start_date, end_date)

    """ Test whether the start and end date are correct """
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    assert (end - start).days > 0, 'The date range is inaccurate'

    """ Test if it returns a list type """
    assert type(res) == list, 'The function does not return a list of lists accurately'

    """ Test 2: Check if the function is returning the correct fastest currency """
    assert fastest_slowest_currency('2019-05-23', '2022-05-30')[0][0] == 'TRY'

    """ Test 3: Check if the function is returning the correct slowest currency """
    assert fastest_slowest_currency('2019-05-23', '2022-05-30')[1][0] == 'IDR'

def test_currency_convert():
    df_conv_rates = retrieve_data('https://raw.githubusercontent.com/mrnabiz/forx_source/main/data/raw/raw_data_cad.csv')
    names = {'AUD':1,'BRL':2,'CNY':3, 'EUR':4, 'HKD':5, 'INR':6, 'IDR':7, 'JPY':8, 'MXN':9, 'NZD':10, 'NOK':11, 'PEN':12, 
         'RUB':13, 'SAR':14, 'SGD':15, 'ZAR':16, 'KRW':17, 'SEK':18, 'CHF':19, 'TWD':20, 'TRY':21, 'GBP':22, 'USD':23} #initializations
    
    with pytest.raises(ValueError, match=r"The currency to be converted is invalid!"): # Test for invalid input of currency1
                       currency_convert(2, 'AAA', 'CNY')
    with pytest.raises(ValueError, match=r"The currency to be converted to is invalid!"): # Test for invalid input of currency2
                       currency_convert(2, 'CNY', 'AAA')
    with pytest.raises(ValueError, match=r"Please enter an positive amount!"): # Test for input a negative amount 
                       currency_convert(-2, 'CNY', 'USD')
    assert type(currency_convert(2, 'CAD', 'USD')) is float or type(currency_convert(1, 'CAD', 'CAD')) is int , " The output data type is wrong!" # Test for the output data type
    
    assert currency_convert(2, 'CAD','CAD') == 2,"Wrong output value" #Test for exchanging the same currency
    
    assert currency_convert(2, 'CNY','CAD') == round(2*float(df_conv_rates.iloc[-1][names['CNY']]),3),"Wrong output value!" #Test for converting another currency to CAD
    
    assert currency_convert(2, 'CAD', 'CNY') == round(2/(float(df_conv_rates.iloc[-1][names['CNY']])),3), "Wrong output value!" #Test for converting CAD to another currency
                                                      /(float(df_conv_rates.iloc[-1][names['CNY']])),3), "Wrong output value!" # Test the conversion of two currencies which both not CAD
    