import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd 
import utils
import get_models_data


models_with_data=get_models_data.get_models_withdata()
Flow_file_path = utils.notebook+'/FlowFromEdge.csv'
data = pd.read_csv(Flow_file_path, delimiter='\t', header=None)
print('hey')
print(models_with_data)
for m in models_with_data:
    G = nx.DiGraph()
    model = m['Model']
    train_data = m['training_data']
    eval_data=m['eval_data']
    tr_meth=m['training_method']
    eval_meth=m['eval_method']
    G.add_edge(model, tr_meth)
    G.add_edge(model,eval_meth)
    G.add_edge(tr_meth,train_data)
    G.add_edge(eval_meth, eval_data)

    for index, row in data.iterrows():
        if row[4] == 'data':
            from_node = row[0]
            to_node = row[2]
            if from_node!=to_node:
                G.add_edge(from_node, to_node)

    # Create a subgraph containing variables related to a given model 
    subgraph = nx.ego_graph(G, model, radius=8, center=True, undirected=False)

    pos = nx.spring_layout(subgraph, seed=42)
    nx.draw(
        subgraph,
        pos,
        with_labels=True,
        node_size=1000,
        node_color='skyblue',
        font_size=10,
        font_color='black',
        font_weight='bold',
        arrows=True,
    )
    plt.title("Subgraph Related to X_train")
    plt.show()




