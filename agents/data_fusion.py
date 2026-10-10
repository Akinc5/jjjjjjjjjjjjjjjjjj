def fuse_and_clean_data(events):
    # Simple fusion logic (deduplication and merging by location/event type)
    return list({e['text']: e for e in events}.values())