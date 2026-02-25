"""BedJet module."""

from __future__ import annotations

import logging

from bleak.backends.device import BLEDevice
from bleak_retry_connector import BleakClientWithServiceCache, establish_connection

from .bedjet import (
    BEDJET2_SERVICE_UUID,
    BEDJET3_SERVICE_UUID,
    BedJet,
    BedJetButton,
    BedJetCommand,
    BedJetState,
    OperatingMode,
)
from .powerlayer import (
    POWERLAYER_SERVICE_UUID,
    POWERLAYER_UUID,
    PowerLayer,
    PowerLayerButton,
    PowerLayerState,
)

__all__ = [
    "BedJet",
    "BedJetState",
    "BedJetButton",
    "BedJetCommand",
    "OperatingMode",
    "BEDJET2_SERVICE_UUID",
    "BEDJET3_SERVICE_UUID",
    "PowerLayer",
    "PowerLayerState",
    "PowerLayerButton",
    "POWERLAYER_SERVICE_UUID",
]

_LOGGER = logging.getLogger(__name__)


async def determine_device(device: BLEDevice) -> BedJet | PowerLayer | None:
    """Determine device type."""
    async with await establish_connection(
        BleakClientWithServiceCache,
        device,
        device.name or "BedJet",
        use_services_cache=True,
    ) as client:
        _LOGGER.debug(
            "%s (%s):\n%s",
            device.name,
            device.address,
            "\n".join(
                f"  {key}:\n    {'\n    '.join(str(s) for s in value.values())}"
                for key, value in {
                    "Services": client.services.services,
                    "Characteristics": client.services.characteristics,
                    "Descriptors": client.services.descriptors,
                }.items()
            ),
        )

        if client.services.get_service(BEDJET3_SERVICE_UUID):
            _LOGGER.debug(
                "%s (%s): Setting up BedJet 3 device", device.name, device.address
            )
            return BedJet(device)
        if client.services.get_service(BEDJET2_SERVICE_UUID):
            _LOGGER.debug(
                "%s (%s): Setting up BedJet V2 device", device.name, device.address
            )
            return BedJet(device)
        if client.services.get_service(POWERLAYER_UUID):
            _LOGGER.debug(
                "%s (%s): Setting up PowerLayer device", device.name, device.address
            )
            return PowerLayer(device)
    return None
