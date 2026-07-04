import pandas as pd


class CSVWriter:

    @staticmethod
    def save(products, filepath):
        df = pd.DataFrame(products)
        df.to_csv(filepath, index=False)