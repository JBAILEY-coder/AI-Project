'''
Group Members:

-J'Nelle Bailey: 2008135
-Shavar Black: 2002379
-Sassania Hibbert: 1901201
-Leondre Bronfield 2000070
'''


from tkinter import*
from PIL import ImageTk, Image
import os
from module import ModuleClass
from student import StudentClass
from report import reportClass
from moduledetails import ModuleDetailsClass
import mysql.connector
from tkinter import messagebox
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1170x700+0+0")
        self.root.resizable(False,False)
        self.root.config(bg="white")

        title=Label(self.root,text="Student Management System",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

        #===menu====
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1150,height=90)

        btn_module=Button(M_Frame,text="Module Details",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_moduleDetails).place(x=20,y=5,width=200,height=40 )
        btn_student=Button(M_Frame,text="Student Details",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40 )
        btn_module_master=Button(M_Frame,text="Module Master",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_module).place(x=460,y=5,width=200,height=40 )
        btn_report=Button(M_Frame,text="GPA Report",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40 )
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.quit).place(x=900,y=5,width=200,height=40 )


        #===footer===
        footer=Label(self.root,text="SMS - Student Management System\nContact Us for any Technical Issues: group@gmail.com",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

        #==content_window===
        self.bg_img=Image.open("Artificial Intelligence GP/Images/students.png")
        self.bg_img=self.bg_img.resize((920,350))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        #===update_label===
        module_num = int
        student_num=int
        probation_num=int

    

        #==gives records==
        def countmodules():
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shavar123",
            database="studentmaster")
            mycursor=mydb.cursor()
            modulecount=int
            modcount=str
            try:
                mycursor.execute("SELECT COUNT(moduleid) FROM modulemaster")
                rows=mycursor.fetchall()
                for x in rows:
                    modulecount=x
                modcount=str(modulecount)
                return modcount 
            
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
        def countstudents():
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shavar123",
            database="studentmaster")
            mycursor=mydb.cursor()
            modulecount=int
            modcount=str
            try:
                mycursor.execute("SELECT COUNT(studentid) FROM studentmaster")
                rows=mycursor.fetchall()
                for x in rows:
                    modulecount=x
                modcount=str(modulecount)
                return modcount 
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")

        self.lbl_module=Label(self.root,text="Total Modules\n"+countmodules().replace(',',''),font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white").place(x=400,y=530,width=230,height=100)
        self.lbl_students=Label(self.root,text="Total Students\n"+countstudents().replace(',',''),font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white").place(x=640,y=530,width=230,height=100)
        self.lbl_probation=Label(self.root,text="Students on Probation\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white").place(x=880,y=530,width=270,height=100)


    def add_module(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ModuleClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)

    def add_moduleDetails(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ModuleDetailsClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def quit(self):
        root.destroy()
        exit()

 

if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
    