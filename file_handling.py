import pandas as pd

def save_clean_data(df, output_file):
    df.to_csv(output_file, index=False)

def load_clean_data(input_file):
    return pd.read_csv(input_file)

if __name__ == "__main__":
    # Test the functions
    cleaned_data = pd.read_csv('clean_covid_data.csv')
    save_clean_data(cleaned_data, 'clean_covid_data.csv')
    loaded_data = load_clean_data('clean_covid_data.csv')
    print(loaded_data.head())
