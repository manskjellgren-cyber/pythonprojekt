import csv

def load_data(filepath):
    """Läser in data från en CSV-fil."""
    data = []
    try:
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Gör om temperaturen till ett flyttal
                row['temperature'] = float(row['temperature'])
                data.append(row)
        print(f"✅ Laddade {len(data)} rader från {filepath}")
        return data
    except FileNotFoundError:
        print(f"❌ Filen {filepath} hittades inte!")
        return None

# Lägg till detta i slutet av pipeline.py

if __name__ == "__main__":
    print("--- Starta data pipeline ---")
    raw_data = load_data('data.csv')
    transformed_data = transform_data(raw_data)

    if transformed_data:
        print("\n--- Rapport ---")
        for row in transformed_data:
            print(f"{row['date']}: {row['temperature']}°C / {row['temperature_f']}°F")
    print("--- Pipeline klar ---")
