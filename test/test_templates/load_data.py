def data():
    import pandas as pd
    return pd.DataFrame({
        'pet':      ['cat', 'dog', 'dog', 'fish', 'cat', 'dog', 'cat', 'fish'],
        'children': [4., 6, 3, 3, 2, 3, 5, 4],
        'salary':   [90., 24, 44, 27, 32, 59, 36, 27]
    })