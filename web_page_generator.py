import tkinter
from tkinter import *
import webbrowser



class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")
        
        
        self.lbl_custom = Label(self.master,text="Enter custom text or click the Default HTML page button")
        self.lbl_custom.grid(row=0,column=1,columnspan=2,padx=(20,5),pady=(10,10),sticky=N + W)
        
        self.txt_custom = Entry(self.master,text='')
        self.txt_custom.grid(row=1, column=1,columnspan=3,padx=(30,15),pady=(0,10),sticky=N+E+S+W)
        
        self.custom_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.custom_btn.grid(row=2, column=3, padx=(10,10), pady=(10,10))
        
        self.default_btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.default_btn.grid(row=2, column=2,padx=(10,10), pady=(10,10))
    
    
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        
    def customHTML(self):
        htmlText = self.txt_custom.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        
    
        
        
        
        
if __name__ == "__main__":
    root = tkinter.Tk()
    App = ParentWindow(root)
    root.mainloop()