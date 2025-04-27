import os
import img2pdf
import sys

# קבלת נתיב התמונות
image_folder = sys.argv[1]
images = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('jpg', 'jpeg', 'png'))]

# הדפסת שמות הקבצים של התמונות
print(f"Found images: {images}")

# אם אין תמונות
if not images:
    print("No images found!")
    sys.exit(1)

# המרת התמונות ל-PDF
output_pdf = '/app/output/' + os.environ.get('PDF_NAME', 'output.pdf')
with open(output_pdf, "wb") as f:
    try:
        f.write(img2pdf.convert(images))
        print(f"PDF saved to {output_pdf}")
    except Exception as e:
        print(f"Error occurred while converting images: {e}")
        sys.exit(1)
