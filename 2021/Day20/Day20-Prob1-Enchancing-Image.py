# Puzzle Input ----------
with open('Day20-Input.txt', 'r') as file:
    puzzle = file.read().split('\n\n')

with open('Day20-Test01.txt', 'r') as file:
    test01 = file.read().split('\n\n')


# Main Code ----------

# Get a pixel in the image, or return the default
def get_pixel(x: int, y: int, img: list, default_chr: str):
    img_size = len(img)
    if x < 0 or y < 0 or x >= img_size or y >= img_size:
        return default_chr
    return img[y][x]


# Get the output for a given input coordinate
def get_pixel_output(x: int, y: int, img: list, algorithm: str, default_chr: str):
    binary = []

    # Consider every pixel in the 3 x 3 grid around it, in the right order
    for delta_y in [-1, 0, 1]:
        for delta_x in [-1, 0, 1]:
            input_chr = get_pixel(x + delta_x, y + delta_y, img, default_chr)
            binary += ['0'] if input_chr == '.' else ['1']

    # Convert to binary and get the output pixel
    binary = ''.join(binary)
    return algorithm[int(binary, 2)]


# ENHANCE the image once
def image_enhancement_algorithm(img_input: list, algorithm: str, default_chr='.'):
    # Outputs for when all inputs are light or dark
    all_dark_output = algorithm[0]
    all_light_output = algorithm[511]

    # Save the output image, calculated pixel by pixel
    img_output = ['' for _ in range(len(img_input) + 2)]
    for x in range(-1, len(img_input) + 1):
        for y in range(-1, len(img_input) + 1):
            img_output[y + 1] += get_pixel_output(x, y, img_input, algorithm, default_chr)

    # Update the default character
    # The pixels in the infinite image are either surrounded by . or by #, meaning the binary is either 0 or 511
    if default_chr == '.':
        default_chr = all_dark_output
    else:
        default_chr = all_light_output
    return img_output, default_chr


# ENHANCE the image
def ENHANCE(data: list):
    algorithm, img_input = data
    img_input = img_input.split('\n')

    # Run the enhancement algorithm twice
    default_chr = '.'
    for _ in range(2):
        img_input, default_chr = image_enhancement_algorithm(img_input, algorithm, default_chr)

    # Return the number of light pixels
    return sum(x.count('#') for x in img_input)


# Tests and Solution ----------
print(ENHANCE(test01))
print(ENHANCE(puzzle))
