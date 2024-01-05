from src.settings import main_dir, image_dir, sound_dir


import os
import pygame

pygame.display.init()

def load_image(name, colorkey=1, scale=1):

    fullname = os.path.join(image_dir, name)
    image = pygame.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pygame.transform.scale(image, size)

    image = image.convert()

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)

    return image, image.get_rect()


def load_sound(name):
    fullname = os.path.join(sound_dir, name)

    sound = pygame.mixer.Sound(fullname)

    return sound


def load_all_scores():
    all_scores = []
    file_names = os.listdir(image_dir)
    print(file_names)

    for name in file_names:
        image = load_image(name)
        all_scores.append(image)

    return all_scores

def rename_all_scores():
    file_names = os.listdir(image_dir)

    for name in file_names:
        new_name = 'pattern0' + name[-6:]
        fullname = os.path.join(image_dir, name)
        new_fullname = os.path.join(image_dir, new_name)

        os.rename(fullname, new_fullname)


if __name__ == '__main__':
    rename_all_scores()













