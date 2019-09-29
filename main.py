import cv2
import numpy as np
import re

# Files to be used
text_in = 'bee_text.txt'
image_in_file = 'beemovie_image.jpg'
image_out_file = 'beemovie_out.png'

# Load text file, make upper + remove new lines
file = open(text_in)
file = file.read()
file = file.upper()
file = re.sub("\n", ' ', file)
file = re.sub(" {2}", ' ', file)
char_itr = 0

# Load image
image_in = cv2.imread(image_in_file, cv2.IMREAD_COLOR)
rows, cols, d = image_in.shape

# Create placeholder image w/ 8-bit colour depth
im_scale = 1
image_out = np.zeros((rows * im_scale, cols * im_scale, d), np.uint8)

# Pixel stride in original image - determines spacing of letters
row_stride = 11
col_stride = 10

# Iterate pixels in
for i in range(0, rows - 1, row_stride):
    for j in range(0, cols - 1, col_stride):
        # Reset input string iterator if end of string reached
        if char_itr + 1 > len(file):
            char_itr = 0

        # Format output text
        font = cv2.FONT_HERSHEY_PLAIN   # font style
        thickness = 2                   # font thickness
        scale = 0.9                     # font size
        height = 9                      # Top offset (draw from bottom of char)
        colour = (int(image_in[i, j][0]), int(image_in[i, j][1]), int(image_in[i, j][2]))  # Colour from source img

        # Draw text to output image
        cv2.putText(image_out, file[char_itr], (j * im_scale, i * im_scale + height), font, scale, colour, thickness)

        # Increment to next char in input string
        char_itr += 1

# Write output to file + display
cv2.imwrite(image_out_file, image_out)
cv2.imshow(image_out_file, image_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
