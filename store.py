from tkinter import *
from tkinter import filedialog
from turtle import clear, position
from tkinter import font 

font_tuple = ('Monospace', 10)

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
    
cat_image = PhotoImage(file = r"/Users/shruthituplur/cat.png")
cat_image_resized = cat_image.subsample(10, 10)

bag_pic = PhotoImage(file = "/Users/shruthituplur/bag.png")
bag_pic_resized = bag_pic.subsample(17, 18)

book_pic = PhotoImage(file = "/Users/shruthituplur/book.png")
book_pic_resized = book_pic.subsample(16, 16)

book = Button(root, text = 'book', fg = 'black', image = book_pic_resized, command = lambda: click('book'))
book.grid(row = 5, column = 0)
bag = Button(root, text = 'bag', fg = 'black', image = bag_pic_resized, command = lambda: click('bag'))
bag.grid(row = 5, column = 1)
cat = Button(root, font = font_tuple, text = 'cat', image = cat_image_resized, fg = 'black', command = lambda: click('cat'))
cat.grid(row = 5, column = 2)

clearButton = Button(root, text = 'clear cart', fg = '#AA336A', command = cart_cleared)
clearButton.grid(row = 16, column = 1)

space = Label(root, text = '', fg = 'pink', background = 'pink' )
space.grid(row = 8, column = 1)
space2 = Label(root, text = '', fg = 'pink', background = 'pink' )
space2.grid(row = 10, column = 1)
space3 = Label(root, text = '', fg = 'pink', background = 'pink' )
space3.grid(row = 12, column = 1)
space4 = Label(root, text = '', fg = 'pink', background = 'pink' )
space4.grid(row = 15, column = 1)
space5 =  Label(root, text = '', fg = 'pink', background = 'pink' )
space5.grid(row = 1, column = 1)
viewCart = Label(root, text = 'shopping cart', fg = 'white', background = '#AA336A')
viewCart.grid(row = 9, column = 1)


label1 = Label(root, text = 'book - $100', background = '#AA336A', fg = 'white', width = 10)
label1.grid(row = 6, column = 0)
label2 = Label(root, text = 'bag - $200', background = '#AA336A', fg = 'white', width = 10)
label2.grid(row = 6, column = 1)
labelCat = Label(root, text = 'cat - $400', background = '#AA336A', fg = 'white', width = 10)
labelCat.grid(row = 6, column = 2)

storeName = Label(root, text = "shruthi's store", background = '#AA336A', fg = 'white', width = 10, padx = 100)
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
        
         
 
viewTotal = Button(root, text = 'view cart total', fg = '#AA336A', background = '#AA336A', command = view_total)
viewTotal.grid(row = 13, column = 1)
    
root.mainloop()