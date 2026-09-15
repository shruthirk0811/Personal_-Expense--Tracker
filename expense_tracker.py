import csv
import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt

print("welcome to Personal Expense tracker!")

expenses=[]

def save_expenses():
   with open("expense.csv","w",newline="") as file:
      writer=csv.DictWriter (
         file,
         fieldnames=["id","amount","category","date"]
      )
      writer.writeheader()
      writer.writerows(expenses)
print("Expenses saved successfully!")

print("------------------------------------")
print("  PERSONAL EXPENSE TRACKER")
print("====================================")
while True:
 
 print("1.Add an Expense")
 print("2.Viwe All Expenses")
 print("3.Generate Report")
 print("4.Show Spending Chart")
 print("5.Save and exit")
 choice=input("Enter your choice:")
 if choice=="1":
    amount=float(input("Enter expense amount : ₹"))
    category=input("Enter Category:")
    date=input("Enter date (YYYY-MM-DD):")

    expense_id=len(expenses)+1

    expense={
        "id":expense_id,
        "amount":amount,
        "category":category,
        "date":date
    }
    expenses.append(expense)



    print("\n Expense added sucessfully!")
    print("Expense ID:", expense["id"])
    print("Amount:",expense["amount"])
    print("Category:",expense["category"])
    print("Date:",expense["date"])

    

 elif choice =="2":
    print("\n *********** ALL EXPENSES *************")

    if len(expenses)==0:
       print(" No expenses found.")
    else:
       for expense in expenses:
          print("ID:", expense["id"])
          print("Date:",expense["date"])
          print("Category:",expense["category"])
          print("Amount:",expense["amount"])
          print("----------------------------------")


 elif choice =="3":
    print("\n @@@@@@@@@ EXPENSE REPORT @@@@@@@@")
    total=sum(expense["amount"]for expense in expenses)
    print("Total Spending:",total)
    categories={} 
    for expense in expenses:
        category=expense["category"]
        amount=expense["amount"]
        if category in categories:
             categories[category] += amount
        else:
             categories[category] = amount
       
    print("\n Spending by Category:")
    for category, amount in categories.items():
          print(category,":",amount)
          print("======================================")


 elif choice =="4":
    print("\n =============== SPENDING CHART ============")
    categories={}
    for expense in expenses:
       category=expense["category"]
       amount=expense["amount"]

       if category in categories:
          categories[category] += amount
       else:
          categories[category]=amount

    if categories:
       plt.bar(categories.keys(),categories.values())
       plt.xlabel("Category")
       plt.ylabel("Amount")
       plt.title("Spending by Category")
       plt.show()
    else:
       print("No expenses availabel to show.")

 elif choice =="5":
    save_expenses()
    print("Expenses saved successfully !")
    print("Thank you for using Personal Expense Tracker!")
    break

 else:
    print("Invalid choice!")
    