
from time import sleep
import copy
import labirint
import ai

move_history = []
all_graph_top = []
matrix_adjacency = []
labirint = []

labirint = copy.deepcopy(labirint.labirint_source)
ai.AI(5,3)