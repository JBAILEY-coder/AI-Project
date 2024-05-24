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

class ModuleDetailsClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1170x580+90+170")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)

        title=Label(self.root,text="Module Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,width=1180,height=35)

        #===Variables===
        self.var_moduleID=StringVar()
        self.var_module=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_studentID=StringVar()
        self.var_letterGrade=StringVar()
        self.var_gradepoints=StringVar()
        self.var_results=StringVar()


         #===footer===
        footer=Label(self.root,text="SMS - Student Management System\nContact Us for any Technical Issues: group@gmail.com",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)


        #===Widgets===
        lbl_ModuleID=Label(self.root,text="Module ID",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_Module=Label(self.root,text="Module",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_Year=Label(self.root,text="Year",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_Semester=Label(self.root,text="Semester",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
        lbl_StudentID=Label(self.root,text="Student ID",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        lbl_LetterGrade=Label(self.root,text="Letter Grade",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=270)
        lbl_GradePoints=Label(self.root,text="Grade Points",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=320)
        lbl_Results=Label(self.root,text="Result Status",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=370)
        
        
        
        self.studentID_list=[]
        self.moduleID_list=[]
        self.letter_grade=[]
        #function call to update the list
        self.fetch_student()
        self.fetch_moduleID()
        self.fetch_lettergrade()

        self.txt_ModuleID=ttk.Combobox(self.root,textvariable=self.var_moduleID,values=(self.moduleID_list),state=('readonly'),font=("goudy old style",15,"bold")).place(x=200,y=60,width=200)
        self.txt_Module=Entry(self.root,textvariable=self.var_module,font=("goudy old style",15,"bold"),bg="lightyellow",state=('disabled')).place(x=200,y=100,width=200)
        self.txt_Year=Entry(self.root,textvariable=self.var_year,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=140,width=200)
        self.txt_Semester=Entry(self.root,textvariable=self.var_semester,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=200,y=180,width=200)
        self.txt_StudentID=ttk.Combobox(self.root,textvariable=self.var_studentID,values=(self.studentID_list),state=('readonly'),font=("goudy old style",15,"bold")).place(x=200,y=220,width=200)
        self.txt_letterGrade=ttk.Combobox(self.root,textvariable=self.var_letterGrade,values=(self.letter_grade),state=('readonly'),font=("goudy old style",15,"bold")).place(x=200,y=270,width=200)
        self.txt_GradePoints=Entry(self.root,textvariable=self.var_gradepoints,font=("goudy old style",15,"bold"),bg="lightyellow",state='disabled').place(x=200,y=320,width=200)
        self.txt_Results=Entry(self.root,textvariable=self.var_results,state=('disabled'),font=("goudy old style",15,"bold")).place(x=200,y=370,width=200)
        #===Buttons===
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add).place(x=200,y=420,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update).place(x=320,y=420,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete).place(x=440,y=420,width=110,height=40)
        


#===Content===
        #self.C_Frame=Frame(self.root,relief=RIDGE).place(x=620,y=50,width=470,height=340)
        scrollx=Scrollbar(self.root,bd=2,orient=HORIZONTAL)
        self.ModuleDetailsTable=ttk.Treeview(self.root,columns=("Module ID","Module","Year","Semester","Student ID","Letter Grade","Grade Point","Result Status"),xscrollcommand=scrollx.set)
        
        
        self.ModuleDetailsTable.place(x=620,y=50,width=470,height=340)

        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.config(command=self.ModuleDetailsTable.xview)

        self.ModuleDetailsTable.heading("Module ID",text="Module ID")
        self.ModuleDetailsTable.heading("Module",text="Module")
        self.ModuleDetailsTable.heading("Year",text="Year")
        self.ModuleDetailsTable.heading("Semester",text="Semester")
        self.ModuleDetailsTable.heading("Student ID",text="Student ID")
        self.ModuleDetailsTable.heading("Letter Grade",text="Letter Grade")
        self.ModuleDetailsTable.heading("Grade Point",text="Grade Point")
        self.ModuleDetailsTable.heading("Result Status",text="Result Status")
        self.ModuleDetailsTable["show"]='headings'
        self.ModuleDetailsTable.column("Module ID",width=70)
        self.ModuleDetailsTable.column("Module",width=100)
        self.ModuleDetailsTable.column("Year",width=100)
        self.ModuleDetailsTable.column("Semester",width=100)
        self.ModuleDetailsTable.column("Student ID",width=100)
        self.ModuleDetailsTable.column("Letter Grade",width=100)
        self.ModuleDetailsTable.column("Grade Point",width=100)
        self.ModuleDetailsTable.column("Result Status",width=100)
        self.ModuleDetailsTable.bind("<ButtonRelease-1>",self.get_data)
        
        
        #self.get_module()
        self.show()
        



    def fetch_lettergrade(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()
        try:
            mycursor.execute("SELECT letter FROM grademaster")
            rows=mycursor.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.letter_grade.append(row[0])
           

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    

    def get_status(self):
        if self.var_letterGrade.get()!="D+" and self.var_letterGrade.get()!="D" and self.var_letterGrade.get()!="F":
            self.var_results.set("Pass")
        else:
            self.var_results.set("Fail")
    
    def get_lettergrade(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()
        letter = self.var_letterGrade.get()
        mycursor.execute("SELECT value FROM grademaster WHERE letter=%s",(letter,))
        rows=mycursor.fetchall()
        delimiter=""
        v=""
        for x in rows:
            v = "".join(str(x))
        v=v.strip(")")
        v=v.strip(",")
        v=v.replace("(","")
        self.var_gradepoints.set(v)


    def get_module(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()
        ID = self.var_moduleID.get()
        mycursor.execute("SELECT module FROM modulemaster WHERE moduleid=%s",(ID,))
        rows=mycursor.fetchall()
        delimiter=""
        v=""
        for x in rows:
            v = "".join(x)
        self.var_module.set(v)
        '''
        mycursor.execute("SELECT numberofcredits FROM modulemaster WHERE moduleid=%s",(ID,))
        rows=mycursor.fetchall()
        f=""
        for li in rows:
            for j in li:
                f+=str(j)
        self.var_gradepoints.set(f)
        '''

        
        #Puts the selected data in the text boxes
    def get_data(self,ev):
        r=self.ModuleDetailsTable.focus()
        content=self.ModuleDetailsTable.item(r)
        row=content["values"] 
        #print(row)
        self.var_moduleID.set(row[0])
        self.var_module.set(row[1])
        self.var_year.set(row[2])
        self.var_semester.set(row[3])
        self.var_studentID.set(row[4])
        self.var_letterGrade.set(row[5])
        self.var_gradepoints.set(row[6])
        self.var_results.set(row[7])

    def add(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()

        try:
            
            mycursor.execute("SELECT COUNT(studentid) FROM moduledetails WHERE moduleid=%s AND studentid=%s",(self.var_moduleID.get(),self.var_studentID.get()))
            rows=mycursor.fetchone()
            for x in rows:
                print(x)
            if self.var_moduleID.get()=="":
                messagebox.showerror("Error",f"Module does not exist in database")
            if self.var_year.get()=="":
                messagebox.showerror("Error",f"Year required")
            if self.var_semester.get()=="":
                messagebox.showerror("Error",f"Semester required")
            if self.var_studentID.get()=="":
                messagebox.showerror("Error",f"Student ID required")
            else:
                if x==0:
                    self.get_module()
                    self.get_lettergrade()
                    self.get_status()
                    mycursor.execute("INSERT INTO moduledetails(moduleid, module, year, semester, studentid, letter,gradepoints, results) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_moduleID.get(),self.var_module.get(),self.var_year.get(),self.var_semester.get(),self.var_studentID.get(),self.var_letterGrade.get(),self.var_gradepoints.get(),self.var_results.get()))
                    mydb.commit()
                    messagebox.showinfo("Success",f"Module Details was successfully added",parent=self.root)
                    self.clear()
                else:
                    messagebox.showerror("Error",f"Student record with this module already exists")     
        
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def clear(self):
        self.show()
        #self.get_module()
        self.var_moduleID.set("")
        self.var_module.set("")
        self.var_year.set("")
        self.var_semester.set("")
        self.var_studentID.set("")
        self.var_letterGrade.set("")
        self.var_gradepoints.set("")
        self.var_results.set("")
        

    def delete(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()
        try:
            if self.var_moduleID.get() == "":
                messagebox.showerror("Error",f"Module ID required")
            else:
                option=messagebox.askyesno("Confirm",f"Do you really want to delete?",parent=self.root)
                if option == True:
                    mycursor.execute("DELETE FROM moduledetails WHERE studentid=%s AND moduleid=%s",(self.var_studentID.get(),self.var_moduleID.get()))
                    mydb.commit()
                    messagebox.showinfo("Success",f"Module Detail was successfully deleted",parent=self.root)
                    self.clear()
                else:
                    messagebox.showinfo("",f"Module Detail was not deleted",parent=self.root)
                    self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def show(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()
        try:
            mycursor.execute("SELECT * FROM moduledetails")
            rows=mycursor.fetchall()
            self.ModuleDetailsTable.delete(*self.ModuleDetailsTable.get_children())
            for x in rows:
                self.ModuleDetailsTable.insert('',END,values=x)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    
    def fetch_student(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()
        try:
            mycursor.execute("SELECT studentid FROM studentmaster")
            rows=mycursor.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.studentID_list.append(row[0])
            #print(v)\
            #self.module_list=v
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    


    def fetch_moduleID(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()
        try:
            mycursor.execute("SELECT moduleid FROM modulemaster")
            rows=mycursor.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.moduleID_list.append(row[0])
            #print(v)\
            #self.module_list=v
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


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
                self.get_module()
                self.get_lettergrade()
                self.get_status()
                SQL=("UPDATE moduledetails SET module=%s, year=%s, semester=%s, studentid=%s, letter=%s,gradepoints=%s, results=%s WHERE moduleid=%s")
                update=(self.var_module.get(),self.var_year.get(),self.var_semester.get(),self.var_studentID.get(),self.var_letterGrade.get(),self.var_gradepoints.get(),self.var_results.get(),self.var_moduleID.get())   
                mycursor.execute(SQL,update)   
                mydb.commit()
                messagebox.showinfo("Success",f"Module Details was successfully updated",parent=self.root)
                self.clear()
        


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



if __name__=="__main__":
    root=Tk()
    obj=ModuleDetailsClass(root)
    root.mainloop()
