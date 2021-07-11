#!/usr/bin/env python3
from rdflib import Dataset, Graph
from pathlib import Path

from rdflib.namespace import OWL, RDF, SKOS

# In rdflib/plugins/serializers/turtle.py
#   CHANGE def getQName(self, uri, gen_prefix=True):
#   INTO def getQName(self, uri, gen_prefix=False):


def OWL_Ontology_base(input_file):
    """Get first subject of `rdf:type owl:Ontology`"""
    g = Graph().parse(str(input_file), format=input_file.suffix[1:])

    for subject in g.subjects(predicate=RDF.type, object=OWL.Ontology):
        return subject

    for subject in g.subjects(predicate=RDF.type, object=SKOS.ConceptScheme):
        return subject


def generate_TriG():
    trig = Dataset()

    for input_file in Path("./data/").glob("*.ttl"):
        graph_uri = OWL_Ontology_base(input_file)

        g = trig.graph(graph_uri)
        g.parse(str(input_file), format=input_file.suffix[1:])

    trig.bind("xsd", "http://www.w3.org/2001/XMLSchema#")

    trig.serialize("./data/concat/nta8035.trig", format="trig", encoding="utf-8")


if __name__ == "__main__":
    generate_TriG()
