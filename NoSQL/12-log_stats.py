#!/usr/bin/env python3
"""12-log_stats.py"""
from pymongo import MongoClient

def main():
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Ümumi log sayı
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Metodlara görə say
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # GET /status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    main()
