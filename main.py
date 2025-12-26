import os
from graph.neo4j_loader import Neo4jLoader
from nlp.pdf_parser import parse_pdf
from nlp.entity_extractor import extract_entities

PDF_DIR = "data/papers"

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "12345678"


def main():
    kg = Neo4jLoader(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

    for file in os.listdir(PDF_DIR):
        if not file.lower().endswith(".pdf"):
            continue

        pdf_path = os.path.join(PDF_DIR, file)
        print(f"\n📄 Processing: {file}")

        parsed = parse_pdf(pdf_path)      # dict
        text = parsed["text"]             # ✅ string only

        entities = extract_entities(text)

        kg.enrich(
            paper_title=file.replace(".pdf", ""),
            authors=entities["authors"],
            methods=entities["methods"],
            results=entities["results"],
            citations=entities["citations"],
        )

    kg.close()
    print("\n✅ Knowledge Graph Enriched Successfully")


if __name__ == "__main__":
    main()
