import io
import os
import pandas as pd
from google.cloud import vision
from google.cloud.vision import types
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\\Users\\User\\Documents\\gcloudstuff\\apikeys.json'
client = vision.ImageAnnotatorClient()
def detectText(img):
    with io.open(img,'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    df = pd.DataFrame(columns=['locale','description'])
    for text in texts:
        df = df.append(
            dict(
                locale=text.locale,
                description=text.description 
            ),
            ignore_index = True
        )
    return df

    print (df['description'][0])
FILE_NAME = 'text3.jpg'
FOLDER_PATH = r'C:\Users\User\Documents\gcloudstuff\visionex'
print (detectText(os.path.join(FOLDER_PATH,FILE_NAME)))
    
