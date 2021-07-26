import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, height=108, width=192)
canvas.pack()

frame = tk.Frame(root, bg='#555555')
frame.place(relwidth=1, relheight=1)

testLabel = tk.Label(frame, text='hello world!')
button = tk.Button(frame, text='test', bg='gray', fg='red')

entry = tk.Entry(frame, bg='orange', text='test')
entry.pack()

testLabel.pack()
button.pack()
root.mainloop()