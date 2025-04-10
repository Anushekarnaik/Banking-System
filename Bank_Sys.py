import csv

if __name__=="__main__":
    a=1
    with open('BankSystem.csv', 'r', newline='') as inline:
        reader = csv.DictReader(inline)
        for row in reader:
            a+=1
    global counter
    counter = a
    while True:
        user_input=input("\n'1' for:Account Creation\n'2' for:Log In\n'exit' for:Exit the Program\n'Enter Your Choice':")
        match user_input:
            case '1':
                holder_name = input("Enter your name:")
                password = input("Enter you password:")
                int_deposit = int(input("Enter Initial Deposit Amount(minimum $100):"))
                if int_deposit >= 100:
                    st = str(counter) + '.csv'
                    with open(st, 'w', newline='') as o_file:
                        writer_r = csv.writer(o_file)
                        writer_r.writerow([f'Welcome To Online Banking'])
                        writer_r.writerow([f'Your Account No:{counter} has been created'])
                        writer_r.writerow([f'Initial Amount Added ${int_deposit}'])
                    with open('BankSystem.csv', 'a', newline='') as outfile:
                        fieldnames = ['Account Number', 'Name', 'Password', 'Ini_Deposit']
                        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                        if counter == 1:
                            writer.writeheader()
                        writer.writerow({'Account Number': counter, 'Name': holder_name, 'Password': password,
                                         'Ini_Deposit': int_deposit})
                        print(f"Processed data written to File.")
                        counter += 1
                else:
                    print("Minimum $100 you have Deposit while creating account")

            case '2':
                a=False
                acc_no=int(input("Enter you Account Number to log In:"))
                pass_word=input("Enter your Password:")
                with open('BankSystem.csv', 'r', newline='') as inline:
                    reader = csv.DictReader(inline)
                    for row in reader:
                        if  acc_no==int(row['Account Number']) and pass_word==row['Password']:
                            a=True
                            break
                if not a:
                    print("Account number and Password is not Matching!\n go for'2' once again Typed Your Account Number and Password")
                while a:
                    user_i=input("\n'1' for:Check Balance\n'2' for:Deposit Money\n'3' for Withdraw Money\n'4' for:Transfer Money\n'5' for:Passbook print\n'6' for:Logout\n'Enter Your Choice':")
                    match user_i:
                        case '1':
                            with open('BankSystem.csv', 'r', newline='') as inline:
                                reader = csv.DictReader(inline)
                                for row in reader:
                                    if acc_no == int(row['Account Number']):
                                        print("Balance Amount:$",int(row['Ini_Deposit']))
                                        break
                        case '2':
                            rows=[]
                            res=0
                            dep_amount=int(input("Enter Deposit Amount:$"))
                            with open('BankSystem.csv', 'r', newline='') as inline:
                                reader = csv.DictReader(inline)
                                for row in reader:
                                    if acc_no == int(row['Account Number']):
                                        res=int(row['Ini_Deposit'])+dep_amount
                                        print("Balance Amount After Deposit:$",res)
                                        row['Ini_Deposit']=str(res)
                                    rows.append(row)
                            with open('BankSystem.csv', 'w', newline='') as inline:
                                fieldnames = ['Account Number', 'Name','Password', 'Ini_Deposit']
                                writer = csv.DictWriter(inline, fieldnames=fieldnames)
                                writer.writeheader()
                                writer.writerows(rows)
                            print("Deposit updated successfully.")
                            st = str(acc_no) + '.csv'
                            with open(st, 'a', newline='') as o_file:
                                writer_r = csv.writer(o_file)
                                writer_r.writerow([f'Deposit of {dep_amount} is success Balance:${res} '])
                        case '3':
                            res=0
                            with_draw=int(input("Enter the Withdraw Amount:"))
                            rows = []
                            with open('BankSystem.csv', 'r', newline='') as inline:
                                reader = csv.DictReader(inline)
                                for row in reader:
                                    if acc_no == int(row['Account Number']):
                                        if with_draw<int(row['Ini_Deposit']):
                                            res = int(row['Ini_Deposit']) - with_draw
                                            row['Ini_Deposit'] = str(res)
                                            print(f"Withdraw of Amount {with_draw} successful!")
                                            print("Balance Amount After Withdrawal:$", res)
                                        else:
                                            print("Insufficient Fund!!")
                                    rows.append(row)
                            with open('BankSystem.csv', 'w', newline='') as inline:
                                fieldnames = ['Account Number', 'Name', 'Password', 'Ini_Deposit']
                                writer = csv.DictWriter(inline, fieldnames=fieldnames)
                                writer.writeheader()
                                writer.writerows(rows)
                            st = str(acc_no) + '.csv'
                            with open(st, 'a', newline='') as o_file:
                                writer_r = csv.writer(o_file)
                                writer_r.writerow([f'Withdraw of {with_draw} is success Balance:${res} '])
                        case '4':
                            a = False
                            A= False
                            amount_send = int(input("Enter the Transfer Amount:"))
                            acc_no1=int(input("Enter the Account number to send:"))
                            if acc_no!=acc_no1:
                                with open('BankSystem.csv', 'r', newline='') as inline:
                                    reader = csv.DictReader(inline)
                                    for row in reader:
                                        if acc_no1 == int(row['Account Number']):
                                            A=True
                                            break
                                    if not A:
                                        print("You entered Account Number is not available!")
                                        A=True
                                        a=True
                                    else:
                                        res=0
                                        rows = []
                                        with open('BankSystem.csv', 'r', newline='') as inline:
                                            reader = csv.DictReader(inline)
                                            for row in reader:
                                                if acc_no == int(row['Account Number']):
                                                    if amount_send < int(row['Ini_Deposit']):
                                                        res = int(row['Ini_Deposit']) - amount_send
                                                        row['Ini_Deposit'] = str(res)
                                                        print(f"Amount {amount_send} detected!")
                                                        a = True
                                                        st = str(acc_no) + '.csv'
                                                        with open(st, 'a', newline='') as o_file:
                                                            writer_r = csv.writer(o_file)
                                                            writer_r.writerow([f'Transfer of {amount_send} for Account No:{acc_no1} is success Balance:${res} '])
                                                rows.append(row)
                                        with open('BankSystem.csv', 'w', newline='') as inline:
                                            fieldnames = ['Account Number', 'Name', 'Password', 'Ini_Deposit']
                                            writer = csv.DictWriter(inline, fieldnames=fieldnames)
                                            writer.writeheader()
                                            writer.writerows(rows)
                                        if not a:
                                            print("Insufficient Fund to Transform the Amount!!")
                                            a=True
                                        else:
                                            rows = []
                                            with open('BankSystem.csv', 'r', newline='') as inline:
                                                reader = csv.DictReader(inline)
                                                for row in reader:
                                                    if acc_no1 == int(row['Account Number']):
                                                        res = int(row['Ini_Deposit']) + amount_send
                                                        row['Ini_Deposit'] = str(res)
                                                    rows.append(row)
                                            with open('BankSystem.csv', 'w', newline='') as inline:
                                                fieldnames = ['Account Number', 'Name', 'Password', 'Ini_Deposit']
                                                writer = csv.DictWriter(inline, fieldnames=fieldnames)
                                                writer.writeheader()
                                                writer.writerows(rows)
                                            print("Transformed  successfully.")
                                            st = str(acc_no1) + '.csv'
                                            with open(st, 'a', newline='') as o_file:
                                                writer_r = csv.writer(o_file)
                                                writer_r.writerow([f'Transfer of {amount_send} form Account No:{acc_no} to you is success Balance:${res} '])
                            else:
                                print("Account Number is yours\n Enter correct Account Number!")
                                A=True
                                a=True
                        case '5':
                            st = str(acc_no) + '.csv'
                            with open(st, 'r', newline='') as o_file:
                                reader=csv.reader(o_file)
                                for i in reader:
                                    print(i)
                        case '6':
                            print("Log outing!!")
                            break
            case 'exit':
                print("Exiting program")
                break
            case _:
                print("You typed:",{user_input})