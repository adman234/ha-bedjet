<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://brands.home-assistant.io/bedjet/dark_logo.png">
  <img alt="bedjet logo" src="https://brands.home-assistant.io/bedjet/logo.png">
</picture>

# BedJet for Home Assistant

This project provides various entities to allow control of a [BedJet V2 or BedJet 3](https://bedjet.com) device.

> ⚠️ **Important**
>
> BedJet devices only allow **one active Bluetooth connection at a time**. If the BedJet mobile app is open (or running in the background) and connected to the device, Home Assistant will not be able to connect to it. The BedJet remote is not affected by this limitation, as it uses RF rather than Bluetooth.
>
> Before proceeding, **make sure the BedJet app is fully closed**. If you need to use the app (for example, to adjust biorhythm programs), temporarily disable the Home Assistant integration.

## Installation

### Manual

1. Download or clone this repository
2. Copy the `custom_components/bedjet` folder to your Home Assistant `custom_components` directory
3. Restart Home Assistant

## Setup

1. Go to [Settings > Devices & services](https://my.home-assistant.io/redirect/integrations/)
2. In the bottom-right corner, select **Add integration**
3. Type `BedJet` and select the **BedJet** integration
4. Follow the instructions to add the integration

## Screenshot

![screenshot](images/BedJet3-HA.png)

## Changes in this fork

- **Reduced reconnect churn** — the integration now stays connected for 5 minutes after the last command (up from 1 minute) and polls every 5 minutes instead of every 15 seconds. This significantly reduces the connect/disconnect cycling that causes BedJet 3 reliability issues.
- **Commands no longer silently fail** — if the device is disconnected when a command is sent (e.g. changing temperature), it will now reconnect automatically before sending rather than dropping the command with no feedback.
- **Fixed notification handler crash** — unknown mode bytes from newer firmware no longer terminate the BLE notification subscription, which previously caused the device to appear stuck/unavailable until HA restarted.
- **Fixed turn on/off controls** — the climate entity's on/off buttons now work correctly instead of throwing an error.

## Credits

Based on the original integration by [@natekspencer](https://github.com/natekspencer/ha-bedjet), with V2 support contributions by [@jdaleo23](https://github.com/jdaleo23).
