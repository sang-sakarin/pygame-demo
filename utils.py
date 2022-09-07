import pygame

from os import walk


def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):

        img_files.sort()

        for img_file in img_files:
            full_path = f"{path}/{img_file}"
            image_surf = pygame.image.load(full_path).convert_alpha()

            surface_list.append(image_surf)

    return surface_list
