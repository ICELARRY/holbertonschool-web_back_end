#!/usr/bin/env python3
""" 11-schools_by_topic """

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object
        topic: string, topic to search for

    Returns:
        List of matching school documents
    """
    # Find all documents where 'topics' array contains 'topic'
    return list(mongo_collection.find({"topics": topic}))
