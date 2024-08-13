#!/usr/bin/env python3
"""A Python script that provides some stats about Nginx
logs stored in MongoDB."""

from pymongo import MongoClient


def logger_stats():
    """This method provides some stats about Nginx
    logs stored in MongoDB.
    Args:
        none
    Returns:
        none """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_log = client.logs.nginx

    # Number of documents in the collection
    records = nginx_log.count_documents({})
    # Number of documents per method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_count = {method: nginx_log.count_documents({"method": method})
                     for method in methods}

    # Number of documents with method=GET and path=/status
    status_check = nginx_log.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{records} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {methods_count[method]}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    logger_stats()
