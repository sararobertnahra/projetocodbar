import uvicorn 
import fastapi 
import cv2
from pyzbar.pyzbar import decode

def start(image):
    img = cv2.imread(image)
    detectedBarcodes = decode(img)
    if not detectedBarcodes:
        print("Barcode não detectado ou barcode danificado") 
    else:
        for barcode in detectedBarcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(img, (x-10, y-10), (x + w+10, y + h+10), (255, 0, 0), 2)
            if barcode.data!="":
                print(barcode.data)
                print(barcode.type)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    image="edp.pdf"
    start(image)

app = fastapi.FastAPI()

@app.get("/")
def handleroot():
    return "Deu certo!"


def start(image):
    uvicorn.run(app,host="0.0.0.0", port=5000)