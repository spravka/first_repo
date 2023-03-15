*** Settings ***
Library  SeleniumLibrary

*** Variables ***
#${}
#@
#&
${error_message}

*** Keywords ***
Poprawne Logowanie
    Open Browser  https://pl.wikipedia.org  chrome
    Wait Until Element Is Visible  pt-login  3  Mamy blad
    Click Element  pt-login
    ${my_value}  Get Text  pt-login
    Should Be Empty  ${my_value}
    Input Text  wpName1  RobotTests
    ${my_value}  Get Text  //*[@id="wpPassword1"]
    Should Be Empty  ${my_value}
    Input Text  //*[@id="wpPassword1"]  RobotFramework
    Checkbox Should Not Be Selected  wpRemember
    select checkbox  wpRemember
    click button  wploginAttempt
    Capture Page Screenshot  screen.png
    Close Browser


*** Test Cases ***
#Niepoprawne Logowanie
#    Open Browser  https://pl.wikipedia.org  chrome
#    Wait Until Element Is Visible  pt-login  3  Mamy blad
#    Click Element  pt-login
#    ${my_value}  Get Text  pt-login
#    Should Be Empty  ${my_value}
#    Input Text  wpName1  RobotTests
#    ${my_value}  Get Text  //*[@id="wpPassword1"]
#    Should Be Empty  ${my_value}
#    Input Text  //*[@id="wpPassword1"]  RobotFramework
#    Checkbox Should Not Be Selected  wpRemember
#    select checkbox  wpRemember
#    click button  wploginAttempt
#    Wait Until Element Is Visible  //*[@id="userloginForm"]/form/div[1]  3
#    ${my_error_message}  Get Text  //*[@id="userloginForm"]/form/div[1]
#    Log To Console  ${my_error_message}
#    Log  ${my_error_message}
#    should be equal as strings  ${my_error_message}  ${error_message}
#    Capture Page Screenshot  screen.png
#    Close Browser

Poprawne Logowanie
    Open Browser  https://pl.wikipedia.org  chrome
    Wait Until Element Is Visible  pt-login  3  Mamy blad
    Click Element  pt-login
    ${my_value}  Get Text  pt-login
    Should Be Empty  ${my_value}
    Input Text  wpName1  RobotTests
    ${my_value}  Get Text  //*[@id="wpPassword1"]
    Should Be Empty  ${my_value}
    Input Text  //*[@id="wpPassword1"]  RobotFramework
    Checkbox Should Not Be Selected  wpRemember
    select checkbox  wpRemember
    click button  wploginAttempt
    Capture Page Screenshot  screen.png
    Close Browser