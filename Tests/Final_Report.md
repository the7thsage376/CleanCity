## 🧪 CleanCity QA Final Test Report

### 📋 Project Summary

**Application Name**: CleanCity – Waste Pickup Scheduler<br>

**Testing Period**: July 10 – July 14, 2025 <br>

**Tested By**: Tosin A. Williams, Lerato Moloi, Thandolwethu L. Ndhlovu

**Objective**: 
-Ensure functional integrity, usability, accessibility, and performance of the CleanCity web application, including registration, scheduling, administrative functions, content management, Authentication system, community features,dashboard interaction, and navigation flows.

---

### ✅ Test Coverage Overview
| Feature              | Status | Functional Req. | Notes                                             |
| -------------------- | ------ | -------------- | ------------------------------------------------- |
| Home Page Load       | ✅ Pass | FR-01       | Loaded correctly via React script.                |
| User Registration    | ✅ Pass | FR-02          | Valid credentials used.                           |
| Schedule Pickup Form | ✅ Pass | FR-03          | Dropdowns, text fields, and submit button tested. |
| Login                | ✅ Pass | FR-04          | Credentials verified after registration.          |
| Dashboard Navigation | ✅ Pass | FR-05          | Reached successfully post-login.                  |
| Blog Access         | ✅ Pass | FR-06          | Navigation functional.                            |
| Community Page      | ✅ Pass | FR-07          | Navigation functional.                            |
| Awareness Page      | ✅ Pass | FR-08          | Navigation functional.                            |
| Feedback Page       | ✅ Pass | FR-09          | Navigation functional.                            |
| Logout Functionality | ✅ Pass | FR-10          | Session terminated and returned to login page.    |
| Admin pickup request modification| Fail | FR-055 | There is no user interface available to modify requests|
|



Tools used: Selenium (Python), ChromeDriver, Visual Studio Code, Git, GitHub

---

### 🧪 Selenium Automated Test

Test Script Path: Tests/selenium/cleancity_flow.py

Description:

* Navigates to CleanCity app via http://localhost:3000
* Performs registration, schedules a pickup with dropdown selection
* Logs in, navigates all relevant pages, and logs out
* Includes Select handling for dropdowns and controlled delays via time.sleep()

Execution Result:

* Script ran successfully
* Observed a slight delay in form response due to heavy loading on development server

---

### 📂 Defect Log Summary

Defect ID: D-001
Title: Inconsistent App URL Handling

Description:
Opening the application using VS Code Live Server (http://127.0.0.1:5500) results in data loss — scheduled pickups do not reflect in the dashboard. However, launching via React script (http://localhost:3000) performs as expected.

Screenshots:
📎 Tests/Jira_Screenshots/Screenshot (752).png (Live Server)
📎 Tests/Jira_Screenshots/Screenshot (753).png (React App)

Severity: Critical
Priority: High
Status: Open
Logged By: Tosin A. Williams
Date: July 13, 2025

---

### 🔚 Final Notes

* The system works as intended on the correct environment (npm start / localhost:3000).
* One defect logged and documented with screenshots.
* Selenium script provides a reusable automation flow.
* The core functionality isn't working as intended for the website's purpose.

> ✅ This test cycle confirms functional readiness of CleanCity for demo/presentation.

---

Prepared by: Tosin A. Williams
Date: July 14, 2025
