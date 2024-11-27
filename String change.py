Sen = "handled team communication and operations for 60+ People and Reduced 1 Hour of Work by Creating Weekly Process Reports, Dashboards and Ad hoc Analysis using Advanced Excel functions(VLOOKUP, Pivot tables) and PowerPoint."

result = ""
for i in Sen:
    if i.isupper():
        result += i.lower()
    else:
        result += i

print(result)
