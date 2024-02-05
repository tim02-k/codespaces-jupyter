#i = input('Geben sie eine positive Ganzzahl ein: ')
#num = int(i)

def quersum(num):
    if num < 0:
        num *= -1
    if num == 0:
        return int(0)
    else: return int(num%10 + quersum(num/10))

#print(quersum(num))

