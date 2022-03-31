import os
from PIL import Image
import PyPDF2


def jpgEditorToPdf(source_folder, output_folder, pdf_name):
    for files in os.listdir(source_folder):
        if os.path.exists(output_folder):
            im1 = Image.open(fr'{source_folder}/{files}')
            cropped = im1.crop(box=(0, 0, 2298, 2925))
            cropped.save(f'{output_folder}/{files}')
        else:
            os.makedirs(output_folder)
            im1 = Image.open(fr'{source_folder}/{files}')
            cropped = im1.crop(box=(0, 0, 2298, 2925))
            cropped.save(f'{output_folder}/{files}')

    # first_image = os.listdir(output_folder)[0]
    # im2 = Image.open(fr'{output_folder}/{first_image}')
    # im2.convert('RGB')
    # im2.save(f'{pdf_name}.pdf')

    jpg_list = os.listdir(output_folder)
    jpg_list_sorted = sorted(jpg_list, key=lambda x: int(x[:-4]))

    merger = PyPDF2.PdfFileMerger()

    for files2 in jpg_list_sorted:
        im3 = Image.open(fr'{output_folder}/{files2}')
        im3.convert('RGB')
        im3.save(f'{output_folder}/{files2[:-4]}.pdf')

        merger.append(f'{output_folder}/{files2[:-4]}.pdf')

    merger.write(f'{pdf_name}.pdf')
    merger.close()

    for tempPdf in os.listdir(output_folder):
        if tempPdf[-4:] == '.pdf':
            os.remove(f'{output_folder}/{tempPdf}')


location_folder = r'C:\Users\i5_4thGen\Desktop\Electrical engineering files\2nd Year\Engineering Data Analysis\quiz\Final Exam'
source_folder = fr'{location_folder}\pictures'
output_folder = fr'{location_folder}\output_folder'
pdf_name = fr'{location_folder}\wow'

jpgEditorToPdf(source_folder, output_folder, pdf_name)
