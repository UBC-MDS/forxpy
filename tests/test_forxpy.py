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