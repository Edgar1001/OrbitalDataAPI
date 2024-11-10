from datetime import datetime, timezone

def iso_to_seconds(iso_time: str) -> float:
    dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))  
    return (dt - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()  

