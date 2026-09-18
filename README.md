# ☀️ Sunnode

A solar-powered edge server — a tiny, self-sufficient computer that runs entirely off sunlight and stored battery power, with zero grid electricity.

## Why This Exists

AI and cloud computing are hitting a real wall: power. Global data center electricity demand is set to grow 26% in 2026 alone, reaching 565 terawatt-hours, and total power demand is expected to nearly triple by 2030. Companies like Sam Altman-backed Exowatt are racing to solve this exact problem at gigawatt scale by building solar-powered data centers.

Sunnode is a $50 proof of the same core idea, shrunk down to desk scale: **can a real, working piece of internet infrastructure run entirely off sunlight and a battery, with no grid power at all?**

## What It Does

A Raspberry Pi Pico WH serves a live status webpage over WiFi, showing:
- Real-time ambient light level (via BH1750 light sensor)
- System uptime
- Live proof that it's running — no wall power involved

## Hardware

| Part | Purpose |
|---|---|
| Raspberry Pi Pico WH | Runs the code, serves the webpage |
| FUTUREZEN 10W Solar Panel | Charges the battery from sunlight |
| Evopow 10000mAh Power Bank | Stores energy, powers the Pico |
| BH1750 Light Sensor | Measures ambient light (I2C) |
| Breadboard + jumper wires | Wiring |

**Total cost: ~$50**

## Wiring

- Solar panel (USB out) → Power bank (USB in)
- Power bank (USB out) → Pico WH (USB in)
- BH1750 → Pico: VCC→3V3, GND→GND, SCL→GP1, SDA→GP0

## How It's Tested

The core demo: cover the solar panel to simulate night/cloud cover. The page stays live, running on stored battery. Uncover it, and the battery recharges while the page keeps serving the whole time — no downtime, no grid power, ever.

## Status

🟡 **In progress** — code written, parts ordered, hardware build pending parts arrival.

## Roadmap

- [x] Design + parts list
- [x] Starter MicroPython code (WiFi + web server + light sensor)
- [ ] Physical wiring
- [ ] Live testing (cover/uncover demo)
- [ ] Add uptime persistence across power cycles
- [ ] Tier 1: upgrade to Raspberry Pi 4, host a real service off solar

## Built By
[Braden Salcetti ‘31]
