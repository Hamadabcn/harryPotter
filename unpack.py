# “Variable Unpacking” is a special assignment operation. 
# It allows you to assign all members of an iterable object (such as list , set ) to multiple variables at once
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "knuts")