# # # # # !"#$%&\'()*+\,-./:;<=>?@[\\]^_`{|}~
# # # # import pyperclip
# # # #
# # # # past = pyperclip.paste()
# # # # print(past)
# # # # pyperclip.copy('hi this is new🎈🎈🎈')
# # # # print(pyperclip.paste())
# # # # pyperclip.copy(past)
# # # # print(pyperclip.paste())
# # # # # emoji('adsfhdsujhh?.>,🎈🎈🎈')
# # #
# # # import openpyxl
# # #
# # # wb = openpyxl.load_workbook('sample.xlsx')
# # # excel = wb[wb.sheetnames[0]]
# # #
# # # print(excel.cell(2, 2).value)
# #
# #
# # data = None
# # lis = data.split(',')
# # for i in lis:
# #     print(i.strip())
#
#
# #Import the required library
# from tkinter import*
#
# #Create an instance of tkinter frame
# win= Tk()
#
# #Define geometry of the window
# win.geometry("750x250")
#
# #Define a function to close the popup window
# def close_win(top):
#    top.destroy()
#
# #Define a function to open the Popup Dialogue
# def popupwin():
#    #Create a Toplevel window
#    top= Toplevel(win)
#    top.geometry("250x100")
#
#    #Create an Entry Widget in the Toplevel window
#    entry= Entry(top, width= 25)
#    entry.pack()
#
#    #Create a Button Widget in the Toplevel Window
#    button= Button(top, text="Ok", command=lambda:close_win(top))
#    button.pack(pady=5, side= TOP)
# #Create a Label
# label= Label(win, text="Click the Button to Open the Popup Dialogue", font= ('Helvetica 15 bold'))
# label.pack(pady=20)
#
# #Create a Button
# button= Button(win, text= "Click Me!", command= popupwin, font= ('Helvetica 14 bold'))
# button.pack(pady=20)
# win.mainloop()

#
#
# with open('setting.txt','w', encoding="utf-8") as file:
#    file.write('hi|h')
#
#
# with open('setting.txt','r') as file:
#    print(tuple(file.read().strip('|').split('|')))
#
# with open("setting", "a", encoding='utf-8') as file:
#    file.write("Date: %s\nTime: %s\nPhone number: %s\nMessage:")

# def setting_add(name):
#    with open('setting.txt', 'a', encoding="utf-8") as file:
#       file.write(str(name) + '|')
#
#
# def setting_remove(name):
#    with open('setting.txt', 'r') as file:
#       new_setting = (file.read().strip('|').split('|'))
#    new_setting.remove(name)
#    with open('setting.txt', 'w', encoding="utf-8") as file:
#       file.write('')
#    for set in new_setting:
#       setting_add(set)
#

from tkinter import messagebox


messagebox.showinfo("Information","Informative message")
# messagebox.showerror("Error", "Error message")
# messagebox.showwarning("Warning","Warning message")

