import io,os
from google.cloud import vision
from google.cloud.vision import ImageAnnotatorClient
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\User\\Documents\\gcloudstuff\\apikeys.json"
client = vision.ImageAnnotatorClient()
file_name ='test.jpg'
  
with io.open(file_name,'rb') as image_file:
    content = image_file.read()
    image = types.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotations

print ('Labels:')
for label in labels:
    print (label.description)


