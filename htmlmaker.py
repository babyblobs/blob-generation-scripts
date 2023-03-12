"""
@author: sway
"""

import os
import json
def htmlmaker(trait):
    blobColor = "Bright" if trait["Face Color"] == "Dark" else "Dark"
    if trait["Tier"] == 4 and os.path.exists(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/1-1/foregrounds/{trait["Blob Style"]}.png'):
        with open(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/html/{trait["Random ID"]}.html', 'w') as f:
        #with open(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/html/{trait["Blob Style"]}.html', 'w') as f:
            f.write(f"""<!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>Baby Blob</title>
          <link rel="stylesheet" href="main.min.css">
        </head>
        <body class="center">
            <img id="background" src="1-1/backgrounds/{trait["Blob Style"]}.png" draggable="false">
            <img id="base" src="1-1/bases/{trait["Blob Style"]}.png" class="animate__animated" draggable="false">
            <img id="face" src="1-1/faces/{trait["Blob Style"]}.png" class="animate__animated" draggable="false">
            <img id="foreground" src ="1-1/foregrounds/{trait["Blob Style"]}.png" draggable="false">
            <script src="main.min.js"></script>
        </body>
        </html>""")
    elif trait["Tier"] == 4:
        with open(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/html/{trait["Random ID"]}.html', 'w') as f:
        # with open(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/html/{trait["Blob Style"]}.html', 'w') as f:
            f.write(f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Baby Blob</title>
            <link rel="stylesheet" href="main.min.css">
        </head>
        <body class="center">
            <img id="background" src="1-1/backgrounds/{trait["Blob Style"]}.png" draggable="false">
            <img id="base" src="1-1/bases/{trait["Blob Style"]}.png" class="animate__animated" draggable="false">
            <img id="face" src="1-1/faces/{trait["Blob Style"]}.png" class="animate__animated" draggable="false">
            <script src="main.min.js"></script>
        </body>
        </html>""")
    elif trait["Tier"] == 3 and os.path.exists(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/backgrounds/T3/{trait["Background"]}Fg.png'):
        with open(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/html/{trait["Random ID"]}.html', 'w') as f:
            f.write(f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Baby Blob</title>
            <link rel="stylesheet" href="main.min.css">
        </head>
        <body class="center">
            <img id="background" src="backgrounds/T3/{trait["Background"]}Bg.png" draggable="false">
            <img id="base" src="bases/{trait["Shape"]}/T3/{blobColor}/{trait["Blob Style"]}.png" class="animate__animated" draggable="false">
            <img id="face" src="faces/{trait["Face Color"]}/{trait["Face"]}.png" class="animate__animated" draggable="false">
            <img id="foreground" src ="backgrounds/T3/{trait["Background"]}Fg.png" draggable="false">
            <script src="main.min.js"></script>
        </body>
        </html>""")
    elif trait["Tier"] == 3:
        with open(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/html/{trait["Random ID"]}.html', 'w') as f:
            f.write(f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Baby Blob</title>
            <link rel="stylesheet" href="main.min.css">
        </head>
        <body class="center">
            <img id="background" src="backgrounds/T3/{trait["Background"]}Bg.png" draggable="false">
            <img id="base" src="bases/{trait["Shape"]}/T3/{blobColor}/{trait["Blob Style"]}.png" class="animate__animated" draggable="false">
            <img id="face" src="faces/{trait["Face Color"]}/{trait["Face"]}.png" class="animate__animated" draggable="false">
            <script src="main.min.js"></script>
        </body>
        </html>""")
    else:
        with open(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/html/{trait["Random ID"]}.html', 'w') as f:
            f.write(f"""<!DOCTYPE html>
         <html lang="en">
         <head>
             <meta charset="UTF-8">
             <meta name="viewport" content="width=device-width, initial-scale=1.0">
             <meta http-equiv="X-UA-Compatible" content="ie=edge">
             <title>Baby Blob</title>
             <link rel="stylesheet" href="main.min.css">
         </head>
         <body class="center">
             <img id="background" src="backgrounds/T{trait["Tier"]}/{trait["Background"]}.png" draggable="false">
             <img id="base" src="bases/{trait["Shape"]}/T{trait["Tier"]}/{blobColor}/{trait["Blob Style"]}.png" class="animate__animated" draggable="false">
             <img id="face" src="faces/{trait["Face Color"]}/{trait["Face"]}.png" class="animate__animated" draggable="false">            
             <script src="main.min.js"></script>
         </body>
         </html>""")


    # if os.path.exists(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/foregrounds/{name}.png'):
traitsfile = open(
    'C:/Users/<Your username>Desktop/blobs/generation/nfts/combined-raw.json', 'r')
jsondata = traitsfile.read()
traits = json.loads(jsondata)

for trait in traits:
    htmlmaker(trait)
