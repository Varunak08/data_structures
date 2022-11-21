class Node:
    def __init__(self, id, label, country, longitude, internal, latitude, type):
        self.id = id
        self.label = label
        self.country = country
        self.longitude = longitude
        self.internal = internal
        self.latitude = latitude
        self.type = type

node_fields = {
    0: {'name': 'id', 'type': 'int'},
    1: {'name': 'label', 'type': 'string'},
    2: {'name': 'Country', 'type': 'string'},
    3: {'name': 'Longitude', 'type': 'float'},
    4: {'name': 'Internal', 'type': 'int'},
    5: {'name': 'Latitude', 'type': 'float'},
    6: {'name': 'type', 'type': 'string'},
}

def readNodes(nodes):
    l = 0
    f = open('nodes.txt', 'r')
    currNode = {}
    for line in f:
        if (line.startswith('node') or line.startswith(']')):
            l = 0
            continue
        val = line.split()[1]
        type = node_fields[l]['type']
        field_name = node_fields[l]['name']
        if type == 'int':
            currNode[field_name] = int(val)
        elif type == 'string':
            currNode[field_name] = val.replace("\"", "")
        elif type == 'float':
            currNode[field_name] = float(val)
        l += 1
        if l == 7:
            # Build node
            nodes[currNode['id']] = currNode
            currNode = {}
            l = 0

def buildAdjList(adjList, nodes):
    l = 0
    currEdge = {}
    f = open('edges.txt', 'r')
    for line in f:
        if line.startswith('edge') or line.startswith(']') or line.startswith('LinkLabel'):
            l = 0
            continue
        val = int(line.split()[1])
        if l == 0:
            currEdge['src'] = val 
        if l == 1:
            currEdge['dest'] = val
            src = currEdge['src']
            dest = currEdge['dest']
            if src not in adjList:
                adjList[src] = []
            if nodes[dest] not in adjList[src]:
                adjList[src].append(nodes[dest])
            l = 0
        l += 1

def count_edges(adjList):
    count = 0
    for i in adjList:
        count += len(adjList[i])
    return count

def buildMatrix(adjList, matrix):
    for key in adjList:
        for node in adjList[key]:
            matrix[key][node['id']] = 1

def main():
    nodes = {}
    readNodes(nodes)
    
    adjList = {}
    buildAdjList(adjList, nodes)

    num_nodes = len(nodes)
    num_edges = count_edges(adjList)

    print("NUMBER OF VERTICES: ", num_nodes)
    print("NUMBER OF EDGES: ", num_edges)

    matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    buildMatrix(adjList, matrix)
    

main()
