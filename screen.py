import pyautogui
import os
import time

# Optional delay before screenshot
time.sleep(2)  

# Capture the screenshot
screenshot = pyautogui.screenshot()

# Save the screenshot
save_path = "screenshot.png"
screenshot.save(save_path)

# Print the saved location
print("Screenshot saved at:", os.path.abspath(save_path))
