import cv2
import pytesseract
import openai

openai.api_key = "sk-"


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_path, psm = 3, dpi = 70, oem= 3):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='spa', config=f'--psm {psm} --dpi {dpi} --oem {oem}')

    return text


image_path = 'guia.png'
prompt = "Responde a cada punto de esta guia"
text = extract_text(image_path)


response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": text},    ],
    max_tokens=500,
    n=1,
    stop=None,
    temperature=0.5,
)        

assistant_response = response['choices'][0]['message']['content']
print(assistant_response)
