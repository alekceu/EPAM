import copy
import mod_labirint
import mod_ai

mod_labirint.labirint = copy.deepcopy(mod_labirint.labirint_source)
mod_labirint.get_all_graph_top()
mod_labirint.create_matrix_adjacency()
print("====================================")
mod_labirint.algoritm_deustrikti(5,3)
#mod_ai.AI(5,3)