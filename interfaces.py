from tkinter import *


class Window():
    def __init__(self,master):
        self.master = master
        
        #LabelFrame

        self.frame1 = LabelFrame(self.master,borderwidth=0, bg='#EBA938', width=650, height=60)
        self.frame1.place(x=0, y=0)


        #Entrada para buscar el video

        self.enlace = Entry(self.frame1, width=50
                            ,borderwidth=0,
                            insertborderwidth=0, highlightcolor ='white',
                            highlightbackground = 'white',
                            fg='#949292', justify='center'
                            )
        self.enlace.place(x=100, y=20)
        self.enlace.insert(0,'http://youtube.com/SAdxad')

        #Boton de Aceptar

        self.aceptar = Button(self.frame1, text='Aceptar',
                                bg='#FF6F61', fg='white',
                                borderwidth=0, highlightbackground = '#EBA938',
                                activeforeground ='#F9402E',
                                pady=1
        
                            )
        self.aceptar.place(x=510, y=19)
     
       
    