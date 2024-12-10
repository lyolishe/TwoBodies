from tkinter import *
from tkinter import ttk
from body import Body, Cords
from constants import frame_rate

root = Tk()

root.title('two bodies')
root.geometry('1920x1280')
root.update()

bodies = list[Body]()

windowCenter = Cords(root.winfo_width() / 2, root.winfo_height() / 2)


def click(event):
    global bodies
    bodies.append(Body(cnvs, 100, Cords(event.x, event.y)))


def updateBodies():
    global bodies, root, mainBdy

    root.after(frame_rate, updateBodies)
    if len(bodies) > 0:
        for body in bodies:
            if body.collidesWith(mainBdy):
                bodies.remove(body)
                cnvs.delete(body.shape)
                continue

            dcords = body.calcMovement(mainBdy)
            cnvs.move(body.shape, dcords.x, dcords.y)


cnvs = Canvas(root, background="white", highlightthickness=0)
cnvs.pack(fill=BOTH, expand=True)

mainBdy = Body(cnvs, 60000, windowCenter, 'yellow')

cnvs.bind('<Button-1>', click)

root.after(frame_rate, updateBodies)

root.mainloop()