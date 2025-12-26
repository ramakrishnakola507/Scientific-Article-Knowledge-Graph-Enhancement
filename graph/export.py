from neo4j import GraphDatabase
import json

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "12345678"

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

export = {"nodes": [], "relationships": []}

with driver.session() as session:
    nodes = session.run("MATCH (n) RETURN id(n) AS id, labels(n) AS labels, properties(n) AS props")
    for n in nodes:
        export["nodes"].append({
            "id": n["id"],
            "labels": n["labels"],
            "properties": n["props"]
        })

    rels = session.run("""
        MATCH (a)-[r]->(b)
        RETURN type(r) AS type, id(a) AS start, id(b) AS end, properties(r) AS props
    """)
    for r in rels:
        export["relationships"].append({
            "type": r["type"],
            "start": r["start"],
            "end": r["end"],
            "properties": r["props"]
        })

driver.close()

with open("kg_dump.json", "w") as f:
    json.dump(export, f, indent=2)

print("✅ Knowledge Graph exported to kg_dump.json")
