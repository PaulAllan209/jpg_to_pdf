# jpg_to_pdf
Automatically resize an image and then combine it into a PDF.

Steps

1. Rename all pictures into 1, 2, 3.... and so on how ever you want it in order.
2. Input the size of the image you want it to appear on the PDF inside the 'cropped' variable (note that there are two defined cropped variables one in line 10 and one in line 15.)
3. Place all the pictures inside a folder named 'pictures'.
4. Copy the location of the parent folder of the folder 'pictures'.
5. Paste it inside the r string of the variable 'location_folder'.
6. Run the code and it will output the cropped pictures into the 'output_folder' and it will also output a PDF which have a default name of 'wow.pdf'.

Libraries.
PIL(Pillow fork).
PyPDF2.
