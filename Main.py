from queue import PriorityQueue


class Graph:
    def __init__(self):
        self.NodesNumber = int(input("Enter the number of nodes\n"))
        self.MyGraph = []
        for i in range(self.NodesNumber):
            self.MyGraph.append([])

        NodeEdges = input().split(",")

        while NodeEdges[0] != "END":
            FirstEntry = NodeEdges[0].split(" ")
            StartNode = int(FirstEntry[0])
            CurrentEdge = FirstEntry[1].split(":")
            NodeEdges.remove(NodeEdges[0])
            self.MyGraph[StartNode].append((int(CurrentEdge[1]), int(CurrentEdge[0])))
            self.MyGraph[int(CurrentEdge[0])].append((int(CurrentEdge[1]), StartNode))
            for Edge in NodeEdges:
                CurrentEdge = Edge.split(":")
                self.MyGraph[StartNode].append((int(CurrentEdge[1]), int(CurrentEdge[0])))
                self.MyGraph[int(CurrentEdge[0])].append((int(CurrentEdge[1]), StartNode))

            NodeEdges = input().split(",")

    def SelectAlgorithm(self, Info):
        Info = Info.split(" ")
        if Info[0] == "Dijkstra":
            return self.Dijkstra(int(Info[1]), int(Info[2]))
        elif Info[0] == "A*":
            return self.AStarPlatinum(int(Info[1]), int(Info[2]))

    def Dijkstra(self, StartNode, TargetNode):
        Distance = []
        Parent = []
        MaxInt = 10e7
        for i in range(self.NodesNumber):
            Distance.append(MaxInt)
            Parent.append(-1)

        MyQueue = PriorityQueue()
        Distance[StartNode] = 0
        MyQueue.put((0, StartNode))

        while not MyQueue.empty():
            CurrentNode = MyQueue.get()
            for AdjacentNode in self.MyGraph[CurrentNode[1]]:
                if Distance[AdjacentNode[1]] > Distance[CurrentNode[1]] + AdjacentNode[0]:
                    Distance[AdjacentNode[1]] = Distance[CurrentNode[1]] + AdjacentNode[0]
                    Parent[AdjacentNode[1]] = CurrentNode[1]
                    MyQueue.put((AdjacentNode[0], AdjacentNode[1]))

        Path = str(TargetNode)
        CurrentParent = Parent[TargetNode]
        while CurrentParent != -1:
            Path = str(CurrentParent) + "->" + Path
            CurrentParent = Parent[CurrentParent]

        print(Path)
        return Distance[TargetNode]

    def AStarPlatinum(self, StartNode, TargetNode):
        Distance = []
        Parent = []
        HeuristicString = input("Enter the heuristic for each node\n").split(",")
        Heuristic = []
        MaxInt = 10e7
        for i in range(self.NodesNumber):
            Distance.append(MaxInt)
            Parent.append(-1)
            Heuristic.append(int(HeuristicString[i]))

        MyQueue = PriorityQueue()
        Distance[StartNode] = 0
        MyQueue.put((Heuristic[StartNode], StartNode))

        while not MyQueue.empty():
            CurrentNode = MyQueue.get()
            for AdjacentNode in self.MyGraph[CurrentNode[1]]:
                if Distance[AdjacentNode[1]] > Distance[CurrentNode[1]] + AdjacentNode[0]:
                    Distance[AdjacentNode[1]] = Distance[CurrentNode[1]] + AdjacentNode[0]
                    Parent[AdjacentNode[1]] = CurrentNode[1]
                    MyQueue.put((AdjacentNode[0] + Heuristic[AdjacentNode[1]], AdjacentNode[1]))

        Path = str(TargetNode)
        CurrentParent = Parent[TargetNode]
        while CurrentParent != -1:
            Path = str(CurrentParent) + "->" + Path
            CurrentParent = Parent[CurrentParent]

        print(Path)
        return Distance[TargetNode]


NewGraph = Graph()
print(NewGraph.SelectAlgorithm(input("Enter the algorithm name then from and to\n")))
