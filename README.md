# Chevron Logo Detector

Chevron Logo Detector is a PyQt6 GUI application. The purpose of this application is to search and process batches of images and allocated the images into their
respective folders using Google Cloud Vision API. The application allocated the processed images into a logo detected folder, failed deteced folder, and undetected folder.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

What things you need to install the software and how to install them

```
  - clone the project repo
  - install pycharm or any ide
  - install the project requirements
  - setup google vision API https://cloud.google.com/vision/docs/setup
  - to setup google credential applications you can use os.environ["GOOGLE_APPLICATION_CREDENTIALS'] = "specify path of json key"
```

## DEMO

On application start a pop up will ask for input:

<img width="494" alt="Screen Shot 2022-10-18 at 2 57 27 PM" src="https://user-images.githubusercontent.com/56740595/196554604-64114279-e8cf-4c9f-89d9-c90e96852dd8.png">
  
Once the select file button is clicked a file dialog will appear

<img width="789" alt="Screen Shot 2022-10-18 at 2 58 09 PM" src="https://user-images.githubusercontent.com/56740595/196559356-9ff46513-029e-4edb-86fe-bdd32d6c15cb.png">

Select the folder to be filtered, the images will then be processed and moved to the provided folders:

![Screen Shot 2022-10-18 at 2 58 49 PM](https://user-images.githubusercontent.com/56740595/196559777-a874c7d5-bc56-4790-b638-06792c3809ee.png)

This is what the folders should look like once the images have been processed:

![Screen Shot 2022-10-18 at 2 59 41 PM](https://user-images.githubusercontent.com/56740595/196559834-9e17ec3d-3c95-45d7-bd16-c73c687d25bf.png)

