import requests

def ocr_space_file(filename, overlay=False, api_key="", language='spa'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

ocr_space_file('guia.png')
print(ocr_space_file('guia.png'))
