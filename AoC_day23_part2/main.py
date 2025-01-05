from collections import defaultdict
nodeList = []
def dfs(currNode , graph , prevNodes , vis):
    global nodeList
    nodeList.append(prevNodes)
    vis[currNode] = True
    for node in graph[currNode]:
        if not vis[node]:
            flag = True
            for x in prevNodes:
                if node not in graph[x]:
                    flag = False
            if not flag:
                continue
            prevNodes.append(node)
            dfs(node , graph , prevNodes , vis )
    #vis[currNode] = False
    return

def main():
    graph = defaultdict(list)
    allNodes = set()
    with open("input.txt") as file:
        content = file.readlines()
    for line in content:
        nodes = line.strip().split('-')
        graph[nodes[0]].append(nodes[1])
        graph[nodes[1]].append(nodes[0])
        allNodes.add(nodes[1])
        allNodes.add(nodes[0])
    vis = defaultdict(bool)

    for x in allNodes:
        vis = defaultdict(bool)
        dfs(x , graph, [] , vis)

    mxList = []
    for lst in nodeList:
        if len(lst)>len(mxList):
            mxList = lst
    mxList.sort()
    print(','.join(map(str,mxList)))

if __name__=='__main__':
    main()

