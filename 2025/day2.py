#read txt file
with open('2025/day2-input.txt') as f:
    line = f.readline()
ranges = [tuple(map(int, r.split('-'))) for r in line.strip().split(',')]
counter1 = 0
counter2 = 0
import math
def get_divisors(n):
    divs = set() # Using a set to automatically handle duplicates for perfect squares
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i) # Add the corresponding divisor
    return sorted(list(divs)) # Convert to a sorted list
for r in ranges:
    for n in range(r[0], r[1]+1):
        s=str(n)
        if s[:len(s)//2]==s[len(s)//2:]:
            counter1+=n
        devisors=get_divisors(len(s))
        for d in devisors:
            invalid=True
            if d==len(s):
                invalid=False
                break
            for i in range(1,len(s)//d):
                if s[(i*d):(i+1)*d]!=s[0:d]:
                    invalid=False
                    break
            if invalid:
                break
        if invalid:
            counter2+=n        
print(counter1)
print(counter2)