from neo4j import GraphDatabase
import os

class GraphHelper:
    def __init__(self):
        uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        user = os.getenv("NEO4J_USER", "neo4j")
        password = os.getenv("NEO4J_PASSWORD", "test")
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def remember_concept(self, user_id: str, concept: str, context: str = None):
        with self.driver.session() as session:
            session.run(
                "MERGE (u:User {id: $user_id}) "
                "MERGE (c:Concept {name: $concept}) "
                "MERGE (u)-[:LEARNED {context: $context}]->(c)",
                user_id=user_id, concept=concept, context=context
            )

    def recall_concepts(self, user_id: str):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (u:User {id: $user_id})-[:LEARNED]->(c:Concept) RETURN c.name as concept",
                user_id=user_id
            )
            return [record["concept"] for record in result]
