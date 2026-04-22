# Systems Integration MVP - Financial Services

## Description
This MVP simulates the "Compliance workflows integrated into one flow" solution from RemoveFriction's portfolio. It demonstrates how high-volume case handling with manual compliance checks (KYC) can be automated and synced across three departments (Sales, Compliance, Risk) using tools like Microsoft Dynamics, Logic Apps, and Power Automate.

## How to use it
Click the "Run Automated KYC Integration" button to simulate the data flow across the three departmental systems. You will see the status update sequentially as the integration logic progresses, ultimately marking the case as "KYC Approved".

## How to start it
1. From the root of the project, you can serve the directory using Python's built-in HTTP server:
   ```bash
   python3 -m http.server 8080
   ```
2. Navigate to `http://localhost:8080/mvps/systems-integration/` in your web browser.
