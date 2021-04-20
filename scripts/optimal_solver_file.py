import networkx as nx
from pathlib import Path
from typing import List
import qtensor
import fire


def main(file: Path):
    with open(file) as f:
        lines = f.readlines()
    V, E = [int(x.strip()) for x in lines[0].split(' ')]
    G = nx.Graph()
    ints = [
        [int(x.strip()) for x in line.split(' ')]
        for line in lines[1:]
    ]
    G.add_edges_from((i, j) for i,j,w in ints)
    G = nx.convert_node_labels_to_integers(G)

    cost, state = qtensor.tools.maxcut.maxcut_optimal(G)
    print('Optimal cost', cost)


if __name__=="__main__":
    fire.Fire(main)
