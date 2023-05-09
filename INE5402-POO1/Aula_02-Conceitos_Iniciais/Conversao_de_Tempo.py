sec_tempo = int(input("Dê o tempo da operação em segundos: "))

sec_tempof = sec_tempo % 60
min_tempo = sec_tempo // 60
hor_tempo = min_tempo //60
min_tempof = min_tempo % 60

print(f"Tempo: {hor_tempo}:{min_tempof}:{sec_tempof}")