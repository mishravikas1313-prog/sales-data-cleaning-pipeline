from src.extract import extract_data
from src.transform import profile_data, transform_data
from src.validation import validate_data
from src.load import load_data

def main():

    datasets = extract_data()
    
    profile_data(datasets)

    datasets = transform_data(datasets)

    validate_data(datasets)

    load_data(datasets)
    
if __name__ == "__main__":
    main()
    

