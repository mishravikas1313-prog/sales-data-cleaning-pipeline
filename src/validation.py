def validate_duplicates(datasets):

    print("\n========== DUPLICATE VALIDATION ==========\n")

    for table_name, df in datasets.items():

        duplicates = df.duplicated().sum()

        print(f"{table_name} : {duplicates} duplicate rows")

def validate_missing_values(datasets):

    print("\n========== MISSING VALUE VALIDATION ==========\n")

    for table_name, df in datasets.items():

        print(f"\n{table_name.upper()}")

        print(df.isnull().sum())

def validate_relationships(datasets):

    invalid_customers = (
        ~datasets["orders"]["customer_id"]
        .isin(datasets["customers"]["customer_id"])
    ).sum()
    print(f"Orders with invalid customer_id : {invalid_customers}")

    invalid_products = (
    ~datasets["order_items"]["product_id"]
    .isin(datasets["products"]["product_id"])
    ).sum()
    print(f"Order items with invalid product_id : {invalid_products}")

    invalid_sellers = (
    ~datasets["order_items"]["seller_id"]
    .isin(datasets["sellers"]["seller_id"])
    ).sum()
    print(f"Order items with invalid seller_id : {invalid_sellers}")

    invalid_orders = (
    ~datasets["order_payments"]["order_id"]
    .isin(datasets["orders"]["order_id"])
    ).sum()
    print(f"Payments with invalid order_id : {invalid_orders}")

def validate_data(datasets):

    print("\n========== STARTING DATA VALIDATION ==========\n")

    validate_duplicates(datasets)
    validate_missing_values(datasets)
    validate_relationships(datasets)

    print("\n========== DATA VALIDATION COMPLETED ==========\n")