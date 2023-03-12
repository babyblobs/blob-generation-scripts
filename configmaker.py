"""
@author: sway
"""

import json

jsons = {}

traitsfile = open(
    'C:/Users/<Your username>/Desktop/blobs/generation/nfts/combined-raw.json', 'r')
jsondata = traitsfile.read()
traits = json.loads(jsondata)

counter = 0


for trait in traits:
    blobInfo = {}
    blobInfo["link"] = "https://arweave.net/kQsAW9t6QMMG6a5_D1XxnC7nnPwRZrwjL38h9hPTIpQ/{id}.json".format(id=trait["Random ID"])
    blobInfo["name"] = "BabyBlob #{id}".format(id=trait["tokenId"])
    blobInfo["onChain"] = False
    jsons[str(counter)] = blobInfo
    print(counter)
    counter = counter + 1

with open('C:/Users/<Your username>Desktop/blobs/generation/nfts/config-section.json', 'w') as outfile:
    json.dump(jsons, outfile, indent=4)
