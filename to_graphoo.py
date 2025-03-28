from rdflib import Graph
from pygraphml import GraphMLParser, Graph as PyGraph

# Load RDF file
rdf_graph = Graph()
rdf_graph.parse("asterisksinsports2.rdf", format="xml")  # Adjust the format if needed (e.g., "ttl" for Turtle)

# Create a new GraphML object
graphml_graph = PyGraph()

# Convert RDF triples to GraphML nodes and edges
for subj, pred, obj in rdf_graph:
    # Add nodes for subject and object
    subj_node = graphml_graph.add_node(str(subj))
    obj_node = graphml_graph.add_node(str(obj))
    
    # Add an edge between subject and object with the predicate as label
    graphml_graph.add_edge(subj_node, obj_node, label=str(pred))

# Export to GraphML
parser = GraphMLParser()
parser.write(graphml_graph, "asterisksinsports2.graphml")

print("Conversion complete! The file 'asterisksinsports2.graphml' is ready for use in yEd.")