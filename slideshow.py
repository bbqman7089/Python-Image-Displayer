from PIL import Image
import tkinter as tk
import time, os, random
wait = 0
os.system('pkill Preview')
interval = 5
cwd = os.getcwd()
window = tk.Tk()
window.title('Image Presenter')
info = tk.Label(text='This program will take all the jpg and png files in its folder which is currently ' +cwd+ ' and will display them.\nIt also assumes that your default image viewer is Preview.')
info.pack()
adv_info = tk.Label(text="\nThe time you enter and the time the pictures are displayed for may differ.\nThis is because the computer will take some time to open the image by itself,\n but Python won't care and keeps going as if the image opened instantly.")
question = tk.Label(text='How long between photos (in seconds) (default is 5): ')
img_list = [x for x in os.listdir() if x.endswith(".png") or x.endswith('.jpg')]
img_list = sorted(img_list, key=str.lower)
pos = 0
image = ''
for f in range(len(img_list)):
    file = img_list[pos]
    image = image + file + '\n'
    pos = pos+1
img_list = str(img_list)
info_present = tk.Label(text='The files that will be displayed are '+image+ '')
info_present.pack()
def get_time():
    global interval
    wait = entry.get()
    interval = wait
    interval = float(interval)
button = tk.Button(text="Press to set a new time",command=get_time)
text_entry = tk.Entry(width = 5)
question.pack()
text_entry.pack()
button.pack()
def rnd_img():
    global interval
    pos = 0
    dir_list = [x for x in os.listdir() if x.endswith(".png") or x.endswith('.jpg')]
    if len(dir_list) > 0:
        for i in range(len(dir_list)):
            file = dir_list[pos]
            img = Image.open(file)
            img.show()
            print(file)
            pos = pos + 1
            time.sleep(interval)
            os.system('pkill Preview')
start_button = tk.Button(text='Start', width=10, command=rnd_img)
start_button.pack()
adv_info.pack()
window.mainloop()
