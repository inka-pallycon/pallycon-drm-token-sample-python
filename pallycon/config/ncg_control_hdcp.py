CONTROL_HDCP = (0, 1, 2)

HDCP_NONE = CONTROL_HDCP[0]  # 'HDCP_NONE'
HDCP_V1_4 = CONTROL_HDCP[1]  # 'HDCP_V1.4'
HDCP_V2_2 = CONTROL_HDCP[2]  # 'HDCP_V2.2'


def check(control_hdcp):
    return control_hdcp in CONTROL_HDCP

