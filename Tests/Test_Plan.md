# Test Plan: CleanCity -Waste Pickup.
**Group Name:** The Preservation

**Date:** 15-07-2025

**Scheduler:** Test Strategy (Week 1)

---

## Scope and Objectives

### Scope:
In the span of this testing cycle , we will cover tests for:

- Authentication System
- Waste Management
- Dashboard and Analytics
- Content Management
- Community Features
- Administrative Functions
- Non Functional Testing

### Objectives:
Verify that:
- [x] Users can register and login with the correct credentials
- [ ] Users can Schedule a waste pickup request
- [x] Users can access community and post blogs
- [ ] Admins can track and monitor any waste pickup request
- [ ] Users track any waste pickup request they made

---

## Test Environment and Tools
### Test Environments
- Browsers: Chrome, Firefox, Safari, Edge
- Devices: Desktop (Windows, macOS), Mobile (Android, iOS)
- Network: 3G, 4G, WiFi

### Group Member: Lerato Moloi
> **Testing Device:** Laptop
> 
> **Browser Used:** Microsoft Edge
> 
> **Network Conditions:** Fibre Wifi
> 
> **Testing Tools:** SonarQube

### Group Member: Tosin A. Williams
> **Testing Device:** laptop window 10
> 
> **Browser Used:** Chrome
> 
> **Network Conditions:** WiFi
> 
> **Testing Tools:** DevTools

### Group Member: Thandolwethu L. Ndhlovu
> **Testing Device:** Laptop Lenovo Latitude`7490`
> 
> **Browser Used:** Chrome
> 
> **Network Conditions:** Fibre WiFi
> 
> **Testing Tools:** DevTools, Jest

---

## Defect Reporting Standard
### Bug Report Template
```markdown
**Title**: Login with Invalid Credentials Shows No Feedback
**Description**: Logging in with invalid credentials does not give an Error message and instead resets the form.
**Environment**: Chrome Desktop
**Steps to Reproduce**:  
1. Go to login page  
2. Enter invalid credentials 
3. Click Login 

**Expected**: A clear error message appears  
**Actual**: Nothing happens, and the form resets  
**Severity**: Major 
**Priority**: High
```
### Testing Types
 Type             | Focus Areas |
|------------------|-------------|
| Functional       | Core features, input validations |
| Usability        | Navigation flow, UI clarity |
| Performance      | Page load times, responsiveness |
| Compatibility    | Cross-browser & responsive testing |
| Accessibility    | WCAG 2.1, screen reader support |
| Security         | Input sanitization, localStorage data handling |


### Test Roles
Refer to the [Test_Roles.md](https://github.com/the7thsage376/CleanCity/blob/main/Tests/Test_roles.md) file.



End of Test_Plan

