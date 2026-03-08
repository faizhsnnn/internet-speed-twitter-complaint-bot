# Internet Speed Twitter Complaint Bot

## Overview

This project automates the process of testing internet speed and posting a complaint on Twitter (X) if the measured speed does not match the promised bandwidth.

Using Selenium WebDriver, the bot performs a full browser automation workflow:

1. Runs a Speedtest on speedtest.net.
2. Collects download and upload speeds.
3. Logs into Twitter using Google authentication.
4. Posts a tweet highlighting the discrepancy between promised and actual internet speeds.

This project was built as part of #90DaysOfCode to explore end-to-end browser automation workflows.

---

## Technologies Used

- Python
- Selenium WebDriver
- ChromeDriver
- WebDriverWait & Expected Conditions

---

## Key Concepts Demonstrated

- Browser automation using Selenium
- Dynamic element handling with explicit waits
- Handling login flows and multiple browser windows
- Web scraping of dynamically rendered content
- Automating social media interaction
- Workflow automation with conditional logic

---

## Automation Workflow

1. Launch browser session.
2. Navigate to Speedtest.net.
3. Accept cookies if required.
4. Start the speed test.
5. Wait for the test to complete.
6. Extract download and upload speeds.
7. Navigate to Twitter login page.
8. Authenticate using Google login.
9. Compose a tweet comparing actual vs promised speeds.
10. Publish the tweet automatically.

---

## Installation

Install dependencies:

```
pip install selenium
```

Ensure ChromeDriver is compatible with your Chrome browser version and accessible via PATH.

## Run
```
python main.py
```

---
## Example Tweet
Hey Internet Provider, why is my internet speed 42down/8up when I pay for 150down/10up?

---
### Why This Project Matters

This project demonstrates how browser automation can be used to:

Monitor service performance

Automate repetitive online workflows

Integrate multiple platforms within a single automation script

Build end-to-end automation pipelines

---
## Author

Faiz Hasan

Python Automation & Backend Developer
