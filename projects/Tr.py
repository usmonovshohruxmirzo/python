# Hexadecimal data provided
hex_data = '''
00010000 10001000 0100100E 00100000 100000E0 E0000000 00000E00 0E001000 0000E000 00E00000
010E0010 000E0000 00E00001 0000E000 0EEEEEEE EEEEEE00 00100000 00000000 00000010 00100000
'''

# Remove spaces and newlines
hex_data = hex_data.replace(' ', '').replace('\n', '')

# Convert the hex data to binary data, each hex digit becomes 4 bits
binary_data = ''.join([bin(int(c, 16))[2:].zfill(4) for c in hex_data])

# Convert binary data to 4-bit greyscale values
pixels = [int(binary_data[i:i+4], 2) for i in range(0, len(binary_data), 4)]

# Image dimensions
rows = 10
cols = 16

# Reshape the pixel values into a 10x16 array
image_array = np.array(pixels).reshape((rows, cols))

# Plot the image
plt.figure(figsize=(6, 6))
plt.imshow(image_array, cmap='gray', vmin=0, vmax=15)
plt.axis('off')  # Hide axes
plt.show()
