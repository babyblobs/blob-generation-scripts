"""
@author: sway
"""

import json

jsons = []

traitsfile = open(
    'C:/Users/<Your username>Desktop/blobs/generation/nfts/combined-raw.json', 'r')
jsondata = traitsfile.read()
traits = json.loads(jsondata)

counter = 0


for trait in traits:
    blob = {}
    randomID = trait["Random ID"]
    blob["name"] = "BabyBlob #{id}".format(id=str(trait["tokenId"]))
    blob["symbol"] = "BABYBLOBS"
    blob["description"] = "Baby Blobs is a collection of 8078 cute, interactive Blob NFTs living on the Solana blockchain. Owning a pet Blob gives you access to an ever-expanding Blobverse and lets you participate in exclusive events and opportunities. Some Blobs are rarer than others, and some will reveal hidden features in the future. Visit https://babyblobs.art to learn more. You can interact with your Blob by tapping using 1-5 fingers; by moving your finger or the cursor around; or by pressing J, H, R, or B." 
    blob["seller_fee_basis_points"] = 250
    blob["image"] = "https://arweave.net/l0BpohK4twqn8OyMRbGnM0mgArxtTAvcYxPlhfdecN0/{id}.png".format(id=trait["Random ID"])
    blob["animation_url"] = "https://arweave.net/w3HkUkmCHYr-UgRldjg3RlHBOgwlXtIg9k1iZCGcSrA/{id}.html".format(
        id=str(trait["Random ID"]),)
    blob["external_url"] = "https://babyblobs.art"
    blob["attributes"] = [
        {"trait_type": "Tier",
         "value": trait["Tier"],
         "max_value": 4},
        {"trait_type": "Blob Style",
         "value": "{base}".format(base=trait["Blob Style"])},
        {"trait_type": "Background",
         "value": "{bg}".format(bg=trait["Background"])},
        {"trait_type": "Face",
         "value": "{face}".format(face=trait["Face"])},
        {"trait_type": "Face Color",
         "value": "{brightnes}".format(brightnes=trait["Face Color"])},
        {"trait_type": "Shape",
         "value": "{type}".format(type=trait["Shape"])}
    ]
    blob["collection"] = {"name": "Baby Blobs Gen #1",
                          "family": "Baby Blobs"}
    blob["properties"] = {"files": [
        {
            "uri": "https://arweave.net/l0BpohK4twqn8OyMRbGnM0mgArxtTAvcYxPlhfdecN0/{id}.png".format(id=trait["Random ID"]),
            "type": "image/png"
        }
    ],
        "category": "html",
        "creators": [
            {
                "address": "6rdyFpbDoLUp7xJ3RRwxoNA6qia1PFv6pR8XscaDSGxe",
                "share": 25
            },
            {
                "address": "9Zciu3YUp2cFjir4aXs75iPZMqqDndcq8JgfodwkTTW7",
                "share": 25
            },
            {
                "address": "E1swQRTDMQ3rukARV484JMBAWqqRyGLoTm8UKfCUd9Za",
                "share": 25
            },
            {
                "address": "DNLYTU56dysF78JCyAQpA6ZvWXqBtYEso8pdnVhmNdhK",
                "share": 25
            }
    ]}

    jsons.append(blob)
    with open(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/json-hex/{randomID}.json', 'w') as outfile:
        json.dump(blob, outfile, indent=4)
    print(counter)
    counter = counter + 1

with open('C:/Users/<Your username>Desktop/blobs/generation/nfts/traits.json', 'w') as outfile:
    json.dump(jsons, outfile, indent=4)
