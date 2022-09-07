import pygame

from os import walk


def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):

        for img_file in img_files:
            full_path = f"{path}/{img_file}"
            print(full_path)
            image_surf = pygame.image.load(full_path).convert_alpha()
            # print(full_path)

            surface_list.append(image_surf)

    return surface_list
