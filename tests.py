from main import *
print("Testing");
k = 20;                       # Number of iterations

#Test case 0
print("Test0:");
n=177;                        # testing any single prime number
if (isPrime(n,k)):
    print (n,"is probably prime");
else:
    print(n,"is a composite");
    print("\n");

#Test case 1 from 1 to 10 000, showing 15 nubmers in a row)
print("Test1:");
print("All primes smaller than 10 000: ");
j=1;                          # iterator to print only 15 numbers in a row
for n in range(1, 10000):
    if (isPrime(n, k)):       # running the test
        print(n, end=" ");
        j+=1;
    if (j==15):
        print("\n");
        j=1;

#Test case 2 accuracy verification
print("\n","Test2:");
print("\n","Accuracy of the test for arbitrary prime number found beforehand");
print("k=20");
n=9929;                        # prime number found before
if (isPrime(n,k)):
    print(n, end=" ");
    print(Accuracy(n,k),"%");
else:
    print(n,"is a composite");
    print("\n");

#Test case 3 greater k
print("\n","Test3:");
k=50;
print("\n","Accuracy of the test for arbitrary prime number found beforehand");
print("k=50");
n=9929;
if (isPrime(n,k)):
    print(n, end=" ");
    print(Accuracy(n,k),"%");
else:
    print(n,"is a composite");
    print("\n");

#Test case 4 large prime number
print("\n","Test4:");
print("\n","Accuracy of the test for arbitrary large prime number found beforehand")
n=110087781361756128648241472441; # random known prime number
k=1;
print("k=1");
if (isPrime(n,k)):
    print(n, end=" ");
    print(Accuracy(n, k), "%");
else:
    print(n,"is a composite");
    print("\n");
k=20000;
print("k=20000");
if (isPrime(n,k)):
    print(n, end=" ");
    print(Accuracy(n, k), "%");
else:
    print(n,"is a composite");
    print("\n");