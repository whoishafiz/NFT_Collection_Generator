
# GRINNER Collection – NFT Generator

Welcome to the official **GRINNER** repository! Supporting open sources projects, this code powers the generation of the unique, algorithmically crafted **GRINNER** NFT collection, now available on [OpenSea](https://opensea.io/collection/grinner/overview).

## 🌐 Collection Links

- 🌊 **[OpenSea Collection](https://opensea.io/collection/grinner/overview)**
- 💬 **[Join Our Discord Community](https://discord.gg/YNyzJkyEN9)**

## 🖼️ About GRINNER

The **GRINNER** collection is a digital art series representing a quirky, vibrant set of characters built using layered visual traits. Each image is generated from a mix of:
- **Backgrounds** 🌈
- **Teeth Styles** 😁
- **Species** 🦁🐼
- **Eye Designs** 👁️
- **Occupations** 🏗️
- **Social Issues** 🌎
- **Head Accessories** 👑

 It serves as an initiative to raise awareness on global issues & accelerating solutions through channeling acquired funds towards sustainable development. The developed characters and its traits are themed around endangered species and global issues to help raise awareness. The collection was created by an single entrepreneur. With a total of 76 different digitally drawn traits fed into a weighted RNG algorithm, every GRINNER artwork is unique.

## 📜 How the Generator Works

This Python script:
- Randomly combines traits for **888 unique images**, weighted by rarity factors.
- Ensures every image is unique with no duplicates.
- Merges transparent PNG layers to compose each final artwork.
- Generates a JSON metadata file (`all-traits.json`) for potential blockchain integration.

The final images and metadata are stored in:
```
./images/
./metadata/
```

## 🏗️ Usage Instructions

1. Ensure you have Python 3.x and `PIL` (Pillow) installed.
2. Place the required trait images in `./Functions/GRINNER/` (PNG format with transparency).
3. Run the script:
```bash
python GRINNER.py
```
4. Generated images will appear in `./images/`, and metadata in `./metadata/`.

## 🔥 Join the Movement

The **GRINNER** collection is not just art—it’s a commentary on the modern world’s chaos, beauty, and contradictions. In an era characterized by the thriving presence of artificial intelligence, capable of generating information and content at an unprecedented pace, much of which is often regarded as superfluous and irrelevant to the majority, the act of ignoring has become second nature as a coping mechanism to deal with this information overflow. Consequently, the ignorance also makes it increasingly challenging to distinguish the value of human-made creations and its implications (whether it is a positive or bad influence).

With the incorporation of present technology and trends, GRINNER was engineered as a movement against the problem by presenting itself as a digital artwork, that also functions as a utility to network and expedite solutions within the web3.0 space. The design and dynamics of the collection aims to remain active and relevant by putting emphasis on what really matters, achieving sustainability.

- Show off your **GRINNER** NFTs online 🌐
- Connect with fellow collectors on **[Discord](https://discord.gg/YNyzJkyEN9)** 💬
- Support and spread the movement by sharing your favorite **GRINNERs** 📢
