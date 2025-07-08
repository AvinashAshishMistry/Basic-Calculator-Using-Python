from tkinter import*
def show(value):
    
   screen_equation = screen.get()
   clicked_now = value

   if(clicked_now == "DEL"):
      screen_equation = screen_equation[:-1]
      screen.delete(0,END)
      screen.insert(0,screen_equation)
   elif(clicked_now == "AC"):
      screen.delete(0,END)
   elif(clicked_now == "="):
      screen_equation = screen_equation.replace("x","*")
      screen_equation = screen_equation.replace("÷","/")
      per_index = screen_equation.find("%")
      pre_left = per_index-1;
      pre_right = per_index+1;
      if(per_index != -1 and per_index-1 >= 0 and per_index+1 < len(screen_equation)):
         while pre_left > 0:
            if(screen_equation[pre_left-1].isdigit() or screen_equation[pre_left-1] == "."):
               pre_left = pre_left - 1
            else:
               break;
         while pre_right < len(screen_equation)-1:
            if(screen_equation[pre_right+1].isdigit() or screen_equation[pre_right+1] == "."):
               pre_right = pre_right + 1
            else:
               break;
          
         left_num = float(screen_equation[pre_left:per_index])
         right_num = float(screen_equation[per_index+1:pre_right+1])
         per_ans = (left_num/100)*right_num
         screen_equation = screen_equation[:pre_left] + str(per_ans) + screen_equation[pre_right:]
      try:
         evalution = eval(screen_equation)
         screen.delete(0,END)
         screen.insert(0,evalution)
         print(evalution)
      except:
         screen.delete(0,END)
         screen.insert(0,"Syntax Error")

   elif(clicked_now.isdigit() or clicked_now == "."):
      screen.insert(END,clicked_now)

   elif(clicked_now in ["+","-","x","÷","%"]):

      if(screen_equation == "" or screen_equation[-1].isdigit() or screen_equation[-1] == "."):
         screen_equation = screen_equation + clicked_now
         screen.delete(0,END) 
         screen.insert(0,screen_equation)    

      elif(screen_equation[-1] in ["+","-","x","÷","%"] and screen_equation != ""):
         screen_equation = screen_equation[:-1] + clicked_now;
         screen.delete(0,END)
         screen.insert(0,screen_equation)  

root=Tk()
root.title("! ! ! Calculator using Python ! ! !")
root.geometry("500x700")
root.config(bg="black")
# root.maxsize(330,600)
root.minsize(500,600)

Label(root,
      bg="black",fg="red",
      font=("Georgia ",22,"bold"),
      text="! ! ! Calculator Using Python ! ! !",
      padx=8,pady=5,).pack(side=TOP,padx=5,pady=5)

screen=Entry(root,
             textvariable="",
             font="lucida 31 ",
             bg="grey",fg="black",
             borderwidth=4,relief=GROOVE)
screen.pack(side=TOP,padx=3,pady=3)

f1=Frame(root,bg="black")
f1.pack()
delet=Button(f1,text="DEL",
            font="lucida 30 ",
            width= 4, height= 1,
            bg="yellow",fg="red",
            borderwidth=5,relief=GROOVE,
            command= lambda : show("DEL"))
delet.pack(side=LEFT,padx=5,pady=5)

AC=Button(f1,text="AC",
             font="lucida 30 ",
             width= 4, height= 1,
             bg="yellow",fg="red",
             borderwidth=5,relief=GROOVE,
             command= lambda : show("AC"))
AC.pack(side=LEFT,padx=5,pady=5)

division=Button(f1,text="÷",
                font="lucida 30 ",
                width= 4, height= 1,
                bg="yellow",fg="red",
                borderwidth=5,relief=GROOVE,
                command= lambda : show("÷")) 
division.pack(side=LEFT,padx=6,pady=5)

minus=Button(f1,text="-",
             font="lucida 30 ",
             width= 4, height= 1,
             bg="yellow",fg="red",
             borderwidth=5,relief=GROOVE,
             command= lambda : show("-"))
minus.pack(side=LEFT,padx=5,pady=5)


f2=Frame(root,bg="black")
f2.pack()
one=Button(f2,text="1",
           font="lucida 30 ",
           width= 4, height= 1,
           bg="yellow",fg="red",
           borderwidth=5,relief=GROOVE,
           command= lambda : show("1"))
one.pack(side=LEFT,padx=5,pady=5)

two=Button(f2,text="2",
           font="lucida 30 ",
           width= 4, height= 1,
           bg="yellow",fg="red",
           borderwidth=5,relief=GROOVE,
           command= lambda: show("2"))
two.pack(side=LEFT,padx=5,pady=5)

three=Button(f2,text="3",
             font="lucida 30 ",
             width= 4, height= 1,
             bg="yellow",fg="red",
             borderwidth=5,relief=GROOVE,
             command= lambda: show("3"))
three.pack(side=LEFT,padx=5,pady=5)

puls=Button(f2,text="+",
            font="lucida 30 ",
            width= 4, height= 1,
            bg="yellow",fg="red",
            borderwidth=5,relief=GROOVE,
            command= lambda : show("+"))
puls.pack(side=LEFT,padx=5,pady=5)

f3=Frame(root,bg="black")
f3.pack()

four=Button(f3,text="4",
            font="lucida 30 ",
            width= 4, height= 1,
            bg="yellow",fg="red",
            borderwidth=5,relief=GROOVE,
            command= lambda:show("4"))
four.pack(side=LEFT,padx=5,pady=5)

five=Button(f3,text="5",
            font="lucida 30 ",
            width= 4, height= 1,
            bg="yellow",fg="red",
            borderwidth=5,relief=GROOVE,
            command= lambda: show("5"))
five.pack(side=LEFT,padx=5,pady=5)

six=Button(f3,text="6",
           font="lucida 30 ",
           width= 4, height= 1,
           bg="yellow",fg="red",
           borderwidth=5,relief=GROOVE,
           command= lambda: show("6")) 
six.pack(side=LEFT,padx=5,pady=5)

multiply=Button(f3,text="X",
                font="lucida 30 ",
                width= 4, height= 1,
                bg="yellow",fg="red",
                borderwidth=5,relief=GROOVE,
                command= lambda:show("x"))
multiply.pack(side=LEFT,padx=5,pady=5)

f4=Frame(root,bg="black")
f4.pack()

seven=Button(f4,text="7",
             font="lucida 30 ",
             width= 4, height= 1,
             bg="yellow",fg="red",
             borderwidth=5,relief=GROOVE,
             command= lambda : show("7"))
seven.pack(side=LEFT,padx=5,pady=5)

eight=Button(f4,text="8",
             font="lucida 30 ",
             width= 4, height= 1,
             bg="yellow",fg="red",
             borderwidth=5,relief=GROOVE,
             command= lambda : show("8"))
eight.pack(side=LEFT,padx=5,pady=5)

nine=Button(f4,text="9",
            font="lucida 30 ",
            width= 4, height= 1,
            bg="yellow",fg="red",
            borderwidth=5,relief=GROOVE,
            command= lambda : show("9"))
nine.pack(side=LEFT,padx=5,pady=5)

percentage=Button(f4,text="%",
                  font="lucida 30 ",
                  width= 4, height= 1,
                  bg="yellow",fg="red",
                  borderwidth=5,relief=GROOVE,
                  command= lambda: show("%"))
percentage.pack(side=LEFT,padx=5,pady=5)

f5=Frame(root,bg="black")
f5.pack()

zero=Button(f5,text="0",
            font="lucida 30 ",
            width= 4, height= 1,
            bg="yellow",fg="red",
            borderwidth=5,relief=GROOVE,
            command= lambda : show("0"))
zero.pack(side=LEFT,padx=5,pady=5)

double_zero=Button(f5,text="00",
                   font="lucida 30 ",
                   width= 4, height= 1,
                   bg="yellow",fg="red",
                   borderwidth=5,relief=GROOVE,
                   command= lambda: show("00"))
double_zero.pack(side=LEFT,padx=5,pady=5)

dot=Button(f5,text=".",
           font="lucida 30 ",
           width= 4, height= 1,
           bg="yellow",fg="red",
           borderwidth=5,relief=GROOVE,
           command= lambda: show("."))
dot.pack(side=LEFT,padx=5,pady=5)

equal=Button(f5,text="=",
             font="lucida 30 ",
             width= 4, height= 1,
             bg="yellow",fg="red",
             borderwidth=5,relief=GROOVE,
             command= lambda : show ("="))
equal.pack(side=LEFT,padx=5,pady=5)

root.mainloop()