from dateutil import parser

def format_event(event):
    ts = parser.isoparse(event["timestamp"])
    readable_ts = ts.strftime("%d %B %Y - %I:%M %p UTC")
    
    return {
        "author": event["author"],
        "avatar": event.get("avatar", ""),
        "type": event["type"],
        "from_branch": event.get("from_branch"),
        "to_branch": event.get("to_branch"),
        "timestamp": readable_ts
    }