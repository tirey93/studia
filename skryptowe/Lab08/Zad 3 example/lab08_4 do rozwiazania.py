# 8.4. Dla pliku dane.dat obliczyć prędkość w danej chwili v=s/t
# i zapisać do pliku dane1.dat w miejscu prędkości zamiast 0.000000.
# Uwaga na dzielenie przez zero!

with open("dane.dat","r") as file_r:
    with open("dane1.dat","w") as file_w:
        for line in file_r:   #  f.readlines()
            if line[0] == "#": 
                file_w.write(line)
            else:
                all = [float(val) for val in line.split()]
                file_w.write(f'{all[0]} {all[1]} {all[1] / all[0] if all[0 != 0.0] else None}\n')

