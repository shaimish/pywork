# Import numpy
import numpy as np


# heights and positions are available as lists

positions = ['GK', 'M', 'A', 'D']
heights = [191, 184, 185, 180]


# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

gk_heights = np_heights[np_positions == 'GK']
print ("gk-hights -->" + str(gk_heights))

other_heights = np_heights[np_positions != 'GK']
other_heights

gk = np.median(gk_heights)
ngk = np.median(other_heights)

# Heights of the goalkeepers: gk_heights


# Heights of the other players: other_heights


# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(gk))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(ngk))