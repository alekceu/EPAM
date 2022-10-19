#Задаем лабирин
import random
from time import sleep



labirint_source = [
    [1, 1, 1, 1, 1, 1 ,1 ],
    [1, 0, 0, 0, 1, 0 ,1 ],
    [1, 0, 1, 0, 0, 0 ,2 ],
    [1, 0, 0, 1, 1, 0 ,1 ],
    [1, 0, 0, 0, 1, 1 ,1 ],
    [1, 0, 1, 0, 0, 0 ,1 ],
    [1, 1, 1, 1, 1, 1 ,1 ]
]

labirint = []
labirint_exit = 0
all_graph_top = []
matrix_adjacency = []
matrix = []
move_history = []
shortest_way = []

# Вывод лабиринта на экран 
def show_labirint():
    global labirint
    for i in range(len(labirint)):
        for j in range(len(labirint[i])):
            print(labirint[i][j], end=' ')
        print()
    sleep(0.5)

# Создать матрицу смежности 
def get_all_graph_top():
    global labirint, all_graph_top, labirint_exit
    for i in range(len(labirint)):
        for j in range(len(labirint[i])):
            local_graph_list = []
            if labirint[i][j] == 0 :
                local_graph_list.append([i,j])
                if labirint[i][j-1] == 0 : #слева
                    local_graph_list.append([i,j-1])
                if labirint[i][j+1] == 0:
                    local_graph_list.append([i,j+1])
                if labirint[i-1][j] == 0:
                    local_graph_list.append([i-1,j])
                if labirint[i+1][j] == 0:
                    local_graph_list.append([i+1,j])
                all_graph_top.append(local_graph_list)
                if labirint[i][j-1] == 2 or labirint[i][j+1] == 2 or labirint[i-1][j] ==2 or labirint[i+1][j]==2:
                    labirint_exit = i

def create_matrix_adjacency():
    global labirint, all_graph_top, matrix_adjacency
    for i in range(len(all_graph_top)):
        local_graph_list = []
        for l in range(len(all_graph_top)):
            local_graph_list.append("0")
        matrix_adjacency.append(local_graph_list)
    

    for i in range(len(all_graph_top)):
        for j in range(len(all_graph_top[i])):
            if j != 0:
                for l in range(len(all_graph_top)):
                    if all_graph_top[i][j][0] == all_graph_top[l][0][0] and all_graph_top[i][j][1] == all_graph_top[l][0][1]:
                        matrix_adjacency[i][l] = 1

    for i in range(len(all_graph_top)):
        for j in range(len(all_graph_top)):
            print(matrix_adjacency[i][j], end=' ')
        print()

def algoritm_deustrikti(x,y):
    global matrix_adjacency, shortest_way, matrix, labirint_exit
    is_exit = 0
    for i in range(len(all_graph_top)):
        if all_graph_top[i][0][0] == x and all_graph_top[i][0][1] == y:
            start_top_point = i
    while is_exit != labirint_exit :
        shortest_way.append(start_top_point)
        local_list = []
        for i in range(len(matrix_adjacency)):
            if len(shortest_way) <= 1:
                if matrix_adjacency[start_top_point][i] == 1:
                    local_list.append(1)
                else:
                    local_list.append(0)
            else:
                if matrix_adjacency[start_top_point][i] == 1:
                    local_list.append(1 + matrix[len(shortest_way)-1][i])
                else:
                    local_list.append(0 + matrix[len(shortest_way)-1][i])
        matrix.append(local_list)
        min = 10000000000000000000000000
        for i in range(len(local_list)):
            if local_list[i] > 0 and min >= local_list[i]:
                min = local_list[i]
        local_next_move = []
        for i in range(len(local_list)):
            if min == local_list[i]:
                local_next_move.append(i)
        next_move = "False"
        while next_move == "False": 
            make_decision = random.choice(local_next_move)
            if make_decision in shortest_way :
                local_next_move.remove(make_decision)
            else:
                start_top_point = make_decision
                next_move = "True"
        is_exit = start_top_point
        print(matrix[len(shortest_way)-1])