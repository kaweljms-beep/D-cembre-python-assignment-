
sandwichOrders = [
    'pastrami', 'tuna', 'Pastrami',
    'ham', 'pastrami', 'bush_meat'
]

print("sorry we ran out of pastrami lol")

while 'pastrami' in sandwichOrders:
    sandwichOrders.remove('pastrami')

Finished_sandwiches = []

while sandwichOrders:
    sandwhich = sandwichOrders.pop(0)
    print(f"i made ur {sandwhich} sandwich")
    Finished_sandwiches.append(sandwhich)

print("\nFinished sandwiches:")
for s in Finished_sandwiches:
    print(s)
