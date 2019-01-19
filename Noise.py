import noise
import numpy as np

def getNoise(shape = (1024,1024),scale = 100.0,octaves = 6,persistence = 0.5,lacunarity = 2.0):

    world = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = noise.pnoise2(i/scale,
                                        j/scale,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=shape[0],
                                        repeaty=shape[1],
                                        base=0)
    return world
