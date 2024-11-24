#Johan Godhino

import pandas as pd 
import tkinter as tk
from tkinter import messagebox
try:
    df = pd.read_csv("records.csv")
except Exception as e :
    pass
data = {
          "Date":[],
          "Description":[],
          "Amount":[],
          "Type":[]}
       
df = pd.DataFrame(data)

class Budgettrackerapp:
    def __init__(self,root) :
        self.root= root
        self.root.title("Budget Tracker")
        
        #Labels 
        self.label_date= tk.Label(root, text="Date(DD-MM-YYYY)")
        self.label_date.grid(row=0, column=0)
        self.entry_date = tk.Entry(root)
        self.entry_date.grid(row=0,column=1)
        
        self.label_desc= tk.Label(root, text="Description")
        self.label_desc.grid(row=1, column=0)
        self.entry_desc = tk.Entry(root)
        self.entry_desc.grid(row=1,column=1)
        
        self.label_Amount= tk.Label(root, text="Amount")
        self.label_Amount.grid(row=2, column=0)
        self.entry_Amount = tk.Entry(root)
        self.entry_Amount.grid(row=2,column=1)
        
        self.label_type= tk.Label(root, text="Type")
        self.label_type.grid(row=3, column=0)
        self.entry_type = tk.Entry(root)
        self.entry_type.grid(row=3,column=1)
        
        #buttons
        self.btn_add = tk.Button(root, text="Add Entry", command= self.add_entry)
        self.btn_add.grid(row=4, column=1,columnspan=2)
        
        self.btn_view = tk.Button(root, text="View Entries", command=self.view_entry)
        self.btn_view.grid(row=5, column=1,columnspan=2)
        
    def add_entry(self):
        date = self.entry_date.get()
        description= self.entry_desc.get()
        amount = self.entry_Amount.get()
        type= self.entry_type.get()
        print(date, description, amount, type)
        
        if date and description and amount and type:
            new_entry = pd.DataFrame({
                "Date":[date],
                "Description":[description],
                "Amount":[amount],
                "Type":[type]
            })
            global df 
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_csv("records.csv")
            messagebox.showinfo("Success!", "Entry saved succesfully!")
            self.entry_date.delete(0,tk.END)
            self.entry_desc.delete(0,tk.END)
            self.entry_Amount.delete(0,tk.END)
            self.entry_type.delete(0,tk.END)
        else:
            messagebox.showerror("Error","All fields are required!")
         
    def view_entry(self):
        global df 
        self.top = tk.Toplevel(self.root)
        self.top.title("View Entries")
        text= tk.Text(self.top)
        text.pack()
        
        for index, row in df.iterrows():
          text.insert(tk.END, "Date: " + row['Date'] + 
                   " Description: " + row['Description'] + 
                   " Amount: " + str(row['Amount']) + 
                   " Type: " + row['Type'])
          edit_btn = tk.Button(self.top, text="Edit", command= lambda i = index:self.edit_entry(i) )
          delete_btn=tk.Button(self.top, text="Delete", command=lambda i = index:self.delete_entry(i))
          text.insert(tk.END,"\n")
          text.window_create(tk.END, window= edit_btn)
          text.insert(tk.END, " ")
          text.window_create(tk.END, window= delete_btn)
          text.insert(tk.END,"\n\n")
    
    def edit_entry(self,index):
        global df 
        self.top_edit = tk.Toplevel(self.root)
        self.top_edit.title("Edit Entry")
        
        self.edit_date= tk.Entry(self.top_edit)
        self.edit_date.insert(0, df.at[index, 'Date'])
        self.edit_date.pack()
        
        self.edit_desc= tk.Entry(self.top_edit)
        self.edit_desc.insert(0, df.at[index, 'Description'])
        self.edit_desc.pack()
        
        self.edit_amount= tk.Entry(self.top_edit)
        self.edit_amount.insert(0, df.at[index, 'Amount'])
        self.edit_amount.pack()
        
        self.edit_type= tk.Entry(self.top_edit)
        self.edit_type.insert(0, df.at[index, 'Type'])
        self.edit_type.pack()
        save_btn = tk.Button(self.top_edit, text = "Save", command=lambda i=index: self.save_edit(i))
        
    def save_edit(self,index):
        global df
        df.at[index,'Date']= self.edit_date.get()
        df.at[index,'Description']= self.edit_desc.get()
        df.at[index,'Amount']= self.edit_amount.get()
        df.at[index,'type']= self.edit_type.get()
        df.to_csv('records.csv', index=False)
        messagebox.showinfo('Saved',"Entry updated succesfully!")
        self.top_edit.destroy()
        self.top.destroy()
        self.view_entries()

    def delete_entry(self,index):
        global df 
        df.drop(index, inplace = True)
        df.reset_index(drop=True, inplace = True)
        df.to_csv('records.csv', index= False)
        messagebox.showinfo("Success!", "Entry deleted")
        self.top.destroy()
        self.view_entries()
    
          
        
root = tk.Tk()
app = Budgettrackerapp(root)
root.mainloop()