## Defect-log
  

### Bug report [ WM003 ]

**Title**: Homepage Feature Cards Show Hover Effect but Are Not Clickable

**Description**: The “Easy Scheduling,” “Dashboard,” and “Blog & Community” feature cards on the homepage appear interactive (with hover effect), but clicking them does not trigger any navigation or action.

**Environment**: Chrome

**Severity**: Minor

**Priority**: Medium


**Steps To Reproduce**:

Launch the app on http://localhost:3000.

Scroll to the feature card section.

Hover over each card and click on them.

**Expected Result**:

Cards should navigate to their corresponding pages when clicked.

Actual Result:
No response or navigation occurs when the cards are clicked.
---

### Bug report [ DA002 ]

**Title**:Scheduled Waste Pickup Not Reflected on Dashboard


**Description**: When a user successfully submits a pickup request through the scheduling form, the request does not appear on the dashboard as expected.

**Environment**: Chrome

**Severity**: Major

**Priority**: High


**Steps To Reproduce**:

Navigate to the Schedule Pickup page.

Fill in all fields correctly.

Submit the form.

Go to the Dashboard to verify request history.


**Expected Result**:
New pickup request should be displayed or reflected in the dashboard's list or statistics.

**Actual Result**:
Dashboard remains empty  no visible record of the submission.



---

### Defect ID: D-001

**Title:** Inconsistent App URL Handling

**Description:**
When the CleanCity application is opened using the VS Code Live Server (`http://127.0.0.1:5500`), user actions such as scheduling a waste pickup do not reflect on the dashboard. However, when the app is launched via `npm start` using React scripts (`http://localhost:3000`), all features and data interactions behave as expected.

**Steps to Reproduce:**

1. Start the application using `npm start`.
2. Observe that the app runs at `http://localhost:3000`.
3. Instead, open the app via VS Code Live Server which launches at `http://127.0.0.1:5500`.
4. Attempt to register, schedule a pickup, or perform any data-driven task.
5. Login to dashboard and observe that scheduled pickups are missing.

**Expected Result:**

* All user actions (e.g., scheduling pickups) should reflect in the dashboard regardless of which local server is used.

**Actual Result:**

* Data does not persist or reflect properly when the app is opened via Live Server.

**Evidence (Screenshots):**

* 📸 **Screenshot 1:** App running at `http://localhost:3000` with full feature access and correct behavior.
  ![localhost-app](../screenshots/Screenshot%20\(753\).png)
* 📸 **Screenshot 2:** App running at `http://127.0.0.1:5500/index.html` with form displayed, but backend functionality (e.g., scheduling pickup) not reflected.
  ![liveserver-app](../screenshots/Screenshot%20\(752\).png)

**Severity:** Critical
**Priority:** High
**Status:** Open
**Logged By:** Tosin A. Williams
**Date:** July 13, 2025


### Defect ID: FR-001 User Registration
**Title**: Register with Incorrect Email Format Does Not Throw Error
**Description**: Logging in with invalid email format does not give an Error message and instead accepts registration.
**Environment**: Chrome Desktop
**Steps to Reproduce**:  
1. Navigate To register page
2. Enter a fullname
3. Enter an email with username@domain without the .com
4. Enter a valid password
5. Click Create account

**Expected**: A clear error for invalid email appears  
**Actual**: System accepts user registration as valid  
**Severity**: Major 
**Priority**: High


### Defect ID: FR-001.2 User Registration
**Title**: User Registration Does Not Contain Phone Number
**Description**: Logging in with invalid email format does not give an Error message and instead accepts registration.
**Environment**: Chrome Desktop
**Steps to Reproduce**:  
1. Navigate To register page
2. Observe lack of phone number field

**Expected**: Registration should contain a field for Phone number  
**Actual**: Registration does not contain a field for Phone number
**Severity**: Minor 
**Priority**: Low


### Defect ID: FR-045 User Profile
**Title**: Unable to Upload Profile Pictures

**Description**: When Editing a profile , a user cannot upload a profile photo.

**Environment**: Chrome Desktop

**Steps to Reproduce**:  
1. Navigate To profile page
2. Click edit profile
3. Click on the profile photo

**Expected**:User should be able to upload a profile picture

**Actual**: User is not able to upload a profile picture
**Severity**: Minor 
**Priority**: Low


### Defect ID: FR-046 User Profile
**Title**: Unable to See User Stats and History

**Description**: When viewing a profile , a user cannot see their stats and History.

**Environment**: Chrome Desktop

**Steps to Reproduce**:  
1. Post a blog on the community page
2. Navigate To profile page
3. Oserve post History and Stats

**Expected**:User should be able view their post history

**Actual**: User is not able to view their post history
**Severity**: Major
**Priority**: Highest


### Defect ID: FR-046 User Profile
**Title**: Unable To Follow Community Members

**Description**: Following other community members is not possible.

**Environment**: Chrome Desktop

**Steps to Reproduce**:  
1. Navigate to the community page
2. Try to follow a community member
**Expected**:User should be able follow other community members

**Actual**: User is not able to follow other community members
**Severity**: Major
**Priority**: High


### Defect ID: FR-046 User Profile
**Title**: User Post Data Inconsistency

**Description**: Any community post or comment made by a user is saved into localStorage wit no linkage to post author.

**Environment**: Chrome Desktop

**Steps to Reproduce**:  
1. Log in with one account
2. Navigate to community page
3. Post or comment on the page
4. Observe post author
5. Log out from fist account
6. Login with new account
7. Navigate to community page
8. Observe post author
**Expected**: Author should be addressed to first account

**Actual**: New account is addressed as author
**Severity**: Critical
**Priority**: Highest
