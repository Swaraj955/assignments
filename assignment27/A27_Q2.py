class BankAccount:
    ROI = 10.5   

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder:", self.Name)
        print("Balance:", self.Amount)

    def Deposit(self):
        amt = float(input("Enter amount to deposit: "))
        self.Amount += amt
        print("Amount deposited successfully")

    def Withdraw(self):
        amt = float(input("Enter amount to withdraw: "))
        if amt <= self.Amount:
            self.Amount -= amt
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest



b1 = BankAccount("Sanket", 1000)
b2 = BankAccount("Rahul", 2000)

print("\nAccount 1")
b1.Display()
b1.Deposit()
b1.Withdraw()
print("Interest:", b1.CalculateInterest())
b1.Display()

print("\nAccount 2")
b2.Display()
b2.Deposit()
b2.Withdraw()
print("Interest:", b2.CalculateInterest())
b2.Display()