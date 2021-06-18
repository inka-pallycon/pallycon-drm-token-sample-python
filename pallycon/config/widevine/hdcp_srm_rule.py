HDCP_SRM_RULE = ('HDCP_SRM_RULE_NONE', 'CURRENT_SRM')

HDCP_SRM_RULE_NONE = HDCP_SRM_RULE[0]
CURRENT_SRM = HDCP_SRM_RULE[1]

def check(srm_rule) -> bool:
    return srm_rule in HDCP_SRM_RULE

