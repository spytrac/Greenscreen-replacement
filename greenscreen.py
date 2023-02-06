###
### Author: Anuj Dipakkumar Jariwala
### Description: Creating a program that can combine a still image with a
###             background (or fill) image and a green, blue, or red screen.
###             The program will take in 5 inputs from the user, as described
###             in the PA specification. The program will then use the
###             functions named greenscreen_algo, to modify the pixels from
###             the greenscreen image to combine the greenscreen image with
###             the fill image. The program will then use the function named
###             create_image, to create a new image file from the given
###             pixels. 
###

def greenscreen_algo(pixels_gs,pixel_list_b,channel,c_d):
    ''' This function will take in the 3d list of pixels from the greenscreen
    image, the 3d list of pixels from the fill image, the color channel to
    use, and the color channel difference to use. The function will then
    modify the pixels from the greenscreen image to combine the greenscreen
    image with the fill image. Using if statements, the function will check
    if the pixel is green, blue, or red and checks if the defined condition
    is met. If the condition is met, the pixel will be replaced with the
    corresponding pixel from the fill image. The function will then return
    the modified 3d list of pixels from the greenscreen image.
    '''
    
    # pixels_gs: A 3d list. The pixels from the greenscreen image.
    for pixel_line in range(len(pixels_gs)):
        for pixel_key in range(len(pixels_gs[pixel_line])): 
            # using i and j as a variable to make the code more readable
            i = pixel_line
            j = pixel_key
            if (channel == 'r') and \
(int(pixels_gs[i][j][0]) > int(float(pixels_gs[i][j][1])*float(c_d)))\
and (int(pixels_gs[i][j][0]) > int(float(pixels_gs[i][j][2])*float(c_d))):
                for k in range(3):
                    pixels_gs[i][j][k] = pixel_list_b[i][j][k]
            elif (channel == 'g') and\
(int(pixels_gs[i][j][1]) > int(float(pixels_gs[i][j][0])*float(c_d)))\
and (int(pixels_gs[i][j][1]) > int(float(pixels_gs[i][j][2])*float(c_d))):
                for k in range(3):
                    pixels_gs[i][j][k] = pixel_list_b[i][j][k]
            elif (channel == 'b') and \
(int(pixels_gs[i][j][2]) > int(float(pixels_gs[i][j][1])*float(c_d)))\
and (int(pixels_gs[i][j][2]) > int(float(pixels_gs[i][j][0])*float(c_d))):
                for k in range(3):
                    pixels_gs[i][j][k] = pixel_list_b[i][j][k]

def create_image(file_name, file_name_b,pixels_gs):
    ''' Create a new image file from the given pixels.
    By using the write method, this function will write the pixels to a new
    file. The new file will be named file_name.
    file_name: A string. The name of the new file to be created.
    pixels: A 3d list. The pixels to be written to the new file. 
    '''
    size = get_image_dimensions_string(file_name_b)
    # write_file: Using the open function to open the file in write mode by
    #             using the file_name as the argument.
    write_file = open(file_name, 'w')
    write_file.write('P3\n')
    write_file.write(' '.join(size)+'\n')
    write_file.write('255\n')
    for value in pixels_gs:
        for key in value:
            for i in key:
                write_file.write(str(i)+' ')
        write_file.write('\n')
    write_file.close()
    print('Output file written. Exiting.')


def get_image_dimensions_string(file_name):
    '''
    Given the file name for a valid PPM file, this function will return the
    image dimensions as a string. For example, if the image stored in the
    file is 150 pixels wide and 100 pixels tall, this function should return
    the string '150 100'.
    file_name: A string. A PPM file name.
    '''
    # image_file: Using the open function to open the file in read mode by
    #             using the file_name as the argument.
    image_file = open(file_name, 'r')
    image_file.readline()
    return image_file.readline().strip('\n').split(' ')

def load_image_pixels(file_name):
    ''' Load the pixels from the image saved in the file named file_name.
    The pixels will be stored in a 3d list, and the 3d list will be returned.
    Each list in the outer-most list are the rows of pixels.
    Each list within each row represents and individual pixel.
    Each pixels is representd by a list of three ints, which are the RGB values of that pixel.
    '''
    # pixels: A 3d list. The pixels from the image stored in the file named file_name.
    pixels = []
    # image_file: Using the open function to open the file in read mode by
    #             using the file_name as the argument.
    image_file = open(file_name, 'r')
    image_file.readline()
    image_file.readline()
    image_file.readline()
    for line in image_file:
        line = line.strip('\n ')
        rgb_row = line.split(' ')
        # row: A list. A list of pixels.
        row = []
        for i in range(0, len(rgb_row), 3):
            # pixel: A list. A list of 3 ints, representing the RGB values of a pixel.
            pixel = [int(rgb_row[i]), int(rgb_row[i+1]), int(rgb_row[i+2])]
            row.append(pixel)
        pixels.append(row)

    return pixels

def main():
    ''' This function will take in the 5 inputs from the user, as described
    in the PA specification. The function will use the provided
    load_image_pixels functions to load the pixels from the image saved in
    the file named file_name. The function will validate the inputs from the
    user, and if the inputs are valid, the function will call the
    greenscreen_algo function to modify the pixels from the greenscreen
    image to combine the greenscreen image with the fill image.If the inputs 
    are invalid, the function will print an error message and exit.The function
    will then call the create_image function to create a new image file from
    the modified pixels. '''
    # Channel: The color channel to use. This will be a string, either 'r', 'g', or 'b'.
    channel = input('Enter color channel\n')
    if channel not in 'rgb':
        print('Channel must be r, g, or b. Will exit.')
        exit()
    # Color Difference: The color difference to use. This will be a float.
    channel_difference = input('Enter color channel difference\n')
    if int(float(channel_difference)) not in range(1,10):
        print('Invalid channel difference. Will exit.')
        exit()
    # gs_file: The name of the file containing the greenscreen image.
    gs_file = input('Enter greenscreen image file name\n')
    # fi_file: The name of the file containing the fill image.
    fi_file = input('Enter fill image file name\n')
    width_height_gs = get_image_dimensions_string(gs_file)
    width_height_fi = get_image_dimensions_string(fi_file)
    if width_height_gs[0] != width_height_fi[0] and width_height_gs[1] != width_height_fi[1]:
        print('Images not the same size. Will exit.')
        exit()
    # out_file: The name of the file to save the output image to.
    out_file = input('Enter output file name\n')
    pixels_gs = load_image_pixels(gs_file)
    pixels_fi = load_image_pixels(fi_file)
    # Call the greenscreen_algo function to modify the pixels from the
    # greenscreen image to combine the greenscreen image with the fill image.
    greenscreen_algo(pixels_gs,pixels_fi,channel,channel_difference)
    # Call the create_image function to create a new image file from the
    # modified pixels.
    create_image(out_file, gs_file,pixels_gs)

main()

