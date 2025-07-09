**Student Name**: Lerato Moloi <br>
**Date**:

## Test cases  

<!--test case Template-->
- **ID**: 
- **Test**:
- **Environment**:  
- **Severity**
- **Priority**:
- **Steps to reproduce**:
- **Expected**:
- **Actual**:
- **Attachments**:
- **Status**: 
---

**Student Name**: Tosin A. Williams <br>
**Date**: 09/07/2025

## Test cases  

<!--test case Template-->
 # ✅ CleanCity - Test Cases (Week 2)

## 🗑️ Waste Management Test Cases

### Test Case WM001 – Submit Waste Pickup Request
- **Preconditions**: User is logged in
- **Steps**:
  1. Go to "Schedule Pickup" page
  2. Fill in pickup address, date, and time
  3. Click "Submit"
- **Expected Result**: Pickup request is saved and visible on Dashboard
- **Actual Result**: Not displayed on Dashboard (❌ Bug found - see DA002)

---

### Test Case WM002 – Cancel Pickup Request
- **Preconditions**: A pickup request has been created
- **Steps**:
  1. Go to Dashboard
  2. Select a pickup request
  3. Click "Cancel"
- **Expected Result**: Request is removed or marked as canceled
- **Actual Result**: _[To be tested]_

---

## 📊 Dashboard Analytics Test Cases

### Test Case DA001 – View All Pickup Requests
- **Preconditions**: At least one pickup request exists
- **Steps**:
  1. Navigate to Dashboard page
- **Expected Result**: All user requests are listed
- **Actual Result**: Dashboard remains empty (❌ Bug found)

---

### Test Case DA002 – Dashboard Analytics Cards Update Correctly
- **Preconditions**: Multiple pickup requests with different statuses exist
- **Steps**:
  1. Navigate to Dashboard
  2. Observe status counts/charts
- **Expected Result**: Accurate statistics for pickups shown
- **Actual Result**: _[To be tested]_


---

**Student Name**: Thandolwethu Ndhlovu <br>
**Date**: 09/07/2025

## Test cases  

<!--test case Template-->
 # ✅ CleanCity - Test Cases (Week 2)

 ## 🔐 Authentication System Test Cases
 ### Test Case AS001 - Register account with missing fields
- **Steps to Reproduce:**
 1. Enter a valid Name and Password
 2. Leave email as ""
 3. Click create Account
- **Expected:**
System should throw an error for empty field.
- **Actual:**
System throws an error for empty field
- **Status:** Passed

  ---

   ### Test Case AS002 - Log in with invalid Credentials
 - **Preconditions:** User has registered an account
- **Steps to Reproduce:**
 1. Navigate to login page
 2. Enter invalid email or password
 3. Click Sign in
- **Expected:**
System should throw invalid error.
- **Actual:**
System throws invalid error
- **Status:** Passed
---


