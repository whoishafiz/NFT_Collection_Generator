from PIL import Image 
from IPython.display import display 
import random
import json
import os

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = ["Lilac", "Baby Blue", "Turquoise", "Lime Green", "Yellow", "Fuschia", "Sand", "Cinder", "White", "Noise"]
background_weights = [40, 15, 15, 10, 5, 5, 4, 3, 2, 1]

teeth = ["Normal", "Fangs", "Toothless", "Bugs", "Villain", "Shark", "Braces", "Perfect", "Grills", "Mascot"]
teeth_weights = [40, 15, 15, 10, 5, 5, 4, 3, 2, 1]

species = ["Ape", "Canary", "Turtle", "Brown Bear", "Tiger", "Panther", "Sea Turtle", "Penguin", "Giant Panda", "Albino Ape", "Albino Tiger", "Blastoise", "Blue Finch", "Koopa", "Pink Panther", "Polar Bear"]
species_weights = [34, 15, 15, 10, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1]

eyes = ["Normal", "Cheshire", "Dead", "Tired", "Money", "BTC", "Tears", "Hearts", "Shades", "Glitch"]
eyes_weights = [40, 15, 15, 10, 5, 5, 4, 3, 2, 1]

occupation = ["None", "Traditional", "Hustler", "Athlete", "Officer", "Military", "Engineer", "Business", "Doctor", "Android"]
occupation_weights = [40, 15, 15, 10, 5, 5, 4, 3, 2, 1]

issue = ["None", "Dirty Economy", "Linked Up", "Feeling Microwaved", "Trash Everywhere", "Get Medicated", "Always Rain", "Swisha Weather", "Too Hot", "It's Me"]
issue_weights = [40, 15, 15, 10, 5, 5, 4, 3, 2, 1]

head = ["None", "Scar", "Teardrop", "Beauty Spot", "Hero", "Snake Piercings", "Brain", "Antenna", "Crown", "Wizard"]
head_weights = [40, 15, 15, 10, 5, 5, 4, 3, 2, 1]


#Classify traits

background_files = {
    "Lilac": "b1",
    "Baby Blue": "b2",
    "Turquoise": "b3",
    "Lime Green": "b4",
    "Yellow": "b5",
    "Fuschia": "b6",
    "Sand": "b7",
    "Cinder": "b8",
    "White": "b9",
    "Noise": "b10",
}

teeth_files = {
    "Normal": "t1",
    "Fangs": "t2",
    "Toothless": "t3",
    "Bugs": "t4",
    "Villain": "t5",
    "Shark": "t6",
    "Braces": "t7",
    "Perfect": "t8",
    "Grills": "t9",
    "Mascot": "t10"
}

species_files = {
    "Ape": "s1",
    "Canary": "s2",
    "Turtle": "s3",
    "Brown Bear": "s4",
    "Tiger": "s5",
    "Panther": "s6",
    "Sea Turtle": "s7",
    "Penguin": "s8",
    "Giant Panda": "s9",
    "Albino Ape": "s10",
    "Albino Tiger": "s11",
    "Blastoise": "s12",
    "Blue Finch": "s13",
    "Koopa": "s14",
    "Pink Panther": "s15",
    "Polar Bear": "s16"
}

eyes_files = {
    "Normal": "e1",
    "Cheshire": "e2",
    "Dead": "e3",
    "Tired": "e4",
    "Money": "e5",
    "BTC": "e6",
    "Tears": "e7",
    "Hearts": "e8",
    "Shades": "e9",
    "Glitch": "e10"
}

occupation_files = {
    "None": "o1",
    "Traditional": "o2",
    "Hustler": "o3",
    "Athlete": "o4",
    "Officer" : "o5",
    "Military": "o6",
    "Engineer": "o7",
    "Business": "o8",
    "Doctor": "o9",
    "Android": "o10"
}

issue_files = {
    "None": "i1",
    "Dirty Economy": "i2",
    "Linked Up": "i3",
    "Feeling Microwaved": "i4",
    "Trash Everywhere": "i5",
    "Get Medicated": "i6",
    "Always Rain": "i7",
    "Swisha Weather": "i8",
    "Too Hot": "i9",
    "It's Me": "i10"
}

head_files = {
    "None": "h1",
    "Scar": "h2",
    "Teardrop": "h3",
    "Beauty Spot": "h4",
    "Hero": "h5",
    "Snake Piercings": "h6",
    "Brain": "h7",
    "Antenna": "h8",
    "Crown": "h9",
    "Wizard": "h10"
}


## Generate Traits

TOTAL_IMAGES = 888 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():
    
    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["background"] = random.choices(background, background_weights)[0]
    new_image ["teeth"] = random.choices(teeth, teeth_weights)[0]
    new_image ["species"] = random.choices(species, species_weights)[0]
    new_image ["eyes"] = random.choices(eyes, eyes_weights)[0]
    new_image ["occupation"] = random.choices(occupation, occupation_weights)[0]
    new_image ["issue"] = random.choices(issue, issue_weights)[0]
    new_image ["head"] = random.choices(head, head_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
    
    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)

# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))
# Add token Id to each image
i = 1
for item in all_images:
    item["tokenId"] = i
    i = i + 1


# Get Trait Counts

background_count = {}
for item in background:
    background_count[item] = 0
    
teeth_count = {}
for item in teeth:
    teeth_count[item] = 0

species_count = {}
for item in species:
    species_count[item] = 0
    
eyes_count = {}
for item in eyes:
    eyes_count[item] = 0
    
occupation_count = {}
for item in occupation:
    occupation_count[item] = 0
    
issue_count = {}
for item in issue:
    issue_count[item] = 0
    
head_count = {}
for item in head:
    head_count[item] = 0

for image in all_images:
    background_count[image["background"]] += 1
    teeth_count[image["teeth"]] += 1
    species_count[image["species"]] += 1
    eyes_count[image["eyes"]] += 1
    occupation_count[image["occupation"]] += 1
    issue_count[image["issue"]] += 1
    head_count[image["head"]] += 1

print(background_count)
print(teeth_count)
print(species_count)
print(eyes_count)
print(occupation_count)
print(issue_count)
print(head_count)

#### Generate Images

os.mkdir(f'./images')

for item in all_images:

    im1 = Image.open(f'./Functions/TRAITS/{background_files[item["background"]]}.png').convert('RGBA')
    im2 = Image.open(f'./Functions/TRAITS/{teeth_files[item["teeth"]]}.png').convert('RGBA')
    im3 = Image.open(f'./Functions/TRAITS/{species_files[item["species"]]}.png').convert('RGBA')
    im4 = Image.open(f'./Functions/TRAITS/{eyes_files[item["eyes"]]}.png').convert('RGBA')
    im5 = Image.open(f'./Functions/TRAITS/{occupation_files[item["occupation"]]}.png').convert('RGBA')
    im6 = Image.open(f'./Functions/TRAITS/{issue_files[item["issue"]]}.png').convert('RGBA')
    im7 = Image.open(f'./Functions/TRAITS/{head_files[item["head"]]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)
    com6 = Image.alpha_composite(com5, im7)

                     

    #Convert to RGB
    rgb_im = com6.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)

os.mkdir(f'./metadata')

METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)
    
