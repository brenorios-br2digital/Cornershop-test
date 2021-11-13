import os
import sys
import numpy as np
import pandas as pd
import re
from models import Product, BranchProduct
from database_setup import engine
from sqlalchemy.orm import sessionmaker


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")
PRODUCTS_PATH = os.path.join(ASSETS_DIR, "PRODUCTS.csv")
PRICES_STOCK_PATH = os.path.join(ASSETS_DIR, "PRICES-STOCK.csv")

NOHTMLTAGS_REGEX = re.compile('<.*?>')
UNITS = ["ML", "GRS", "GR", "PZA", "UN", "LT", "KG"]
BRANCHES = ["MM", "RHSM"]

STORE_NAME = "Richart's"


def process_csv_files():
    products_df = pd.read_csv(filepath_or_buffer=PRODUCTS_PATH, sep="|",)
    prices_stock_df = pd.read_csv(
        filepath_or_buffer=PRICES_STOCK_PATH, sep="|",)

    # Stock is greater than 0 AND only products on MM and RHSM
    prices_stock_df = prices_stock_df[(
        (prices_stock_df.BRANCH.isin(BRANCHES)) & (prices_stock_df.STOCK > 0))]

    # MERGE DATAFRAMES ON SKU
    df = pd.merge(products_df,
                  prices_stock_df, on='SKU')

    print(df.columns)

    # Filtering unique values by branch
    for branch in BRANCHES:
        df[(df.BRANCH == branch)].drop_duplicates(inplace=True)

    branch_products = []
    for i, row in df[:200].iterrows():
        description = row['DESCRIPTION']
        description_list = description.split(' ')
        name = row['NAME']

        # Check if contains any string in PACKAGES list
        package = row['BUY_UNIT']
        if row['BUY_UNIT'] is not None and row['BUY_UNIT'] in description_list:
            package = f"{description_list[description_list.index(row['BUY_UNIT']) - 1]} {row['BUY_UNIT']}"

        # Combine Categories and Subcategories columns into one
        row["CATEGORY"] = f"{row['CATEGORY']} | {row['SUB_CATEGORY']} | {row['SUB_SUB_CATEGORY']}"

        # Remove html tags
        row['DESCRIPTION'] = re.sub(NOHTMLTAGS_REGEX, '', description)
        row['NAME'] = re.sub(NOHTMLTAGS_REGEX, '', name)

        product = Product(
            store=STORE_NAME + row["BRANCH"], sku=row['SKU'], barcodes=row['BARCODES'], brand=row['BRAND'], name=row['NAME'], description=row['DESCRIPTION'], package=package, image_url=row['IMAGE_URL'], category=row["CATEGORY"])
        branch_product = BranchProduct(
            product_id=product.id, branch=row["BRANCH"], stock=row['STOCK'], price=row['PRICE'], product=product)

        branch_products.append(branch_product)

    # sqlite:///db.sqlite

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add_all(branch_products)
    session.commit()


if __name__ == "__main__":
    process_csv_files()
