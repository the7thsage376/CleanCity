**Student Name**: Lerato Moloi <br>
**Date**: 09/07/2025

## Test cases  

<!--test case Template-->
## Request Management test cases

### Test case RM001 - Admin pickup request modification
**Precondition**: The user is logged in as an admin

**Steps To Reproduce**:<br>

1. Click on the Admin Tab
2. Go to update request status
3. Select the pickup request
4. Select a status for the request
5. Click update status

**Expected**: The status of the selected pickup request is changed.<br>
**Actual**: The pickup request status is changed.<br>
 **Status**: Pass

 ### Test case RM002 - Admins assigning pickup dates and times

 **Precondition**: User is logged in as admin<br>

**Steps to Reproduce**:
1. Click the Admin Panel Tab
2. Click on the edit button of the Action column<br>
 
**Expected**:  The user can change the pickup dates and times of the requests<br>
**Actual**: The Edit button is unresponsive<br>
**Status**: Fail


### Test case RM003 - Filtering and Search capabilties

**Precondition**:  User must be logged in as either an admin or a regular user<br>

- **Expected**:  Filter and Search results display items that meet the conditions.<br>
- **Actual**:  The location filter for “Eldoret” displays pickup requests in Nairobi (refer to bug report FR-056)<br>
- **Status**: Fail
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

     ### Test Case AS003 - Log Out from User Account
 - **Preconditions:** User has registered an account and logged in
- **Steps to Reproduce:**
 1.Click on Log out 
- **Expected:**
User should be redirected to Login page.
- **Actual:**
User is redirected to Login page
- **Status:** Passed

  ---

     ### Test Case AS004 - Checking Role Based Access
 - **Preconditions:** User has registered a User and an Admin account
- **Steps to Reproduce:**
 1. Login with User account
 2. Observe functions available to User account
 3. Logout with User account
 4. Login with Admin account
 5. Observe functions available to Admin account
- **Expected:**
Admin features should be hidden from User account.
- **Actual:**
  Admin features are hidden to User account
- **Status:** Passed

  ---

  ##  👥 Community Features Test Cases
     ### Test Case CM001 - Edit a User Profile
 - **Preconditions:** User has registered  and logged  in with an account
- **Steps to Reproduce:**
 1. Navigate to the profile
 2. Click edit profile
 3. Edit any field
 4. Click save
 5. Observe changes to profile  
- **Expected:**
Any changes made to the profile should persist.
- **Actual:**
  Changes made to profile persist 
- **Status:** Passed

---

   ### Test Case CM002 - Upload a Profile Picture
 - **Preconditions:** User has registered  and logged  in with an account
- **Steps to Reproduce:**
 1. Navigate to the profile
 2. Click edit profile
 3. Click on the profile photo  
- **Expected:**
User should be able to upload a picture.
- **Actual:**
  User is not able to upload a picture.
- **Status:** Falied

--

  ### Test Case CM003 - Community Post Author Consistency
 - **Preconditions:** User must have two or more accounts
- **Steps to Reproduce:**
 1. Log in with first account
 2. Navigate to community page
 3. Make a post on the community
 4. Observe post author
 5. Log out from first account
 6. Log in with a new account
 7. Navigate to community page
 8. Observe post author 
- **Expected:**
Author should be addressed as first account.
- **Actual:**
  New account inherits the author tittle of post.
- **Status:** Falied

  ---

    ### Test Case CM004 - Check User Stats and History 
 - **Preconditions:** User has registered  and logged  in with an account
- **Steps to Reproduce:**
 1. Post a blog on the community page 
 2. Navigate to the profile
 3. Observe post history and achievements 
- **Expected:**
User post history and achievements should be visible.
- **Actual:**
  User history and achievements are not shown.
- **Status:** Falied

---

  ### Test Case CM005 - Follow a Community Member
 - **Preconditions:** User has registered  and logged  in with an account
- **Steps to Reproduce:**
 1. Navigate to community page
 2. Follow a community member 
- **Expected:**
User should be able to follow any community member.
- **Actual:**
  User is not able to follow any community member.
- **Status:** Falied

---


