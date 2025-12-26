# Scientific Article Knowledge Graph Enhancement

This project builds and enriches a **Knowledge Graph (KG)** from scientific research articles using **Natural Language Processing (NLP)** and **Neo4j**.  
The goal is to extract meaningful entities and relationships from PDFs and enhance the graph structure to improve connectivity and analytical insights.

---

## 🚀 Project Overview

Scientific articles contain rich but unstructured information.  
This project converts that information into a **structured knowledge graph**, then performs **graph enrichment** to improve:

- Relationship density  
- Graph connectivity  
- Analytical usefulness (degree, centrality, clustering)

---

## 🧠 Key Features

- 📄 **PDF Parsing** – Extracts raw text from research papers  
- 🧬 **Entity Extraction** – Identifies key scientific entities using NLP  
- 🔗 **Knowledge Graph Construction** – Stores entities & relations in Neo4j  
- 📈 **Graph Enrichment** – Adds inferred relationships to strengthen the graph  
- 📊 **Before vs After Metrics** – Quantitative comparison of graph quality  

---

## 🏗️ Project Structure

.
├── main.py # Entry point (runs pipeline)
├── requirements.txt # Python dependencies
├── docker-compose.yml # Neo4j container setup
├── kg_dump.json # Exported knowledge graph
│
├── data/
│ └── papers/ # Input research PDFs
│
├── nlp/
│ ├── pdf_parser.py # PDF text extraction
│ ├── entity_extractor.py # Named entity extraction
│ ├── extractor.py # NLP pipeline
│ └── patterns.py # Rule-based patterns
│
├── graph/
│ ├── neo4j_loader.py # Loads graph into Neo4j
│ ├── metrics.py # Graph metrics (before/after)
│ └── export.py # KG export utilities
│
└── .gitignore

yaml

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

git clone https://github.com/ramakrishnakola507/Scientific-Article-Knowledge-Graph-Enhancement.git
cd Scientific-Article-Knowledge-Graph-Enhancement
2️⃣ Create Virtual Environment
bash
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies

pip install -r requirements.txt
4️⃣ Start Neo4j (Docker)

docker-compose up -d
Neo4j Browser:
👉 http://localhost:7474
(Default credentials are defined in docker-compose.yml)

▶️ Running the Project

python main.py
This will:

Parse PDFs

Extract entities

Build the initial knowledge graph

Apply graph enrichment

Display before vs after metrics

📊 Graph Enrichment Explained
Before Enrichment

Sparse graph

Fewer relationships

Lower connectivity metrics

After Enrichment

Additional inferred relationships

Improved degree & density

Better analytical structure

Metrics are computed in:

graph/metrics.py
🧪 Example Metrics Used
Node count

Relationship count

Average degree

Graph density

These metrics clearly show the impact of enrichment.

🛑 What is NOT pushed to GitHub
To keep the repository clean and lightweight:

❌ Virtual environment (venv/)

❌ Neo4j runtime data (neo4j_data/, neo4j_logs/)

❌ Cache files (__pycache__/)

These are intentionally ignored using .gitignore.

📌 Technologies Used
Python

spaCy / NLP

Neo4j

Docker

Cypher Query Language

🎯 Use Cases
Scientific literature analysis

Research trend discovery

Knowledge graph construction

Graph analytics & enrichment

👤 Author
Rama Krishna Kola
GitHub: https://github.com/ramakrishnakola507

⭐ If you like this project
Give it a ⭐ on GitHub — it helps a lot!
