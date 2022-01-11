
import sys
class Customer:
    '''Customer class with bank relatamted operations'''
    BankName='INDUSIND'

    def __init__(self,Name,Balance=0):

        self.Name=Name
        self.Balance=Balance

    def deposit(self,amt):
        self.Balance=amt+self.Balance
        print('After deposit the Bal:',self.Balance)

    def withdraw(self,amt):
        if amt>self.Balance:
            print('Insufficient Funds')
            sys.exit()
        else:
            self.Balance=self.Balance-amt
            print('After withdrawl the Bal:',self.Balance)
            
        
print('Welcome To:',Customer.BankName)
Name=input('Enter your Name')
c=Customer(Name)

while True:
         print('d-Deposit\nw-Withdraw\ne-Exit')

         option=input('Choose your Option')
         if option=='d' or option=='D':
             amt=float(input('Enter the amt to Deposit'))
             c.deposit(amt)
         elif option=='w' or option=='W':
             amt=float(input('Enter the amt to withdrawl'))
             c.withdraw(amt)   
         elif option=='e' or option=='E':
             print('Thanks for Banking')
             sys.exit()

         else:
             print('Choose valid option')
         
  #FirstPush.... .... 
  #SecondPush......
  #thirdPush....
       
         
         
