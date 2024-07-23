import MySQLdb
from prettytable import PrettyTable

def line():
    for i in range(50):
        print("-",end="")
    print()

def arrow():
    for i in range(50):
        print(">",end="")
    print()

db=MySQLdb.connect("localhost","root","tiger","tick")
cur=db.cursor()
pn="                 -BOOK MY SHOW-                     "
sn="           (Feel The Theatre At Home)               "

line()
print()
for i in pn:
    print(i,end="")
print()
for i in sn:
    print(i,end="")
print()

print()
arrow()
line()
print()

while True:
    print("                 -Current Shows-                  ")
    print(""">> Mirzapur Season II
>>Laxmii
>>Aashram II
>>Ludo
>>Chhalaang
>>Serious Men
>>Kota Factory
>>Scam 1992:The Harshad Mehta Story""")
    lis=["Mirzapur Season II","Laxmii","Aashram II","Ludo","Chhalaang","Serious Men","Kota Factory","Scam 1992:The Harshad Mehta Story"]
    print("~Book any show at just Rs.20")
    print()
    arrow()
    
    print()
    print("-Booking Main Menu-")
    print("1=> Make a Booking")
    print("2=> Delete a Booking")
    print("3=> Edit Booking")
    print("4=> Display Bookings")
    print("5=> Search Record")
    print("6=> Exit")
    print()
    line()
    m=int(input("Select Task(1 to 6): "))
    line()
    
    if m==1:
        v1=input("Enter Name: ")
        v2=input("Enter Email id: ")
        v3=input("Enter Show Name(please check the spelling.): ")
        v4=int(input("Enter Phone No.(10 digits): "))
        v5=int(input("Enter Credit Card No.(16 digits): "))
        v6=input("Enter Password: ")
        if v3 in lis:
            sql='insert into BOOKINGS values("%s","%s","%s",%s,%s,"%s")'%(v1,v2,v3,v4,v5,v6)
            print(sql)
            cur.execute(sql)
            db.commit
            line()
            print()
            print("-Booking Confirmed-")
            print("-Payment Successful-")
            print()
            line()
            arrow()
            print()
        else:
            line()
            print("!!!Show Not Available!!!")
            line()

    elif m==2:
        while True:
            line()
            print("                  -Delete Menu-                  ")
            print("""1=> Delete All Record
2=> Delete by Name
3=> Delete by Email id
4=> Delete by Show Booked
5=> Delete by Phone No.
6=> Delete by Credit Card No.
7=> Delete by Password
8=> Exit to Main Menu""")
            print()
            line()
            d=int(input("Select Task(1 to 8): "))
            line()
            print()

            if d==1:
                print("Data in Table is: ")
                cur.execute('select * from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','Credit_Card_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()
                ch=input("Do You Want To Delete(Y/N): ")
                if ch=="y" or ch=="Y":
                    cur.execute('delete from BOOKINGS')
                    db.commit()
                    print(">> Data Removed <<")
                    print()
                    line()
                    print()

                else:
                    print("Continue...")
                    print()
                    line()
                    print()

            elif d==2:
                print("Data in Table is: ")
                cur.execute('select * from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','Credit_Card_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()
                ch=input("Do You Want To Delete(Y/N): ")
                if ch=="y" or ch=="Y":
                    c=input("Enter NAME(To Be Deleted): ")
                    cur.execute("select * from BOOKINGS where NAME='%s'"%c)
                    rows=cur.fetchall()
                    print(rows)
                    line()
                    c=input("Enter NAME(To Be Deleted): ")
                    cur.execute("delete from BOOKINGS where NAME='%s'"%c)
                    db.commit()
                    line()
                    print(">> Data Removed <<")
                    line()
                else:
                    print("Continue...")
                    print()
                    line()
                    print()

            elif d==3:
                print("Data in Table is: ")
                cur.execute('select * from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','Credit_Card_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()
                ch=input("Do You Want To Delete(Y/N): ")
                if ch=="y" or ch=="Y":
                    c=input("Enter EMAIL ID(To Be Deleted): ")
                    cur.execute("select * from BOOKINGS where EMAIL_ID='%s'"%c)
                    rows=cur.fetchall()
                    print(rows)
                    line()
                    c=input("Enter NAME(To Be Deleted): ")
                    cur.execute("delete from BOOKINGS where EMAIL_ID='%s'"%c)
                    db.commit()
                    line()
                    print(">> Data Removed <<")
                    line()
                else:
                    print("Continue...")
                    print()
                    line()
                    print()

            elif d==4:
                print("Data in Table is: ")
                cur.execute('select * from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','Credit_Card_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()
                ch=input("Do You Want To Delete(Y/N): ")
                if ch=="y" or ch=="Y":
                    c=input("Enter SHOW(To Be Deleted): ")
                    cur.execute("select * from BOOKINGS where SHOW_BOOKED='%s'"%c)
                    rows=cur.fetchall()
                    print(rows)
                    line()
                    c=input("Enter SHOW(To Be Deleted): ")
                    cur.execute("delete from BOOKINGS where SHOW_BOOKED='%s'"%c)
                    db.commit()
                    line()
                    print(">> Data Removed <<")
                    line()
                else:
                    print("Continue...")
                    print()
                    line()
                    print()

            elif d==5:
                print("Data in Table is: ")
                cur.execute('select * from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','Credit_Card_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()
                ch=input("Do You Want To Delete(Y/N): ")
                if ch=="y" or ch=="Y":
                    c=input("Enter PHONE NO(To Be Deleted): ")
                    cur.execute("select * from BOOKINGS where PHONE_NO='%s'"%c)
                    rows=cur.fetchall()
                    print(rows)
                    line()
                    c=input("Enter PHONE NO(To Be Deleted): ")
                    cur.execute("delete from BOOKINGS where PHONE_NO='%s'"%c)
                    db.commit()
                    line()
                    print(">> Data Removed <<")
                    line()
                else:
                    print("Continue...")
                    print()
                    line()
                    print()

            elif d==6:
                print("Data in Table is: ")
                cur.execute('select * from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','Credit_Card_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()
                ch=input("Do You Want To Delete(Y/N): ")
                if ch=="y" or ch=="Y":
                    c=input("Enter CREDITCARD NO(To Be Deleted): ")
                    cur.execute("select * from BOOKINGS where CREDITCARD_NO='%s'"%c)
                    rows=cur.fetchall()
                    print(rows)
                    line()
                    c=input("Enter CREDITCARD NO(To Be Deleted): ")
                    cur.execute("delete from BOOKINGS where CREDITCARD_NO='%s'"%c)
                    db.commit()
                    line()
                    print(">> Data Removed <<")
                    line()
                else:
                    print("Continue...")
                    print()
                    line()
                    print()

            elif d==7:
                print("Data in Table is: ")
                cur.execute('select * from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','Credit_Card_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()
                ch=input("Do You Want To Delete(Y/N): ")
                if ch=="y" or ch=="Y":
                    c=input("Enter PASSWORD(To Be Deleted): ")
                    cur.execute("select * from BOOKINGS where PASSWORD='%s'"%c)
                    rows=cur.fetchall()
                    print(rows)
                    line()
                    c=input("Enter PASSWORD(To Be Deleted): ")
                    cur.execute("delete from BOOKINGS where PASSWORD='%s'"%c)
                    db.commit()
                    line()
                    print(">> Data Removed <<")
                    line()
                else:
                    print("Continue...")
                    print()
                    line()
                    print()

            elif d==8:
                ch=input("Y(to Continue)/N(to Exit{Move to Main Menu}): ")
                if ch=="y" or ch=="Y":
                    continue
                else:
                    break
                print()
                arrow()
                print()

            else:
                arrow()
                print(">> Enter Valid Input <<")
                arrow()
                print()
                    
    elif m==3:
        while True:
            print("                  -Update Menu-                  ")
            print("""1=> Update NAME Only
2=> Update EMAIL ID Only
3=> Update SHOW BOOKED Only
4=> Update PHONE NO
5=> Update CREDITCARD NO
6=> Update PASSWORD
7=> Exit to Main Menu""")
            print()
            line()
            print()
            u=int(input("Select Task(1 to 7): "))
            print()
            line()

            if u==1:
                print("Data in Table is: ")
                cur.execute('select * from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','CreditCard_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()
                v1=input("Enter old NAME: ")
                v2=input("Enter new NAME: ")
                sql='update BOOKINGS set NAME="%s" where NAME="%s"'%(v2,v1)
                cur.execute(sql)
                db.commit()
                line()
                print()
                print(">> Data Updated <<")
                print()
                line()
                print()

            elif u==2:
                print("Data in Table is: ")
                cur.execute('select * from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','CreditCard_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()
                v1=input("Enter old EMAIL_ID: ")
                v2=input("Enter new EMAIL_ID: ")
                sql='update BOOKINGS set EMAIL_ID="%s" where EMAIL_ID="%s"'%(v2,v1)
                cur.execute(sql)
                db.commit()
                line()
                print()
                print(">> Data Updated <<")
                print()
                line()
                print()

            elif u==3:
                print("Data in Table is: ")
                cur.execute('select * from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','CreditCard_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()
                v1=input("Enter old SHOW BOOKED: ")
                v2=input("Enter new SHOW BOOKED: ")
                sql='update BOOKINGS set SHOW_BOOKED="%s" where SHOW_BOOKED="%s"'%(v2,v1)
                cur.execute(sql)
                db.commit()
                line()
                print()
                print(">> Data Updated <<")
                print()
                line()
                print()

            elif u==4:
                print("Data in Table is: ")
                cur.execute('select * from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','CreditCard_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()
                v1=input("Enter old PHONE NO: ")
                v2=input("Enter new PHONE NO: ")
                sql='update BOOKINGS set PHONE_NO=%s where PHONE_NO=%s'%(v2,v1)
                cur.execute(sql)
                db.commit()
                line()
                print()
                print(">> Data Updated <<")
                print()
                line()
                print()

            elif u==5:
                print("Data in Table is: ")
                cur.execute('select * from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','CreditCard_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()
                v1=input("Enter old CREDITCARD NO: ")
                v2=input("Enter new CREDITCARD NO: ")
                sql='update BOOKINGS set CREDITCARD_NO=%s where CREDITCARD_NO=%s'%(v2,v1)
                cur.execute(sql)
                db.commit()
                line()
                print()
                print(">> Data Updated <<")
                print()
                line()
                print()

            elif u==6:
                print("Data in Table is: ")
                cur.execute('select * from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','CreditCard_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()
                v1=input("Enter old PASSWORD: ")
                v2=input("Enter new PASSWORD: ")
                sql='update BOOKINGS set PASSWORD="%s" where PASSWORD="%s"'%(v2,v1)
                cur.execute(sql)
                db.commit()
                line()
                print()
                print(">> Data Updated <<")
                print()
                line()
                print()

            elif u==7:
                ch=input("Y(to Continue)/N(to Exit{Move to Main Menu}): ")
                if ch=="y" or ch=="Y":
                    continue
                else:
                    break
                print()
                arrow()
                print()

            else:
                arrow()
                print(">> Enter Valid Input <<")
                arrow()
                print()

    elif m==4:
        while True:
            print("                  -Display Menu-                  ")
            print("""1=> Display All Record
2=> Display Name Only
3=> Display Email id Only
4=> Display Shows Booked
5=> Display Phone No
6=> Display Credit Card No
7=> Display Password
8=> Exit To Main Menu""")
            line()
            dis=int(input("Select Task(1 to 8): "))
            line()

            if dis==1:
                print("Data in Table is: ")
                cur.execute('select * from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','Credit_Card_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()

            elif dis==2:
                cur.execute('select NAME from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['NAME'])
                for x in rows:
                    t.add_row([x])
                print(t)

            elif dis==3:
                cur.execute('select EMAIL_ID from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['EMAIL_ID'])
                for x in rows:
                    t.add_row([x])
                print(t)

            elif dis==4:
                cur.execute('select SHOW_BOOKED from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['SHOW_BOOKED'])
                for x in rows:
                    t.add_row([x])
                print(t)

            elif dis==5:
                cur.execute('select PHONE_NO from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['PHONE_NO'])
                for x in rows:
                    t.add_row([x])
                print(t)

            elif dis==6:
                cur.execute('select CREDITCARD_NO from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['CREDITCARD_NO'])
                for x in rows:
                    t.add_row([x])
                print(t)

            elif dis==7:
                cur.execute('select PASSWORD from BOOKINGS')
                rows=cur.fetchall()
                t=PrettyTable(['PASSWORD'])
                for x in rows:
                    t.add_row([x])
                print(t)

            elif dis==8:
                ch=input("Y(to Continue)/N(to Exit{Move to Main Menu}): ")
                if ch=="y" or ch=="Y":
                    continue
                else:
                    break
                print()
                arrow()
                print()

            else:
                arrow()
                print(">> Enter Valid Input <<")
                arrow()
                print()

    elif m==5:
        while True:
            print("                  -Search Menu-                 ")
            print("""1=> Search by Name
2=> Search by Email_id
3=> Search by Show Booked
4=> Search by Phone No.
5=> Search by CreditCard No.
6=> Search by Password
7=> Exit""")
            line()
            s=int(input("Select Task(1 to 7): "))
            line()

            if s==1:
                na=str(input("Enter the Name(to be searched): "))
                print("Record is: ")
                cur.execute('select * from BOOKINGS where Name="%s"'%(na))
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','Credit_Card_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()

            elif s==2:
                na=str(input("Enter the Email_id(to be searched): "))
                print("Record is: ")
                cur.execute('select * from BOOKINGS where Email_id="%s"'%(na))
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','Credit_Card_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()

            elif s==3:
                na=str(input("Enter the Show_Booked(to be searched): "))
                print("Record is: ")
                cur.execute('select * from BOOKINGS where Show_Booked="%s"'%(na))
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','Credit_Card_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()

            elif s==4:
                na=str(input("Enter the Phone_No(to be searched): "))
                print("Record is: ")
                cur.execute('select * from BOOKINGS where Phone_No="%s"'%(na))
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','Credit_Card_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()

            elif s==5:
                na=str(input("Enter the Credit_Card_No(to be searched): "))
                print("Record is: ")
                cur.execute('select * from BOOKINGS where CreditCard_No="%s"'%(na))
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','Credit_Card_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()

            elif s==6:
                na=str(input("Enter the Password(to be searched): "))
                print("Record is: ")
                cur.execute('select * from BOOKINGS where Password="%s"'%(na))
                rows=cur.fetchall()
                t=PrettyTable(['Name','Email_id','Show','Phone_No','Credit_Card_No','Password'])
                for x,y,z,a,b,c in rows:
                    t.add_row([x,y,z,a,b,c])
                print(t)
                line()

            elif s==7:
                ch=input("Y(to Continue)/N(to Exit{Move to Main Menu}): ")
                if ch=="y" or ch=="Y":
                    continue
                else:
                    break
                print()
                arrow()
                print()
                
    elif m==6:
        ch=input("Y(to Continue)/N(to Exit): ")
        if ch=="y" or ch=="Y":
            continue
        else:
            break
        print()
        arrow()
        print()

    else:
        arrow()
        print(">> Enter Valid Input <<")
        arrow()
        print()


                




           

                    

        

            
