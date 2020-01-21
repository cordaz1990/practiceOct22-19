from typing import TextIO, Dict
from io import StringIO

def count_birds(observations_file: TextIO) -. Dict[str, int]:
      """ Returna set of the bird species listed in obsevations_file, which has one bird spacies per line.
      
      >>> infile = StringIO('bird 1\\nbird 2\\nbird 1\\n')
      >>> count_birds(infile)
      {'bird 1':2, 'bird 2':1}
      
      bird_to_observations = {}
      for line in observations_file:
            bird = line.strip()
            if bird in bird_to_observations:
                  bird_to_observations[bird] = bird_to_observations[bird] + 1
                  
      else:
           bird_to_observations[bird] = 1
      
      return bird_to_observations
      
if__name__ == "__main__':
      with open('observations.txt') as observatins_file:
      bird_to_observations = count_birds(observations_file)
      for bird, observations in bird_to_observations.items():
            print(bird, observations)
