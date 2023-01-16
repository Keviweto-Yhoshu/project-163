from tkinter import *
root = Tk()
root.title("Heart_disease_Report")
root.geometry("400x00")

question1_radioButton=StringVar(value="0")

Question1=Label(root, text ="Do you have Chest pain, tightness,and discomfort?")
Question1.pack()
question1_r1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes")
question1_r1.pack()
question1_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no")
question1_r2.pack()


question2_radioButton=StringVar(value="0")
Question2=Label(root, text ="Do you have shortness of Breath?")
Question2.pack()
question2_r1=Radiobutton(root, text = "yes", variable=question2_radioButton, value="yes")
question2_r1.pack()
question2_r2=Radiobutton(root, text = "no", variable=question2_radioButton, value="no")
question2_r2.pack()


question3_radioButton=StringVar(value="0")
Question3=Label(root, text ="Are there any symptoms of numbness,weakness in arms or legs?")
Question3.pack()
question3_r1=Radiobutton(root, text = "yes", variable=question3_radioButton, value="yes")
question3_r1.pack()
question3_r2=Radiobutton(root, text = "no", variable=question3_radioButton, value="no")
question3_r2.pack()


question4_radioButton=StringVar(value="0")
Question4=Label(root, text ="Do you have pain in neck,jaw,throat,or back?")
Question4.pack()
question4_r1=Radiobutton(root, text = "yes", variable=question4_radioButton, value="yes")
question4_r1.pack()
question4_r2=Radiobutton(root, text = "no", variable=question4_radioButton, value="no")
question4_r2.pack()


question5_radioButton=StringVar(value="0")
Question5=Label(root, text ="Do you sometimes, have an irregular  heartbeats that feel rapid?")
Question5.pack()
question5_r1=Radiobutton(root, text = "yes", variable=question5_radioButton, value="yes")
question5_r1.pack()
question5_r2=Radiobutton(root, text = "no", variable=question5_radioButton, value="no")
question5_r2.pack()


question6_radioButton=StringVar(value="0")
Question6=Label(root, text ="Are there any symptoms of dizziness or lightheadedness?")
Question6.pack()
question6_r1=Radiobutton(root, text = "yes", variable=question6_radioButton, value="yes")
question6_r1.pack()
question6_r2=Radiobutton(root, text = "no", variable=question6_radioButton, value="no")
question6_r2.pack()



def fever_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question3_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question4_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question5_radioButton.get()=="yes":
        score = score+20
        print(score) 
    if question6_radioButton.get()=="yes":
        score = score+20
        print(score)  
        
    if score <= 40:
        messagebox.showinfo("Report","You don't need to visit a doctor.")
    elif  score > 40 and score <= 80: 
        messagebox.showinfo("Report","You might perhaps have to visit a doctor")
    else :
        messagebox.showinfo("Report","I strongly advise you to visit a doctor")
        

        
btn = Button(root, text= "click me", command= fever_score)
btn.pack()
root.mainloop()

