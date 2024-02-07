import requests
import cv2
import numpy as np
from io import BytesIO

png_url = "https://deckofcardsapi.com/static/img/6H.png"

# Download the PNG file
response = requests.get(png_url)
png_data = BytesIO(response.content)

# Read the PNG data using cv2
png_array = np.asarray(bytearray(png_data.read()), dtype=np.uint8)
img = cv2.imdecode(png_array, cv2.IMREAD_UNCHANGED)

# Display the PNG image using cv2
cv2.imshow("PNG Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()







