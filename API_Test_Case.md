#Positive Testcase

Scenario	              Preconditions	                                           Expected Result
Create                  lead with valid data	                                   Valid token	201 Created / 200 OK
Minimal                 required fields	Valid token	                             Lead created successfully
Response                validation	Valid request	Response                       contains created lead data

#Negative Testcase

Scenario	              Request                           Issue	                     Expected                Result
Missing                 name	                            No name	                   400                     Bad Request
Missing                 email	                            No email	                 400                     Bad Request
Invalid                 email                             format	                   "abc"	                 Validation error
Empty                   request                           body	                     {}	400                  Bad Request
Invalid                 data                              types	                     isQualified: "yes"	     Validation error


#Authrization TestCase 

Scenario	              Expected Result
Missing token	          401 Unauthorized
Invalid token	          401 Unauthorized



#Edge Cases - 

Scenario	                                   Expected Result
Duplicate email	                             Error or handled gracefully
Very long name	                             Validation error or truncation
Special characters in name	                 Accepted or validated properly
Boolean fields variations	                   Accept only true/false
Large payload	                               System handles gracefully

#Full Flow - 

Scenario	                          Steps	                                                                                  Expected Result
Full flow:                          Login → Create → Fetch	1. Login 2. Create lead 3. Get leads	                          Lead appears in list



#Validation Checklist

- Status codes are correct
- Response time is acceptable (<2s assumed)
- JSON structure is valid
- Required fields are present
- No sensitive data exposed


GET /api/leads
POST /api/leads









