from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from qdrant_client.models import PointStruct

import streamlit as st
import openai
import requests
import json

client = QdrantClient(host="localhost", port=6333)

vector_size = 1536
client.create_collection(
    collection_name='university_collection',
    vectors_config={
        'title': VectorParams(
            distance=Distance.COSINE,
            size=vector_size,
        ),
        'content': VectorParams(
            distance=Distance.COSINE,
            size=vector_size,
        ),
    }
)