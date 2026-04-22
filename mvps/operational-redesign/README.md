# Operational Redesign MVP - Manufacturing

## Description
This MVP simulates the "Multi-site reporting rebuilt into a single operational view" solution from RemoveFriction's portfolio. It demonstrates an executive dashboard that consolidates performance data across multiple plants and displays automated variance alerts, reflecting the reduction of reporting cycles and real-time visibility.

## How to use it
The dashboard provides a read-only executive view. It displays current variance alerts from the manufacturing plants and a performance table detailing output and targets met. After 3 seconds, a simulated data update adds a new plant to the performance table.

## How to start it
1. From the root of the project, you can serve the directory using Python's built-in HTTP server:
   ```bash
   python3 -m http.server 8080
   ```
2. Navigate to `http://localhost:8080/mvps/operational-redesign/` in your web browser.
