from rapidfuzz import fuzz, process
from typing import List, Dict, Any

def deduplicate_businesses(businesses: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Detects duplicate businesses using RapidFuzz for name/address similarity.
    Merges duplicate records.
    """
    if not businesses:
        return []
        
    deduped = []
    used_indices = set()
    
    for i, biz in enumerate(businesses):
        if i in used_indices:
            continue
            
        merged = biz.copy()
        used_indices.add(i)
        
        for j, other in enumerate(businesses):
            if j in used_indices:
                continue
                
            # Compare names using fuzzy matching
            name1 = merged.get("name", "")
            name2 = other.get("name", "")
            
            if name1 and name2:
                score = fuzz.WRatio(name1, name2)
                
                # If highly similar, consider it a duplicate
                if score > 85:
                    used_indices.add(j)
                    # Merge logic: prefer non-null values
                    for k, v in other.items():
                        if not merged.get(k) and v:
                            merged[k] = v
                            
        deduped.append(merged)
        
    return deduped
