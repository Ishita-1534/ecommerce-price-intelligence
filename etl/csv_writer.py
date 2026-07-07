import pandas as pd


class CSVWriter:

    @staticmethod
    def save(products, filepath):

        data = []

        for product in products:
            data.append(product.to_dict())

        df = pd.DataFrame(data)

        df.to_csv(filepath, index=False, encoding="utf-8-sig")

        print(f"CSV saved successfully at: {filepath}")