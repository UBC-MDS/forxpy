import pytest
from forxpy.forxpy import *

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
