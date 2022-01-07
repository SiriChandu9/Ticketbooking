#import library modules
import time
import random

#Define variables......
options="yes"
Ticket_No=random.randint(0,200) #used in ticket receipt
Category=[] #list includes ticket category
unit_cost=[]#list includes cost per ticket
total_qty=[]#list includes total quantity per category
total_cost=[]#list includes total cost per category

LogoDate=time.strftime("%d/%m/%Y", time.localtime(time.time()))
present_month_year=time.strftime("%m/%Y", time.localtime(time.time()))#credit card
Logoclock=time.strftime("%r",time.localtime(time.time()))
Datetime=time.strftime("%d/%m/%Y \t\t\t %H:%M:%S",time.localtime(time.time()))#used in ticket receipt

#print welcome message
print('*'*80)
print(LogoDate+"\t\t"+"Welcome to Movie Ticket Booking App"+ "\t"+' '+Logoclock)
print('*'*80)
print(' ')


#price details on ticket category
def price_detail():
    print('')
    print("price Details:")
    print(' ')
    print('Ticket Category         Cost(in Rupees)    ')
    print('-'*30)
    print('ADULT                   100    ')
    print('CHILD                   20     ')
    print('VIP                     150    ')
    print('CONCESSION              70     ')
    print(' ')

#price calculation on category selection
def calculation():
    ticket_type=int(input('How many categories of tickets do you want to purchase?(1-4)'))
    if ticket_type > 4 or ticket_type == 0:
        print('Invalid type count.retry!!!')
        print(' ')
        ticket_type=int(input('How many categories of tickets do you want to purchase?(1-4) '))
        
    print(' ')
    for i in range(ticket_type):
        Choose_Category=input('Choose a category like A for Adult or C for Child or V for Vip or CO for Concession: ')

        #Adult selection
        if Choose_Category == 'A'or Choose_Category == 'a' :
            Adult_qty=int(input("How many adult tickets do you want to purchase? "))
            print(' ')
            Total_adult_price=Adult_qty*100
            CatType='Adult'
            Category.append(CatType)
            cost=100
            unit_cost.append(cost)
            total_qty.append(Adult_qty)
            total_cost.append(Total_adult_price)
            
        #Child Selection
        elif Choose_Category =='C' or Choose_Category == 'c':
            Child_qty=int(input("How many child tickets do you want to purchase? "))
            print(' ')
            Total_child_price=Child_qty*20
            CatType='Child'
            Category.append(CatType)
            cost=20
            unit_cost.append(cost)
            total_qty.append(Child_qty)
            total_cost.append(Total_child_price)
            
        #vip Selection
        elif Choose_Category =='V' or Choose_Category == 'v':
            Vip_qty=int(input("How many vip tickets do you want to purchase? "))
            print(' ')
            Total_vip_price=Vip_qty*150
            CatType='Vip'
            Category.append(CatType)
            cost=150
            unit_cost.append(cost)
            total_qty.append(Vip_qty)
            total_cost.append(Total_vip_price)

        #Concession selection
        elif Choose_Category =='CO' or Choose_Category == 'co':
            concession_qty=int(input("How many concession tickets do you want to purchase? "))
            print(' ')
            Total_concession_price=concession_qty*70
            CatType='Concession'
            Category.append(CatType)
            cost=70
            unit_cost.append(cost)
            total_qty.append(concession_qty)
            total_cost.append(Total_concession_price)

        else:
            print(' ')
            print('please choose a valid category.')
            print(' ')
            
            
                    
#cart details before payment process
def cart_detail():
    print(' ')
    print('Bill Details:')
    print(' ')
    print("Ticket Category",'\t',"Unit Cost",'\t\t',"Qty",'\t\t',"Total cost")
    print('-'*80)
    #use to design template for bill details
    subtotal=0
    for i in range(len(Category)):
        print(Category[i],'\t\t\t',unit_cost[i], '\t\t\t',total_qty[i], '\t\t',total_cost[i])
        subtotal=int(total_cost[i])+subtotal

    print('\t\t\t\t\t\t','---------------------------')
    print('\t\t\t\t\t\t\t','Subtotal:',str(subtotal),'/-')
    print(' ')
    Tax_price=subtotal*0.15
    print('\t\t\t\t\t\t ','Tax Amount(15%): ',str(Tax_price),'/-')
    print('\t\t\t\t\t\t ','-------------------------------')
    Total=Tax_price+subtotal
    print('\t\t\t\t','Total cost of all tickets with Tax:',str(Total),'/-')


#Ticket receipt after payment process
def ticket_receipt():
    print(' ')
    print("*"*80)
    print("Ticket No:",Ticket_No,"\t\t\t\t\t",'Date:',Datetime)
    print("*"*80)
    print("Ticket Category",'\t',"Unit Cost" ,'\t\t',"QTY",'\t\t',"Total Cost")
    print(' ')

    #used to design template for ticket receipt
    subtotal=0
    for i in range(len(Category)):
        print(Category[i],'\t\t\t',unit_cost[i],'\t\t\t',total_qty[i],'\t\t',total_cost[i])
        subtotal=int(total_cost[i])+subtotal

    print('\t\t\t\t\t\t','-------------------------------')
    print('\t\t\t\t\t\t\t','Subtotal:',str(subtotal),'$')

    Tax_price=subtotal*0.15
    print('\t\t\t\t\t\t\t','Tax Amount(15%): ',str(Tax_price),'$')

    print('\t\t\t\t\t\t','-------------------------------')
    Total=Tax_price+subtotal
    print('\t\t\t\t','Total cost of all tickets with Tax: ',str(Total), '$')


#function used to write purchase data into file
def data_write_file(Category,total_qty,unit_cost,total_cost):
    with open('transaction.txt','w') as f:

        #design data representation template
        f.write("*"*50+'\n')
        f.write("Ticket No: %d\n"%Ticket_No)
        f.write(Datetime)
        f.write('\n')
        f.write("*"*50+'\n')
        f.write('\n')

        for i in range(len(Category)):
            f.write('Category: ')
            f.write('%s\n'%Category[i])
            f.write('Qty: ')
            f.write('%d\n'%total_qty[i])
            f.write('Unit cost: ')
            f.write('%d\n'%unit_cost[i])
            f.write('Total cost: ')
            f.write('%d\n'%total_cost[i])
            f.write('\n')

        f.write('------------------------------\n')
        subtotal=0
        for i in range(len(total_cost)):
            subtotal=total_cost[i]+subtotal
        f.write("TotalCost(in rupees) %.f\n"%subtotal)
        Tax_price=subtotal*0.15
        Total=Tax_price+subtotal
        f.write("TotalCost with Tax(in rupees) %.f\n"%Total)
        f.write('------------------------------\n')
        f.close()

#Ticket purchasing process
def purchase_ticket():
    #print('The ticket categories are Adult,Child,Vip and Concession.')
    #print(' ')
    show_price=input('Do you want to know the price of categories? Y/N or y/n: ')

    print(' ')
    if show_price in 'Y' or show_price in 'y':
        price_detail()
    elif show_price in 'N' or show_price in 'n':
        print("Let's purchase tickets")
        print(' ')
    else:
        print("Sorry your answer is not valid.")
        show_price=input('Do you want to know the price of categories? Y/N or y/n: ')
        print(' ')

    calculation()
    print(' ')
    cart_detail()
    print(' ')
    print('Please enter your credit card details to proceed payment')
    print(' ')
    print('Credit card Details:')
    print('-'*30)

    Card_number=input('Enter your credit card number (min 14 digit long): ')
    if len(Card_number)<14 or len(Card_number)>14:
        print(' ')
        print('Invalid credit card number.retry!!')
        Card_number=input('Enter your credit card number (min 14 digit long): ')

    print(' ')
    Expiry_date=input('Enter valid expiry date of card (month/year like 12/2021): ')
    if Expiry_date <= present_month_year:
        print('Invalid expiry date.retry!!')
        print(' ')
        Expiry_date=input('Enter valid expiry date of card (month/year like 12/2021): ')
        print(' ')
    print('Thank you for your information. we are processing your payment......')
    print(' ')
    print('You have successfully purchased the tickets.')
    print(' ')
    ticket_receipt()
    print(' ')
    print('Thank you for purchasing !!! Choose option to close the application or continue \n.')
    data_write_file(Category,total_qty,unit_cost,total_cost)

#Main menu:
while options in ("yes","y","Y","Yes"):
    print("It's show time...Book a best seat for YOU and enter into a Fantasy World !!")
    print(' ')
    print("Here comes your options:")
    print("1.Show price details")
    print("2.Purchase Tickets")
    print("3.Exit")
    print('\n')
    choice=input("choose a valid option as 1 or 2 or 3: ")
    print(' ')
    if choice == '1':
        price_detail()
        Buy_ticket=input("Do you want to purchase tickets? Y/N or y/n: ")
        print(' ')
        if Buy_ticket in("Y","y"):
            purchase_ticket()
            
    elif choice == '2':
        purchase_ticket()

    elif choice == '3':
        print("Thank you for visiting us!!!")
        break
    else:
        print("choose a valid option.")
        options='yes'
                          
            
            
        
        

    
        
            
        
    
       
    
        
    
    
    





    
            
