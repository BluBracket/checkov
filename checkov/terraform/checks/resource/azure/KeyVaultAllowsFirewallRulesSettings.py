from checkov.common.models.enums import CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class KeyVaultAllowsFirewallRulesSettings(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure that key vault allows firewall rules settings"
        id = "CKV_AZURE_109"
        supported_resources = ['azurerm_key_vault']
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return "network_acls/[0]/default_action"

    def get_expected_value(self):
        return "allow"


check = KeyVaultAllowsFirewallRulesSettings()
