import mlopsdataproject as mdp


def test_download_data_columns():
    columns=mdp.download_data().columns.tolist()
    expected=['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

    assert columns==expected
