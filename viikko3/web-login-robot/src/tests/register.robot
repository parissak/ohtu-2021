*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page


*** Test Cases ***
Register With Valid Username and Password
    Register With Username And Password  validname  validpass12  validpass12
    Register Should Succeed

Register With too Short Username And Valid Password
    Register With Username And Password  ab  validpass12  validpass12  
    Register Should Fail With Message  Error with username
 
Register With Valid Username And Too Short Password 
    Register With Username And Password  validnameb  pass  pass
    Register Should Fail With Message  Error with password  

Register With Nonmatching Password And Password Confirmation
    Register With Username And Password  validnamec  validpass12  nope
    Register Should Fail With Message  Error with password confirmation

Login After Successful Registration
    Register With Username And Password  validnamed  validpass12  validpass12
    Go To Login Page
    Login With Username And Password  validnamed  validpass12
    Login Should Succeed

Login After Failed Registration
    Register With Username And Password  validnamee  nonvalid  nonvalid
    Go To Login Page
    Login With Username And Password  validnamee  nonvalid
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open 
    Page Should Contain  ${message}

Register With Username And Password
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Input Text  username  ${username}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password_confirmation}
    Click Button  Register