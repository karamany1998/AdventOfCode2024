
from collections import defaultdict

nodeList = []
vis = defaultdict(bool)
def dfs(currNode , graph , prevNodes):
    global nodeList
    global vis

    vis[currNode] = True
    for node in graph[currNode]:
        if not vis[node]:
            nodeList.append(node)
            vis[node] = True
            dfs(node , graph )
    return



def main():

    graph = defaultdict(list)
    allNodes = set()
    with open("input.txt") as file:
        content = file.readlines()
    for line in content:
        nodes = line.strip().split('-')
        ##print(nodes)
        graph[nodes[0]].append(nodes[1])
        graph[nodes[1]].append(nodes[0])
        allNodes.add(nodes[1])
        allNodes.add(nodes[0])
    #print(len(graph))
    ans = set()

    for node in allNodes:

        for i in range(0 , len(graph[node])):
            for j in range(i+1 , len(graph[node])):
                node1 = graph[node][i]
                node2 = graph[node][j]

                if node in graph[node1] and node in graph[node2] and node1 in graph[node2] :
                    tup = (node , node1 , node2)
                    sorted_tup = tuple(sorted(tup))
                    ans.add(sorted_tup)

    cnt = 0

    for party in ans:
        if party[0][0]=='t' or party[1][0]=='t' or party[2][0]=='t':
            cnt+=1

    print('cnt is ' , cnt)


    #print(graph)
   #print(ans)




if __name__=='__main__':
    main()

