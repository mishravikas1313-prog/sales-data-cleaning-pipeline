import pandas as pd

def profile_data(datasets):

    print("\n========== DATA PROFILING ==========\n")

    for table_name, df in datasets.items():

        print(f"\n{'='*50}")
        print(f"TABLE : {table_name.upper()}")
        print(f"{'='*50}")

        print(f"Rows, Columns : {df.shape}")

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print(f"\nDuplicate Rows : {df.duplicated().sum()}")

    print("\n========== PROFILING COMPLETE ==========\n")


def clean_customers(df):

    print("\nCleaning Customers Table...")

    print(f"Initial Rows : {len(df)}")

    # Remove leading/trailing spaces
    df["customer_city"] = df["customer_city"].str.strip()
    df["customer_state"] = df["customer_state"].str.strip()

    print("✓ Leading/trailing spaces removed")

    # Standardize text
    df["customer_city"] = df["customer_city"].str.title()
    df["customer_state"] = df["customer_state"].str.upper()

    print("✓ City and state names standardized")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print(f"✓ Duplicates removed : {duplicates}")

    print(f"Final Rows : {len(df)}")

    print("Customers table cleaned.\n")

    return df

def clean_orders(df):

    print("\nCleaning Orders Table...")

    print(f"Initial Rows : {len(df)}")

    # Convert datetime columns
    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for col in date_columns:
        df[col] = pd.to_datetime(df[col])

    print("✓ Datetime columns converted")

    # Standardize order status
    df["order_status"] = df["order_status"].str.strip().str.lower()

    print("✓ Order status standardized")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print(f"✓ Duplicates removed : {duplicates}")

    print(f"Final Rows : {len(df)}")

    print("Orders table cleaned.\n")

    return df

def clean_order_items(df):

    print("\nCleaning Order Items Table...")

    print(f"Initial Rows : {len(df)}")

    # Convert shipping date to datetime
    df["shipping_limit_date"] = pd.to_datetime(df["shipping_limit_date"])

    print("✓ Shipping date converted to datetime")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print(f"✓ Duplicates removed : {duplicates}")

    print(f"Final Rows : {len(df)}")

    print("Order Items table cleaned.\n")

    return df

def clean_order_payments(df):

    print("\nCleaning Order Payments Table...")

    print(f"Initial Rows : {len(df)}")

    # Standardize payment type
    df["payment_type"] = df["payment_type"].str.strip().str.lower()

    print("✓ Payment type standardized")

    # Validate payment values
    invalid_payments = (df["payment_value"] <= 0).sum()

    print(f"✓ Invalid payment values found : {invalid_payments}")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print(f"✓ Duplicates removed : {duplicates}")

    print(f"Final Rows : {len(df)}")

    print("Order Payments table cleaned.\n")

    return df

def clean_order_reviews(df):

    print("\nCleaning Order Reviews Table...")

    print(f"Initial Rows : {len(df)}")

    # Convert review dates to datetime
    df["review_creation_date"] = pd.to_datetime(df["review_creation_date"])
    df["review_answer_timestamp"] = pd.to_datetime(df["review_answer_timestamp"])

    print("✓ Review dates converted to datetime")

    # Check missing review comments
    missing_titles = df["review_comment_title"].isnull().sum()
    missing_messages = df["review_comment_message"].isnull().sum()

    print(f"✓ Missing review titles : {missing_titles}")
    print(f"✓ Missing review messages : {missing_messages}")

    print("✓ Missing review comments preserved (business-valid NULLs)")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print(f"✓ Duplicates removed : {duplicates}")

    print(f"Final Rows : {len(df)}")

    print("Order Reviews table cleaned.\n")

    return df

def clean_products(df):

    print("\nCleaning Products Table...")

    print(f"Initial Rows : {len(df)}")

    # Fill missing category
    missing_category = df["product_category_name"].isnull().sum()
    df["product_category_name"] = df["product_category_name"].fillna("Unknown")

    print(f"✓ Missing categories filled : {missing_category}")

    # Fill missing numeric values with median
    numeric_columns = [
        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm"
    ]

    for col in numeric_columns:
        missing = df[col].isnull().sum()

        if missing > 0:
            df[col] = df[col].fillna(df[col].median())
            print(f"✓ {col} : {missing} missing values filled")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print(f"✓ Duplicates removed : {duplicates}")

    print(f"Final Rows : {len(df)}")

    print("Products table cleaned.\n")

    return df

def clean_sellers(df):

    print("\nCleaning Sellers Table...")

    print(f"Initial Rows : {len(df)}")

    # Remove leading/trailing spaces
    df["seller_city"] = df["seller_city"].str.strip()
    df["seller_state"] = df["seller_state"].str.strip()

    print("✓ Leading/trailing spaces removed")

    # Standardize text
    df["seller_city"] = df["seller_city"].str.title()
    df["seller_state"] = df["seller_state"].str.upper()

    print("✓ City and state names standardized")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print(f"✓ Duplicates removed : {duplicates}")

    print(f"Final Rows : {len(df)}")

    print("Sellers table cleaned.\n")

    return df

def clean_geolocation(df):

    print("\nCleaning Geolocation Table...")

    print(f"Initial Rows : {len(df)}")

    # Remove leading/trailing spaces
    df["geolocation_city"] = df["geolocation_city"].str.strip()
    df["geolocation_state"] = df["geolocation_state"].str.strip()

    print("✓ Leading/trailing spaces removed")

    # Standardize text
    df["geolocation_city"] = df["geolocation_city"].str.title()
    df["geolocation_state"] = df["geolocation_state"].str.upper()

    print("✓ City and state names standardized")

    # Remove exact duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print(f"✓ Exact duplicate rows removed : {duplicates}")

    print(f"Final Rows : {len(df)}")

    print("Geolocation table cleaned.\n")

    return df

def clean_category_translation(df):

    print("\nCleaning Category Translation Table...")

    print(f"Initial Rows : {len(df)}")

    # Remove leading/trailing spaces
    df["product_category_name"] = df["product_category_name"].str.strip()
    df["product_category_name_english"] = (
        df["product_category_name_english"].str.strip()
    )

    print("✓ Leading/trailing spaces removed")

    # Standardize text
    df["product_category_name"] = (
        df["product_category_name"].str.lower()
    )

    df["product_category_name_english"] = (
        df["product_category_name_english"]
        .str.strip()
        .str.title()
    )

    print("✓ Category names standardized")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print(f"✓ Duplicates removed : {duplicates}")

    print(f"Final Rows : {len(df)}")

    print("Category Translation table cleaned.\n")

    return df

def transform_data(datasets):

    print("\n========== STARTING DATA TRANSFORMATION ==========\n")

    datasets["customers"] = clean_customers(datasets["customers"])
    datasets["orders"] = clean_orders(datasets["orders"])
    datasets["order_items"] = clean_order_items(datasets["order_items"])
    datasets["order_payments"] = clean_order_payments(datasets["order_payments"])
    datasets["order_reviews"] = clean_order_reviews(datasets["order_reviews"])
    datasets["products"] = clean_products(datasets["products"])
    datasets["sellers"] = clean_sellers(datasets["sellers"])
    datasets["geolocation"] = clean_geolocation(datasets["geolocation"])
    datasets["category_translation"] = clean_category_translation(
        datasets["category_translation"])

    print("\n========== DATA TRANSFORMATION COMPLETED ==========\n")

    return datasets



