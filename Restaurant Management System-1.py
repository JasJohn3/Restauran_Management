from tkinter import *
import random
import time


root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management Systems")

text_Input= StringVar()
operator=""
#=======================================(Defines the frame input information, size, font, color)=======================================#
Tops = Frame(root, width = 1600,height = 50,bg="powder blue",relief = SUNKEN)
Tops.pack(side=TOP)
#=======================================(Left Frame)=======================================#
f1 = Frame(root, width = 800,height = 700, relief = SUNKEN)
f1.pack(side=LEFT)
#=======================================(Right Frame)=======================================#
f2 = Frame(root, width = 300,height = 700,relief = SUNKEN)
f2.pack(side=RIGHT)
#=======================================(Time)=======================================#
localtime=time.asctime(time.localtime(time.time()))
#=======================================(Labels for Restauran Management System)=======================================#
lblInfo = Label(Tops, font=('arial',50,'bold'),text="Restaurant Management System",fg="steel blue",bd=10,anchor ='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial',20,'bold'),text=localtime,fg="steel blue",bd=10,anchor ='w')
lblInfo.grid(row=1,column=0)
#=======================================(Left Side Functions and Methods)=======================================#
#=======================================(Calculator)=======================================#

#=======================================(Button Click function for each button in the calculator)=======================================#
def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    text_Input.set(operator)
#=======================================(Clears the display by giving a blank input)=======================================#
def btnClearDisplay():
    global operator
    operator =""
    text_Input.set(operator)

#=======================================(Equals button evaluates the string input)=======================================#
def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator =""
#=======================================(Bottom Buttons)=======================================#
#-------------------(Total Button)-----------------------------------#
def Ref():
     x = random.randint(000000,999999)
     randomRef =str(x)
     rand.set(randomRef)

     CoFries = float(Fries.get())
     CoDrinks = float(Drinks.get())
     CoFillet = float(Fillet.get())
     CoBurger = float(Burger.get())
     CoChicken_Burger = float(Chicken_Burger.get())
     CoCheese_Burger = float(Cheese_Burger.get())

     costofFries=CoFries * 0.99
     costofDrinks=CoDrinks * 0.99
     costofFillet=CoFillet * 2.99
     CostofBurger = CoBurger * 2.87
     CostChicken_Burger = CoChicken_Burger * 2.89
     CostCheese_Burger = CoCheese_Burger * 2.89

     CostofMeal = "$",str('%.2f') % (costofFries + costofDrinks + costofFillet + CostofBurger + CostChicken_Burger + CostCheese_Burger)

     PayTax = ((costofFries + costofDrinks + costofFillet + CostofBurger + CostChicken_Burger + CostCheese_Burger) * .08)

     TotalCost = (costofFries + costofDrinks + costofFillet + CostofBurger + CostChicken_Burger + CostCheese_Burger)

     Ser_Charge = ((costofFries + costofDrinks + costofFillet + CostofBurger + CostChicken_Burger + CostCheese_Burger)/99)

     Service = "$",str('%.2f' % Ser_Charge)

     OverallCost = "$",str('%.2f' % (PayTax + TotalCost + Ser_Charge))
     PaidTax = "$",str('%.2f' % PayTax)

     Service_Charge.set(Service)
     Cost.set(CostofMeal)
     Tax.set(PaidTax)
     SubTotal.set(CostofMeal)
     Total.set(OverallCost)

     
     
#-------------------(Exit Button)-----------------------------------#
def Exit():
    root.destroy()
#-------------------(Reset Button)-----------------------------------#
def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Fillet.set("")
    Chicken.set("")
    Cheese.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")
 
    
txtDisplay = Entry(f2,font=('arial',20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue",justify='right')
txtDisplay.grid(columnspan=4)
#=======================================(Calculator Buttons 7,8,9,+)=======================================#

#-------------------Button 7-----------------------------------#
btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7", bg="powder blue",
            command=lambda: btnClick(7)).grid(row=2,column=0)
#-------------------Button 8-----------------------------------#
btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8", bg="powder blue",
            command=lambda: btnClick(8)).grid(row=2,column=1)
#-------------------Button 9-----------------------------------#
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9", bg="powder blue",
            command=lambda: btnClick(9)).grid(row=2,column=2)
#-------------------Button (+)-----------------------------------#
Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+", bg="powder blue",
            command=lambda: btnClick("+")).grid(row=2,column=3)

#=======================================(Calculator Buttons 4,5,6,-)=======================================#

#-------------------Button 4-----------------------------------#
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4", bg="powder blue",
            command=lambda: btnClick(4)).grid(row=3,column=0)
#-------------------Button 5-----------------------------------#
btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5", bg="powder blue",
            command=lambda: btnClick(5)).grid(row=3,column=1)
#-------------------Button 6-----------------------------------#
btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6", bg="powder blue",
            command=lambda: btnClick(6)).grid(row=3,column=2)
#-------------------Button (-)-----------------------------------#
Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-", bg="powder blue",
            command=lambda: btnClick("-")).grid(row=3,column=3)
#=======================================(Calculator Buttons 1,2,3,*)=======================================#

#-------------------Button 1-----------------------------------#
btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1", bg="powder blue",
            command=lambda: btnClick(1)).grid(row=4,column=0)
#-------------------Button 2-----------------------------------#
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2", bg="powder blue",
            command=lambda: btnClick(2)).grid(row=4,column=1)
#-------------------Button 3-----------------------------------#
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3", bg="powder blue",
            command=lambda: btnClick(3)).grid(row=4,column=2)
#-------------------Button (*)-----------------------------------#
Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*", bg="powder blue",
            command=lambda: btnClick("*")).grid(row=4,column=3)
#=======================================(Calculator Buttons 0,Clear,Equals, Divide)=======================================#

#-------------------Button 0-----------------------------------#
btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0", bg="powder blue",
            command=lambda: btnClick(0)).grid(row=5,column=0)
#-------------------Button (C)-----------------------------------#
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C", bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)
#-------------------Button (=)-----------------------------------#
btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=", bg="powder blue",command=btnEqualsInput).grid(row=5,column=2)
#-------------------Button (/)-----------------------------------#
Divide=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/", bg="powder blue",
            command=lambda: btnClick("/")).grid(row=5,column=3)
#=======================================(Right Side Functions and Methods)=======================================#
#=======================================(Restaurant Info 1)=======================================#

#-----------------------------------------(Variables)----------------------------------------------------#
rand =StringVar()
Fries =StringVar()
Burger =StringVar()
Fillet =StringVar()
Chicken =StringVar()
Cheese =StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Chicken_Burger=StringVar()
Cheese_Burger=StringVar()

#-----------------------------------------(Reference Number)----------------------------------------------------#
lblReference = Label(f1,font=('arial',16,'bold'),text="Reference",bd=16, anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4, bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)
#-----------------------------------------(Fries)----------------------------------------------------#
lblFries = Label(f1,font=('arial',16,'bold'),text="Fries",bd=16, anchor='w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4, bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)
#-----------------------------------------(Burger)----------------------------------------------------#
lblBurger = Label(f1,font=('arial',16,'bold'),text="Burger",bd=16, anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4, bg="powder blue",justify='right')
txtBurger.grid(row=2,column=1)
#-----------------------------------------(Fillet)----------------------------------------------------#
lblFillet = Label(f1,font=('arial',16,'bold'),text="Fillet",bd=16, anchor='w')
lblFillet.grid(row=3,column=0)
txtFillet=Entry(f1,font=('arial',16,'bold'),textvariable=Fillet,bd=10,insertwidth=4, bg="powder blue",justify='right')
txtFillet.grid(row=3,column=1)
#-----------------------------------------(Chicken)----------------------------------------------------#
lblChicken = Label(f1,font=('arial',16,'bold'),text="Chicken",bd=16, anchor='w')
lblChicken.grid(row=4,column=0)
txtChicken=Entry(f1,font=('arial',16,'bold'),textvariable=Chicken_Burger,bd=10,insertwidth=4, bg="powder blue",justify='right')
txtChicken.grid(row=4,column=1)
#----------------------------------(Cheese)----------------------------------------------------#
lblCheese = Label(f1,font=('arial',16,'bold'),text="Cheese",bd=16, anchor='w')
lblCheese.grid(row=5,column=0)
txtCheese=Entry(f1,font=('arial',16,'bold'),textvariable=Cheese_Burger,bd=10,insertwidth=4, bg="powder blue",justify='right')
txtCheese.grid(row=5,column=1)
#=======================================(Restaurant Info 2)=======================================#

#-----------------------------------------(Drinks)----------------------------------------------------#
lblDrinks = Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16, anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4, bg="#ffffff",justify='right')
txtDrinks.grid(row=0,column=3)
#-----------------------------------------(Cost)----------------------------------------------------#
lblCost = Label(f1,font=('arial',16,'bold'),text="Cost",bd=16, anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4, bg="#ffffff",justify='right')
txtCost.grid(row=1,column=3)
#-----------------------------------------(Service Charge)----------------------------------------------------#
lblService = Label(f1,font=('arial',16,'bold'),text="Service Charge",bd=16, anchor='w')
lblService.grid(row=2,column=2)
txtService=Entry(f1,font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4, bg="#ffffff",justify='right')
txtService.grid(row=2,column=3)
#-----------------------------------------(State Tax)----------------------------------------------------#
lblStateTax = Label(f1,font=('arial',16,'bold'),text="State Tax",bd=16, anchor='w')
lblStateTax.grid(row=3,column=2)
txtStateTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4, bg="#ffffff",justify='right')
txtStateTax.grid(row=3,column=3)
#-----------------------------------------(Sub Total)----------------------------------------------------#
lblSubTotal = Label(f1,font=('arial',16,'bold'),text="SubTotal",bd=16, anchor='w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4, bg="#ffffff",justify='right')
txtSubTotal.grid(row=4,column=3)
#-----------------------------------------(Total Cost)----------------------------------------------------#
lblTotal = Label(f1,font=('arial',16,'bold'),text="Total",bd=16, anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal=Entry(f1,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4, bg="#ffffff",justify='right')
txtTotal.grid(row=5,column=3)

#=======================================(Bottom Buttons)=======================================#
#-----------------------------------------(Total)----------------------------------------------------#
btnTotal=Button(f1,padx=16,pady=8, bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text="Total", bg="powder blue",command= Ref).grid(row=7,column=1)
#-----------------------------------------(Reset)----------------------------------------------------#
btnReset=Button(f1,padx=16,pady=8, bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text="Reset", bg="powder blue",command= Reset).grid(row=7,column=2)
#-----------------------------------------(Exit)----------------------------------------------------#
btnExit=Button(f1,padx=16,pady=8, bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text="Exit", bg="powder blue",command= Exit).grid(row=7,column=3)

root.mainloop()
