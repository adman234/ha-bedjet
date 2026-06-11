"""BedJet event entity."""

from __future__ import annotations

from homeassistant.components.event import EventEntity
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from . import BedJetConfigEntry
from .entity import BedJetEntity
from .pybedjet import BedJet
from .pybedjet.const import (
    BEDJET_EVENT_TURNED_OFF,
    BEDJET_EVENT_TURNED_ON,
    BEDJET_EVENT_UNEXPECTED_SHUTOFF,
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: BedJetConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the event platform for BedJet."""
    data = entry.runtime_data
    async_add_entities([BedJetEventEntity(data.coordinator, data.device, entry.title)])


class BedJetEventEntity(BedJetEntity, EventEntity):
    """Representation of a BedJet action event."""

    _attr_translation_key = "action"
    _attr_event_types = [
        BEDJET_EVENT_TURNED_ON,
        BEDJET_EVENT_TURNED_OFF,
        BEDJET_EVENT_UNEXPECTED_SHUTOFF,
    ]

    def __init__(
        self,
        coordinator: DataUpdateCoordinator[None],
        device: BedJet,
        name: str,
    ) -> None:
        """Initialize a BedJet event entity."""
        self._attr_unique_id = f"{device.address}_action"
        super().__init__(coordinator, device, name)

    async def async_added_to_hass(self) -> None:
        """Register callbacks."""
        await super().async_added_to_hass()
        self.async_on_remove(
            self._device.register_event_callback(self._async_handle_event)
        )

    @callback
    def _async_handle_event(self, event_type: str, attributes: dict[str, str]) -> None:
        """Handle a device action event."""
        self._trigger_event(event_type, attributes)
        self.async_write_ha_state()
