from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os

class Face_Recogination_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # first image3
        img = Image.open(r"C:/Users/bajaj/Desktop/face_recogination system/college_images/Stanford.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second image
        img1 = Image.open(r"C:/Users/bajaj/Desktop/face_recogination system/college_images/facialrecognition.png")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(r"C:/Users/bajaj/Desktop/face_recogination system/college_images/u.jpg")
        img2 = img2.resize((1000, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=550, height=130)
        
        
        #bg image
        img3 = Image.open(r"C:/Users/bajaj/Desktop/face_recogination system/college_images/wp2551980.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img= Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        
        # student button
        img4 = Image.open(r"college_images\gettyimages-1022573162.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4) 
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")

        b1_1.place(x=200,y=300,width=220,height=40)
        
       
        #  Detect face
        img5 = Image.open(r"college_images\face_detector1.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5) 
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        
         #  Attendence face
        img6 = Image.open(r"college_images\BestFacialRecognition.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6) 
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        
         #  Help face btton
        img7 = Image.open(r"college_images\help-desk.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7) 
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Help desk",cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        
        # Train face btton
        img8 = Image.open(r"college_images\Train.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8) 
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train data ",cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        
        # photos face btton
        img9 = Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9) 
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos ",cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)
         
        
        
         # developer face btton
        img10 = Image.open(r"college_images\Team-Management-Software-Development.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10) 
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Developer ",cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)
        
          # exit face btton
        img11 = Image.open(r"college_images\exit.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11) 
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="exit ",cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)
        
    def open_img(self):
      os.startfile("data")
         
        
        
     #=====================Function bddutton==========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recogination_System(root)
    root.mainloop()
