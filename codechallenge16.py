import os
print("----------------------------------------")
print("Clients' Water Information System")
print("----------------------------------------")

client_list = {}

while True:

    print("Choose what you want to do \n a - add the name of client \n b - name of client + address \n c - name of client + water bill \n d - exit")

    s = input("=--->").lower

    def client():
        for w,m in client_list.items():
            print(f"name -- {w}, address -- {m}")


    if s == 'a':
        name = input('Name: ').lower()
        address = input('Address: ').lower()

        client_list[name] = address
        client()

        os.system('cls')
        continue

