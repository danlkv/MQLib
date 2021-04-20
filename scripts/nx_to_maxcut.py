import networkx as nx
from pathlib import Path
from typing import List
import fire

def convert_graph_to_maxcut(G: nx.Graph) -> List[str]:
    """ Assert maxcut with unity coefficients
    Returns:
        lines for the maxcut problem file
    """
    V = G.number_of_nodes()
    E = G.number_of_edges()
    first_line = f'{V} {E}'
    lines = [first_line]
    G = nx.convert_node_labels_to_integers(G, first_label=1)
    for i, j in G.edges:
        lines.append(f"{i} {j} 1")
    return lines


def main(file:Path, N=30, d=3):
    G = nx.random_regular_graph(d, N)
    lines = convert_graph_to_maxcut(G)
    with open(file, 'w+') as f:
        f.writelines('\n'.join(lines))


if __name__=="__main__":
    fire.Fire(main)
