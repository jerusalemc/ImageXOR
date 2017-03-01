import argparse
import pickle
import random
import os

from PIL import Image, ImageDraw, ImageFont


def pickle_dump_with_filename(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)


def pickle_load_with_filename(filename):
    result = None
    with open(filename, 'rb') as f:
        result = pickle.load(f)
    return result


def get_chars_set(path):
    """
    Expect a text file that each line is a char
    """
    chars = list()
    with open(path) as f:
        for line in f:
            line = "%s" % line
            char = line.split()[0]
            chars.append(char)
    return chars
    # old code for split chars list
    # size = len(chars)
    # random.shuffle(chars)
    # train = chars[0: round(size * 0.6)]
    # val = chars[round(size * 0.6): round(size * 0.8)]
    # test = chars[round(size * 0.8): size]
    # pickle_dump_with_filename(train, 'chars_train')
    # pickle_dump_with_filename(val, 'chars_val')
    # pickle_dump_with_filename(test, 'chars_test')
    # return (train, val, test)


def draw_char_bitmap(ch, num, font, save_dir, canvas_size, x_offset=25, y_offset=25, gray=False):
    image = Image.new("RGB", (canvas_size, canvas_size), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.text((x_offset, y_offset), ch, (0, 0, 0), font=font)
    if gray:
        image = image.convert('L')
    print(f'draw {ch}')
    if num is None:
        image.save(f'{save_dir}/{ch}.png')
    else:
        image.save(f'{save_dir}/{num}.png')


def save_bitmaps(save_dir, chars):
    for i, c in enumerate(chars):
        draw_char_bitmap(c, i, font, save_dir, canvas_size, x_offset, y_offset, gray=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--font', type=str, default='font/simkai.ttf', help='the directory of font')
    parser.add_argument('--ch_lists', type=str, default='characters/top_3000_simplified.txt', help='specify the file contain characters list')
    parser.add_argument('--font_size', type=int, default=100, help="the size of the font")
    parser.add_argument('--canvas_size', type=int, default=128, help='the size of canvas')
    parser.add_argument('--x_offset', type=int, default=15, help='x offset')
    parser.add_argument('--y_offset', type=int, default=15, help='y offset')
    parser.add_argument('--gray', action='store_true', help='output a gray image instead of a color image')
    parser.add_argument('--output_dir', type=str, default='output/top_3000/simkai', help='output directory of font images')
    FLAGS = parser.parse_args()

    font_size = FLAGS.canvas_size
    canvas_size = FLAGS.canvas_size
    chars_file = FLAGS.ch_lists
    x_offset = FLAGS.x_offset
    y_offset = FLAGS.y_offset
    # train, val, test = get_chars_set((char_file))
    # train = pickle_load_with_filename('chars_train')
    # val = pickle_load_with_filename('chars_val')
    # test = pickle_load_with_filename('chars_test')

    font_name = FLAGS.font
    font = ImageFont.truetype(font_name, font_size)

    gray = FLAGS.gray
    output_dir = FLAGS.output_dir

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    chars = get_chars_set(chars_file)

    save_bitmaps(output_dir, chars=chars)

    # save_bitmap('A/train', train)
    # save_bitmap('A/val', val)
    # save_bitmap('A/test', test)
