from tkinter import *
from tkinter import filedialog
from turtle import clear, position

root = Tk()
root.configure(background = 'pink', width = 1000, height = 1000)
root.geometry("500x800")

total = 0
item_count  = []

def cart_cleared():
    global total
    global item_count
    shoppingCart.delete('1.00', END)
    orderTotal.delete('1.00', END)
    item_count = []
    total = 0

book = Button(root, text = 'book', fg = 'black', command = lambda: click('book'))
book.grid(row = 5, column = 0)
bag = Button(root, text = 'bag', fg = 'black', command = lambda: click('bag'))
bag.grid(row = 5, column = 1)
cat = Button(root, text = 'cat', fg = 'black', command = lambda: click('cat'))
cat.grid(row = 5, column = 2)

clearButton = Button(root, text = 'clear cart', fg = 'black', command = cart_cleared)
clearButton.grid(row = 16, column = 1)

space = Label(root, text = '', fg = 'pink', background = 'pink' )
space.grid(row = 8, column = 1)
space2 = Label(root, text = '', fg = 'pink', background = 'pink' )
space2.grid(row = 10, column = 1)
space3 = Label(root, text = '', fg = 'pink', background = 'pink' )
space3.grid(row = 12, column = 1)
space4 = Label(root, text = '', fg = 'pink', background = 'pink' )
space4.grid(row = 15, column = 1)

viewCart = Label(root, text = 'shopping cart', fg = 'white', background = 'black')
viewCart.grid(row = 9, column = 1)


label1 = Label(root, text = '$100', background = 'black', fg = 'white', width = 10)
label1.grid(row = 6, column = 0)
label2 = Label(root, text = '$200', background = 'black', fg = 'white', width = 10)
label2.grid(row = 6, column = 1)
label3 = Label(root, text = '$400', background = 'black', fg = 'white', width = 10)
label3.grid(row = 6, column = 2)

storeName = Label(root, text = "shruthi's store", background = 'black', fg = 'white', width = 10, padx = 100)
storeName.grid(row = 0, column = 1)

shoppingCart = Text(root, background = 'white', fg = 'black', width = 20)
shoppingCart.grid(row = 11, column = 1)
orderTotal = Text(root, background = 'white', fg = 'black', height = 10, width = 40)
orderTotal.grid(row = 14, column = 1) 
    
def click(item):
    global shoppingCart
    global total
    if item == 'book':
        total += 100
        item_count.append(item)  
        shoppingCart.insert(END, item + '\n')
    
    elif item == 'bag': 
        total += 200
        item_count.append(item)  
        shoppingCart.insert(END, item + '\n')  
        
    elif item == 'cat': 
        total += 400
        item_count.append(item)  
        shoppingCart.insert(END, item + '\n')  
        
        
        
def view_total(): 
    global item_count
    global total
    book_count = item_count.count('book')
    purchaseStringBook = '\nBooks purchased: %i ' % book_count
    bag_count = item_count.count('bag')
    purchaseStringBag = '\nBags purchased: %i ' % bag_count
    cat_count = item_count.count('cat')
    purchaseStringCat = '\nCats purchased: %i ' % cat_count   
    totalString = '\n\nYour total is: $%i' % total  
    orderTotal.insert('1.00', totalString)
    orderTotal.insert('1.00', purchaseStringBook)  
    orderTotal.insert('1.00', purchaseStringBag)   
    orderTotal.insert('1.00', purchaseStringCat)  
        
         
 
viewTotal = Button(root, text = 'view order total', fg = 'black', background = 'black', command = view_total)
viewTotal.grid(row = 13, column = 1)
    
root.mainloop()