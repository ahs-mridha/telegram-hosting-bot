from PIL import Image

def enhance(path):

    img = Image.open(path)

    img = img.resize(
        (img.width*2,img.height*2),
        Image.LANCZOS
    )

    output = path.replace(".jpg","_enhanced.jpg")

    img.save(output)

    return output