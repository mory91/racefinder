import numpy as np
import json
import random
from align import AlignDlib
from pprint import pprint

alignment = AlignDlib('models/landmarks.dat')

def triplet_generator():
    with open('result.json') as f:
        data = json.load(f)
    race = [[],[],[],[],[]]

    for key, value in data.items():
        if int(file[4:].split('_')[2]) == 0 :
            race[0].append(value['file'])
        elif int(file[4:].split('_')[2]) == 1 :
            race[1].append(value['file'])
        elif int(file[4:].split('_')[2]) == 2 :
            race[2].append(value['file'])
        elif int(file[4:].split('_')[2]) == 3 :
            race[3].append(value['file'])
        elif int(file[4:].split('_')[2]) == 4 :
            race[4].append(value['file']) 

    while True:
        triplets_a = []
        triplets_n = []
        triplets_p = []
        for i in range(4)
            choices = [0,1,2,3,4]
            rand_race = random.choice (choices)
            choices.remove(rand_race)
            rand_n_race = random.choice (choices)
            rand_a = random.choice (race[random_race])
            rand_p = random.choice (race[random_race])
            rand_n = random.choice (race[random_n_race])
            triplets_a.append(resize96(rand_a))
            triplets_p.append(resize96(rand_p))
            triplets_n.append(resize96(rand_n))

        yield [np.array(triplets_a) , np.array(triplets_p), np.array(triplets_n)], None
def resize96 (path):
    jc_orig = load_image(path)
    bb = alignment.getLargestFaceBoundingBox(jc_orig)
    jc_aligned = alignment.align(96, jc_orig, bb, landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)
    return jc_aligned