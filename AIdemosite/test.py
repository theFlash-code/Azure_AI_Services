# import os
# from azure.keyvault.secrets import SecretClient
# from azure.identity import DefaultAzureCredential

# keyVaultName = os.environ["KEY_VAULT_NAME"]
# print(keyVaultName)
# KVUri = f"https://{keyVaultName}.vault.azure.net"

# credential = DefaultAzureCredential()
# client = SecretClient(vault_url=KVUri, credential=credential)

# secretName = 'REGION'
# secretValue = 'eastasia'

# # print(f"Creating a secret in {keyVaultName} called '{secretName}' with the value '{secretValue}' ...")

# # client.set_secret(secretName, secretValue)

# # print(" done.")

# print(f"Retrieving your secret from {keyVaultName}.")

# retrieved_secret = client.get_secret(secretName)

# print(f"Your secret is '{retrieved_secret.value}'.")
# # print(f"Deleting your secret from {keyVaultName} ...")

# # poller = client.begin_delete_secret(secretName)
# # deleted_secret = poller.result()

# print(" done.")