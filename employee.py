from tkinter import*
from tkinter import messagebox
import pymysql
import time
class EmpSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Employee Salary Management System")
        self.root.geometry("1450x900+0+0")
        self.root.config(bg="#fff")
        title=Label(self.root,text="Employee Salary Management System",font=("times new roman",24,"bold"),bg="#262626", fg="white",anchor="w",padx=10)
        title.place(x=0,y=0,relwidth=1)
        
        #frame1----------
        #variables---------------------------------
        self.var_emp_code= StringVar()
        self.var_emp_designation= StringVar()
        self.var_emp_name= StringVar()
        self.var_emp_age= StringVar()
        self.var_emp_gender= StringVar()
        self.var_emp_email= StringVar()
        self.var_emp_loc= StringVar()
        self.var_emp_doj= StringVar()
        self.var_emp_dob= StringVar()
        self.var_emp_exp= StringVar()
        self.var_emp_pid=StringVar()
        self.var_emp_contact=StringVar()
        self.var_emp_sts=StringVar()



        F1 = Frame(self.root,bd=4,relief=RIDGE,bg="#fff")
        F1.place(x=10,y=60,width=730,height=650)
        title1=Label(F1,text="Employee Details",font=("times new roman",20),bg="#262626", fg="white",anchor="w",padx=10)
        title1.place(x=0,y=0,relwidth=1)

        l_code=Label(F1,text="Employee Code:",font=("times new roman",20),bg="#fff", fg="black")
        l_code.place(x=10,y=60)
        t_code=Entry(F1,font=("times new roman",15),textvariable=self.var_emp_code,bg="lightyellow", fg="black")
        t_code.place(x=220,y=67,width=200)
        btn_search=Button(F1,text="Search",command=self.search,font=("times new roman",19),bg="#fff", fg="black")
        btn_search.place(x=430,y=64,height=30) 

        #row1------------
        l_des=Label(F1,text="Designation:",font=("times new roman",20),bg="#fff", fg="black")
        l_des.place(x=10,y=110)
        t_des=Entry(F1,font=("times new roman",15),textvariable=self.var_emp_designation,bg="lightyellow", fg="black")
        t_des.place(x=160,y=118,width=200)
        l_doj=Label(F1,text="D.O.J:",font=("times new roman",20),bg="#fff", fg="black")
        l_doj.place(x=380,y=110)
        t_doj=Entry(F1,font=("times new roman",15),textvariable=self.var_emp_doj,bg="lightyellow", fg="black")
        t_doj.place(x=512,y=118)

        #row2------------
        l_name=Label(F1,text="Name:",font=("times new roman",20),bg="#fff", fg="black")
        l_name.place(x=10,y=160)
        t_name=Entry(F1,font=("times new roman",15),textvariable=self.var_emp_name,bg="lightyellow", fg="black")
        t_name.place(x=160,y=166,width=200)
        l_dob=Label(F1,text="D.O.B:",font=("times new roman",20),bg="#fff", fg="black")
        l_dob.place(x=380,y=160)
        t_dob=Entry(F1,font=("times new roman",15),textvariable=self.var_emp_dob,bg="lightyellow", fg="black")
        t_dob.place(x=512,y=166)

        #row3------------
        l_age=Label(F1,text="Age:",font=("times new roman",20),bg="#fff", fg="black")
        l_age.place(x=10,y=210)
        t_age=Entry(F1,font=("times new roman",15),textvariable=self.var_emp_age,bg="lightyellow", fg="black")
        t_age.place(x=160,y=216,width=200)
        l_exp=Label(F1,text="Experience:",font=("times new roman",19),bg="#fff", fg="black")
        l_exp.place(x=380,y=210)
        t_exp=Entry(F1,font=("times new roman",15),textvariable=self.var_emp_exp,bg="lightyellow", fg="black")
        t_exp.place(x=512,y=216, width=204)

        # #row4------------
        l_gender=Label(F1,text="Gender:",font=("times new roman",20),bg="#fff", fg="black")
        l_gender.place(x=10,y=260)
        t_gender=Entry(F1,font=("times new roman",15),textvariable=self.var_emp_gender,bg="lightyellow", fg="black")
        t_gender.place(x=160,y=266,width=200)
        l_pid=Label(F1,text="Proof ID:",font=("times new roman",19),bg="#fff", fg="black")
        l_pid.place(x=380,y=260)
        t_pid=Entry(F1,font=("times new roman",15),textvariable=self.var_emp_pid,bg="lightyellow", fg="black")
        t_pid.place(x=512,y=266)

        # #row5------------
        l_email=Label(F1,text="Email:",font=("times new roman",20),bg="#fff", fg="black")
        l_email.place(x=10,y=310)
        t_email=Entry(F1,font=("times new roman",15),textvariable=self.var_emp_email,bg="lightyellow", fg="black")
        t_email.place(x=160,y=316,width=200)
        l_phn=Label(F1,text="Contact No:",font=("times new roman",18),bg="#fff", fg="black")
        l_phn.place(x=380,y=310)
        t_phn=Entry(F1,font=("times new roman",15),textvariable=self.var_emp_contact,bg="lightyellow", fg="black")
        t_phn.place(x=512,y=316, width=204)

        #row6------------
        l_loc=Label(F1,text="Hired Location:",font=("times new roman",17),bg="#fff", fg="black")
        l_loc.place(x=10,y=360)
        t_loc=Entry(F1,font=("times new roman",15),textvariable=self.var_emp_loc,bg="lightyellow", fg="black")
        t_loc.place(x=160,y=366,width=200)
        l_sts=Label(F1,text="Status:",font=("times new roman",20),bg="#fff", fg="black")
        l_sts.place(x=380,y=360)
        t_sts=Entry(F1,font=("times new roman",15),textvariable=self.var_emp_sts,bg="lightyellow", fg="black")
        t_sts.place(x=512,y=366, width=204)

        #row7------------
        l_add=Label(F1,text="Address:",font=("times new roman",20),bg="#fff", fg="black")
        l_add.place(x=10,y=410)
        self.t_add=Entry(F1,font=("times new roman",15),bg="lightyellow", fg="black")
        self.t_add.place(x=160,y=416,width=554,height=215)

        #frame2----------
        #variables---------------------------------
        self.var_emp_month= StringVar()
        self.var_emp_year= StringVar()
        self.var_emp_sal= StringVar()
        self.var_emp_t_days= StringVar()
        self.var_emp_absent= StringVar()
        self.var_emp_medical= StringVar()
        self.var_emp_pf= StringVar()
        self.var_emp_convence= StringVar()
        self.var_emp_net_sal= StringVar()

        F2 = Frame(self.root,bd=4,relief=RIDGE,bg="#fff")
        F2.place(x=750,y=60,width=690,height=315)

        title2=Label(F2,text="Employee Salary Details",font=("times new roman",20),bg="#262626", fg="white",anchor="w",padx=10)
        title2.place(x=0,y=0,relwidth=1)

        #row1--------
        l_month=Label(F2,text="Month:",font=("times new roman",18),bg="#fff", fg="black")
        l_month.place(x=30,y=50)
        t_month=Entry(F2,font=("times new roman",15),textvariable=self.var_emp_month,bg="lightyellow", fg="black")
        t_month.place(x=120,y=55,width=100)
        
        l_year=Label(F2,text="Year:",font=("times new roman",18),bg="#fff", fg="black")
        l_year.place(x=230,y=50)
        t_year=Entry(F2,font=("times new roman",15),textvariable=self.var_emp_year,bg="lightyellow", fg="black")
        t_year.place(x=290,y=55,width=100)

        l_salary=Label(F2,text="B. Salary:",font=("times new roman",18),bg="#fff", fg="black")
        l_salary.place(x=400,y=50)
        t_salary=Entry(F2,font=("times new roman",15),textvariable=self.var_emp_sal,bg="lightyellow", fg="black")
        t_salary.place(x=505,y=55,width=140)

        #row2--------
        l_days=Label(F2,text="Total Days:",font=("times new roman",18),bg="#fff", fg="black")
        l_days.place(x=30,y=100)
        t_days=Entry(F2,font=("times new roman",15),textvariable=self.var_emp_t_days,bg="lightyellow", fg="black")
        t_days.place(x=150,y=105,width=150)
        
        l_absents=Label(F2,text="Total Absents:",font=("times new roman",18),bg="#fff", fg="black")
        l_absents.place(x=310,y=100)
        t_absents=Entry(F2,font=("times new roman",15),textvariable=self.var_emp_absent,bg="lightyellow", fg="black")
        t_absents.place(x=480,y=105,width=166)

        #row3--------
        l_medical=Label(F2,text="Medical:",font=("times new roman",18),bg="#fff", fg="black")
        l_medical.place(x=30,y=150)
        t_medical=Entry(F2,font=("times new roman",15),textvariable=self.var_emp_medical,bg="lightyellow", fg="black")
        t_medical.place(x=150,y=155,width=150)
        
        l_pf=Label(F2,text="Provident Funds:",font=("times new roman",18),bg="#fff", fg="black")
        l_pf.place(x=310,y=150)
        t_pf=Entry(F2,font=("times new roman",15),textvariable=self.var_emp_pf,bg="lightyellow", fg="black")
        t_pf.place(x=480,y=155,width=164)

        #row4--------
        l_convence=Label(F2,text="Convence:",font=("times new roman",18),bg="#fff", fg="black")
        l_convence.place(x=30,y=200)
        t_convence=Entry(F2,font=("times new roman",15),textvariable=self.var_emp_convence,bg="lightyellow", fg="black")
        t_convence.place(x=150,y=205,width=150)
        
        l_nSalary=Label(F2,text="Net Salary:",font=("times new roman",18),bg="#fff", fg="black")
        l_nSalary.place(x=310,y=200)
        t_nSalary=Entry(F2,font=("times new roman",15),textvariable=self.var_emp_net_sal,bg="lightyellow", fg="black")
        t_nSalary.place(x=480,y=205,width=164)


        #buttons-----
        btn_calc=Button(F2,text="Calculate",font=("times new roman",19),command=self.calculate,bg="#fff", fg="black")
        btn_calc.place(x=100,y=240,height=30,width=140)

        btn_save=Button(F2,text="Save",font=("times new roman",19),command=self.add,bg="#fff", fg="black")
        btn_save.place(x=250,y=240,height=30,width=140)

        btn_clr=Button(F2,text="Clear",font=("times new roman",19),command=self.clear,bg="#fff", fg="black")
        btn_clr.place(x=400,y=240,height=30,width=140)

        btn_update=Button(F2,text="Update",font=("times new roman",19),command=self.update,bg="#fff", fg="black")
        btn_update.place(x=126,y=275,height=30,width=190)

        btn_delete=Button(F2,text="Delete",font=("times new roman",19),command=self.delete,bg="#fff", fg="black")
        btn_delete.place(x=330,y=275,height=30,width=185)

        #frame3----------
        F3 = Frame(self.root,bd=4,relief=RIDGE,bg="#fff")
        F3.place(x=750,y=383,width=690,height=326)

        #Calculator Frame-----
        self.var_text=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_text.set(self.var_operator)

        def result():
            res=str(eval(self.var_operator))
            self.var_text.set(res)
            self.var_operator='' 

        def clear_calc():
            self.var_text.set('')
            self.var_operator=''

        Calc_Frame = Frame(F3,bg="white",bd=2,relief=RIDGE)
        Calc_Frame.place(x=2,y=2,width=250,height=313)

        t_result=Entry(Calc_Frame,font=("times new roman",18),bg="lightyellow",textvariable=self.var_text, fg="black",justify=RIGHT)
        t_result.place(x=1,y=2,relwidth=1,height=50)

        #row1----------
        btn_7 = Button(Calc_Frame,text="7",command=lambda:btn_click(7),font=("times new roman",15,"bold"))
        btn_7.place(x=1,y=55,width=60,height=60)

        btn_8 = Button(Calc_Frame,text="8",command=lambda:btn_click(8),font=("times new roman",15,"bold"))
        btn_8.place(x=62,y=55,width=60,height=60)

        btn_9 = Button(Calc_Frame,text="9",command=lambda:btn_click(9),font=("times new roman",15,"bold"))
        btn_9.place(x=123,y=55,width=60,height=60)

        btn_div_calc = Button(Calc_Frame,text="/",command=lambda:btn_click('/'),font=("times new roman",15,"bold"))
        btn_div_calc.place(x=183,y=55,width=60,height=60)

        #row2----------
        btn_4 = Button(Calc_Frame,text="4",command=lambda:btn_click(4),font=("times new roman",15,"bold"))
        btn_4.place(x=1,y=118,width=60,height=60)

        btn_5 = Button(Calc_Frame,text="5",command=lambda:btn_click(5),font=("times new roman",15,"bold"))
        btn_5.place(x=62,y=118,width=60,height=60)

        btn_6 = Button(Calc_Frame,text="6",command=lambda:btn_click(6),font=("times new roman",15,"bold"))
        btn_6.place(x=123,y=118,width=60,height=60)

        btn_mul_calc = Button(Calc_Frame,text="*",command=lambda:btn_click('*'),font=("times new roman",15,"bold"))
        btn_mul_calc.place(x=183,y=118,width=60,height=60)

        #row3----------
        btn_1 = Button(Calc_Frame,text="1",command=lambda:btn_click(1),font=("times new roman",15,"bold"))
        btn_1.place(x=1,y=181,width=60,height=60)

        btn_2 = Button(Calc_Frame,text="2",command=lambda:btn_click(2),font=("times new roman",15,"bold"))
        btn_2.place(x=62,y=181,width=60,height=60)

        btn_3 = Button(Calc_Frame,text="3",command=lambda:btn_click(3),font=("times new roman",15,"bold"))
        btn_3.place(x=123,y=181,width=60,height=60)

        btn_sub_calc = Button(Calc_Frame,text="-",command=lambda:btn_click('-'),font=("times new roman",15,"bold"))
        btn_sub_calc.place(x=183,y=181,width=60,height=60)

        #row4----------
        btn_0 = Button(Calc_Frame,text="0",command=lambda:btn_click(0),font=("times new roman",15,"bold"))
        btn_0.place(x=1,y=244,width=60,height=60)

        btn_clr = Button(Calc_Frame,text="C",command=clear_calc,font=("times new roman",15,"bold"))
        btn_clr.place(x=62,y=244,width=60,height=60)

        btn_add_calc = Button(Calc_Frame,text="+",command=lambda:btn_click('+'),font=("times new roman",15,"bold"))
        btn_add_calc.place(x=123,y=244,width=60,height=60)

        btn_total = Button(Calc_Frame,text="=",command=result,font=("times new roman",15,"bold"))
        btn_total.place(x=183,y=244,width=60,height=60)

        #salary frame-------
        Sal_Frame = Frame(F3,bg="white",bd=2,relief=RIDGE)
        Sal_Frame.place(x=255,y=2,width=424,height=313)

        title_sal=Label(Sal_Frame,text="Salary Receipt",font=("times new roman",20),bg="#262626", fg="white",anchor="w",padx=10)
        title_sal.place(x=0,y=0,relwidth=1)

        Sal_Frame2 = Frame(Sal_Frame,bg='white',bd=2,relief=RIDGE)
        Sal_Frame2.place(x=0,y=34,relwidth=1,height=273)
        self.sample=f'''\tCompany Name, XYZ\n\tAddress: XYZ, Floor4
-----------------------------------------------------------------
  Employee ID\t\t:   
  Salary of\t\t:   Mon-YYYY
  Generated on\t\t:   DD-MM-YYYY
-----------------------------------------------------------------
  Total Days\t\t:   DD
  Total Present\t\t:   DD
  Total Absent\t\t:   DD
  Convence\t\t:   Rs.----
  Medical\t\t:   Rs.----
  PF\t\t:   Rs.----
  Gross Payment\t\t:   Rs.-------
  Net Salary\t\t:   Rs.-------
-----------------------------------------------------------------
  This is computer generated slip, not
  required any signature
  '''

        scroll_y = Scrollbar(Sal_Frame2, orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_sal_rect = Text(Sal_Frame2,font=("times new roman",13),bg='lightyellow',yscrollcommand=scroll_y.set)
        self.txt_sal_rect.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_sal_rect.yview)
        self.txt_sal_rect.insert(END,self.sample)

    #-------------------all functions starts here-------------------------
    def search(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
            row=cur.fetchone()
            
            if row==None:
                messagebox.showerror('Error','Wrong Employee ID!!!',parent=self.root)
            else:
                self.var_emp_code.set(row[0])
                self.var_emp_designation.set(row[1])
                self.var_emp_name.set(row[2])
                self.var_emp_age.set(row[3])
                self.var_emp_gender.set(row[4])
                self.var_emp_email.set(row[5])
                self.var_emp_loc.set(row[6])
                self.var_emp_doj.set(row[7])
                self.var_emp_dob.set(row[8])
                self.var_emp_exp.set(row[9])
                self.var_emp_pid.set(row[10])        
                self.var_emp_contact.set(row[11])        
                self.var_emp_sts.set(row[12])
                self.t_add.delete(END)
                self.t_add.insert(END,row[13])

                self.var_emp_month.set(row[14])
                self.var_emp_year.set(row[15])
                self.var_emp_sal.set(row[16])
                self.var_emp_t_days.set(row[17])
                self.var_emp_absent.set(row[18])
                self.var_emp_medical.set(row[19])
                self.var_emp_pf.set(row[20])
                self.var_emp_convence.set(row[21])
                self.var_emp_net_sal.set(row[22])

                file_1=open('Salary_Receipts/'+str(row[23]),'r')
                self.txt_sal_rect.delete('1.0',END)
                for i in file_1:
                    self.txt_sal_rect.insert(END,i)
                file_1.close()
                    
        except Exception as ex:
            messagebox.showerror('Error',f'error due to: {str(ex)}')
    
    def clear(self):
        self.var_emp_code.set('')
        self.var_emp_designation.set('')
        self.var_emp_name.set('')
        self.var_emp_age.set('')
        self.var_emp_gender.set('')
        self.var_emp_email.set('')
        self.var_emp_loc.set('')
        self.var_emp_doj.set('')
        self.var_emp_dob.set('')
        self.var_emp_exp.set('')
        self.var_emp_pid.set('')     
        self.var_emp_contact.set('')       
        self.var_emp_sts.set('')
        self.t_add.delete(END)

        self.var_emp_month.set('')
        self.var_emp_year.set('')
        self.var_emp_sal.set('')
        self.var_emp_t_days.set('')
        self.var_emp_absent.set('')
        self.var_emp_medical.set('')
        self.var_emp_pf.set('')
        self.var_emp_convence.set('')
        self.var_emp_net_sal.set('')
        self.txt_sal_rect.delete('1.0',END)
        self.txt_sal_rect.insert(END,self.sample)

    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror('Error','Employee ID requiered!!')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                
                if row==None:
                    messagebox.showerror('Error','Wrong Employee ID!!!',parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                        cur.execute("delete from emp_salary where e_id=%s",(self.var_emp_code.get()))
                        con.commit()
                        con.close() 
                        messagebox.showinfo("Delete","Employee Data has been Successfully Deleted!!",parent=self.root)
                        self.clear()   
            except Exception as ex:
                messagebox.showerror('Error',f'error due to: {str(ex)}')

    def update(self):
        if self.var_emp_code.get()=='' or self.var_emp_net_sal.get()=='' or self.var_emp_name.get()=='':
            messagebox.showerror("Error","Employee Details are required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                
                if row==None:
                    messagebox.showerror('Error','This Employee ID is Invalid!!',parent=self.root)
                else:
                    cur.execute("UPDATE `emp_salary` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hr_location`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`proof_id`=%s,`contact_no`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basic_salary`=%s,`total_days`=%s,`absent_days`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_salary`=%s,`salary_receipt`=%s WHERE `e_id`=%s",
                    (
                        self.var_emp_designation.get(),
                        self.var_emp_name.get(),
                        self.var_emp_age.get(),
                        self.var_emp_gender.get(),
                        self.var_emp_email.get(),
                        self.var_emp_loc.get(),
                        self.var_emp_doj.get(),
                        self.var_emp_dob.get(),
                        self.var_emp_exp.get(),
                        self.var_emp_pid.get(),        
                        self.var_emp_contact.get(),        
                        self.var_emp_sts.get(),
                        self.t_add.get(),

                        self.var_emp_month.get(),
                        self.var_emp_year.get(),
                        self.var_emp_sal.get(),
                        self.var_emp_t_days.get(),
                        self.var_emp_absent.get(),
                        self.var_emp_medical.get(),
                        self.var_emp_pf.get(),
                        self.var_emp_convence.get(),
                        self.var_emp_net_sal.get(),
                        self.var_emp_code.get()+".txt",
                        self.var_emp_code.get()
                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('Salary_Receipts/'+str(self.var_emp_code.get())+".txt",'w')
                    file_.write(self.txt_sal_rect.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("Success","Record Updated Successfully!!")

            except Exception as ex:
                messagebox.showerror('Error',f'error due to: {str(ex)}')
    
    def add(self):
        if self.var_emp_code.get()=='' or self.var_emp_net_sal.get()=='' or self.var_emp_name.get()=='':
            messagebox.showerror("Error","Employee Details are required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                
                if row!=None:
                    messagebox.showerror('Error','This Employee already exist',parent=self.root)
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_emp_code.get(),
                        self.var_emp_designation.get(),
                        self.var_emp_name.get(),
                        self.var_emp_age.get(),
                        self.var_emp_gender.get(),
                        self.var_emp_email.get(),
                        self.var_emp_loc.get(),
                        self.var_emp_doj.get(),
                        self.var_emp_dob.get(),
                        self.var_emp_exp.get(),
                        self.var_emp_pid.get(),        
                        self.var_emp_contact.get(),        
                        self.var_emp_sts.get(),
                        self.t_add.get(),

                        self.var_emp_month.get(),
                        self.var_emp_year.get(),
                        self.var_emp_sal.get(),
                        self.var_emp_t_days.get(),
                        self.var_emp_absent.get(),
                        self.var_emp_medical.get(),
                        self.var_emp_pf.get(),
                        self.var_emp_convence.get(),
                        self.var_emp_net_sal.get(),
                        self.var_emp_code.get()+".txt"
                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('Salary_Receipts/'+str(self.var_emp_code.get())+".txt",'w')
                    file_.write(self.txt_sal_rect.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("Success","Record Added Successfully!!")

            except Exception as ex:
                messagebox.showerror('Error',f'error due to: {str(ex)}')
            
    def calculate(self):
        if self.var_emp_month==' ' or self.var_emp_year=='':
            messagebox.showerror('Error','All Fields are Required')
        else:
            per_day=int(self.var_emp_sal.get())/int(self.var_emp_t_days.get())
            work_day=int(self.var_emp_t_days.get())-int(self.var_emp_absent.get())
            sal_=per_day*work_day
            deduct=int(self.var_emp_medical.get())+int(self.var_emp_pf.get())
            addition=int(self.var_emp_convence.get())
            net_sal=sal_-deduct+addition
            self.var_emp_net_sal.set(str(round(net_sal,2)))
            new_sample=f'''\tCompany Name, XYZ\n\tAddress: XYZ, Floor4
-----------------------------------------------------------------
  Employee ID\t\t:   {self.var_emp_code.get()}
  Salary of\t\t:   {self.var_emp_month.get()}-{self.var_emp_year.get()}
  Generated on\t\t:   {str(time.strftime("%d-%m-%Y"))}
-----------------------------------------------------------------
  Total Days\t\t:   {self.var_emp_t_days.get()}
  Total Present\t\t:   {str(int(self.var_emp_t_days.get())-int(self.var_emp_absent.get()))}
  Total Absent\t\t:   {self.var_emp_absent.get()}
  Convence\t\t:   Rs.{self.var_emp_convence.get()}
  Medical\t\t:   Rs.{self.var_emp_medical.get()}
  PF\t\t:   Rs.{self.var_emp_pf.get()}
  Gross Payment\t\t:   Rs.{self.var_emp_sal.get()}
  Net Salary\t\t:   Rs.{self.var_emp_net_sal.get()}
-----------------------------------------------------------------
  This is computer generated slip, not
  required any signature
  '''
            self.txt_sal_rect.delete('1.0',END)
            self.txt_sal_rect.insert(END,new_sample)


root=Tk()
obj1 = EmpSystem(root)
root.mainloop()