from number import Number_game

n=int(input('number of Rounds (1,3,5): '))
print('\n\n\n')

if n not in [1,3,5]:
    print('Invalid choice....!')
    exit()

p1=Number_game(n)
i=0
# win=False
while i<n: #i+=1
    i+=1
    print('-'*40)
    print('Round: ',i)
    print('-'*40)
    R=p1.result(int(input(f'Enter your choice: (1-{p1.max}): ')))
    if R=='You won':
        print(R)
        break
    else: print(R,'\n\n')

else:
    print('You lost')
    print(f'number: {p1.computer}')