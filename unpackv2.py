def total(galleons, sickles, knuts, pennies):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25, "pennies": 1}

print(total(**coins), "knuts")