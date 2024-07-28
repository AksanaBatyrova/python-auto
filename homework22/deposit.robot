*** Settings ***
Library    deposit_keywords.py

*** Variables ***
${VALID_AMOUNT}         1000
${VALID_TERM}           1
${VALID_RATE}           10
${NEGATIVE_AMOUNT}      -1000
${NEGATIVE_TERM}        -1
${NEGATIVE_RATE}        -10
${NAN_AMOUNT}           Text1000
${NAN_TERM}             Text1
${NAN_RATE}             Text(10)


*** Test Cases ***
Valid Deposit
    [Documentation]    Test to check if output of a function is correct
    Log To Console     Test 1. Verify that program is working correctly with valid data
    ${result}    Deposit    ${VALID_AMOUNT}    ${VALID_TERM}    ${VALID_RATE}
    Should Be Equal As Numbers    ${result}    1104.71

Invalid Amount
    [Documentation]    Test to check if function returns error if amount is below 0
    Log To Console     Test 2. Verify that program return error if amount is negative
    Run Keyword And Expect Error    ValueError: Values should be positive
    ...    Deposit    ${NEGATIVE_AMOUNT}    ${VALID_TERM}    ${VALID_RATE}

Invalid Term
    [Documentation]    Test to check if function returns error if term is below 0
    Log To Console     Test 3. Verify that program return error if term is negative
    Run Keyword And Expect Error    ValueError: Values should be positive
    ...    Deposit    ${VALID_AMOUNT}    ${NEGATIVE_TERM}    ${VALID_RATE}

Invalid Rate
    [Documentation]    Test to check if function returns error if rate is below 0
    Log To Console     Test 4. Verify that program return error if rate is negative
    Run Keyword And Expect Error    ValueError: Values should be positive
    ...    Deposit    ${VALID_AMOUNT}    ${VALID_TERM}    ${NEGATIVE_RATE}

Invalid Type Amount
    [Documentation]    Test to check if function returns error if amount is not a number
    Log To Console     Test 5. Verify that program return error if amount is not a number
    Run Keyword And Expect Error    ValueError: Values should be numbers
    ...    Deposit Strings    ${NAN_AMOUNT}    ${VALID_TERM}    ${VALID_RATE}

Invalid Type Term
    [Documentation]    Test to check if function returns error if term is not a number
    Log To Console     Test 6. Verify that program return error if term is not a number
    Run Keyword And Expect Error    ValueError: Values should be numbers
    ...    Deposit Strings    ${VALID_AMOUNT}    ${NAN_TERM}    ${VALID_RATE}

Invalid Type Rate
    [Documentation]    Test to check if function returns error if rate is not a number
    Log To Console     Test 7. Verify that program return error if rate is not a number
    Run Keyword And Expect Error    ValueError: Values should be numbers
    ...    Deposit Strings    ${VALID_AMOUNT}    ${VALID_TERM}    ${NAN_RATE}
