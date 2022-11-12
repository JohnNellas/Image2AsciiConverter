import argparse
import image2ascii

# parse arguments
parser = argparse.ArgumentParser(
    description='A simple python script for converting an image to an ascii image.')
parser.add_argument("-p", "--imagePath", required=True,
                    type=str, help="Path to the image.")
parser.add_argument("-s", "--savePath", required=True, type=str,
                    help="Path containing the output of the program.")

parser.add_argument("--resizeFlag", required=False,
                    action="store_true", help="Specify if resize is desired.")
parser.add_argument("--noResizeFlag", dest="resizeFlag", required=False,
                    action="store_false", help="Specify if no resize is desired.")
parser.add_argument("--invertFlag", required=False, action="store_true",
                    help="Specify if image invertion is desired.")
parser.add_argument("--noInvertFlag", dest="invertFlag", required=False,
                    action="store_false", help="Specify if no image invertion is desired.")
parser.add_argument("-w", "--targetWidth", required=False,
                    type=int, default=256, help="The target image width ")
parser.add_argument("-g", "--targetHeight", required=False, type=int,
                    default=256, help="The target image height for the image resize.")
args = parser.parse_args()

image_path, save_path = args.imagePath, args.savePath

if args.resizeFlag:
    target_size = (args.targetWidth, args.targetHeight)
else:
    target_size = None

invertFlag = args.invertFlag

# create an image to ascii converter object
converter = image2ascii.Image2AsciiConverter()

# read the specified image
converter.read_image(image_path,
                     show_image=True,
                     invertFlag=invertFlag,
                     target_size=target_size)

# convert image to ascii
converter.convertImage()

# save ascii
converter.save_ascii_image(save_path)
