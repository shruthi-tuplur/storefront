from tkinter import *
from tkinter import filedialog
from turtle import clear, position
from tkinter import font 


#setting up the window of the overall widget
root = Tk()
root.configure(background = 'pink', width = 1000, height = 1000)
root.geometry("500x800")

#initializing variables to find sum of items as they are added into the cart
total = 0
book_count = 0
bag_count = 0
cat_count = 0


#importing background images for item buttons
cat_image = PhotoImage(file = r"/Users/shruthituplur/cat.png")
cat_image_resized = cat_image.subsample(10, 10)

bag_pic = PhotoImage(file = "/Users/shruthituplur/bag.png")
bag_pic_resized = bag_pic.subsample(17, 18)

book_pic = PhotoImage(file = "/Users/shruthituplur/book.png")
book_pic_resized = book_pic.subsample(16, 16)

 
#creating item buttons and placing them in the widget    
book = Button(root, text = 'book', fg = 'black', image = book_pic_resized, command = lambda: click('book'))
book.grid(row = 5, column = 0)

bag = Button(root, text = 'bag', fg = 'black', image = bag_pic_resized, command = lambda: click('bag'))
bag.grid(row = 5, column = 1)

cat = Button(root, text = 'kitty', image = cat_image_resized, fg = 'black', command = lambda: click('kitty'))
cat.grid(row = 5, column = 2)



        
        
  
#creating spacers for aesthetic adjustments
space = Label(root, text = '', fg = 'pink', background = 'pink' )
space.grid(row = 8, column = 1)
space2 = Label(root, text = '', fg = 'pink', background = 'pink' )
space2.grid(row = 10, column = 1)
space3 = Label(root, text = '', fg = 'pink', background = 'pink' )
space3.grid(row = 13, column = 1)
space4 = Label(root, text = '', fg = 'pink', background = 'pink' )
space4.grid(row = 16, column = 1)
space5 =  Label(root, text = '', fg = 'pink', background = 'pink' )
space5.grid(row = 1, column = 1)


#setting up and placing labels
view_cart_label = Label(root, text = 'shopping cart', fg = 'white', background = '#AA336A')
view_cart_label.grid(row = 9, column = 1)


book_label = Label(root, text = 'book - $100', background = '#AA336A', fg = 'white', width = 10)
book_label.grid(row = 6, column = 0)

bag_label = Label(root, text = 'bag - $200', background = '#AA336A', fg = 'white', width = 10)
bag_label.grid(row = 6, column = 1)

cat_label = Label(root, text = 'kitty - $400', background = '#AA336A', fg = 'white', width = 10)
cat_label.grid(row = 6, column = 2)

storeName = Label(root, text = "shruthi's store", background = '#AA336A', fg = 'white', width = 10, padx = 100)
storeName.grid(row = 0, column = 1)

#creating text boxes so user can view their shopping cart and their order total
shoppingCart = Text(root, background = 'white', fg = 'black', width = 20)
shoppingCart.grid(row = 11, column = 1)

orderTotal = Text(root, background = 'white', fg = 'black', height = 10, width = 40)
orderTotal.grid(row = 16, column = 1) 

#setting up command, button, and placement for button that allows user to see their total          
def view_total(): 
    global item_count
    global total
    orderTotal.delete('1.00', END)
    item_count  = book_count + bag_count + cat_count

    purchaseStringBook = '\nAmount of books in cart: %i ' % book_count
    
    purchaseStringBag = '\nAmount of bags in cart: %i ' % bag_count
    
    purchaseStringCat = '\nAmount of cats in cart: %i ' % cat_count   
    totalString = '\n\nYour total is: $%i' % total  
    
    orderTotal.insert('1.00', totalString)
    orderTotal.insert('1.00', purchaseStringBook)  
    orderTotal.insert('1.00', purchaseStringBag)   
    orderTotal.insert('1.00', purchaseStringCat) 
        
         
 
viewTotalLabel = Label(root, text = 'cart total', fg = 'pink', background = '#AA336A')
viewTotalLabel.grid(row = 15, column = 1)
    
#setting up delete button so user can delete the last item placed in their cart

def delete_item():
    global total
    global item_count
    global book_count
    global bag_count
    global cat_count
    last_item = shoppingCart.get('end-2l', "end-1l")
    if len(last_item) == 5:
        total -= 100
        book_count = book_count - 1
    if len(last_item) == 4:
        total -= 200
        bag_count -= 1 
    if len(last_item) == 6:
        total -= 400
        cat_count -= 1
    shoppingCart.delete("end-2l", "end-1l") 
    view_total()
             
           
   
    
delete_button = Button(root, text = 'delete last item', fg = '#AA336A', command = delete_item)
delete_button.grid(row = 12, column = 1)    

#setting up command and button so user can clear their cart
def cart_cleared():
    global total
    global item_count
    global book_count
    global bag_count
    global cat_count
    book_count = 0
    bag_count = 0
    cat_count = 0
    shoppingCart.delete('1.00', END)
    orderTotal.delete('1.00', END)
    item_count = []
    total = 0
    view_total()
 
clearButton = Button(root, text = 'clear cart', fg = '#AA336A', command = cart_cleared)
clearButton.grid(row = 17, column = 1)

#command for item buttons
def click(item):
    global shoppingCart
    global total
    global book_count
    global bag_count
    global cat_count
    if item == 'book':
        total += 100
        book_count += 1 
        shoppingCart.insert(END, item + '\n')
    
    elif item == 'bag': 
        total += 200
        bag_count += 1
        shoppingCart.insert(END, item + '\n')  
        
    elif item == 'kitty': 
        total += 400
        cat_count += 1
        shoppingCart.insert(END, item + '\n')  
    view_total()    


root.mainloop()