from main import main
import config
from utilities import Stats
import pandas as pd

expecting = {
    251: Stats(1, 0, 2, 0),
    333: Stats( 1, 0, 1, 0),
    480: Stats( 1, 1, 0, 0),
    490: Stats( 1, 1, 0, 0),
    500: Stats( 1, 1, 0, 0),
    510: Stats( 1, 1, 0, 0),
    520: Stats( 1, 1, 0, 0),
    500: Stats( 1, 1, 0, 0),
    1700: Stats( 1, 1, 0, 1),
    1900: Stats( 0, 0, 0, 1),
}

title = ["th_min", "th_max", "blur", "rmse"]
results = []
for th_min in range(120, 200, 10):
    for th_max in range(th_min + 10, 200, 10):
        for blur in range(3, 17, 2):
            sum = 0
            for i in expecting.keys():
                result = main(i, th_min,  th_max, blur)
                sum += result.calculate_rmse(expecting[i])
            print(f"min: {th_min}, max: {th_max}, blur: {blur}, sum: {sum}")
            results.append([th_min, th_max, blur, sum])


df = pd.DataFrame(results)
df.to_csv("scores.csv", header=title, index=False) 
