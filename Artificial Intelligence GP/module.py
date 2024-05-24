'''
Group Members:

-J'Nelle Bailey: 2008135
-Shavar Black: 2002379
-Sassania Hibbert: 1901201
-Leondre Bronfield 2000070
'''
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
import os
from tkinter import ttk
import mysql.connector
import database


class ModuleClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1170x480+90+170")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)

        title=Label(self.root,text="Module Master",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,width=1180,height=35)

        #===Variables===
        self.var_moduleID=StringVar()
        self.var_moduleName=StringVar()
        self.var_moduleCredits=StringVar()
        #===Widgets===
        lbl_ModuleID=Label(self.root,text="Module ID",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_ModuleName=Label(self.root,text="Module Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_ModuleCredits=Label(self.root,text="Number of Credits",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)

        self.txt_ModuleID=Entry(self.root,textvariable=self.var_moduleID,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=60,width=200)
        self.txt_ModuleName=Entry(self.root,textvariable=self.var_moduleName,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=100,width=200)
        self.txt_ModuleCredits=Entry(self.root,textvariable=self.var_moduleCredits,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=140,width=200)

        #===Buttons===
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add).place(x=200,y=300,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update).place(x=320,y=300,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete).place(x=440,y=300,width=110,height=40)
        


#===Content===
        #self.C_Frame=Frame(self.root,relief=RIDGE).place(x=620,y=50,width=470,height=340)
        self.ModuleTable=ttk.Treeview(self.root,columns=("Module ID","Module Name","Module Credits"))

        
        self.ModuleTable.place(x=620,y=50,width=470,height=340)
        self.ModuleTable.heading("Module ID",text="Module ID")
        self.ModuleTable.heading("Module Name",text="Module Name")
        self.ModuleTable.heading("Module Credits",text="Module Credits")
        self.ModuleTable["show"]='headings'
        self.ModuleTable.column("Module ID",width=50)
        self.ModuleTable.column("Module Name",width=100)
        self.ModuleTable.column("Module Credits",width=100)
        self.ModuleTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        


#Things to do
#Connect database
#Get input from text boxes and add to database when saved button is clicked
#Display info in the ModuleTable

        
        








        #===footer===
        footer=Label(self.root,text="SMS - Student Management System\nContact Us for any Technical Issues: group@gmail.com",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
#Puts the selected data in the text boxes
    def get_data(self,ev):
        r=self.ModuleTable.focus()
        content=self.ModuleTable.item(r)
        row=content["values"] 
        #print(row)
        self.var_moduleID.set(row[0])
        self.var_moduleName.set(row[1])
        self.var_moduleCredits.set(row[2])

    
    def add(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()
        try:
            if self.var_moduleID.get()=="":
                messagebox.showerror("Error",f"Module ID required")
            if self.var_moduleName.get()=="":
                messagebox.showerror("Error",f"Module Name required")
            if self.var_moduleCredits.get()=="":
                messagebox.showerror("Error",f"Module Credits required")
            else:
                mycursor.execute("INSERT INTO modulemaster(moduleid, module, numberofcredits) VALUES (%s,%s,%s)",(self.var_moduleID.get(),self.var_moduleName.get(),self.var_moduleCredits.get()))
                mydb.commit()
                messagebox.showinfo("Succes",f"Module was successfully added",parent=self.root)
                self.clear()
        
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        


    def clear(self):
        self.show()
        self.var_moduleID.set("")
        self.var_moduleName.set("")
        self.var_moduleCredits.set("")
        

    def delete(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()
        try:
            if self.var_moduleID.get()=="":
                messagebox.showerror("Error",f"Module ID required")
            else:
                option=messagebox.askyesno("Confirm",f"Do you really want to delete?",parent=self.root)
                if option == True:
                    mycursor.execute("DELETE FROM modulemaster WHERE moduleid=%s",(self.var_moduleID.get(),))
                    mydb.commit()
                    messagebox.showinfo("Succes",f"Module was successfully deleted",parent=self.root)
                    self.clear()
                else:
                    messagebox.showinfo("",f"Module was not deleted",parent=self.root)
                    self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due tp {str(ex)}")


    def show(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()
        try:
            mycursor.execute("SELECT * FROM modulemaster")
            rows=mycursor.fetchall()
            self.ModuleTable.delete(*self.ModuleTable.get_children())
            for x in rows:
                self.ModuleTable.insert('',END,values=x)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due tp {str(ex)}")


    def update(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()
        try:
            if self.var_moduleID.get()=="":
                messagebox.showerror("Error",f"Module ID required")
            else:
                SQL=("UPDATE modulemaster SET module=%s, numberofcredits=%s WHERE moduleid=%s")
                update=(self.var_moduleName.get(),self.var_moduleCredits.get(),self.var_moduleID.get())   
                mycursor.execute(SQL,update)   
                mydb.commit()
                messagebox.showinfo("Success",f"Module was successfully updated",parent=self.root)
                self.clear()
        


        except Exception as ex:
            messagebox.showerror("Error",f"Error due tp {str(ex)}")



if __name__=="__main__":
    root=Tk()
    obj=ModuleClass(root)
    root.mainloop()