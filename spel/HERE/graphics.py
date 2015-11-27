import pygame
import os
#-------------------------------------------------------------------------------
# graphics.py
#
#-------------------------------------------------------------------------------

main_dir = os.path.split(os.path.abspath(__file__))[0]

#-------------------------------------------------------------------------------
# Load images from the graphics folder.
#-------------------------------------------------------------------------------
def load_image(file):
    """Load image from the graphics folder and optimize them for play"""
    file = os.path.join(main_dir, 'graphics', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert_alpha()

# The player model
playerbase = load_image("Human1.png")

