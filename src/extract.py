import pandas as pd
from pathlib import Path


def extract_data():
    raw_path = Path("data/raw")

    datasets = {
        "customers": pd.read_csv(raw_path / "olist_customers_dataset.csv"),
        "orders": pd.read_csv(raw_path / "olist_orders_dataset.csv"),
        "order_items": pd.read_csv(raw_path / "olist_order_items_dataset.csv"),
        "order_payments": pd.read_csv(raw_path / "olist_order_payments_dataset.csv"),
        "order_reviews": pd.read_csv(raw_path / "olist_order_reviews_dataset.csv"),
        "products": pd.read_csv(raw_path / "olist_products_dataset.csv"),
        "sellers": pd.read_csv(raw_path / "olist_sellers_dataset.csv"),
        "geolocation": pd.read_csv(raw_path / "olist_geolocation_dataset.csv"),
        "category_translation": pd.read_csv(
            raw_path / "product_category_name_translation.csv"
        ),
    }

    print("Data extracted successfully.\n")

    for name, df in datasets.items():
        print(f"{name}: {df.shape}")

    return datasets

if __name__ == "__main__":
    extract_data()




    