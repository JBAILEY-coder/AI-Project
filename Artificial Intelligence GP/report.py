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
import alert
from pyswip import Prolog
prolog=Prolog()
prolog.consult("Calculation.pl")

class reportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1170x580+90+170")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)

        title=Label(self.root,text="GPA Report",font=("goudy old style",20,"bold"),bg="orange",fg="white").place(x=0,y=0,width=1180,height=35)

        #===Variables==
        self.var_studentID=StringVar()
        self.var_gpa=StringVar()
        self.var_year=StringVar()
        self.totcreditssemester1=int
        self.totcreditssemester2=int
        self.GPEsemester1=[]
        self.GPEsemester2=[]
        self.totalGPEsemester1=0
        self.totalGPEsemester2=0
        self.semester1gpa=StringVar()
        self.semester2gpa=StringVar()
        self.totalcredits=int
        self.totalGPE=float
        self.overallGPA=StringVar()
        self.defaultGPA=2.2

        #==Labels==
        lbl_StudentID=Label(self.root,text="Student ID",font=("goudy old style",15,"bold"),bg="white").place(x=350,y=60)

         #===footer===
        footer=Label(self.root,text="SMS - Student Management System\nContact Us for any Technical Issues: group@gmail.com",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

        

        #==Result Labels===

      
        lbl_semester1gpa=Label(self.root,text="Semester 1 GPA",font=("goudy old style",15,"bold"),bg="white").place(x=450,y=370)
        lbl_semester2gpa=Label(self.root,text="Semester 2 GPA",font=("goudy old style",15,"bold"),bg="white").place(x=450,y=410)
        lbl_cumulativegpa=Label(self.root,text="Cumulative GPA",font=("goudy old style",15,"bold"),bg="white").place(x=450,y=450)





        self.txt_semester1gpa=Entry(self.root,textvariable=self.semester1gpa,font=("goudy old style",15,"bold"),bg="lightyellow",state='readonly').place(x=600,y=370,width=130)
        self.txt_semester2gpa=Entry(self.root,textvariable=self.semester2gpa,font=("goudy old style",15,"bold"),bg="lightyellow",state='readonly').place(x=600,y=410,width=130)
        self.txt_semester2gpa=Entry(self.root,textvariable=self.overallGPA,font=("goudy old style",15,"bold"),bg="lightyellow",state='readonly').place(x=600,y=450,width=130)
        
        
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",cursor="hand2",fg="white",command=self.year).place(x=670,y=55,width=100)

        
        



        
        #===Student ID====
        self.studentID_list=[]
      
        self.fetch_studentID()
     
        self.txt_ModuleID=ttk.Combobox(self.root,textvariable=self.var_studentID,values=(self.studentID_list),state=('readonly'),font=("goudy old style",15,"bold")).place(x=450,y=60,width=200)
        


        #==Buttons==
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",cursor="hand2",fg="white",command=self.year).place(x=670,y=55,width=100)

    def fetch_studentID(self):
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
          
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    

        scrolly=Scrollbar(self.root,bd=2,orient=VERTICAL)
        self.ReportTable=ttk.Treeview(self.root,columns=("Modules Done","Semester","Credits Achieved","Year Done","Grade Point Average"),xscrollcommand=scrolly.set)
        
        
        self.ReportTable.place(x=390,y=160,width=550,height=200)

        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.ReportTable.yview)

        self.ReportTable.heading("Modules Done",text="Modules Done")
        self.ReportTable.heading("Semester",text="Semester")
        self.ReportTable.heading("Credits Achieved",text="Credits Achieved")
        self.ReportTable.heading("Year Done",text="Year Done")
        self.ReportTable.heading("Grade Point Average",text="Grade Point Average")
        self.ReportTable["show"]='headings'
        self.ReportTable.column("Modules Done",width=150)
        self.ReportTable.column("Semester",width=60)
        self.ReportTable.column("Credits Achieved",width=100)
        self.ReportTable.column("Year Done",width=50)
        self.ReportTable.column("Grade Point Average",width=120)
        
       
        
        
        
    def clear(self):
        self.semester1gpa.set(" ")
        self.semester2gpa.set(" ")
        self.overallGPA.set(" ")

        

    def year(self):
        lbl_year=Label(self.root,text="Year Done",font=("goudy old style",15,"bold"),bg="white").place(x=350,y=110)
        self.txt_year=Entry(self.root,textvariable=self.var_year,font=("goudy old style",15,"bold")).place(x=450,y=110,width=200)
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",cursor="hand2",fg="white",command=self.search).place(x=670,y=100,width=100)

        
        
    def search(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()

        try:
            self.clear()
            mycursor.execute("SELECT moduleid FROM moduledetails WHERE studentid=%s",(self.var_studentID.get(),))
            rows=mycursor.fetchall()
          
            
            
            mycursor.execute("SELECT COUNT(moduleid) FROM moduledetails WHERE studentid=%s",(self.var_studentID.get(),))
            rows=mycursor.fetchone()
            for t in rows:
                print(t)
                
            if t==0:
                messagebox.showerror("Error",f"Student did not pass any modules")     
            else:
                self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    
    def show(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shavar123",
        database="studentmaster")
        mycursor=mydb.cursor()
        self.totalGPE=0
        self.totalGPEsemester1=0
        self.totalGPEsemester2=0
        information=[]
        
        try:
            self.clear()

            mycursor.execute("SELECT modulemaster.module, moduledetails.semester, modulemaster.numberofcredits, moduledetails.year, moduledetails.gradepoints FROM moduledetails INNER JOIN studentmaster ON moduledetails.studentid=studentmaster.studentid INNER JOIN modulemaster ON moduledetails.moduleid=modulemaster.moduleid WHERE moduledetails.studentid=%s AND moduledetails.year=%s",(self.var_studentID.get(),self.var_year.get()))
            rows=mycursor.fetchall()
            self.ReportTable.delete(*self.ReportTable.get_children())
            for x in rows:
                self.ReportTable.insert('',END,values=x)

            if str(rows) != "[]":
                calculations.totcredits(self)
                
                self.GPEsemester1=calculations.calculateGPE(self,"1")
                t=0
                for i in self.GPEsemester1:
                    self.totalGPEsemester1+=self.GPEsemester1[t]
                    t+=1
            
                self.GPEsemester2=calculations.calculateGPE(self,"2")
                t=0
                for i in self.GPEsemester2:
                    self.totalGPEsemester2+=self.GPEsemester2[t]
                    t+=1
            
                self.totalGPE=float(self.totalGPEsemester1)+float(self.totalGPEsemester2)
           

                GPA=calculations.GPA(self)
                mycursor.execute("SELECT studentmaster.studentid, studentmaster.studentname, studentmaster.studentemail, studentmaster.school, studentmaster.programme FROM moduledetails INNER JOIN studentmaster ON moduledetails.studentid=studentmaster.studentid INNER JOIN modulemaster ON moduledetails.moduleid=modulemaster.moduleid WHERE moduledetails.studentid=%s AND moduledetails.year=%s",(self.var_studentID.get(),self.var_year.get()))
                rows=mycursor.fetchone()
                for x in rows:
                    information.append(x)

                if GPA<=self.defaultGPA:
                    alert.send_alert(str(information[0]),str(information[1]),str(information[2]),str(information[3]),str(information[4]),GPA)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    

if __name__=="__main__":
    root=Tk()
    obj=reportClass(root)
    root.mainloop()