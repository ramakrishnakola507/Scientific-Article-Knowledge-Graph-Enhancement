from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "12345678")

driver = GraphDatabase.driver(URI, auth=AUTH)

queries = {
    "All Nodes": "MATCH (n) RETURN n",
    "Author → Paper": "MATCH (a:Author)-[:WROTE]->(p) RETURN a,p",
    "Methods Used": "MATCH (p:Paper)-[:USES_METHOD]->(m) RETURN p,m",
    "Results": "MATCH (p:Paper)-[:HAS_RESULT]->(r) RETURN p,r",
    "Citations": "MATCH (p1:Paper)-[:CITES]->(p2) RETURN p1,p2"
}

with driver.session() as session:
    for name, q in queries.items():
        result = session.run(q)
        print(f"{name}: {len(list(result))} records")

driver.close()
