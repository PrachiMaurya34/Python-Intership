import pandas as pd
import matplotlib.pyplot as plt

def load_clean_data(input_file):
    return pd.read_csv(input_file)

def basic_analysis(df):
    total_confirmed = df['Confirmed'].sum()
    total_deaths = df['Deaths'].sum()
    total_recovered = df['Recovered'].sum()

    print(f"Total Confirmed Cases: {total_confirmed}")
    print(f"Total Deaths: {total_deaths}")
    print(f"Total Recovered: {total_recovered}")

    top_countries = df.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False).head(10)
    bottom_countries = df.groupby('Country/Region')['Confirmed'].sum().sort_values().head(10)

    print("\nTop 10 Countries with the highest number of cases:")
    print(top_countries)

    print("\nBottom 10 Countries with the lowest number of cases:")
    print(bottom_countries)

    return top_countries, bottom_countries

def plot_trends(df):
    df['Date'] = pd.to_datetime(df['ObservationDate'])
    daily_data = df.groupby('Date')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(daily_data['Date'], daily_data['Confirmed'], label='Confirmed Cases')
    plt.plot(daily_data['Date'], daily_data['Deaths'], label='Deaths')
    plt.plot(daily_data['Date'], daily_data['Recovered'], label='Recovered')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('COVID-19 Trends Over Time')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    input_file = 'clean_covid_data.csv'
    df = load_clean_data(input_file)
    top_countries, bottom_countries = basic_analysis(df)
    plot_trends(df)
