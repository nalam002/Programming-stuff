from tkinter import Tk, Label, Button
from tkinter.filedialog import askopenfilename, askopenfilenames
import re
import pandas as pd

def opencsv():
    filez = askopenfilenames(parent=root,title='Choose a file',filetypes=(("csv files", "*.csv"),("All files","*.*")))
    filesnames = root.tk.splitlist(filez)
    mylabel2 = Label(root, text = "Following files have been opened, you can find the newly generated files in the same folder.").pack()
    for filename in filesnames:
        df = pd.read_csv(filename)
        col_list = ["ID","Start time","Completion time","Email","Name","Total points","Quiz feedback","Grade posted time","ID2",\
        "Points - ID2","Feedback - ID2","Name2","Points - Name","Feedback - Name"]

        for col in col_list:
            df.drop(col, axis = 1, inplace = True)

        df = df[df.columns.drop(list(df.filter(regex='Points|Feedback|remainder')))]
        dfn=df.transpose()
        new_filename = re.sub('\.csv', '_edited.csv', filename)
        dfn.to_csv(new_filename, encoding ='utf-8-sig', index = True)



root = Tk()
root.title("Quiz formatter for MS Forms")

message = "This is a tiny program to open .csv quiz response files downloaded from microsoft forms\n \
and create a new csv file with only the questions."
mylabel = Label(root, text = message).pack()
mybutton =Button(root, text ="Choose csv files to convert.", command=opencsv).pack()

root.mainloop()