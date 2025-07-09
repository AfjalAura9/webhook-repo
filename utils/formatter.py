# utils/formatter.py
from dateutil import parser

def format_event(event):
    ts = parser.isoparse(event["timestamp"])
    readable_ts = ts.strftime("%d %B %Y - %I:%M %p UTC")

    if event["type"] == "push":
        return f'{event["author"]} pushed to "{event["to_branch"]}" on {readable_ts}'
    elif event["type"] == "pull_request":
        return f'{event["author"]} submitted a pull request from "{event["from_branch"]}" to "{event["to_branch"]}" on {readable_ts}'
    elif event["type"] == "merge":
        return f'{event["author"]} merged branch "{event["from_branch"]}" to "{event["to_branch"]}" on {readable_ts}'
    else:
        return f'Unknown event by {event.get("author", "someone")} on {readable_ts}'
