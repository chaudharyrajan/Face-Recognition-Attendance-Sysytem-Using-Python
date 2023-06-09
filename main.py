from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import tkinter
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1350x690+0+0")
        self.root.title("Face Recognition System")
                
        #image1
        img=Image.open(r"C:\Users\rajan\OneDrive\Pictures\pho.png")
        img=img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=150)
         #image2
        img2=Image.open(r"C:\Users\rajan\OneDrive\Pictures\pho2.jpg")
        img2=img2.resize((450,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
    
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=450,y=0,width=450,height=150)
        
        #image3
        img3=Image.open(r"C:\Users\rajan\OneDrive\Pictures\pho3.png")
        img3=img3.resize((450,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=900,y=0,width=450,height=150)  
              
        # bg image 4
        img4=Image.open(r"C:\Users\rajan\OneDrive\Pictures\pho4.jpg")
        img4=img4.resize((1350,690),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=150,width=1350,height=690)
        
        title_lbl=Label(bg_img,text="ATTENDANCE MONITERING SYSTEM USING FACE RECOGNITION",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=50)
        
        #student button
        img5=Image.open(r"C:\Users\rajan\OneDrive\Pictures\student1.png")
        img5=img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=180,height=180)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=250,width=180,height=40)
        
        #detect face button
        img6=Image.open(r"C:\Users\rajan\OneDrive\Pictures\facedetect.png")
        img6=img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=450,y=100,width=180,height=180)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=450,y=250,width=180,height=40)
        
        #Attendence button
        img7=Image.open(r"C:\Users\rajan\OneDrive\Pictures\attendance.jpg")
        img7=img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=100,width=180,height=180)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=700,y=250,width=180,height=40)
        
        #Train Face
        img8=Image.open(r"C:\Users\rajan\OneDrive\Pictures\traindata.jpg")
        img8=img8.resize((180,180),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=950,y=100,width=180,height=180)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=950,y=250,width=180,height=40)
        
        #Photo button
        img9=Image.open(r"C:\Users\rajan\OneDrive\Pictures\photo1.jpeg")
        img9=img9.resize((180,180),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=450,y=330,width=180,height=180)
        
        b1_1=Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=450,y=480,width=180,height=40)
        
        #Exit button
        img10=Image.open(r"C:\Users\rajan\OneDrive\Pictures\exit.jpg")
        img10=img10.resize((180,180),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.iExit)
        b1.place(x=700,y=330,width=180,height=180)
        
        b1_1=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=700,y=480,width=180,height=40)
                
    def open_img(self):
        os.startfile("data")
        
        #=======function buttons=========

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
                
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)   
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recongnition", "Are you sure to Exit",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
                  
if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()