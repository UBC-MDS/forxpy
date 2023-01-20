from forxpy import forxpy
from forxpy.forxpy import retrieve_data

def test_count_words():
    """ Test whether the file has been retrieved from the link. """
    assert os.path.isfile("data_raw.csv"), "CSV file is not found"
    
    """ Test whether the first row has been dropped. """
    assert data.index[0] == 1, "First row is not dropped"
    
    """ Test whether the required columns have been dropped. """
    assert 'FXMYRCAD' not in data.columns, "FXMYRCAD column is not dropped"
    assert 'FXTHBCAD' not in data.columns, "FXTHBCAD column is not dropped"
    assert 'FXVNDCAD' not in data.columns, "FXVNDCAD column is not dropped"
    
    """ Test whether the output is pandas DataFrame data type. """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Output is not pd.DataFrame data type")