"""
@author: sway
"""

from PIL import Image
import random
import json
from multiprocessing.pool import ThreadPool as Pool
import os
import time
print("hello")
random.seed(69420)

# NECESSARY INFO

t1darkbases = {'Aegean Teal': 1, 'Charcoal Obsidian': 1, 'Cherry Wine': 1,
               'Cinnamon Chocolate': 1, 'Eggplant Pine': 1, 'Purple Berry': 1}
t1brightbases = {'Apricot Sage': 1, 'Arctic Berry': 1, 'Arctic Helio': 1, 'Bittersweet Iris': 1, 'Butter Tiger': 1, 'Carnation Lavender': 1, 'Cerulean Eggplant': 1, 'Coral Lime': 1, 'Cornflower Fuchsia': 1, 'Egyptian Maya': 1, 'Electric Amethyst': 1, 'Electric Azure': 1, 'Electric Sky': 1, 'Emerald Lime': 1, 'Fandango Lemonade': 1, 'Grape Bubblegum': 1, 'Imperial Peach': 1, 'Iris Orchid': 1, 'Jade Space': 1, 'Lapis Turquoise': 1, 'Lavender Gam': 1,
                 'Mauve Lapis': 1, 'Mellow Lemon': 1, 'Mint Bubblegum': 1, 'Mint Denim': 1, 'Mulberry Byzantine': 1, 'Ocean Sand': 1, 'Ocean Seafoam': 1, 'Olive Yale': 1, 'Orchid Periwinkle': 1, 'Pearl Cloud': 1, 'Pineapple Taffy': 1, 'Pistachio Lollipop': 1, 'Rose Mint': 1, 'Rufous Tart': 1, 'Salmon Taffy': 1, 'Shadow Whisper': 1, 'Taffy Cerise': 1, 'Teal Coral': 1, 'Terracotta Sand': 1, 'Turquoise Mint': 1, 'Viola Bisque': 1, 'Viola Maya': 1, 'Wisteria Periwinkle': 1}
t2darkbases = {'Liquid Deep Ocean': 1,
               'Liquid Heather Eggplant': 1, 'Liquid Inky Cherry': 1}
t2brightbases = {'Bronze': 1, 'Camouflage': 1, 'Creamy Ocean Starfish': 1, 'Gold': 1, 'Liquid Aegean Coral': 1, 'Liquid Aegean Kelly': 1, 'Liquid Aegean Vanilla': 1, 'Liquid African Plum': 1, 'Liquid Amaranth Banana': 1, 'Liquid Apple Butter': 1, 'Liquid Apricot Eggplant': 1, 'Liquid Arctic Cobalt': 1, 'Liquid Arctic Periwinkle': 1, 'Liquid Azure Mint': 1, 'Liquid Baby Blue Banana Rose': 1, 'Liquid Banana Iris': 1, 'Liquid Banana Ocean': 1, 'Liquid Banana Peach': 1, 'Liquid Biscotti Hunter': 1, 'Liquid Botswana Agate': 1, 'Liquid Boysenberry Ocean': 1, 'Liquid Bumblebee Cantaloupe': 1, 'Liquid Buttermilk Tiffany': 1, 'Liquid Byzantine Apricot': 1, 'Liquid Caramel Cream': 1, 'Liquid Cerise Lemon Sky': 1, 'Liquid Cerulean Berry Lime': 1, 'Liquid Cherry Wine Cream': 1, 'Liquid Chiffon Sky': 1, 'Liquid Cinnamon Silk': 1, 'Liquid Cornflower Opal': 1, 'Liquid Cornflower Salmon': 1, 'Liquid Cornflower Wheat': 1, 'Liquid Cotton Parakeet': 1, 'Liquid Cream Crepe': 1, 'Liquid Cream Fern': 1, 'Liquid Creamy Cerulean Iris': 1, 'Liquid Cyan Sapphire': 1, 'Liquid Daffodil Orchid': 1, 'Liquid Denim Iris Ocean': 1, 'Liquid Denim Sepia': 1, 'Liquid Disco Confetti': 1, 'Liquid Electric Fuchsia': 1, 'Liquid Flamingo Punch': 1, 'Liquid Flamingo Sky Ocean': 1, 'Liquid Fuchsia Sky': 1, 'Liquid Holographic Iris': 1, 'Liquid Honey Rouge': 1, 'Liquid Independence Puce': 1, 'Liquid Indigo Mint Taffy': 1, 'Liquid Jam Candy': 1, 'Liquid Lapis Cobalt Geode': 1, 'Liquid Lapis Kelly': 1,
                 'Liquid Lavender Lime': 1, 'Liquid Lavender Sky': 1, 'Liquid Lavender Snow': 1, 'Liquid Lemon Cornflower': 1, 'Liquid Lemon Lime': 1, 'Liquid Lilac Butter Sky': 1, 'Liquid Lilac Macaroon': 1, 'Liquid Magenta Sky': 1, 'Liquid Mauve Teal Ruby': 1, 'Liquid Midnight Vanilla': 1, 'Liquid Minty Iris': 1, 'Liquid Mulberry Salt': 1, 'Liquid Mulberry Tea': 1, 'Liquid Mulberry Wheat': 1, 'Liquid Nacreous Pastel': 1, 'Liquid Navy Thistle': 1, 'Liquid Ocean Rose': 1, 'Liquid Ocean Tiger Geode': 1, 'Liquid Opaline Turquoise': 1, 'Liquid Parmesan Cantaloupe': 1, 'Liquid Pearl Thunder': 1, 'Liquid Peppermint Powder': 1, 'Liquid Periwinkle Carousel': 1, 'Liquid Periwinkle Maya Pearls': 1, 'Liquid Periwinkle Shadow': 1, 'Liquid Pine Mint Tea': 1, 'Liquid Pine Tea': 1, 'Liquid Pistachio Mauve': 1, 'Liquid Radiant  Cyandra': 1, 'Liquid Raisin Pine': 1, 'Liquid Raspberry Mint': 1, 'Liquid Redwood Oat': 1, 'Liquid Rose Mint': 1, 'Liquid Ruby Taupe': 1, 'Liquid Sapphire Yale': 1, 'Liquid Seafoam Iron': 1, 'Liquid Shortbread Moss': 1, 'Liquid Space Mint': 1, 'Liquid Spruce Tea': 1, 'Liquid Stone Blush Geode': 1, 'Liquid Strawberry Bumblebee': 1, 'Liquid Strawberry Eggplant': 1, 'Liquid Strawberry Laurel': 1, 'Liquid Tangerine Forest': 1, 'Liquid Tangerine Lollipop': 1, 'Liquid Thistle Banana Crepe': 1, 'Liquid Tortilla Slate Geode': 1, 'Liquid Turquoise Heather': 1, 'Liquid Ultra Cyan': 1, 'Liquid Viridian Tea': 1, 'Liquid White Hydrangea': 1, 'Platinum': 1, 'Silver': 1, 'Transparent': 1}
t3darkbases = {'Black Diamond': 1, 'Cherry Soda': 1, 'Chocolate Drizzle': 1, 'Chocolate Sprinkles': 1,
               'Cola Soda': 1, 'Deep Space': 1, 'Grape Soda': 1, 'Purple Eclipse': 1}
t3brightbases = {'Amethyst': 1, 'Apple': 1, 'Blue Sapphire': 1, 'Blue Topaz': 1, 'Boba Tea': 1, 'Cherry': 1, 'Closed Brain Coral': 1, 'Citrine': 1, 'Diamond': 1, 'Ebi': 1, 'Emerald': 1, 'Extraterrestrial Cosmos': 1, 'Gold Solar Flare': 1, 'Grooved Brain Coral': 1, 'Hamachi': 1, 'Hirame': 1, 'Hokkigai': 1, 'Ika': 1, 'Kani': 1, 'Kiwi Soda': 1, 'Margherita Pizza': 1, 'Milky Way Sky': 1, 'Olive Mushroom Pizza': 1, 'Onigiri': 1, 'Orange Foliaceous Coral': 1, 'Orange Soda': 1, 'Pepper Mushroom Pizza': 1,
                 'Pepperoni Onion Pizza': 1, 'Pepperoni Pizza': 1, 'Peridot': 1, 'Pineapple': 1, 'Pink Bubble Coral': 1, 'Pink Supernova': 1, 'Pink Tourmaline': 1, 'Purple Tube Sponge': 1, 'Raspberry Soda': 1, 'Red Nebula': 1, 'Ruby': 1, 'Saba': 1, 'Silver Comet': 1, 'Soda Water': 1, 'Strawberry Drizzle': 1, 'Strawberry Sprinkles': 1, 'Strawberry': 1, 'Tai': 1, 'Tako': 1, 'Tamago': 1, 'Turquoise Meteor': 1, 'Unagi': 1, 'Vanilla Drizzle': 1, 'Vanilla Sprinkles': 1, 'Veggie Pizza': 1, 'Watermelon': 1, 'Yellow Topaz': 1}

similarfaces = {frozenset({'Wink', 'Wink Laugh'}): 'Winks', frozenset({'Satisfied', 'Satisfied Nya', 'Melt', 'Neutral Smile'}): 'Satisfieds', frozenset({'Blush Laugh', 'Blush Nya', 'Blep', 'Blush'}): 'Blushes', frozenset({'Smirk', 'Side Eye'}): 'SideEyes', frozenset(
    {'Dizzy', 'Dead'}): 'DizzyDead', frozenset({'Loveful', 'Lovestruck'}): 'Loves', frozenset({'Starstruck', 'Startstruck Blep'}): 'Starstrucks', frozenset({'Hypnotized', 'Hypnotized Drool'}): 'Hypno', frozenset({'Derp', 'Derp Blep'}): 'Derps'}


blackfaces = {'Amazed': 0.5, 'Angry': 1, 'Astonished': 1, 'Blep': 1, 'Bloop': 1, 'Blush Laugh': 1, 'Blush Nya': 1, 'Blush': 1, 'Cry': 1, 'Dead Inside': 0.5, 'Dead': 0.5, 'Derp Blep': 1, 'Derp': 1, 'Disappointed': 1, 'Dizzy': 0.5, 'Drool': 1, 'Evil': 0.2, 'Flower Eyes': 0.2, 'Flustered': 0.5, 'Glower': 0.5, 'Hypnotized Drool': 0.5, 'Hypnotized': 0.5, 'Laugh': 1, 'Loveful': 0.2, 'Lovestruck': 0.2, 'Mad': 0.5, 'Melt': 1,
              'Neutral Smile': 1, 'Plotting': 1, 'Sad': 1, 'Satisfied Nya': 1, 'Satisfied': 1, 'Shocked': 0.5, 'Side Eye': 1, 'Smile': 1, 'Smiling': 1, 'Smirk': 1, 'Smug': 0.5, 'Sparkle Eyes': 0.2, 'Spooked': 0.2, 'Squee': 1, 'Stargaze': 0.2, 'Starstruck Blep': 0.2, 'Starstruck': 0.2, 'Teary': 0.5, 'Tease': 1, 'Twinkle': 0.2, 'UwU': 1, 'Wail': 0.5, 'Weary': 1, 'Wink Laugh': 1, 'Wink': 1, 'Winkle': 0.2, 'Zany': 0.5, 'Devastated': 0.2, 'Energized': 0.2, 'Kuudere': 0.2, 'Struggle': 0.2, 'Wicked': 0.2, 'Third Eye': 0.1}

whitefaces = {'Amazed': 0.5, 'Angry': 1, 'Astonished': 1, 'Blep': 1, 'Bloop': 1, 'Blush Laugh': 1, 'Blush Nya': 1, 'Blush': 1, 'Cry': 1, 'Dead Inside': 0.5, 'Dead': 0.5, 'Derp Blep': 1, 'Derp': 1, 'Disappointed': 1, 'Dizzy': 0.5, 'Drool': 1, 'Evil': 0.2, 'Flower Eyes': 0.2, 'Flustered': 0.5, 'Glower': 0.5, 'Hypnotized Drool': 0.5, 'Hypnotized': 0.5, 'Laugh': 1, 'Loveful': 0.2, 'Lovestruck': 0.2, 'Mad': 0.5, 'Melt': 1,
              'Neutral Smile': 1, 'Plotting': 1, 'Sad': 1, 'Satisfied Nya': 1, 'Satisfied': 1, 'Shocked': 0.5, 'Side Eye': 1, 'Smile': 1, 'Smiling': 1, 'Smirk': 1, 'Smug': 0.5, 'Sparkle Eyes': 0.2, 'Spooked': 0.2, 'Squee': 1, 'Stargaze': 0.2, 'Starstruck Blep': 0.2, 'Starstruck': 0.2, 'Teary': 0.5, 'Tease': 1, 'Twinkle': 0.2, 'UwU': 1, 'Wail': 0.5, 'Weary': 1, 'Wink Laugh': 1, 'Wink': 1, 'Winkle': 0.2, 'Zany': 0.5, 'Devastated': 0.2, 'Energized': 0.2, 'Kuudere': 0.2, 'Struggle': 0.2, 'Wicked': 0.2, 'Third Eye': 0.1}

t1bg = {'Arctic': 1, 'Cornflower': 1, 'Daffodil': 1, 'Indigo': 1,
        'Lime': 1, 'Mint': 1, 'Peach': 1, 'Rose': 1, 'Steel': 1, 'Taffy': 1}

t2bg = {'Arctic1': 0.5, 'Arctic2': 1, 'Arctic3': 1, 'Arctic4': 1, 'Arctic5': 0.5, 'Arctic6': 0.8, 'Arctic7': 0.8, 'Arctic8': 0.8, 'Arctic9': 0.8, 'Cornflower1': 0.5, 'Cornflower2': 1, 'Cornflower3': 1, 'Cornflower4': 1, 'Cornflower5': 0.5, 'Cornflower6': 0.8, 'Cornflower7': 0.8, 'Cornflower8': 0.8, 'Cornflower9': 0.8, 'Daffodil1': 0.5, 'Daffodil2': 1, 'Daffodil3': 1, 'Daffodil4': 1, 'Daffodil5': 0.5, 'Daffodil6': 0.8, 'Daffodil7': 0.8, 'Daffodil8': 0.8, 'Daffodil9': 0.8, 'Indigo1': 0.5, 'Indigo2': 1, 'Indigo3': 1, 'Indigo4': 1, 'Indigo5': 0.5, 'Indigo6': 0.8, 'Indigo7': 0.8, 'Indigo8': 0.8, 'Indigo9': 0.8, 'Lime1': 0.5, 'Lime2': 1, 'Lime3': 1, 'Lime4': 1, 'Lime5': 0.5,
        'Lime6': 0.8, 'Lime7': 0.8, 'Lime8': 0.8, 'Lime9': 0.8, 'Mint1': 0.5, 'Mint2': 1, 'Mint3': 1, 'Mint4': 1, 'Mint5': 0.5, 'Mint6': 0.8, 'Mint7': 0.8, 'Mint8': 0.8, 'Mint9': 0.8, 'Peach1': 0.5, 'Peach2': 1, 'Peach3': 1, 'Peach4': 1, 'Peach5': 0.5, 'Peach6': 0.8, 'Peach7': 0.8, 'Peach8': 0.8, 'Peach9': 0.8, 'Rose1': 0.5, 'Rose2': 1, 'Rose3': 1, 'Rose4': 1, 'Rose5': 0.5, 'Rose6': 0.8, 'Rose7': 0.8, 'Rose8': 0.8, 'Rose9': 0.8, 'Steel1': 0.5, 'Steel2': 1, 'Steel3': 1, 'Steel4': 1, 'Steel5': 0.5, 'Steel6': 0.8, 'Steel7': 0.8, 'Steel8': 0.8, 'Steel9': 0.8, 'Taffy1': 0.5, 'Taffy2': 1, 'Taffy3': 1, 'Taffy4': 1, 'Taffy5': 0.5, 'Taffy6': 0.8, 'Taffy7': 0.8, 'Taffy8': 0.8, 'Taffy9': 0.8}

t3bg = {'background': 1}

t4bg = {'background': 1}

t4darkbases = {1: "1"}

t4brightbases = {1: "1"}

basetypes = {"Round": 1, "Cat": 0.75,
             "Bunny": 0.75, "Fluffy": 0.75, "Poop": 0.75}
basetypest3 = {"Round": 1, "Cat": 0.75,
             "Bunny": 0.75, "Fluffy": 0.75, "Poop": 0.75}


brightbases = [t1brightbases, t2brightbases, t3brightbases, t4brightbases]
darkbases = [t1darkbases, t2darkbases, t3darkbases, t4darkbases]
backgrounds = [t1bg, t2bg, t3bg, t4bg]

# TRAIT GENERATION

# how many blobs you want in total
TOTAL_BLOBS = 8078
TEAM_BLOBS = 100
traits = []
shorttraits = []
randids = []
# t3Count = 0
# t2Count = 0
# t1Count = 0
# pizzaCount = 0
# gemCount = 0
# fruitCount = 0
# coralCount = 0
# dessertCount = 0
# sushiCount = 0


def createCombo():
    # empty dictionary to assign new traits to
    trait = {}
    st = {}
    randomid = 0

    # chooses tier
    tier = random.choices([1, 2, 3, 4], [0.8, 1, 0.25, 0])[0]
    trait["Tier"] = tier

    # chooses whether the base will be dark or bright
    if trait["Tier"] == 1:
        darkorbright = random.choices(
            [0, 1], [len(t1darkbases), len(t1brightbases)])[0]
    elif trait["Tier"] == 2:
        darkorbright = random.choices(
            [0, 1], [len(t2darkbases), len(t2brightbases)])[0]
    elif trait["Tier"] == 3:
        darkorbright = random.choices(
            [0, 1], [len(t3darkbases), len(t3brightbases)])[0]
    else:
        darkorbright = 1

    # list() is basically turning the dictionary result into a list so itll work in the random.choices function
    # backgrounds basetypes etc are dictionaries assigned at the beginning, the keys are the names of the images and the values are the weights
    # i have no idea what [0] does but it works so im not changing it

    if darkorbright == 0:
        trait["Face Color"] = "Bright"
        trait["Blob Style"] = random.choices(
            list(darkbases[tier-1].keys()), list(darkbases[tier-1].values()))[0]
        st["Blob Style"] = trait["Blob Style"]
        trait["Face"] = random.choices(
            list(whitefaces.keys()), list(whitefaces.values()))[0]
        for facearray, newface in similarfaces.items():
            if trait["Face"] in facearray:
                st["Face"] = newface
        if "Face" not in st:
            st["Face"] = trait["Face"]
        trait["Shape"] = random.choices(
            list(basetypes.keys()), list(basetypes.values()))[0]
        st["Shape"] = trait["Shape"]
        trait["Background"] = random.choices(
            list(backgrounds[tier-1].keys()), list(backgrounds[tier-1].values()))[0]
        trait["Random ID"] = hex(random.getrandbits(48))[2:-4]
        randomid = trait["Random ID"]
        

        #trait["Points"] = darkandbright[trait["Brightness"]] + basetypes[trait["BaseType"]] + darkbases[trait["Base"]] + whitefaces[trait["Face"]]

    if darkorbright == 1:
        trait["Face Color"] = "Dark"
        trait["Blob Style"] = random.choices(
            list(brightbases[tier-1].keys()), list(brightbases[tier-1].values()))[0]
        st["Blob Style"] = trait["Blob Style"]
        trait["Face"] = random.choices(
            list(blackfaces.keys()), list(blackfaces.values()))[0]
        for facearray, newface in similarfaces.items():
            if trait["Face"] in facearray:
                st["Face"] = newface
        if "Face" not in st:
            st["Face"] = trait["Face"]
        trait["Shape"] = random.choices(
            list(basetypes.keys()), list(basetypes.values()))[0]
        st["Shape"] = trait["Shape"]
        trait["Background"] = random.choices(
            list(backgrounds[tier-1].keys()), list(backgrounds[tier-1].values()))[0]
        trait["Random ID"] = hex(random.getrandbits(48))[2:-4]
        randomid = trait["Random ID"]

        #trait["Points"] = darkandbright[trait["Brightness"]] + basetypes[trait["BaseType"]] + brightbases[trait["Base"]] + blackfaces[trait["Face"]]

    shape = trait["Shape"]
    blobStyle = trait["Blob Style"]
    tier = trait["Tier"]
    faceColor = trait["Face Color"]
    blobColor = "Bright" if faceColor == "Dark" else "Dark"

    # print(trait)
    # checks for duplicate and if so makes a new combo
    if st in shorttraits:
        return createCombo()

    if os.path.exists(f"C:/Users/<Your username>Desktop/blobs/generation/nfts/bases/{shape}/T{tier}/{blobColor}/{blobStyle}.png"):
        return trait, st, randomid
    else:
        return createCombo()


# appends every new trait (dna) to a list called traits
for i in range(TOTAL_BLOBS):
    newtraitcombo, newshorttrait, randomid = createCombo()
    shorttraits.append(newshorttrait)
    traits.append(newtraitcombo)
    randids.append(randomid)

# function which returns true if all traits are unique


def allUnique(x):
    seen = list()
    return not any(i in seen or seen.append(i) for i in x)


print("AllUnique ", allUnique(traits))
print("RandUnique ", allUnique(randids))
time.sleep(5)
# makes a new dictonary to each blob trait and assigns them tokenIds numerically
i = 0
for item in traits:
    item["tokenId"] = (i+TOTAL_BLOBS-TEAM_BLOBS) % (TOTAL_BLOBS)
    item["ID"] = i
    i = i + 1

oneoutofoneIDs = {random.randint(0, TOTAL_BLOBS-1): "Sketch", random.randint(0, TOTAL_BLOBS-1): "Doodle", random.randint(0, TOTAL_BLOBS-1): "Babiest Blob", random.randint(0, TOTAL_BLOBS-1): "Chalkboard", random.randint(
    0, TOTAL_BLOBS-1): 'Watercolor', random.randint(0, TOTAL_BLOBS-1): 'Hawaii', random.randint(0, TOTAL_BLOBS-1): 'Upside Down', 0: 'FTXUS', 1: 'Candy Machine', 2: 'Cyberpunk', 3: 'Fox', 4: 'FTX', 5: 'Bunny', 6: 'Iceberg', 7: 'Loops', 8: 'Miku', 9: 'Monkey', 10: 'Solflare', 11: 'Bloodie', 12: 'stegaBOB', 13: 'Sway', 14: 'Ponjinge',15:'Cupid', 16:'Red Panda'}

#oneoutofoneIDs = {15: "Sketch", 16: "Doodle", 17: "Babiest Blob", 18: "Chalkboard", 19: 'Watercolor', 20: 'Hawaii', 21: 'Upside Down', 0: 'Bunny', 1: 'Candy Machine', 2: 'Cyberpunk', 3: 'Fox', 4: 'FTX', 5: 'FTXUS', 6: 'Icebergy', 7: 'Loopify', 8: 'Miku', 9: 'Monkey', 10: 'Solflare', 11: 'Bloodie', 12: 'stegaBOB', 13: 'Sway', 14: 'Ponjinge'}

t3keys = {}
t3keys["Pizza"] = ['Margherita Pizza', 'Olive Mushroom Pizza',
                   'Pepper Mushroom Pizza', 'Pepperoni Onion Pizza', 'Pepperoni Pizza', 'Veggie Pizza']
t3keys["Sushi"] = ['Ebi', 'Hamachi', 'Hirame', 'Hokkigai', 'Ika',
                   'Kani', 'Onigiri', 'Tai', 'Tako', 'Tamago', 'Unagi', 'Saba']
t3keys["Drink"] = ['Cherry Soda', 'Cola Soda', 'Grape Soda', 'Boba Tea',
                   'Kiwi Soda', 'Orange Soda', 'Raspberry Soda',  'Soda Water']
t3keys["Gemstone"] = ['Black Diamond', 'Amethyst', 'Blue Sapphire', 'Blue Topaz',
                      'Citrine', 'Diamond', 'Emerald', 'Yellow Topaz', 'Ruby', 'Peridot', 'Pink Tourmaline']
t3keys["Dessert"] = ['Chocolate Drizzle', 'Chocolate Sprinkles', 'Strawberry Drizzle',
                     'Strawberry Sprinkles',  'Vanilla Drizzle', 'Vanilla Sprinkles']
t3keys["Fruit"] = ['Apple', 'Cherry', 'Pineapple', 'Watermelon', 'Strawberry']
t3keys["Coral"] = ['Closed Brain Coral', 'Grooved Brain Coral',
                   'Pink Bubble Coral', 'Purple Tube Sponge', 'Orange Foliaceous Coral']
t3keys["Galaxy"] = ['Deep Space', 'Purple Eclipse', 'Extraterrestrial Cosmos', 'Gold Solar Flare',
                    'Milky Way Sky', 'Red Nebula', 'Silver Comet', 'Turquoise Meteor', 'Pink Supernova']


for trait in traits:
    if trait['ID'] == 17:
        trait["Tier"]= 3
        trait["Face Color"]= "Dark"
        trait["Blob Style"]= "Pepperoni Onion Pizza"
        trait["Face"]= "Squee"
        trait["Shape"]= "Bunny"
        trait["Background"]= "Pizza"
    elif trait['ID'] == 18:
        trait["Tier"]= 3
        trait["Face Color"]= "Dark"
        trait["Blob Style"]= "Blue Topaz"
        trait["Face"]= "Hypnotized"
        trait["Shape"]= "Poop"
        trait["Background"]= "Gemstone"
    elif trait['ID'] == 19:
        trait["Tier"]= 3
        trait["Face Color"]= "Dark"
        trait["Blob Style"]= "Saba"
        trait["Face"]= "Wink Laugh"
        trait["Shape"]= "Round"
        trait["Background"]= "Sushi"
    for oneononeid, oneononename in oneoutofoneIDs.items():
        if trait["ID"] == oneononeid:
            trait["Face Color"] = oneononename
            trait["Blob Style"] = oneononename
            trait["Face"] = oneononename
            trait["Shape"] = oneononename
            trait["Background"] = oneononename
            trait["Tier"] = 4
    # tier 3 stuff
    if trait["Tier"] == 3:
        if trait["Blob Style"] in t3keys["Pizza"]:
            trait["Background"] = "Pizza"
        elif trait["Blob Style"] in t3keys["Sushi"]:
            trait["Background"] = "Sushi"
        elif trait["Blob Style"] in t3keys["Drink"]:
            trait["Background"] = "Drink"
        elif trait["Blob Style"] in t3keys["Gemstone"]:
            trait["Background"] = "Gemstone"
        elif trait["Blob Style"] in t3keys["Dessert"]:
            trait["Background"] = "Dessert"
        elif trait["Blob Style"] in t3keys["Fruit"]:
            trait["Background"] = "Fruit"
        elif trait["Blob Style"] in t3keys["Galaxy"]:
            trait["Background"] = "Galaxy"
        elif trait["Blob Style"] in t3keys["Coral"]:
            trait["Background"] = "Coral"


# WRITE METADATA TO JSON FILE




def renderer(item):
    # if os.path.exists(f"C:/Users/<Your username>Desktop/blobs/generation/nfts/images-id/{item['tokenId']}.png"):
    if os.path.exists(f"C:/Users/<Your username>Desktop/blobs/generation/nfts/images-hex/{item['Random ID']}.png"):
        # if False:
        return 1
    else:
        # size of image
        area = (0, 0, 2000, 2000)

        background = item["Background"]

        shape = item["Shape"]
        faceColor = item["Face Color"]
        blobColor = "Bright" if faceColor == "Dark" else "Dark"
        blobStyle = item["Blob Style"]
        face = item["Face"]
        tier = item["Tier"]
        tokenId = item["tokenId"]
        randomID = item["Random ID"]
        ID = item["ID"]

        _base = Image.open(
            f"C:/Users/<Your username>Desktop/blobs/generation/nfts/bases/{shape}/T{tier}/{blobColor}/{blobStyle}.png").convert('RGBA')

        if tier == 3:
            _background = Image.open(
                f"C:/Users/<Your username>Desktop/blobs/generation/nfts/backgrounds/T3/{background}Bg.png").convert('RGBA')
        else:
            _background = Image.open(
                f"C:/Users/<Your username>Desktop/blobs/generation/nfts/backgrounds/T{tier}/{background}.png").convert('RGBA')

        _face = Image.open(
            f"C:/Users/<Your username>Desktop/blobs/generation/nfts/faces/{faceColor}/{face}.png").convert('RGBA')

        output = _background.copy()
        output.paste(_base, area, _base)
        output.paste(_face, area, _face)
        if os.path.exists(f"C:/Users/<Your username>Desktop/blobs/generation/nfts/backgrounds/T{tier}/{background}Fg.png"):
            _foreground = Image.open(
                f"C:/Users/<Your username>Desktop/blobs/generation/nfts/backgrounds/T{tier}/{background}Fg.png").convert('RGBA')
            output.paste(_foreground, area, _foreground)
        #output.save(
         #   f"C:/Users/<Your username>Desktop/blobs/generation/nfts/images-sorted/T{tier}-{blobStyle}-{shape}-{face}-{tokenId}.png")
        output.save(
            f"C:/Users/<Your username>Desktop/blobs/generation/nfts/images-hex/{randomID}.png")
        '''
        output2 = _base.copy()
        output2.paste(_face,area,_face)
        output2.save(f"C:/Users/<Your username>Desktop/blobs/generation/nfts/html/bases/{randomID}.png")

        output3 = _background.copy()
        output3.save(f"C:/Users/<Your username>Desktop/blobs/generation/nfts/html/backgrounds/{randomID}.png")

        if os.path.exists(f"C:/Users/<Your username>Desktop/blobs/generation/nfts/backgrounds/{tier}/fg/{background}.png"):
            _foreground = Image.open(f"C:/Users/<Your username>Desktop/blobs/generation/nfts/backgrounds/{tier}/{background}Fg.png").convert('RGBA')
            output4 = _foreground.copy()
            output4.save(f"C:/Users/<Your username>Desktop/blobs/generation/nfts/html/foregrounds/{randomID}.png")
        print(tokenId)
        '''


def oneofsrenderer(item):

    area = (0, 0, 2000, 2000)

    background = item["Background"]
    blobStyle = item["Blob Style"]
    tokenId = item["tokenId"]
    randomID = item["Random ID"]
    ID = item["ID"]
    _base = Image.open(
        f"C:/Users/<Your username>Desktop/blobs/generation/nfts/1-1/bases/{blobStyle}.png").convert('RGBA')
    _background = Image.open(
        f"C:/Users/<Your username>Desktop/blobs/generation/nfts/1-1/backgrounds/{blobStyle}.png").convert('RGBA')
    _face = Image.open(
        f"C:/Users/<Your username>Desktop/blobs/generation/nfts/1-1/faces/{blobStyle}.png").convert('RGBA')

    output = _background.copy()
    output.paste(_base, area, _base)
    output.paste(_face, area, _face)
    if os.path.exists(f"C:/Users/<Your username>Desktop/blobs/generation/nfts/1-1/foregrounds/{blobStyle}.png"):
        _foreground = Image.open(
            f"C:/Users/<Your username>Desktop/blobs/generation/nfts/1-1/foregrounds/{blobStyle}.png").convert('RGBA')
        output.paste(_foreground, area, _foreground)
    #output.save(
     #   f"C:/Users/<Your username>Desktop/blobs/generation/nfts/images-sorted/T4-{blobStyle}-{tokenId}.png")
    output.save(
        f"C:/Users/<Your username>Desktop/blobs/generation/nfts/images-hex/{randomID}.png")
    output.save(
        f"C:/Users/<Your username>Desktop/blobs/generation/nfts/ones/{ID}.png")

    '''
    output2 = _base.copy()
    output2.save(f"C:/Users/<Your username>Desktop/blobs/generation/nfts/html/bases/{randomID}.png")
    output3 = _background.copy()
    output3.save(f"C:/Users/<Your username>Desktop/blobs/generation/nfts/html/backgrounds/{randomID}.png")
    print(tokenId)
    '''


# multi processing to render all the blobs faster, not sure how it works exactly just cobbled it together from stack overflow

pool_size = 100  # your "parallelness"

pool = Pool(pool_size)

"""
try:
    for item in traits:
        pool.apply_async(renderer, ([item]))
        #renderer(item)
except Exception as e: print(e)

try:
    for item in range(0, TOTAL_BLOBS):
        pool.apply_async(renderer, ([traits[item]]))
        # renderer(traits[item])
        print(item)
except Exception as e:
    print(e)
"""

pool.close()
pool.join()

for item in oneoutofoneIDs:
    oneofsrenderer(traits[item])

with open('C:/Users/<Your username>Desktop/blobs/generation/nfts/combined-raw.json', 'w') as outfile:
    json.dump(traits, outfile, indent=4)
