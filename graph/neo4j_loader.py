from neo4j import GraphDatabase


class Neo4jLoader:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(
            uri, auth=(user, password)
        )

    def close(self):
        self.driver.close()

    def enrich(self, paper_title, authors, methods, results, citations):
        with self.driver.session() as session:
            # ---- Paper ----
            session.run(
                """
                MERGE (p:Paper {title: $title})
                """,
                title=paper_title
            )

            # ---- Authors ----
            for author in authors:
                session.run(
                    """
                    MERGE (a:Author {name: $name})
                    WITH a
                    MATCH (p:Paper {title: $title})
                    MERGE (a)-[:WROTE]->(p)
                    """,
                    name=author,
                    title=paper_title
                )

            # ---- Methods ----
            for method in methods:
                session.run(
                    """
                    MERGE (m:Method {name: $method})
                    WITH m
                    MATCH (p:Paper {title: $title})
                    MERGE (p)-[:USES_METHOD]->(m)
                    """,
                    method=method,
                    title=paper_title
                )

            # ---- Results ----
            for result in results:
                session.run(
                    """
                    MERGE (r:Result {text: $text})
                    WITH r
                    MATCH (p:Paper {title: $title})
                    MERGE (p)-[:HAS_RESULT]->(r)
                    """,
                    text=result,
                    title=paper_title
                )

            # ---- Citations ----
            for cited_title in citations:
                session.run(
                    """
                    MERGE (c:Paper {title: $cited})
                    WITH c
                    MATCH (p:Paper {title: $title})
                    MERGE (p)-[:CITES]->(c)
                    """,
                    cited=cited_title,
                    title=paper_title
                )
