from app.neo4j_client import get_neo4j
from typing import List, Dict, Any

class GraphService:
    @staticmethod
    async def save_businesses(businesses: List[Dict[str, Any]]):
        """Saves scraped/verified businesses to Neo4j Graph Database."""
        driver = await get_neo4j()
        
        query = """
        UNWIND $businesses AS biz
        MERGE (b:Business {name: biz.name})
        SET b.trust_score = biz.trust_score, 
            b.security_score = biz.security_score,
            b.fraud_risk = biz.fraud_risk
            
        WITH b, biz
        // Link Location
        FOREACH (city IN CASE WHEN biz.city IS NOT NULL THEN [biz.city] ELSE [] END |
            MERGE (l:Location {name: city})
            MERGE (b)-[:LOCATED_IN]->(l)
        )
        
        // Link Website
        FOREACH (web IN CASE WHEN biz.website IS NOT NULL THEN [biz.website] ELSE [] END |
            MERGE (w:Website {url: web})
            MERGE (b)-[:HAS_WEBSITE]->(w)
        )
        """
        
        async with driver.session() as session:
            await session.run(query, businesses=businesses)
            
    @staticmethod
    async def get_graph_data() -> Dict[str, Any]:
        """Returns JSON data formatted for force-directed graph frontend."""
        driver = await get_neo4j()
        
        query = """
        MATCH (n)
        OPTIONAL MATCH (n)-[r]->(m)
        RETURN n, r, m
        LIMIT 200
        """
        
        nodes = []
        links = []
        node_ids = set()
        
        async with driver.session() as session:
            result = await session.run(query)
            records = await result.data()
            
            for row in records:
                # Handle source node
                if row.get('n'):
                    n = row['n']
                    n_id = id(n) # Using memory address for demo, Neo4j ElementId is better
                    if n_id not in node_ids:
                        node_ids.add(n_id)
                        labels = list(n.labels)
                        nodes.append({"id": n_id, "label": labels[0] if labels else "Unknown", "name": n.get("name") or n.get("url") or "Unknown"})
                        
                # Handle target node and relationship
                if row.get('m') and row.get('r'):
                    m = row['m']
                    m_id = id(m)
                    if m_id not in node_ids:
                        node_ids.add(m_id)
                        labels = list(m.labels)
                        nodes.append({"id": m_id, "label": labels[0] if labels else "Unknown", "name": m.get("name") or m.get("url") or "Unknown"})
                        
                    links.append({"source": id(row['n']), "target": m_id, "type": row['r'].type})
                    
        return {"nodes": nodes, "links": links}
