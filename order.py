import csv
from datetime import date
from datetime import datetime

class Orders:
  def __init__(self, tblNum, item, price, quantity, tax):
    self.tblNum = tblNum
    self.item = item
    self.price = price
    self.quantity = quantity
    self.tax = tax
    
  
  def grandTotal(self):
    subTotal = float(self.quantity * self.price)
    withTax = float(subTotal +(subTotal * self.tax))
    return withTax
  
  def storeOrderToCsv(self):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    subTotal = float(self.quantity * self.price)
    data_to_enter = []
    data_to_enter.append(self.tblNum)
    data_to_enter.append(self.item)
    data_to_enter.append(self.price)
    data_to_enter.append(self.quantity)
    data_to_enter.append(self.tax)
    data_to_enter.append(subTotal)
    data_to_enter.append(float(self.grandTotal()))
    data_to_enter.append(str(date.today()))
    data_to_enter.append(current_time)

    #data_entry = list(self.tblNum, self.item, self.price,self.quantity, self.tax, subTotal, float(self.grandTotal()), str(date.today()))
    
    with open('order_data.csv','a') as fd:
      write = csv.writer(fd)   
      write.writerow(data_to_enter)
    fd.close()
    print("Done!!")


  

