import os
from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient

# Set the endpoint and key for your Cosmos DB account
ENDPOINT = ${{secrets.COSMOS_ENDPOINT}}
KEY = ${{secrets.COSMOS_KEY}}

# Set the database and container you want to use
DATABASE_ID = 'integration-test-db'
CONTAINER_ID = 'integration-test-container'

# Create a Cosmos DB client with the endpoint and key
credential = DefaultAzureCredential()
client = CosmosClient(endpoint=ENDPOINT, credential=credential)

# Get a reference to the database and container
database = client.get_database_client(DATABASE_ID)
container = database.get_container_client(CONTAINER_ID)

# Query the container for all items
query = "SELECT * FROM c"
items = list(container.query_items(query=query))

# Print the results
for item in items:
    print(item)
