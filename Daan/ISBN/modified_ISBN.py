#rewritten by Anish G Rao


isbn = input("")

for char in isbn:
    if not (char.isdigit() or char=='.' or char == 'X'):
        print("INPUT ERROR")
        exit()

if len(isbn) == 10:
    #replaces . with 0, and 10 with X, and sums the values 
    #multiplies each value by 10-index, which is the same as 10*first, 9*second etc.
    SUM=sum((10-i)*(j) for i,j in enumerate([0 if char=='.' else 10 if char=='X' else int(char) for char in list(isbn)]))
    if '.' in isbn:
        #checks value 1-10, and checks if it fulfills the modulo requirment
        #10-isbn.... is because that is the amount you would multiply the . value by
        #so we just check.
        print(next(x for x in range(1,11) if (SUM+(10-isbn.find('.'))*x)%11==0))
    else:
        print("VALID" if sum%11==0 else "INVALID")
    exit()

print("INPUT ERROR")
exit()