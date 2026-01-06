Responses = {}
polling = True

while polling:
    Name = input("whats ur name? ")
    place = input("if u could go anywhere where would u go ")

    Responses[Name] = place

    again = input("another person? yes/no ")
    if again.lower() == 'no':
        polling = False

print("\n--- poll resluts ---")
for name, Place in Responses.items():
    print(f"{name} wants to go to {Place}")

