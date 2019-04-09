#!/bin/bash

# Start server in testing mode
cd ../
python serviceHandler.py -test&
sleep 5
cd tests
rm -r test_out
mkdir test_out
# Check if menu section is intially empty
curl -X GET http://127.0.0.1:6000/menusection > test_out/TestOut_1
# Insert menu sections
curl -X POST http://127.0.0.1:6000/menusection -H 'Content-Type: application/json' -d '{"name":"Dinner Menu"}' > test_out/TestOut_2
curl -X POST http://127.0.0.1:6000/menusection -H 'Content-Type: application/json' -d '{"name":"Lunch Menu Basic"}' > test_out/TestOut_3
curl -X POST http://127.0.0.1:6000/menusection -H 'Content-Type: application/json' -d '{"name":"Breakfast Menu"}' > test_out/TestOut_4
curl -X POST http://127.0.0.1:6000/menusection -H 'Content-Type: application/json' -d '{"name":"Lunch Menu Diet"}' > test_out/TestOut_5
# Check if inserted menu sections are available
curl -X GET http://127.0.0.1:6000/menusection  > test_out/TestOut_6
# Edit exisiting menu
curl -X PUT http://127.0.0.1:6000/menusection/2  -H 'Content-Type: application/json' -d '{"name":"Lunch Menu Standard"}' > test_out/TestOut_7
# View updated menu
curl -X GET http://127.0.0.1:6000/menusection > test_out/TestOut_8
# View Specific Menu 
curl -X GET http://127.0.0.1:6000/menusection/3  > test_out/TestOut_9
# View Menu not present
curl -X GET http://127.0.0.1:6000/menusection/5  > test_out/TestOut_10
# Attempt update of menu section not present
curl -X PUT http://127.0.0.1:6000/menusection/7  -H 'Content-Type: application/json' -d '{"name":"Lunch Menu Standard"}' > test_out/TestOut_11
# Delete menu section
curl -X DELETE http://127.0.0.1:6000/menusection/1 -H 'Content-Type: application/json'  -d '{"name":"lunch"}' > test_out/TestOut_12
# Attempt deletion of menu section not present
curl -X DELETE http://127.0.0.1:6000/menusection/8 -H 'Content-Type: application/json'  -d '{"name":"lunch"}' > test_out/TestOut_13
# Attempt menu addition with malformed body
curl -X POST http://127.0.0.1:6000/menusection -H 'Content-Type: application/json' -d '{"name":"Dinner Menu","Price":"100"}' > test_out/TestOut_14