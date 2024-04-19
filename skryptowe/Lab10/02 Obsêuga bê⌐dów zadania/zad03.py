# Napisz przykładowy kod z obsługą błędów przy odczycie ze słownika nieistniejącego klucza

dict = {"key": 5,
        "otherKey": "value"}
try:
    value = dict["not_exists"]
    print(value)
except:
    print("Key doesn't exists")