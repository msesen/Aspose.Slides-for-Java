from asposeslides import Settings
from com.aspose.slides import Presentation
from com.aspose.slides import SaveFormat

from javax import ImageIO
from java.io import File

class Thumbnail:

    def __init__(self):
       
        # Generating a Thumbnail from a Slide
        self.create_thumbnail()

        # Generating a Thumbnail from a Slide with User Defined Dimensions
        self.create_thumbnail_custom_size()

        # Generating a Thumbnail from a Slide in Notes Slides View
        self.create_thumbnail_in_notes_slides_view()

        # Generating a Thumbnail of User Defined Window from a Slide
        self.create_thumbnail_of_user_defined_window()
        
    def create_thumbnail(dataDir):
        
        dataDir = Settings.dataDir + 'WorkingWithSlidesInPresentation/Thumbnail/'    
        
        # Instantiate Presentation class that represents the presentation file
        pres = Presentation(dataDir + 'demo.pptx')

        # Access the first slide
        slide = pres.getSlides().get_Item(0)

        # Create a full scale image
        image = slide.getThumbnail()

        # Save the image to disk in JPEG format
        imageIO = ImageIO

        imageIO.write(image, "jpeg", File(dataDir + "ContentBG_tnail.jpg"))

        print "Created thumbnail, please check the output file." . PHP_EOL

        
    def create_thumbnail_custom_size(dataDir):
        
        # Instantiate Presentation class that represents the presentation file
        pres = Presentation(dataDir + 'demo.pptx')

        # Access the first slide
        slide = pres.getSlides().get_Item(0)

        # User defined dimension
        desired_x = 1200
        desired_y = 800

        # Getting scaled value  of X and Y
        scale_x = (1.0 / java_values(pres.getSlideSize().getSize().getWidth())) * desired_x
        scale_y = (1.0 / java_values(pres.getSlideSize().getSize().getHeight())) * desired_y

        # Create a full scale image
        image = slide.getThumbnail(scale_x, scale_y)

        # Save the image to disk in JPEG format

        imageIO = ImageIO()
        imageIO.write(image, "jpeg", File(dataDir + "ContentBG_tnail.jpg"))

        print "Created thumbnail with custom size, please check the output file.". PHP_EOL
        
    def create_thumbnail_in_notes_slides_view(dataDir):
        
        # Instantiate Presentation class that represents the presentation file
        pres = Presentation(dataDir + 'demo.pptx')

        # Access the first slide
        slide = pres.getSlides().get_Item(0)

        # User defined dimension
        desired_x = 1200
        desired_y = 800

        # Getting scaled value  of X and Y
        scale_x = (1.0 / java_values(pres.getSlideSize().getSize().getWidth())) * desired_x
        scale_y = (1.0 / java_values(pres.getSlideSize().getSize().getHeight())) * desired_y

        # Create a full scale image
        image = slide.getNotesSlide().getThumbnail(scale_x, scale_y)

        # Save the image to disk in JPEG format
        imageIO = ImageIO()
        imageIO.write(image, "jpeg", File(dataDir + "ContentBG_tnail.jpg"))

        print "Created thumbnail in notes slides view, please check the output file." . PHP_EOL
        
    def create_thumbnail_of_user_defined_window(dataDir):
        
        # Instantiate Presentation class that represents the presentation file
        pres = Presentation(dataDir + 'demo.pptx')

        # Access the first slide
        slide = pres.getSlides().get_Item(0)

        # Create a full scale image
        image = slide.getThumbnail(1,1)

        # Getting the image of desired window inside generated slide thumnbnail
        # BufferedImage window = image.getSubimage(windowX, windowY, windowsWidth, windowHeight)
        window_image = image.getSubimage(100, 100, 200, 200)

        # Save the image to disk in JPEG format
        imageIO = ImageIO()
        imageIO.write(image, "jpeg", File(dataDir + "ContentBG_tnail.jpg"))

        print "Created thumbnail of user defined window, please check the output file." . PHP_EOL


if __name__ == '__main__':        
    Thumbnail()