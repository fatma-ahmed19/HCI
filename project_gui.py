import os
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import joblib  # For loading the trained model


class PhotoViewerApp:
    def __init__(self, master, image_folder):
        self.master = master
        self.master.title("Photo Viewer")

        # Create a frame to contain the photo and buttons
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Prevent the frame from resizing based on its contents
        self.frame.pack_propagate(False)

        # Load photos from the specified folder
        self.image_folder = image_folder
        self.photo_paths = sorted(
            [os.path.join(self.image_folder, filename) for filename in os.listdir(self.image_folder) if
             filename.endswith(('.jpg', '.png'))])
        self.current_index = 0

        # Display initial photo
        self.display_photo()

        # Create previous and next buttons
        self.prev_button = tk.Button(self.frame, text="Previous", command=self.show_previous_photo,
                                     font=("Segoe Script", 16), bd=5, relief=tk.RAISED, borderwidth=2, fg="#D27685")
        self.prev_button.grid(row=1, column=0, padx=(0, 120))

        self.next_button = tk.Button(self.frame, text="Next", command=self.show_next_photo, font=("Segoe Script", 16),
                                     bd=5, relief=tk.RAISED, borderwidth=2, fg="#D27685")
        self.next_button.grid(row=1, column=1, padx=(120, 0))

        # Load the trained model
        self.model = joblib.load("SVM_model.pkl")  # Replace "SVM_model.pkl" with the path to your trained model file
        print("Model loaded successfully.")

        # Keep track of last predicted direction
        self.last_predicted_direction = None

        # Create Apply Prediction button
        self.apply_prediction_button = tk.Button(self.frame, text="Apply Prediction", font=("Segoe Script", 16),
                                                 command=self.apply_prediction_and_hide, bd=0, relief=tk.RAISED,
                                                 borderwidth=2, fg="#D27685")
        self.apply_prediction_button.grid(row=2, columnspan=2, padx=10, pady=10, ipadx=50)

        # Bind mouse hover events to change button color
        self.apply_prediction_button.bind("<Enter>", self.on_enter_apply_prediction_button)
        self.apply_prediction_button.bind("<Leave>", self.on_leave_apply_prediction_button)

    def display_photo(self):
        # Load and display the current photo
        if len(self.photo_paths) > 0:
            photo_path = self.photo_paths[self.current_index]
            photo = Image.open(photo_path)
            width, height = photo.size
            photo = photo.resize((600, 600), Image.ANTIALIAS)  # Resize the photo to a fixed size
            photo_tk = ImageTk.PhotoImage(photo)
            self.photo_label = tk.Label(self.frame, image=photo_tk)
            self.photo_label.image = photo_tk  # Keep a reference to prevent garbage collection
            self.photo_label.grid(row=0, columnspan=2)
        else:
            print("No photos found in the specified folder.")

    def show_previous_photo(self):
        if len(self.photo_paths) > 0:
            if self.current_index > 0:
                self.current_index -= 1
            else:
                self.current_index = len(self.photo_paths) - 1
            self.update_photo()

    def show_next_photo(self):
        if len(self.photo_paths) > 0:
            if self.current_index < len(self.photo_paths) - 1:
                self.current_index += 1
            else:
                self.current_index = 0
            self.update_photo()

    def update_photo(self):
        if hasattr(self, 'photo_label'):
            self.photo_label.destroy()
            self.display_photo()

    def predict_movement(self, features):
        # Use the model to predict the movement based on the extracted features
        prediction = self.model.predict(features)
        return prediction

    def apply_prediction_and_hide(self):
        # Specify the directory where prediction files are located
        prediction_file = "prediction_files/predicted_directions_subject04.npz"  # Change this to the specific prediction file you want to apply
        if not os.path.exists(prediction_file):
            print("Prediction file not found.")
            return

        prediction_data = np.load(prediction_file)
        predicted_direction = prediction_data['directions']
        if self.current_index == len(self.photo_paths) - 1:
            # Stop prediction or loop back to the beginning
            # For now, let's just stop the prediction by returning
            print("Reached end of photos, stopping prediction.")
            return
        self.apply_predicted_directions(predicted_direction)
        # Hide the Apply Prediction button after clicking
        self.apply_prediction_button.grid_forget()

    def apply_predicted_directions(self, predicted_direction):
        # Apply prediction results
        for i, direction in enumerate(predicted_direction):
            if direction == 1:  # Right movement
                self.master.after(i * 1000, lambda i=i: self.update_button_color(self.next_button, "#3A4D39"))
                self.master.after(i * 1000, lambda i=i: self.update_button_color(self.prev_button, "SystemButtonFace"))
                self.master.after(i * 1000, lambda i=i: self.show_next_photo())
            elif direction == 0:  # Left movement
                self.master.after(i * 1000, lambda i=i: self.update_button_color(self.prev_button, "#555843"))
                self.master.after(i * 1000, lambda i=i: self.update_button_color(self.next_button, "SystemButtonFace"))
                self.master.after(i * 1000 , lambda i=i: self.show_previous_photo())

    def update_button_color(self, button, color):
        button.config(bg=color)

    def on_enter_apply_prediction_button(self, event):
        self.apply_prediction_button.config(bg="#8CB3D9")  # Change color when mouse enters

    def on_leave_apply_prediction_button(self, event):
        self.apply_prediction_button.config(bg="SystemButtonFace")  # Change color when mouse leaves


def main():
    root = tk.Tk()
    app = PhotoViewerApp(root, "images")
    root.mainloop()


if __name__ == "__main__":
    main()
