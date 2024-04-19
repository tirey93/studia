# Napisz przykładowy kod z obsługą błędów przy otwieraniu pliku do odczytu, który nie istnieje.

try:
    open('file_not_exists')
except FileNotFoundError as e:
    print(f"Error was found: {e}")

