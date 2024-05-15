from statistics import mean,median,multimode

data=[ 4,7,8.5,7.4,4,6
,3.8,8,9.1,4.2,7,8.2
,6,4,5.7,8.1,9.0,6.2]

media = mean(data)

mediana = median(data)

moda=multimode(data)

print(f"media:{media}")

print(f"mediana:{mediana}")

print(f"moda:{moda}")
