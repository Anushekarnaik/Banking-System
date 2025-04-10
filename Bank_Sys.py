import csv
import os
if __name__=="__main__":
    a=1
    with open('BankSystem.csv', 'r', newline='') as inline:
        reader = csv.DictReader(inline)
        for row in reader:
            a+=1
    global counter
    counter = a
    while True:
        user_input=input("'Enter Your Choice' '1' for:Account Creation")
        match user_input:
            case '1':
                holder_name=input("Enter your name:")
                password=input("Enter you password:")
                int_deposit=int(input("Enter Initial Deposit Amount(minimum $100):"))
                if int_deposit>=100:
                    with open('BankSystem.csv', 'a', newline='') as outfile:
                        fieldnames = ['Account Number', 'Name', 'Password', 'Ini_Deposit']
                        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                        if counter==1:
                            writer.writeheader()
                        writer.writerow({'Account Number': counter, 'Name': holder_name, 'Password': password,
                                         'Ini_Deposit': int_deposit})
                        print(f"Processed data written'.")
                        counter+=1
                else:
                    print("Minimum $100 you have Deposit while creating account")
            case 'exit':
                print("Exiting program")
                break
            case _:
                print("You typed:",{user_input})