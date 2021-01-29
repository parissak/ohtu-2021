*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  username  password12
    Output Should Contain  New user registered

Register With Already Taken Username
    Input Credentials  alreadytaken  password12
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  ab  password12
    Output Should Contain  Error with username

Register With Valid Username And Too Short Password
    Input Credentials  username  short1
    Output Should Contain  Error with password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  username  12345678
    Output Should Contain  Error with password

*** Keywords ***
Create User And Input New Command
    Create User  alreadytaken  password12
    Input New Command