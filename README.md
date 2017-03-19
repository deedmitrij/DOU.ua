# DOU.ua
Autotests for DOU on Python:

Steps 1. Calendar.
1) Click "Calendar" from the Main page
2) Click "Add an event" from the Calendar page
3) Fill "Test" in the "Event title" field
4) Fill "500" in the "Price" field
5) Fill "Kyiv" in the "Location" field
6) Fill "Test" in the "Event description" field
7) Click "Send"
Expected result: Text "Событие было отправлено на проверку модераторам сайта".

Steps 2. JOBS search.
1) Click "JOBS" from the Main page
2) Choose in Jobs list field "QA"
3) Enter "Київ" in Search field
4) Set "Search in vacancy descriptions"
5) Click "Find"
Expected result: Header contains number of jobs (first digits from the left till next Space symb").

Steps 3. SALARIES.
1) Click "SALARIES" from the Main page
2) Choose in City field "All Ukraine"
3) Choose in Position field "Junior QA Engineer"
4) Choose Automation QA
Expected result: Field in "I квартиль " is not null.

