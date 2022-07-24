result = {
    'B': 'BattleShip',
    'C': 'Cruiser',
    'D':'Destroyer',
    'F':'Frigate'
}
for i in range(int(input())):
    a = input().upper()
    if a in ['D', 'B', 'C', 'F'] :
        print(result[a])


#SOLVED