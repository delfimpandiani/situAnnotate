# import rdflib
# from rdflib import Graph, Literal
# from rdflib.namespace import XSD
# from rdflib.plugins.sparql import prepareQuery
#
#

# Replace the following values with the actual entity_ID and label you want to query


#
# # Load the RDF data into a graph
# g = Graph()
# g.parse("knowledge_graph.ttl", format="turtle")  # Replace with your knowledge graph file path
#
# # Define the SPARQL query
# query = prepareQuery(
#     """
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX conceptnet: <http://etna.istc.cnr.it/framester2/conceptnet/5.7.0/c/en/>
# PREFIX : <https://w3id.org/situannotate#>
#     SELECT ?entity_type ?strength ?date ?place ?annotator ?architecture ?dataset
#     WHERE {
#         ?annotation a :Annotation ;
#             :aboutAnnotatedEntity entity_ID ;
#             :annotationWithLexicalEntry ?le ;
#             :isAnnotationInvolvedInSituation ?situation ;
#             :hasAnnotationStrength ?strength .
#
# 	?le rdfs:label label^^xsd:string .
#
#         ?situation :onDate ?date ;
#             :atPlace ?place ;
#             :involvesAnnotator ?annotator ;
#             :involvesDataset ?dataset .
#
#         ?annotator :hasModelArchitecture ?architecture ;
#             :pretrainedOnDataset ?pretrainedDataset .
#
#     	entity_ID a ?entity_type .
#
#         FILTER NOT EXISTS {
#         ?subClass rdfs:subClassOf ?entity_type .
#         entity_ID rdf:type ?subClass.
#         FILTER (?subClass != ?entity_type)
#         }
#     }
#     """
# )
#
# # Execute the query with the specified values
# results = g.query(
#     query,
#     initBindings={
#         "entity_ID": Literal(entity_ID),
#         "label": Literal(label),
#     },
# )

entity_ID = "ARTstract_14978"
label = "Impressionism"

query_results = {
  "head": {
    "vars": [
      "entity_type",
      "strength",
      "date",
      "place",
      "annotator",
      "architecture",
      "dataset"
    ]
  },
  "results": {
    "bindings": [
      {
        "entity_type": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#Image"
        },
        "strength": {
          "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
          "type": "literal",
          "value": "0.6149182915687561"
        },
        "date": {
          "datatype": "http://www.w3.org/2001/XMLSchema#date",
          "type": "literal",
          "value": "2023-06-26"
        },
        "place": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#Italy"
        },
        "annotator": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#oschamp_vit-artworkclassifier"
        },
        "architecture": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#visual_transformer"
        },
        "dataset": {
          "type": "uri",
          "value": "https://w3id.org/situannotate#ARTstract"
        }
      }
    ]
  }
}

# Extract information from the query results
entity_type = query_results['results']['bindings'][0]['entity_type']['value'].split('#')[-1]
strength = query_results['results']['bindings'][0]['strength']['value']
date = query_results['results']['bindings'][0]['date']['value']
place = query_results['results']['bindings'][0]['place']['value'].split('#')[-1]
annotator = query_results['results']['bindings'][0]['annotator']['value'].split('#')[-1]
architecture = query_results['results']['bindings'][0]['architecture']['value'].split('#')[-1]
dataset = query_results['results']['bindings'][0]['dataset']['value'].split('#')[-1]


# Format the output
output = f"{entity_ID} is an {entity_type}. The label '{label}' was used with an annotation strength of {strength}, on {date}, in {place}. This annotation was done by an annotator, called {annotator}. When used for creating this annotation, the model had a {architecture} model architecture and had been pretrained on the {dataset} dataset."
print(output)