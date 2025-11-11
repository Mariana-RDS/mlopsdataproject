import pandas as pd
import yfinance as yf


def download_data(
        ticker: str="AAPL",
        start_date: str="2020-01-01",
        end_date: str="2020-12-31",
        multi_level: bool=False
) -> pd.DataFrame:
    

    result = (
        yf.download(ticker,
            start=start_date,
            end=end_date,
            multi_level_index=multi_level
        )
        .reset_index()
    )

    return result