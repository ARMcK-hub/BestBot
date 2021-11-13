# BestBot
A hastily written Webscan Bot that notifies when a product is in stock on a webstore.

<!--

To Execute:
docker start <container_name>
docker exec -it <container_name> python bestbot.py

0. lookup notify data -> err if none
1. for each, create notify objects
- notify method (phone:number, email: @)
2. lookup products -> notify err if none/issue
3. for each, create item objects with metadata
- name
- id
- store
- filters (max price, new/used, ship price, ship date)
4. sort items for optimal runtime
-- can only execute full loop 1/sysminute, can only check store 1/3 sec
-- sort by priority (most interested searched for 1st)
5. create executors for each item (based on store)
- store item lookup method
- store parse data method
- store cart add method
- store filter methods
6. create / set multithreads
7. loop through executors for availability
-a request site data
-b parse for key vars (availability, name, id, filters)
-c validate availability
-d validate other filters
-e for each, push notifications with add cart method - indicate some filters not met (requires user to be logged into recieving device)

-->
