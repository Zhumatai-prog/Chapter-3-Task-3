numbers = input("Enter a list of integer with space: ")
cipher = numbers.split(" ")

move = int(input("Enter a step: "))

for i in range(len(cipher)):
	cipher[i] = int(cipher[i])
print(cipher)

for i in range(move):
	n = cipher.pop(0)
	cipher.append(n)



print (cipher)