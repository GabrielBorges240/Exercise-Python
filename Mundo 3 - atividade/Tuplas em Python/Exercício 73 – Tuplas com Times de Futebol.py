times = (
    "Flamengo",
    "Palmeiras",
    "Athletico-PR",
    "Fluminense",
    "Bahia",
    "Cruzeiro",
    "Atlético-MG",
    "Santos",
    "Coritiba",
    "RB Bragantino",
    "Remo",
    "Chapecoense",
)

print('\033[1;31mLista de times do Brasileirão:\033[m', times)        
print(f'\033[1;32mOs 5 primeiros são:\033[m', times[:5])         
print(f'\033[1;33mOs 4 últimos são:\033[m', times[-4:])
print(f'\033[1;35mTimes em ordem alfabética:\033[m', sorted(times))
print(f'\033[1;96mO Chapecoense está na posição:\033[m', times.index("Chapecoense")+1)
 