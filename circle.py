import io
import urllib.request
from PIL import Image
from PIL import ImageDraw

icon_path = io.BytesIO(urllib.request.urlopen("https://pbs.twimg.com/profile_images/1021820533946499072/bfHxPQ39_400x400.jpg").read())
img = Image.open(icon_path)
offset = 0

mask = Image.new("L", img.size)
draw = ImageDraw.Draw(mask)
draw.ellipse([(offset, offset), (img.size[0] - offset, img.size[1] - offset)], 255)
del draw

img.putalpha(mask)

img.save("icon_circle.png")