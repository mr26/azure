#!/usr/bin/python3.6

## example on how to authenticate using Azure Managed Identities, in this instance I specifically used a system-assigned managed identity.

"""In order to allow the VM from which I ran this code to be able to create resource groups, I had to go to the Azure subscription and 
assign the 'Contributor' role to the VM."""

from msrestazure.azure_active_directory import MSIAuthentication
from azure.storage.blob import BlobServiceClient
from azure.mgmt.subscription import SubscriptionClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.v2019_10_01.models import ResourceGroup

credentials = MSIAuthentication()

sub_client = SubscriptionClient(credentials)

sub_list = sub_client.subscriptions.list()

for sub in sub_list:
    print(sub)

resource_client = ResourceManagementClient(credentials, SUBSCRIPTION_ID)

resource_client.resource_groups.create_or_update('api-test-group1', ResourceGroup(location='eastus'))




