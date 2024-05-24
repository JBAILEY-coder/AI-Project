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

class StudentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1170x480+90+170")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)

        title=Label(self.root,text="Student Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,width=1180,height=35)

        #===Variables===
        self.var_studentID=StringVar()
        self.var_studentname=StringVar()
        self.var_studentEmail=StringVar()
        self.var_school=StringVar()
        self.var_program=StringVar()
        #===Widgets===
        lbl_StudentID=Label(self.root,text="Student ID",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_StudentName=Label(self.root,text="Student Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_StudentEmail=Label(self.root,text="Student Email",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_School=Label(self.root,text="School",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
        lbl_Program=Label(self.root,text="Programme",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        
        

        self.txt_StudentID=Entry(self.root,textvariable=self.var_studentID,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=60,width=200)
        self.txt_StudentName=Entry(self.root,textvariable=self.var_studentname,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=100,width=200)
        self.txt_StudentEmail=Entry(self.root,textvariable=self.var_studentEmail,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=140,width=200)
        self.txt_School=Entry(self.root,textvariable=self.var_school,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=180,width=200)
        self.txt_Program=Entry(self.root,textvariable=self.var_program,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=220,width=200)
        #===Buttons===
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add).place(x=200,y=300,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update).place(x=320,y=300,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete).place(x=440,y=300,width=110,height=40)
        


#===Content===
        
        scrollx=Scrollbar(self.root,bd=2,orient=HORIZONTAL)
        self.StudentTable=ttk.Treeview(self.root,columns=("Student ID","Student Name","Student Email","School","Programme"),xscrollcommand=scrollx.set)
        
        
        self.StudentTable.place(x=620,y=50,width=470,height=340)

        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.config(command=self.StudentTable.xview)

        self.StudentTable.heading("Student ID",text="Student ID")
        self.StudentTable.heading("Student Name",text="Student Name")
        self.StudentTable.heading("Student Email",text="Student Email")
        self.StudentTable.heading("School",text="School")
        self.StudentTable.heading("Programme",text="Programme")
        self.StudentTable["show"]='headings'
        self.StudentTable.column("Student ID",width=70)
        self.StudentTable.column("Student Name",width=100)
        self.StudentTable.column("Student Email",width=100)
        self.StudentTable.column("School",width=100)
        self.StudentTable.column("Programme",width=100)
        self.StudentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        



        #===footer===
        footer=Label(self.root,text="SMS - Student Management System\nContact Us for any Technical Issues: group@gmail.com",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
#Puts the selected data in the text boxes
    def get_data(self,ev):
        r=self.StudentTable.focus()
        content=self.StudentTable.item(r)
        row=content["values"] 
        #print(row)
        self.var_studentID.set(row[0])
        self.var_studentname.set(row[1])
        self.var_studentEmail.set(row[2])
        self.var_school.set(row[3])
        self.var_program.set(row[4])

    def add(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()
        try:
            if self.var_studentID.get()=="":
                messagebox.showerror("Error",f"Student ID required")
            if self.var_studentname.get()=="":
                messagebox.showerror("Error",f"Student Name required")
            if self.var_studentEmail.get()=="":
                messagebox.showerror("Error",f"Student Email required")
            if self.var_school.get()=="":
                messagebox.showerror("Error",f"School required")
            if self.var_program.get()=="":
                messagebox.showerror("Error",f"Program required")
            else:
                mycursor.execute("INSERT INTO studentmaster(studentid,studentname,studentemail,school,programme) VALUES (%s,%s,%s,%s,%s)",(self.var_studentID.get(),self.var_studentname.get(),self.var_studentEmail.get(),self.var_school.get(),self.var_program.get()))
                mydb.commit()
                messagebox.showinfo("Succes",f"Student was successfully added",parent=self.root)
                self.clear()
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due tp {str(ex)}")


    def clear(self):
        self.show()
        self.var_studentID.set("")
        self.var_studentname.set("")
        self.var_studentEmail.set("")
        self.var_school.set("")
        self.var_program.set("")
        

    def delete(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()
        try:
            if self.var_studentID.get()=="":
                messagebox.showerror("Error",f"Student ID required")
            else:
                option=messagebox.askyesno("Confirm",f"Do you really want to delete?",parent=self.root)
                if option == True:
                    mycursor.execute("DELETE FROM studentmaster WHERE studentid=%s",(self.var_studentID.get(),))
                    mydb.commit()
                    messagebox.showinfo("Succes",f"Student was successfully deleted",parent=self.root)
                    self.clear()
                else:
                    messagebox.showinfo("",f"Student was not deleted",parent=self.root)
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
            mycursor.execute("SELECT * FROM studentmaster")
            rows=mycursor.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for x in rows:
                self.StudentTable.insert('',END,values=x)


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
            if self.var_studentID.get()=="":
                messagebox.showerror("Error",f"Student ID required")
            else:
                SQL=("UPDATE studentmaster SET studentname=%s, studentemail=%s, school=%s, programme=%s WHERE studentid=%s")
                update=(self.var_studentname.get(),self.var_studentEmail.get(),self.var_school.get(),self.var_program.get(),self.var_studentID.get())   
                mycursor.execute(SQL,update)   
                mydb.commit()
                messagebox.showinfo("Success",f"Student was successfully updated",parent=self.root)
                self.clear()
        


        except Exception as ex:
            messagebox.showerror("Error",f"Error due tp {str(ex)}")



if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()
