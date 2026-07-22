import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


def load_data(datasets):

    print("\n========== STARTING DATA LOADING ==========\n")

    # Load environment variables
    load_dotenv()

    # Create PostgreSQL connection
    engine = create_engine(
        f"postgresql+psycopg2://"
        f"{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )

    # Load all cleaned tables
    for table_name, df in datasets.items():

        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

        print(f"✓ {table_name} loaded successfully")

    print("\n========== DATA LOADING COMPLETED ==========\n")