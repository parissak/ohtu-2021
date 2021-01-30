*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login With Username And Password
    [Arguments]  ${username}  ${password}
    Input Text  username  ${username}
    Input Password  password  ${password}
    Click Button  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}