"""Tuya 4-gang switch (_TZE204_unsxl4ir) custom quirk."""

from zigpy.profiles import zha, zgp
from zigpy.zcl.clusters.general import Basic, Groups, Scenes, Ota, Time, GreenPowerProxy
from zhaquirks import CustomDevice
from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)
from zhaquirks.tuya.mcu import (
    MoesSwitchManufCluster,
    TuyaOnOff,
    TuyaOnOffNM,
)


class TuyaQuadSwitchTZE204(CustomDevice):
    """Custom device representing _TZE204_unsxl4ir 4-gang Zigbee switch."""

    signature = {
        MODELS_INFO: [("_TZE204_unsxl4ir", "TS0601")],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,  # 0x0104
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,  # 0x0051
                INPUT_CLUSTERS: [
                    0x0004,  # Groups
                    0x0005,  # Scenes
                    0xEF00,  # Tuya manufacturer cluster
                    0x0000,  # Basic
                ],
                OUTPUT_CLUSTERS: [
                    0x0019,  # OTA
                    0x000A,  # Time
                ],
            },
            242: {
                PROFILE_ID: zgp.PROFILE_ID,  # 0xA1E0
                DEVICE_TYPE: zgp.DeviceType.PROXY_BASIC,  # 0x0061
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    MoesSwitchManufCluster,
                    TuyaOnOff,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id, Time.cluster_id],
            },
            2: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [TuyaOnOff],
                OUTPUT_CLUSTERS: [],
            },
            3: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [TuyaOnOff],
                OUTPUT_CLUSTERS: [],
            },
            4: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [TuyaOnOff],
                OUTPUT_CLUSTERS: [],
            },
            242: {
                PROFILE_ID: zgp.PROFILE_ID,
                DEVICE_TYPE: zgp.DeviceType.PROXY_BASIC,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        }
    }
