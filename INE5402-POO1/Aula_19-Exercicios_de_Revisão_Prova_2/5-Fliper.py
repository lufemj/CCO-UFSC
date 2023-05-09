while True:
    seq = input("Informe a sequencia de numeros: ").split()


    dic = {}
    dic['A'] = ['1', '1'] 
    dic['B'] = ['1', '0']
    dic['C'] = ['0', '0'] , ['0', '1']


    for key, value in dic.items():
        if key == 'C':
            for i in range(2):
                if value[i] == seq:
                    print(key)
        elif value == seq:
            print(key)