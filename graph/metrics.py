from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "12345678"

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

def run_metrics():
    with driver.session() as session:
        total_nodes = session.run(
            "MATCH (n) RETURN count(n) AS c"
        ).single()["c"]

        total_edges = session.run(
            "MATCH ()-[r]->() RETURN count(r) AS c"
        ).single()["c"]

        papers = session.run(
            "MATCH (p:Paper) RETURN count(p) AS c"
        ).single()["c"]

        methods = session.run(
            "MATCH (m:Method) RETURN count(m) AS c"
        ).single()["c"]

        results = session.run(
            "MATCH (r:Result) RETURN count(r) AS c"
        ).single()["c"]

    print("\n📊 GRAPH METRICS")
    print("----------------------------")
    print(f"Total Nodes        : {total_nodes}")
    print(f"Total Relationships: {total_edges}")
    print(f"Papers             : {papers}")
    print(f"Methods            : {methods}")
    print(f"Results            : {results}")

    driver.close()

if __name__ == "__main__":
    run_metrics()
