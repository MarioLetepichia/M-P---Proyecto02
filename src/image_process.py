from PIL import Image
import io


def read_file(data):
    """Process file

    Parameters
    ----------
    file_png : data

    Returns
    -------
    byte of arrays
    """

    try:
        im = Image.open('docs/4.png')

    except:
        print('Skipping unreadable image foo.png')

    # resize the image
    img = im.resize((300, 300)) 
    byteIO = io.BytesIO()
    img.save(byteIO, format='PNG')
    byteArr = byteIO.getvalue()
    return byteArr
