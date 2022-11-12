import os
import PIL.ImageOps
import PIL.Image
import numpy as np


class Image2AsciiConverter():

    def __init__(self) -> None:
        """
        A simple class for converting an image to an ascii image.
        """

        super(Image2AsciiConverter, self).__init__()

        self.intensityChars = Image2AsciiConverter.getIntensityChars()

        self.img_array = None

    @staticmethod
    def getIntensityChars() -> str:
        """
            A static method for getting the set of intensity characters.
            
            Returns:
            - the set of intensity characters as a string
        """
        return """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """

    def read_image(self, path: str, show_image=False, invertFlag=False, target_size: tuple = None) -> None:
        """
        A method that loads an image from a path, converts it to grayscale, resizes it and inverts it if 
        specified.

        Arguments:
        - path: the path containing the image.
        - show_image: show the image if specified (default value is False)
        - invertFlag: Invert the image if specified (default value is False)
        - target_size: the target size if resize is specified (default value is None - no resize is performed)

        Returns:
        - None for success
        - integer error code of -1, if the image file is not found
        """
        # if the file does not exist return error code -1
        if not os.path.isfile(path):
            return -1

        self.path = path

        # read the image
        with PIL.Image.open(self.path) as img:

            # check if image has P Mode
            if img.mode == "P":

                # convert image to rgba
                img = img.convert('RGBA')

            # check if image is a RGB image
            if img.mode != "L":

                # convert image to grayscale
                img = img.convert('L')

            # if resize is desired
            if target_size is not None:

                # resize image to the desired target size
                img = img.resize(target_size)

            # invert image if desired
            if invertFlag:
                img = PIL.ImageOps.invert(img)

            # show the image if specified
            if show_image:
                img.show()

            # convert image to a numpy array
            self.img_array = np.array(img)

        return None

    def convertImage(self) -> None:
        """
        A method that converts an image (numpy array) to an ascii image.

        Returns:
        - None for success
        - integer error code of -1, if an image is not previously read
        """

        # if an image is not previously read return an error code of -1
        if self.img_array is None:
            print("Please read an image first by executing the read_image method")
            return -1

        # convert the image to an ascii image
        self.ascii_image = ""
        for i in range(self.img_array.shape[0]):
            for j in range(self.img_array.shape[1]):

                # get the pixel value
                pixel_value = self.img_array[i, j]

                # find the corresponding index in the intensity character set
                idx = 255 - pixel_value

                # if the index is out of bounds
                if idx >= len(self.intensityChars):
                    # put a space character
                    ascii_char = " "
                else:
                    # else (it is in bound) put the corresponding intensity character
                    ascii_char = self.intensityChars[idx]

                # append the character to the ascii image
                self.ascii_image += ascii_char

            # put a newline in the end of each row
            self.ascii_image += "\n"

        return None

    def save_ascii_image(self, save_path: str) -> None:
        """
        Method for saving the ascii image to a text file.

        Arguments:
        save_path: The path to save the ascii image.

        Returns:
        - None for success
        """
        with open(save_path, "w") as f:
            print(self.ascii_image, file=f)

        return None
