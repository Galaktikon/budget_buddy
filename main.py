import tkinter as tk

HEIGHT = 700
WIDTH = 900

promptCount = 1
values = []

def getResponse(label):
    value = responseEntry.get()
    label['text'] = "$" + value
    values.append(int(value))
    
def getResponseA(label):
    value = responseEntry.get()
    label['text'] = "$" + str(int(value)*12)
    
def calculateBudget():
    income = 0
    expenses = 0
    
    for x in range(0, 3):
        income += values[x]
    for x in range(3, len(values)):
        expenses += values[x]
        
    if income > expenses:
        resultLabel['text'] = "Your income is " + str(income - expenses) + " above your expenses, keep it up!"
    elif expenses > income:
        resultLabel['text'] = "Your income is " + str(expenses - income) + " below your expenses, consider canceling a subscription or finding a higher paying job"
    else:
        resultLabel['text'] = "Your income is the same as your expenses, you have no left over money!"
        
def enterFunction():
    global promptCount
    
    if promptCount == 1:
        getResponse(miValue)
        getResponseA(aiValue)
        promptLabel['text'] = "Enter your monthly investment profits (if none enter 0)"
        promptCount = 2
    elif promptCount == 2:
        getResponse(mipValue)
        getResponseA(aipValue)
        promptLabel['text'] = "Enter your extra cash"
        promptCount = 3
    elif promptCount == 3:
        getResponse(utmValue)
        promptLabel['text'] = "Enter your morgage or monthly rent"
        promptCount = 4
    elif promptCount == 4:
        getResponse(rentValue)
        promptLabel['text'] = "Enter your monthly food expenses"
        promptCount = 5
    elif promptCount == 5:
        getResponse(fValue)
        promptLabel['text'] = "Enter your monthly entertainment expenses"
        promptCount = 6
    elif promptCount == 6:
        getResponse(entValue)
        promptLabel['text'] = "Enter your monthly car expenses"
        promptCount = 7
    elif promptCount == 7:
        getResponse(carValue)
        promptLabel['text'] = "Enter your other expenses"
        promptCount = 8
    elif promptCount == 8:
        getResponse(etcValue)
        calculateBudget()

root = tk.Tk()
root.title("Budget Buddy")

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

mainFrame = tk.Frame(root, bg = '#adadad', bd = 5)
mainFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) 

title = tk.Label(mainFrame, text = "Budget Buddy", font = 30, bg = '#ede968')
title.place(relx = 0.3, rely = 0.02, relwidth = 0.4, relheight = 0.05)

incomeFrame = tk.Frame(mainFrame, bg = '#b8e8ae', bd = 5)
incomeFrame.place(relx = 0.05, rely = 0.1, relwidth = 0.425, relheight = 0.5)

miLabel = tk.Label(incomeFrame, text = "Monthly Income:", font = 20, anchor = "w")
miLabel.place(relx = 0, rely = 0, relwidth = 0.7, relheight = 0.2)
miValue = tk.Label(incomeFrame, text = "$0", font = 20, anchor = "e")
miValue.place(relx = 0.7, rely = 0, relwidth = 0.3, relheight = 0.2)

aiLabel = tk.Label(incomeFrame, text = "Annual Income:", font = 20, anchor = "w")
aiLabel.place(relx = 0, rely = 0.2, relwidth = 0.7, relheight = 0.2)
aiValue = tk.Label(incomeFrame, text = "$0", font = 20, anchor = "e")
aiValue.place(relx = 0.7, rely = 0.2, relwidth = 0.3, relheight = 0.2)

mipLabel = tk.Label(incomeFrame, text = "Monthly Investment Profits:", font = 20, anchor = "w")
mipLabel.place(relx = 0, rely = 0.4, relwidth = 0.7, relheight = 0.2)
mipValue = tk.Label(incomeFrame, text = "$0", font = 20, anchor = "e")
mipValue.place(relx = 0.7, rely = 0.4, relwidth = 0.3, relheight = 0.2)

aipLabel = tk.Label(incomeFrame, text = "Annual Investment Profits:", font = 20, anchor = "w")
aipLabel.place(relx = 0, rely = 0.6, relwidth = 0.7, relheight = 0.2)
aipValue = tk.Label(incomeFrame, text = "$0", font = 20, anchor = "e")
aipValue.place(relx = 0.7, rely = 0.6, relwidth = 0.3, relheight = 0.2)

utmLabel = tk.Label(incomeFrame, text = "Extra money:", font = 20, anchor = "w")
utmLabel.place(relx = 0, rely = 0.8, relwidth = 0.7, relheight = 0.2)
utmValue = tk.Label(incomeFrame, text = "$0", font = 20, anchor = "e")
utmValue.place(relx = 0.7, rely = 0.8, relwidth = 0.3, relheight = 0.2)

expenseFrame = tk.Frame(mainFrame, bg = '#e8aeae', bd = 5)
expenseFrame.place(relx = 0.525, rely = 0.1, relwidth = 0.425, relheight = 0.5)

rentLabel = tk.Label(expenseFrame, text = "Morgage / Rent:", font = 20, anchor = "w")
rentLabel.place(relx = 0, rely = 0, relwidth = 0.7, relheight = 0.2)
rentValue = tk.Label(expenseFrame, text = "-$0", font = 20, anchor = "e")
rentValue.place(relx = 0.7, rely = 0, relwidth = 0.3, relheight = 0.2)

fLabel = tk.Label(expenseFrame, text = "Food:", font = 20, anchor = "w")
fLabel.place(relx = 0, rely = 0.2, relwidth = 0.7, relheight = 0.2)
fValue = tk.Label(expenseFrame, text = "-$0", font = 20, anchor = "e")
fValue.place(relx = 0.7, rely = 0.2, relwidth = 0.3, relheight = 0.2)

entLabel = tk.Label(expenseFrame, text = "Entertainment:", font = 20, anchor = "w")
entLabel.place(relx = 0, rely = 0.4, relwidth = 0.7, relheight = 0.2)
entValue = tk.Label(expenseFrame, text = "-$0", font = 20, anchor = "e")
entValue.place(relx = 0.7, rely = 0.4, relwidth = 0.3, relheight = 0.2)

carLabel = tk.Label(expenseFrame, text = "Car Payment:", font = 20, anchor = "w")
carLabel.place(relx = 0, rely = 0.6, relwidth = 0.7, relheight = 0.2)
carValue = tk.Label(expenseFrame, text = "-$0", font = 20, anchor = "e")
carValue.place(relx = 0.7, rely = 0.6, relwidth = 0.3, relheight = 0.2)

etcLabel = tk.Label(expenseFrame, text = "Other:", font = 20, anchor = "w")
etcLabel.place(relx = 0, rely = 0.8, relwidth = 0.7, relheight = 0.2)
etcValue = tk.Label(expenseFrame, text = "-$0", font = 20, anchor = "e")
etcValue.place(relx = 0.7, rely = 0.8, relwidth = 0.3, relheight = 0.2)

promptLabel = tk.Label(mainFrame, text = "Enter your monthly income then press the button.", font = 12, anchor = "w", bd = 3)
promptLabel.place(relx = 0.05, rely = 0.7, relwidth = 0.54, relheight = 0.05)
responseEntry = tk.Entry(mainFrame, font = 12, bd = 3)
responseEntry.place(relx = 0.60, rely = 0.7, relwidth = 0.19, relheight = 0.05)
responseButton = tk.Button(mainFrame, text = "Enter", font = 12, bd = 3, command = enterFunction)
responseButton.place(relx = 0.8, rely = 0.7, relwidth = 0.15, relheight = 0.05)

resultLabel = tk.Label(mainFrame, text = "", font = 12, anchor = "w", bd = 3, wraplength = 500, justify = 'center')
resultLabel.place(relx = 0.2, rely = 0.8, relwidth = 0.6, relheight = 0.15)

root.mainloop()
