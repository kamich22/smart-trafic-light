import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from vehicle_detector import VehicleDetector
import random

root = tk.Tk()

frame = tk.Frame(root, bg="#3e646c")
frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")

class VehicleCountingGUI:
    def __init__(self, root):
        self.root = root
        self.image_path_north = ""
        self.image_path_south = ""
        self.image_path_east = ""
        self.image_path_west = ""
        self.image_display_north = None
        self.image_display_south = None
        self.image_display_east = None
        self.image_display_west = None
        self.image_display_north2 = None
        self.image_display_south2 = None
        self.image_display_east2 = None
        self.image_display_west2 = None
        self.image_path1 = None
        self.image_path2 = None

        # Create a browse button for the North position
        self.browse_button_north = tk.Button(self.root, text="Browse1", command=self.browse_image_north,bg="black", fg="white", width=20, height=2)
        self.browse_button_north.pack(side="top", pady=10)

        # Create a label to display the selected image path for the North position
        self.image_path_label_north = tk.Label(self.root)
        self.image_path_label_north.pack(side="top")

        # Create an image label for the North position
        self.image_label_north = tk.Label(self.root)
        self.image_label_north.pack(side="top")
        self.image_label_north2 = tk.Label(self.root)
        self.image_label_north2.pack(side="top")

        # Create a browse button for the South position
        self.browse_button_south = tk.Button(self.root, text="Browse2", command=self.browse_image_south, bg="black", fg="white", width=20, height=2)
        self.browse_button_south.pack(side="bottom", padx=10)

        # Create a label to display the selected image path for the South position
        self.image_path_label_south = tk.Label(self.root)
        self.image_path_label_south.pack(side="bottom")

        # Create an image label for the South position
        self.image_label_south = tk.Label(self.root)
        self.image_label_south.pack(side="bottom")
        self.image_label_south2 = tk.Label(self.root)
        self.image_label_south2.pack(side="bottom")


        # Create a browse button for the East position
        self.browse_button_east = tk.Button(self.root, text="Browse3", command=self.browse_image_east, bg="black", fg="white", width=20, height=2)
        self.browse_button_east.pack(side="right", pady=10)

        # Create a label to display the selected image path for the East position
        self.image_path_label_east = tk.Label(self.root, text="")
        self.image_path_label_east.pack(side="right")

        # Create an image label for the East position
        self.image_label_east = tk.Label(self.root)
        self.image_label_east.pack(side="right")
        self.image_label_east2 = tk.Label(self.root)
        self.image_label_east2.pack(side="right")

        # Create a browse button for the West position
        self.browse_button_west = tk.Button(self.root, text="Browse 4", command=self.browse_image_west, bg="black", fg="white", width=20, height=2)
        self.browse_button_west.pack(side="left",padx=10)

        # Create a label to display the selected image path for the West position
        self.image_path_label_west = tk.Label(self.root, text="")
        self.image_path_label_west.pack(side="left")

        # Create an image label for the West position
        self.image_label_west = tk.Label(self.root)
        self.image_label_west.pack(side="left")
        self.image_label_west2 = tk.Label(self.root)
        self.image_label_west2.pack(side="left")

        self.compare_button = tk.Button(self.root, text="Compare Counts", command=self.compare_vehicle_counts, bg="black", fg="white", width=40, height=2)
        self.compare_button.pack(anchor="w", side="bottom",)

    def browse_image_north(self):
        # Open a file dialog to choose an image file for the North position
        self.image_path_north = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

        # Update the image path label for the North position
        self.image_path_label_north.config(text=self.image_path_north)

        # Load and display the image for the North position
        self.load_and_display_image(self.image_path_north, self.image_label_north, "north")

    def browse_image_south(self):
        # Open a file dialog to choose an image file for the South position
        self.image_path_south = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

        # Update the image path label for the South position
        self.image_path_label_south.config(text=self.image_path_south)

        # Load and display the image for the South position
        self.load_and_display_image(self.image_path_south, self.image_label_south, "south")

    def browse_image_east(self):
        # Open a file dialog to choose an image file for the East position
        self.image_path_east = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

        # Update the image path label for the East position
        self.image_path_label_east.config(text=self.image_path_east)

        # Load and display the image for the East position
        self.load_and_display_image(self.image_path_east, self.image_label_east, "east")

    def browse_image_west(self):
        # Open a file dialog to choose an image file for the West position
        self.image_path_west = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

        # Update the image path label for the West position
        self.image_path_label_west.config(text=self.image_path_west)

        # Load and display the image for the West position
        self.load_and_display_image(self.image_path_west, self.image_label_west, "west")

    def load_and_display_image(self, image_path, image_label, position):
        if image_path:
            # Load the image
            image = Image.open(image_path)

            # Resize the image to fit within the GUI window
            image = image.resize((250, 250))

            # Convert the image to Tkinter-compatible format
            image_display = ImageTk.PhotoImage(image)

            # Display the image in the label
            image_label.config(image=image_display)
            image_label.image = image_display

            # Save the image display object to the corresponding position
            if position == "north":
                self.image_display_north = image_display
            elif position == "south":
                self.image_display_south = image_display
            elif position == "east":
                self.image_display_east = image_display
            elif position == "west":
                self.image_display_west = image_display
    def load_and_display_image2(self, image_path, image_label, position):
        if image_path:
            # Load the image
            image = Image.open(image_path)

            # Resize the image to fit within the GUI window
            image = image.resize((100, 100))

            # Convert the image to Tkinter-compatible format
            image_display = ImageTk.PhotoImage(image)

            # Display the image in the label
            image_label.config(image=image_display)
            image_label.image = image_display

            # Save the image display object to the corresponding position
            if position == "north":
                self.image_display_north2 = image_display
            elif position == "south":
                self.image_display_south2 = image_display
            elif position == "east":
                self.image_display_east2 = image_display
            elif position == "west":
                self.image_display_west2 = image_display

    def count_vehicles(self, image_path):
        if image_path:
            # Load the selected image
            img = cv2.imread(image_path)

            vd = VehicleDetector()

            # Detect vehicles in the image
            vehicle_boxes = vd.detect_vehicles(img)
            vehicle_count = len(vehicle_boxes)

            # Print the number of vehicles
            print("Number of vehicles:", vehicle_count)

            # Draw bounding boxes and labels on the image
            for box in vehicle_boxes:
                x, y, w, h = box
                cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 1)

            # Display the image with bounding boxes
            self.display_image_with_boxes(img, image_path)

            return vehicle_count

        else:
            print("No image selected.")

    def compare_vehicle_counts(self):
    # Get the vehicle counts for each direction
        count_north = self.count_vehicles(self.image_path_north)
        count_south = self.count_vehicles(self.image_path_south)
        count_east = self.count_vehicles(self.image_path_east)
        count_west = self.count_vehicles(self.image_path_west)
        path1 = "feu_vert.jpg"
        path2 = "feu_rouge.jpg"
        max_count = max(count_north + count_south, count_east + count_west)

        if count_north + count_south == count_east + count_west:
            result = "Equal counts: {}".format(max_count)

            # Select a random image path
            random_path = random.sample([path1, path2], 1)[0]

            # Assign the remaining image path
            remaining_path = path1 if random_path == path2 else path2

            # Load the images for path1 and path2
            self.image_path1 = random_path
            self.image_path2 = remaining_path

            # Display the images
            self.load_and_display_image2(self.image_path1, self.image_label_north2, "north")
            self.load_and_display_image2(self.image_path1, self.image_label_south2, "south")
            self.load_and_display_image2(self.image_path2, self.image_label_east2, "east")
            self.load_and_display_image2(self.image_path2, self.image_label_west2, "west")

        elif count_north + count_south > count_east + count_west:
            self.image_path1 = path1
            self.image_path2 = path2

            # Display the images
            self.load_and_display_image2(self.image_path1, self.image_label_north2, "north")
            self.load_and_display_image2(self.image_path1, self.image_label_south2, "south")
            self.load_and_display_image2(self.image_path2, self.image_label_east2, "east")
            self.load_and_display_image2(self.image_path2, self.image_label_west2, "west")
            result = "Equal counts: {}".format(max_count)

        elif count_north + count_south < count_east + count_west:
            self.image_path1 = path2
            self.image_path2 = path1

            # Display the images
            self.load_and_display_image2(self.image_path1, self.image_label_north2, "north")
            self.load_and_display_image2(self.image_path1, self.image_label_south2, "south")
            self.load_and_display_image2(self.image_path2, self.image_label_east2, "east")
            self.load_and_display_image2(self.image_path2, self.image_label_west2, "west")
            result = "Equal counts: {}".format(max_count)

        print(result)


    def display_image_with_boxes(self, img, image_path):
        # Convert the image to RGB for PIL
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Create a PIL image from the RGB array
        pil_img = Image.fromarray(img_rgb)

        # Resize the image to fit within the GUI window
        pil_img = pil_img.resize((250, 250))

        # Convert the PIL image to Tkinter-compatible format
        image_display = ImageTk.PhotoImage(pil_img)

        # Display the image in the corresponding label
        if image_path == self.image_path_north:
            self.image_label_north.config(image=image_display)
            self.image_label_north.image = image_display
        elif image_path == self.image_path_south:
            self.image_label_south.config(image=image_display)
            self.image_label_south.image = image_display
        elif image_path == self.image_path_east:
            self.image_label_east.config(image=image_display)
            self.image_label_east.image = image_display
        elif image_path == self.image_path_west:
            self.image_label_west.config(image=image_display)
            self.image_label_west.image = image_display

# Create the Tkinter root window

root.geometry("1920x1080")
root.state('zoomed')
# Create an instance of the VehicleCountingGUI class
gui = VehicleCountingGUI(root)

# Start the Tkinter event loop
root.mainloop()
