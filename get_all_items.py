#
import os
from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient

# Set the endpoint and key for your Cosmos DB account
url = os.environ.get('COSMOS_ENDPOINT')
key = os.environ.get('COSMOS_KEY')

print(url)
print(key)

# Set the database and container you want to use
database = 'cosmosdb-tcs-devizdb-maindb'
container = 'frontend'


client = CosmosClient(url = url, credential=key, connection_verify=False)
database = client.get_database_client(database)
connection = database.get_container_client(container)

# Query the container for all items
query = "SELECT * FROM c"
items = list(container.query_items(query=query, enable_cross_partition_query=True))

# Print the results
for item in items:
    print(item)
