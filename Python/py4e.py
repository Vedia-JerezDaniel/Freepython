friends = ['Carlos', 'Sergio', 'Joel']
for bf in friends:
    print('Cena de Navidad: estáis invitados', bf)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

for letter in 'banana' :
    print(letter)

print("123" + "abc")    
x = 1 + 2 * 3 - 8 / 4
x = int(98.6)

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]

fruit = ['Banana']
fruit[0] = 'b'
print(fruit)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])