# Data & Reporting MVP - Distribution

## Description
This MVP simulates the "Inventory visibility restored across regions" solution from RemoveFriction's portfolio. It shows a dashboard replacing complex Excel spreadsheets with a unified view of regional stock levels and margins. It also includes a simulated Purchase Order workflow with automated policy triggers based on limits.

## How to use it
The main panel shows real-time margin visibility and highlights low margins. The side panel demonstrates PO approvals, where POs under a certain threshold are auto-approved, and larger ones require manual approval by clicking the "Approve" button.

## How to start it
1. From the root of the project, you can serve the directory using Python's built-in HTTP server:
   ```bash
   python3 -m http.server 8080
   ```
2. Navigate to `http://localhost:8080/mvps/data-reporting/` in your web browser.
