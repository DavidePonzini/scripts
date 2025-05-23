#!/usr/bin/env python

from __future__ import annotations

from dav_tools import messages, argument_parser, ArgumentAction

from PIL import Image as pil_Image
from PIL import ImageDraw as pil_ImageDraw


class Image:
    def read_file(image_path: str) -> Image:
        image = pil_Image.open(image_path)
        return Image(image)
    
    def __init__(self, image: pil_Image):
        self.image = image
        
    def print_size(self) -> None:
        messages.info(f'Image size is {self.size}', f'Pixel count: {self.size[0] * self.size[1]}', text_min_len=[30])

    @property
    def size(self) -> tuple[int, int]:
        return self.image.size
    
    def get_resized_x(self, new_y: int):
        x, y = self.size
        return int(x / y * new_y)

    def resize(self, new_y: int) -> Image:
        new_size = (self.get_resized_x(new_y), new_y)

        self.image = self.image.resize(new_size, pil_Image.BOX)
        self.print_size()

        return self
    
    def lower_resolution(self, new_y: int = 0) -> Image:
        if new_y <= 0:
            return self
        
        old_x = self.size[0]
        self.resize(new_y).resize(old_x)

        return self

    def show(self):
        messages.progress('showing image')
        self.image.show()

    def draw_grid(self, new_y):
        if new_y <= 0:
            return
        
        x, y = self.size
        new_x = self.get_resized_x(new_y)
        
        offset_x = int(x / new_x)
        offset_y = int(y / new_y)

        draw = pil_ImageDraw.Draw(self.image)
        for yy in range(y):
            for xx in range(x):
                if xx % offset_x == 0 or yy % offset_y == 0 or xx == x-1 or yy == y-1:
                    draw.point((xx, yy), (255, 255, 255))

        return self
    
    def save(self, filename):
        messages.progress('saving image')
        self.image.save(filename)
        messages.success('image saved')




if __name__ == '__main__':
    argument_parser.add_argument('image', help='input file')
    argument_parser.add_argument('height', nargs='?', help='number of pixels on Y axis. X axis is automatically recalculated to preserve proportions', type=int, default=0)
    argument_parser.add_argument('-g', '--grid', action=ArgumentAction.STORE_TRUE, help='show pixel grid')
    argument_parser.add_argument('-o', '--output', help='save result to file')

    argument_parser.args

    image = Image.read_file(argument_parser.args.image)
    image.print_size()
    
    image.lower_resolution(argument_parser.args.height)
    
    if argument_parser.args.grid:
        image.draw_grid(argument_parser.args.height)

    if argument_parser.args.output is None:
        image.show()
    else:
        image.save(argument_parser.args.output)

    