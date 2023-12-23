import requests
from io import BytesIO
from PIL import Image
import numpy as np
import replicate
import os

api_key = "r8_XaccnuBGobrkwLrfp6ObIpFyX3yz8jn0LipPL"
os.environ["REPLICATE_API_TOKEN"] = api_key

def load_image(url):
    response = requests.get(url)
    img_data = BytesIO(response.content)

    pil_image = Image.open(img_data)

    img = np.array(pil_image)
    return img

def refine_image(url):
    output = replicate.run(
        "sczhou/codeformer:7de2ea26c616d5bf2245ad0d5e24f0ff9a6204578a5c876db53142edd9d2cd56",
        input={
            "image": url,
        }
    )
    return output