*** Settings ***
Library    library_keywords.py

*** Variables ***
${USER1_NAME}           John
${USER2_NAME}           Jane
${BOOK1_NAME}           The Raven
${BOOK1_AUTHOR}         Edgar Allan Poe
${BOOK1_PAGES}          6
${BOOK1_ISBN}           9788506007914
${BOOK2_NAME}           Faust, a Tragedy
${BOOK2_AUTHOR}         Johann Wolfgang von Goethe
${BOOK2_PAGES}          165
${BOOK2_ISBN}           1503262146

*** Test Cases ***
Test Book Pages Amount
    [Documentation]    Test to check the work of 'get_pages' function
    Log To Console     Test 1. Verify work of "get_pages" function
    ${book1}    Create Book    ${BOOK1_NAME}    ${BOOK1_AUTHOR}    ${BOOK1_PAGES}    ${BOOK1_ISBN}
    ${pages}    Get Pages    ${book1}
    Should Be Equal As Numbers    ${pages}    ${BOOK1_PAGES}   6

Test Book ISBN
    [Documentation]    Test to check if the ISBN is correct for "Faust, a Tragedy"
    Log To Console     Test 2. Verify work of "get_isbn" function
    ${book2}    Create Book    ${BOOK2_NAME}    ${BOOK2_AUTHOR}    ${BOOK2_PAGES}    ${BOOK2_ISBN}
    ${isbn}    Get Isbn    ${book2}
    Should Be Equal As Numbers    ${isbn}    1503262146

Test Reserve Book
    [Documentation]    Test to check if a book can be reserved
    Log To Console     Test 3. Verify return after book reservation
    ${book1}    Create Book    ${BOOK1_NAME}    ${BOOK1_AUTHOR}    ${BOOK1_PAGES}    ${BOOK1_ISBN}
    ${user1}    Create User    ${USER1_NAME}
    ${message}    Reserve Book    ${user1}    ${book1}
    Should Be Equal    ${message}    You've reserved 'The Raven' by Edgar Allan Poe

Test Is Book Reserved
    [Documentation]    Test to check if a book is reserved
    Log To Console     Test 4. Verify that book is reserved
    ${book1}    Create Book    ${BOOK1_NAME}    ${BOOK1_AUTHOR}    ${BOOK1_PAGES}    ${BOOK1_ISBN}
    ${user1}    Create User    ${USER1_NAME}
    Reserve Book    ${user1}    ${book1}
    ${reserved}    Is Book Reserved    ${book1}
    Should Be True    ${reserved}

Test Reserved Book
    [Documentation]    Test to check if a book already reserved by another user
    Log To Console     Test 5. Verify return if book is already reserved by another user
    ${book2}    Create Book    ${BOOK2_NAME}    ${BOOK2_AUTHOR}    ${BOOK2_PAGES}    ${BOOK2_ISBN}
    ${user1}    Create User    ${USER1_NAME}
    ${user2}    Create User    ${USER2_NAME}
    Reserve Book    ${user1}    ${book2}
    ${message}    Reserve Book    ${user2}    ${book2}
    Should Be Equal    ${message}    'Faust, a Tragedy' by Johann Wolfgang von Goethe is reserved by another user

Test Return Book
    [Documentation]    Test to check if a book can be returned
    Log To Console     Test 6. Verify return of the "return_book" function
    ${book1}    Create Book    ${BOOK1_NAME}    ${BOOK1_AUTHOR}    ${BOOK1_PAGES}    ${BOOK1_ISBN}
    ${user1}    Create User    ${USER1_NAME}
    Reserve Book    ${user1}    ${book1}
    ${message}    Return Book    ${user1}    ${book1}
    Should Be Equal    ${message}    You've returned 'The Raven' by Edgar Allan Poe

Test Returned Book
    [Documentation]    Test to check if a book already returned
    Log To Console     Test 7. Verify return of the "return_book" if book has been already returned
    ${book2}    Create Book    ${BOOK2_NAME}    ${BOOK2_AUTHOR}    ${BOOK2_PAGES}    ${BOOK2_ISBN}
    ${user2}    Create User    ${USER2_NAME}
    Reserve Book    ${user2}    ${book2}
    Return Book    ${user2}    ${book2}
    ${message}    Return Book    ${user2}    ${book2}
    Should Be Equal    ${message}    This book is free, nothing to return