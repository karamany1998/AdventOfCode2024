from collections import defaultdict

dx = [0 , 0, -1 , 1]
dy = [-1 , 1 , 0 , 0 ]

trailSet = set()
def dfs(graph , vis , i , j ):
    global cnt
    global trailSet

    if int(graph[i][j]) == 9:
        trailSet.add((i,j))
        return

    for ch in range(0 , 4):
        newX = i + dx[ch]
        newY = j + dy[ch]

        if vis[(newX , newY ,i , j)]:
            continue
        if newX>= len(graph) or newX<0 or newY>=len(graph[0]) or newY<0:
            continue


        if int(graph[newX][newY]) - int(graph[i][j]) ==1:
            vis[(newX , newY ,i ,j)] = True
            dfs(graph , vis , newX , newY )






def main():
    line = ''
    graph = []
    cnt = 0
    global trailSet
    with open('input.txt') as file:
        for line in file:
            #print('------------------------------------------')
            currLine = line
            if line[-1]=='\n':
                currLine = line[:-1]
            curr = list(currLine)
            graph.append(curr)
            #print(curr)

    #print(graph)

    for i in range(0 , len(graph)):
        for j in range(0 , len(graph[0])):
            if int(graph[i][j]) == 0:
                vis = defaultdict(bool)
                vis[(0, 0, 0,0)] = True
                dfs(graph , vis , i , j )
                cnt += len(trailSet)
                trailSet = set()

    print(cnt)





if __name__=='__main__':
    main()