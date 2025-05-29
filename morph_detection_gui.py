import cv2
import tkinter as tk
from tkinter import filedialog, Label, Button, Frame
from PIL import Image, ImageTk
import numpy as np

def detect_morph(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return "Error: Could not load image"

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    edges_mean = np.mean(edges)
    return edges_mean

def browse_image():
    path = filedialog.askopenfilename()
    if path:
        result = detect_morph(path)
        result_label.config(text=f"Edge Mean: {result}")

root = tk.Tk()
root.title("Morphed Image Detection")

frame = Frame(root)
frame.pack(pady=20)

browse_btn = Button(frame, text="Browse Image", command=browse_image)
browse_btn.pack()

result_label = Label(root, text="Result will appear here")
result_label.pack(pady=10)

root.mainloop()
