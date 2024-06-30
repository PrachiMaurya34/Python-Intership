import pandas as pd
from exceptions import DataCleaningError

def clean_data(input_file):
    try:
        # Load the dataset
        df = pd.read_csv(input_file)
        
        # Check for critical columns
        critical_columns = ['ObservationDate', 'Province/State', 'Country/Region', 'Last Update', 'Confirmed', 'Deaths', 'Recovered']
        for col in critical_columns:
            if col not in df.columns:
                raise DataCleaningError(f"Missing critical column: {col}")

        # Handle missing values
        df['Province/State'].fillna('Unknown', inplace=True)
        df['Confirmed'].fillna(0, inplace=True)
        df['Deaths'].fillna(0, inplace=True)
        df['Recovered'].fillna(0, inplace=True)

        # Convert data types
        df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
        df['Last Update'] = pd.to_datetime(df['Last Update'])

        # Drop duplicates
        df.drop_duplicates(inplace=True)

        return df
    except Exception as e:
        raise DataCleaningError(f"Error while cleaning data: {e}")

if __name__ == "__main__":
    input_file = 'covid_19_data.csv'
    cleaned_data = clean_data(input_file)
    cleaned_data.to_csv('clean_covid_data.csv', index=False)