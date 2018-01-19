import argparse
import os

from PIL import Image, ImageDraw, ImageFont

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--font', type=str, default='font/simkai.ttf', help='input the font name')
    parser.add_argument('--ch', type=str, default='田', help='please input a chinese character')
    parser.add_argument('--font_size', type=int, default=100, help="the size of the font")
    parser.add_argument('--canvas_size', type=int, default=128, help='the size of canvas')
    parser.add_argument('--x_offset', type=int, default=0, help='x offset')
    parser.add_argument('--y_offset', type=int, default=0, help='y offset')
    parser.add_argument('--gray', action='store_true', help='output a gray image instead of a color image')
    parser.add_argument('--output_dir', type=str, default='../input', help='specify the output directory')

    FLAGS = parser.parse_args()
    canvas_size = FLAGS.canvas_size
    font_size = FLAGS.canvas_size
    ch = FLAGS.ch
    font_name = FLAGS.font
    x_offset = FLAGS.x_offset
    y_offset = FLAGS.y_offset
    gray = FLAGS.gray
    output_dir = FLAGS.output_dir

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    print(f'canvas size {canvas_size}')
    print(f'font size {font_size}')

    font = ImageFont.truetype(font_name, font_size)

    image = Image.new("RGB", (canvas_size, canvas_size), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.text((x_offset, y_offset), ch, (0, 0, 0), font=font)
    if gray:
        image = image.convert('L')
    image.save(f'{output_dir}/{ch}.png')
