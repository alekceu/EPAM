#Задаем лабирин
labirint_source = [
    [1, 1, 1, 1, 1, 1 ,1 ],
    [1, 0, 0, 0, 1, 0 ,1 ],
    [1, 0, 1, 0, 0, 0 ,2 ],
    [1, 0, 0, 1, 1, 0 ,1 ],
    [1, 0, 0, 0, 1, 1 ,1 ],
    [1, 0, 1, 0, 0, 0 ,1 ],
    [1, 1, 1, 1, 1, 1 ,1 ]
]

# Вывод лабиринта на экран 
def show_labirint():
    global labirint
    for i in range(len(labirint)):
        for j in range(len(labirint[i])):
            print(labirint[i][j], end=' ')
        print()

# Создать матрицу смежности 
def create_matrix_adjacency():
    global labirint, all_graph_top
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
