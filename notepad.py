from tkinter import *
from tkinter.ttk import Combobox
from tkinter import font, colorchooser, filedialog, messagebox
win = Tk()


class text_editor:
    def __init__(self,win):
        self.url = ''
        self.win = win
        self.current_file = "no"
        self.current_font_family = 'Arial'
        self.current_font_size = 12
        self.current_font_weight = 'normal'
        self.current_font_slant = 'roman'
        self.current_font_underline = 0
        # create icon images path
        self.new_icon = PhotoImage(file="icons2/new.png")
        self.open_icon = PhotoImage(file="icons2/open.png")
        self.save_icon = PhotoImage(file="icons2/save.png")
        self.save_as_icon = PhotoImage(file="icons2/save_as.png")
        self.exit_icon = PhotoImage(file="icons2/exit.png")
        self.copy_icon = PhotoImage(file="icons2/copy.png")
        self.cut_icon = PhotoImage(file="icons2/cut.png")
        self.paste_icon = PhotoImage(file="icons2/paste.png")
        self.clear_all_icon = PhotoImage(file="icons2/clear_all.png")
        self.find_icon = PhotoImage(file='icons2/find.png')
        self.tool_bar_icon = PhotoImage(file='icons2/tool_bar.png')
        self.status_bar_icon = PhotoImage(file='icons2/status_bar.png')
        self.light_default_icon = PhotoImage(file='icons2/light_default.png')
        self.light_plus_icon = PhotoImage(file='icons2/light_plus.png')
        self.dark_icon = PhotoImage(file='icons2/dark.png')
        self.red_icon = PhotoImage(file='icons2/red.png')
        self.monokai_icon = PhotoImage(file='icons2/monokai.png')
        self.night_blue_icon = PhotoImage(file='icons2/night_blue.png')
        self.bold_icon = PhotoImage(file='icons2/bold.png')
        self.italic_icon = PhotoImage(file='icons2/italic.png')
        self.underline_icon = PhotoImage(file='icons2/underline.png')
        self.font_color_icon = PhotoImage(file='icons2/font_color.png')
        self.align_left_icon = PhotoImage(file='icons2/align_left.png')
        self.align_center_icon = PhotoImage(file='icons2/align_center.png')
        self.align_right_icon = PhotoImage(file='icons2/align_right.png')
        

        #create toolbar
        self.tool_bar = Label(win)
        self.tool_bar.pack(side=TOP,fill=X)

        		# font box
        self.font_tuple = font.families()
        self.font_family = StringVar()
        self.font_box = Combobox(self.tool_bar,width=30,textvariable=self.font_family,state='readonly')
        self.font_box['values'] = self.font_tuple
        self.font_box.current(self.font_tuple.index('Arial'))
        self.font_box.grid(row=0,column=0,padx=5)
        self.font_box.bind('<<ComboboxSelected>>',self.change_family)

        # font size 
        self.size_var = IntVar()
        self.font_size = Combobox(self.tool_bar,width=30,textvariable=self.size_var,state='readonly')
        self.font_size['values']=tuple(range(8,80))
        self.font_size.current(4)
        self.font_size.grid(row=0,column=1,padx=5)
        self.font_size.bind('<<ComboboxSelected>>',self.change_size)

        self.bold_btn = Button(self.tool_bar,image=self.bold_icon)
        self.bold_btn.grid(row=0,column=2,padx=5)
        self.bold_btn.bind('<Button-1>',self.bold_file)

        

        self.italic_btn = Button(self.tool_bar,image=self.italic_icon)
        self.italic_btn.grid(row=0,column=3,padx=5)
        self.italic_btn.bind('<Button-1>',self.italic_file)

        self.underline_btn = Button(self.tool_bar,image=self.underline_icon)
        self.underline_btn.grid(row=0,column=4,padx=5)
        self.underline_btn.bind('<Button-1>',self.underline_file)

        self.font_color_btn = Button(self.tool_bar,image=self.font_color_icon)
        self.font_color_btn.grid(row=0,column=5,padx=5)
        self.font_color_btn.bind('<Button-1>',self.font_color_file)

        

        # create text box and scroll bar
        win.title("Npad")
        win.geometry('1000x1000') 
        self.text_area = Text(win,undo=True)
        self.text_area.configure(wrap='word', relief=FLAT)
        self.text_area.pack(fill="both",expand=1)
        self.text_area.focus_set()
        self.scroll = Scrollbar(self.text_area)
        self.scroll.pack(side=RIGHT,fill=Y)
        self.scroll.configure(command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=self.scroll.set,font=(self.current_font_family,self.current_font_size))
        
        
        
        #create menu
        self.main_menu = Menu(win)
        self.win.config(menu=self.main_menu)
        
        #create file menu bar
        self.file = Menu(self.main_menu,tearoff=False)
        self.file.add_command(label="New",image=self.new_icon,compound=LEFT,accelerator="Ctrl+N",command=self.new_file)
        self.win.bind('<Control-n>',self.new_file)
        
        self.file.add_command(label="Open",image=self.open_icon,compound=LEFT,accelerator="Ctrl+O",command=self.open_file)
        self.win.bind('<Control-o>',self.open_file)

        self.file.add_command(label="Save",image=self.save_icon,compound=LEFT,accelerator="Ctrl+S",command=self.save_file)
        self.win.bind('<Control-s>',self.save_file)

        self.file.add_command(label="Save",image=self.save_as_icon,compound=LEFT,accelerator="Ctrl+Alt+S",command=self.save_as_file)
        self.win.bind('<Control-Alt-s>',self.save_as_file)
        
        self.file.add_command(label="Exit",image=self.exit_icon,compound=LEFT,accelerator="Ctrl+Q",command=win.quit)
        self.win.bind('<Control-q>',quit)

        self.main_menu.add_cascade(label="File",menu=self.file)
        
        #create edit menu bar
        self.edit = Menu(self.main_menu,tearoff=False)
        self.edit.add_command(label="Undo",compound=LEFT,accelerator="Ctrl+Z",command=self.text_area.edit_undo)
        self.win.bind('<Control-z>',self.text_area.edit_undo)

        self.edit.add_command(label="Redo",compound=LEFT,accelerator="Ctrl+Y",command=self.text_area.edit_redo)
        self.win.bind('<Control-y>',self.text_area.edit_redo)

        self.edit.add_command(label="Cut",image=self.cut_icon,compound=LEFT,accelerator="Ctrl+X",command=self.cut_file)
        self.win.bind('<Control-x>',self.cut_file)

        self.edit.add_command(label="Copy",image=self.copy_icon,compound=LEFT,accelerator="Ctrl+C",command=self.copy_file)
        self.win.bind('<Control-c>',self.copy_file)

        self.edit.add_command(label="Paste",image=self.paste_icon,compound=LEFT,accelerator="Ctrl+V",command=self.paste_file)
        self.win.bind('<Control-v>',self.paste_file)

        self.edit.add_command(label="Clear ALL",image=self.clear_all_icon,compound=LEFT,accelerator="Ctrl+Atl+X",command=self.clear_file)
        self.win.bind('<Control-Alt-x>',self.clear_file)

        self.edit.add_command(label="Find",image=self.find_icon,command=LEFT,accelerator="Ctrl+F")

        self.main_menu.add_cascade(label="Edit",menu=self.edit)
        
        #create color theme 
        self.color_theme = Menu(self.main_menu,tearoff=False)
        self.theme_choice = StringVar()
        self.color_icons = (self.light_default_icon,self.light_plus_icon,self.dark_icon,self.red_icon,self.monokai_icon,self.night_blue_icon)
        self.color_dict = {
            'Light Default ' : ('#000000', '#ffffff'),
            'Light Plus' : ('#474747', '#e0e0e0'),
            'Dark' : ('#c4c4c4', '#2d2d2d'),
            'Red' : ('#2d2d2d', '#ffe8e8'),
            'Monokai' : ('#d3b774', '#474747'),
            'Night Blue' :('#ededed', '#6b9dc2')
        }
        # display color theme
        self.count = 0
        for i in self.color_dict:
            self.color_theme.add_radiobutton(label = i,image=self.color_icons[self.count],variable=self.theme_choice,compound=LEFT,command=self.change_theme)
            self.count+=1
        
        self.main_menu.add_cascade(label="Color Theme",menu=self.color_theme)

         

    def new_file(self,event=None):
        self.url = ''
        self.text_area.delete(1.0,END)    

    def open_file(self,event=None):
        self.url = filedialog.askopenfile(mode="r",filetype=(('text file','*.txt'),('All file','*.*')))
        if self.url is not None:
            self.result = self.url.read()
            self.text_area.delete(1.0,END)
            self.text_area.insert(INSERT,self.result)
            self.current_file = self.url.name
    
    def save_as_file(self,event=None):
        f = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        if f is None:
            return
        else:
            data = self.text_area.get(1.0,END)
            self.current_file = f.name
            f.write(data)
            f.close()
                
    def save_file(self,event=None):
        if self.current_file =="no":
            self.save_as_file()
        else:
            f = open(self.current_file,"w")
            f.write(self.text_area.get(1.0,END))
            f.close() 

    def copy_file(self,event=None):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def cut_file(self,event=None):
        self.copy_file()
        self.text_area.delete("sel.first","sel.last")
    
    def paste_file(self,event=None):
        self.paste = self.text_area.clipboard_get()   
        self.text_area.insert(INSERT,self.paste)

    def clear_file(self,event=None):
        self.text_area.delete(1.0,END)

    def change_family(self,event=None):
        self.current_font_family = self.font_box.get()
        self.text_area.configure(font=(self.current_font_family,self.current_font_size))
        
    def change_size(self,event=None):
        self.current_font_size = self.font_size.get()
        self.text_area.configure(font=(self.current_font_family,self.current_font_size))
    
    def bold_file(self,event=None):
        
        if self.current_font_weight =='normal':
            self.text_area.configure(font=(self.current_font_family,self.current_font_size,'bold'))
            self.current_font_weight='bold'
        else:
            self.text_area.configure(font=(self.current_font_family,self.current_font_size,'normal'))
            self.current_font_weight='normal'
    
    def italic_file(self,event=None):
        if self.current_font_slant == 'roman':
            self.text_area.configure(font=(self.current_font_family,self.current_font_size,'italic'))
            self.current_font_slant='italic'
        else:
            self.text_area.configure(font=(self.current_font_family,self.current_font_size,'roman'))
            self.current_font_slant='roman'    
    
    def underline_file(self,event=None):
        if self.current_font_underline==0:
            self.text_area.configure(font=(self.current_font_family,self.current_font_size,'underline'))
            self.current_font_underline=1
        else:
            self.text_area.configure(font=(self.current_font_family,self.current_font_size,'normal'))
            self.current_font_underline=0    

    def font_color_file(self,event=None):
        clr = colorchooser.askcolor()
        self.text_area.configure(fg=clr[1])

    def change_theme(self,event=None):
        choose = self.theme_choice.get()
        color_tuple = self.color_dict.get(choose)
        fg_color,bg_color = color_tuple[0],color_tuple[1]
        self.text_area.configure(fg=fg_color,bg=bg_color)


text = text_editor(win)


win.mainloop()