import random
import math

# This function will say if the passed variable is prime number or not
def computeprime(n):
    if n%2==0:return False
    for i in range(2,n//2+1):
    	if(n%i==0):
    		return False
    return True

# This function implements the Euclidian algorithm to find H.C.F.  or GCD of two numbers
def computeHCF(x, y):
	while y:
		x, y = y, x % y
	return x

# creating a list of prime numbers between range 100 to 200, since larger the prime number more it is secured
prime_list=[x for x in range(101,200,2) if computeprime(x)]

# selecting two random  prime nummbers from the list
p = random.choice(prime_list)
q = random.choice(prime_list)

print("the two large prime numbers selected are %d,%d"%(p,q))

# calculating the product of selected prime numbers and euler's totient 
num = p*q
phi = (p-1)*(q-1)

print("the product of two selected prime numbers and euler's totient are : %d, %d"%(num,phi))

#generating public key t should be greater than 1 and less than num
gen_key = True
while gen_key:

	en_key = random.randint(2,num-1)
	if computeHCF(en_key,phi) ==1 :
		gen_key = False
		print("the encryption(public) key generated is %d" %en_key)


# generating private key
gen_key1 = True
while gen_key1:
	dc_key = random.randint(2,100000)
	if (dc_key*en_key)% phi == 1:
		gen_key1 = False
		print("the decryption(private) key generated is %d" %dc_key)


#encryption activity, ord() is built in func which gives ascii number of each caharcter
mystr = input("enter the data to encrypt :")
cryp_text = []
for i in range(len(mystr)):
	m = ord(mystr[i])
	c = (m**en_key)%num
	cryp_text.append(c)
print("the encrypted data is :")
print(cryp_text)

# Decryption activity, chr(ascii) will give the plain text 
plain_text = ""
for j in cryp_text :
	pt = (j**dc_key)%num
	plain_text +=chr(pt)
print("the decrypted data is : " + plain_text)











