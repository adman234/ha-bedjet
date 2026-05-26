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

## Credits

Based on the original integration by [@natekspencer](https://github.com/natekspencer/ha-bedjet), with V2 support contributions by [@jdaleo23](https://github.com/jdaleo23).
