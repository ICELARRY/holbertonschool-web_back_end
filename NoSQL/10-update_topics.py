#!/usr/bin/env python3
""" 10-update_topics.py """

def update_topics(mongo_collection, name, topics):
    """
    Update all school documents with the given name to have a new topics list.

    Args:
        mongo_collection: pymongo collection object
        name (str): name of the school to update
        topics (list): list of strings representing new topics
    """
    if mongo_collection is None or not name or not isinstance(topics, list):
        return

    mongo_collection.update_many(
        {"name": name},         # filter by school name
        {"$set": {"topics": topics}}  # set the 'topics' field
    )
