times = ["Palmeiras", "Flamengo", "Sao Paulo"]
while True:
    count = 0   
    adicionar = input("Informe um Time: ")
    times.append(adicionar)

    for time in times:
        count += 1
        print(count, " - ", time)