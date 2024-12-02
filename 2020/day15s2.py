mylist = '8,11,0,19,1,2'.split(',')
spoken = {}
#lastturn = 2020  # part 1
lastturn = 30000000  # part 2

def addtodict(key, val):
    key = str(key)
    if key not in spoken:
        spoken[key] = { "recent": val, "old": None }
    else:
        spoken[key]["old"] = spoken[key]["recent"]
        spoken[key]["recent"] = val
    spoken["last"] = key

count = 1
for i in range(0, len(mylist)):
    addtodict(mylist[count-1], count)
    count += 1

while count <= lastturn:
    if spoken[spoken["last"]]["old"] is None:
        addtodict(0, count)
    else:
        diff = spoken[spoken["last"]]["recent"] - spoken[spoken["last"]]["old"]
        addtodict(diff, count)
    count += 1

print(spoken["last"])
