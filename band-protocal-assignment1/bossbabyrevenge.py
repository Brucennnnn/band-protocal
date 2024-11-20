def boss_baby_revenge(s):
    countRevenge=0
    if len(s)==0:
        return "Good boy"
    if s[0]=="R":
        return "Bad boy"
    for char in s:
        if char == "S":
            countRevenge += 1
        elif char == "R":
            countRevenge = max(0, countRevenge - 1)
    return "Good boy" if countRevenge == 0 else "Bad boy" 



