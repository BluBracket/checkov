from enum import Enum

from checkov.common.bridgecrew.code_categories import CodeCategoryType


class CustomerSubscription(Enum):
    IAC = "IAC"
    SCA = "SCA"
    SECRETS = "SECRETS"


class BillingPlan(Enum):
    DEVELOPER_BASED = "DEVELOPER_BASED"
    RESOURCE_BASED = "RESOURCE_BASED"


SubscriptionCategoryMapping = {
    CustomerSubscription.IAC: [CodeCategoryType.IAC, CodeCategoryType.SUPPLY_CHAIN],
    CustomerSubscription.SCA: [CodeCategoryType.OPEN_SOURCE, CodeCategoryType.IMAGES],
    CustomerSubscription.SECRETS: [CodeCategoryType.SECRETS]
}

CategoryToSubscriptionMapping = {}
for sub, cats in SubscriptionCategoryMapping.items():
    for cat in cats:
        CategoryToSubscriptionMapping[cat] = sub
