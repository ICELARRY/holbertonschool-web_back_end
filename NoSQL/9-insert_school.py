#!/usr/bin/env python3
""" 9-insert_school.py """

def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a MongoDB collection and return the new _id"""
    if mongo_collection is None or not kwargs:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
