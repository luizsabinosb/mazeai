def coordenada_para_pixel(i, j, cell_size):
    return j * cell_size, i * cell_size

def pixel_para_coordenada(x, y, cell_size):
    return y // cell_size, x // cell_size
