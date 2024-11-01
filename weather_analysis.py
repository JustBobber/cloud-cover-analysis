import csv

def read_csv(csv_file):
    """Read data from csv_file and return a list of [timestamp, cloudcover]"""
    data = []
    try:
        with open(csv_file, 'r') as file:
            csvreader = csv.reader(file)
            
            # Skip the first 4 lines containing metadata
            # csv files from open-meteo contains 4 lines before the data appears
            for _ in range(4):
                next(csvreader)
                
            for row in csvreader:
                timestamp = row[0]
                cloudcover = int(row[1])
                data.append([timestamp, cloudcover])
                
        return data
    except FileNotFoundError:
        print(f"Error: Could not find the file {csv_file}")
        return []

def low_to_mid_cover(data):
    """Return data where cloud cover is between 25% and 50%"""
    return [row for row in data if 25 < row[1] < 50]

def low_cover(data):
    """Return data where cloud cover is 25% or less"""
    return [row for row in data if row[1] <= 25]

def mean(data):
    """Calculate the average cloud cover"""
    if not data:
        return 0
    return sum(row[1] for row in data) / len(data)

def create_cloud_cover_report(period, data):
    """Create a report showing cloud cover statistics for the given period"""
    total_hours = len(data)
    if total_hours == 0:
        return f"No data available for {period}"
        
    medium_hours = len(low_to_mid_cover(data))
    good_hours = len(low_cover(data))
    
    report = f"Gennemsnitligt skydække i {period}: {mean(data):0.2f}%\n"
    report += f"Timer i {period} med 25-50% skydække: {medium_hours} \t"
    report += f"svarende til: {medium_hours / total_hours * 100:0.2f}%\n"
    report += f"Timer i {period} med  0-25% skydække: {good_hours} \t"
    report += f"svarende til: {good_hours / total_hours * 100:0.2f}%\n"
    
    return report

# Read data for each period
data_2024 = read_csv('lafortuna_jan01_okt31_2024.csv')
data_2023 = read_csv('lafortuna_jan01_dec31_2023.csv')
data_2022 = read_csv('lafortuna_jan01_dec31_2022.csv')

# Print reports for each period
print(create_cloud_cover_report("2024", data_2024))
print(create_cloud_cover_report("2023", data_2023))
print(create_cloud_cover_report("2022", data_2022))