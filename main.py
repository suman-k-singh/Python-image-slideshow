import tkinter as tk
import time
from PIL import Image, ImageTk

#Main Application window
root= tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("900x900")

# List of Image paths
image_paths= [
    r"C:\Users\suman\OneDrive\Desktop\Album\img1.jpg",
    r"C:\Users\suman\OneDrive\Desktop\Album\img2.jpg",
    r"C:\Users\suman\OneDrive\Desktop\Album\img3.jpg",
    r"C:\Users\suman\OneDrive\Desktop\Album\img4.jpg",
    r"C:\Users\suman\OneDrive\Desktop\Album\img5.jpg",
    r"C:\Users\suman\OneDrive\Desktop\Album\img6.jpg",
]

image_size= (700, 700)
images= []
for path in image_paths:
    img= Image.open(path)
    img= img.resize(image_size)
    images.append(img)

final_images= []
for img in images:
    photo= ImageTk.PhotoImage(img)
    final_images.append(photo)

image_label= tk.Label(root)
image_label.pack(pady=30)  

def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image= photo
        root.update()
        time.sleep(2)

#BUTTON
play_button= tk.Button(
    root,
    text= "Play the slideshow",
    font=("Arial", 17),
    command=start_slideshow
)  

play_button.pack(pady=40)

root.mainloop()