from tkinter import*
root=Tk()
root.title("addition")
root.geometry("400x200")
label_series=Label(root,text="fibonacci series")
label_flower=Label(root)
label_spirel=Label(root)


def fibonacci():
    num=10
    frist_num=0
    second=1
    sum=0
    counter=1
    while(counter<=num):
        label_series["text"]+=str(sum)+" "
        counter=counter+1
        frist_num=second
        second=sum
        sum=frist_num+second
        label_flower['text']="flower is fully bloomed"
        label_spirel['text']="spirel in right direaction  "+str(second)+"\& totalare"+str(sum)

btn=Button(root,text="show",command=fibonacci)
btn.pack()
label_flower.pack()
label_series.pack()
label_spirel.pack()
root.mainloop()