import os
print("Current Working Directory:", os.getcwd())

import cv2

# Read the image
image = cv2.imread("akpy.jpg")

# Check if the image is loaded
if image is None:
    print("Error: Could not read the image file.")
else:
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Save the blurred image
    cv2.imwrite("blurred_image.jpg", blurred_image)
    print("Blurred image saved as 'blurred_image.jpg'")

    # Display the images (optional, comment out if running in a headless environment)
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
