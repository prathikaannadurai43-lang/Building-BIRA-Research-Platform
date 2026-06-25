from neo4j import AsyncGraphDatabase
from app.config import settings

class Neo4jClient:
    def __init__(self):
        self.driver = None

    async def connect(self):
        self.driver = AsyncGraphDatabase.driver(
            settings.NEO4J_URI, 
            auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
        )

    async def close(self):
        if self.driver:
            await self.driver.close()

neo4j_client = Neo4jClient()

async def get_neo4j():
    if not neo4j_client.driver:
        await neo4j_client.connect()
    return neo4j_client.driver
