import cv2
import glob
from vehicle_detector import VehicleDetector
class vehiculeCounting:
    def count():
    # Load Veichle Detector     
        vd = VehicleDetector()

        # Load images from a folder
        images_folder = glob.glob("images/*.jpg")

        vehicles_folder_count = 0
    
        # Loop through all the images
        for img_path in images_folder:
            print("Img path", img_path)
            img = cv2.imread(img_path)

            vehicle_boxes = vd.detect_vehicles(img)
            vehicle_count = len(vehicle_boxes)

            # Update total count
            vehicles_folder_count += vehicle_count

            for box in vehicle_boxes:
                x, y, w, h = box

                cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 1)

                

            #cv2.imshow("Cars", img)
            #cv2.waitKey(1)

        
        return(vehicles_folder_count,img)