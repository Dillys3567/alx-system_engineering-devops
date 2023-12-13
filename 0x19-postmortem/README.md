Failed Rating for Call Detail Records Report

Dec 12, 2023

By MyTelco Billing Team

The following is the postmortem report experienced earlier this week with our billing systems.
We are providing a postmortem report that details the failure and our response.

Issue Summary
From 2:00PM to 3:30 PM GMT on 25th November, 2023 no new Call Detail Records(CDR) were rated by the rating engine and
pushed for customers to be billed on their transactions(call, SMS or data). This prompted a system
query showing that table spaces for holding Call Detail Records were maxed out at 100%. This resulted
in delays in bill submission to post paid customers.

Timeline
-3:00PM GMT: Issue detected
Billing team realised no bills were being sent to customers
-3:10PM GMT: Query of systems and backtracing ,
revealed table spaces for Call Detail Records were full
-3:15PM GMT: Billing team frees up space in tables
to allow new Call Detail Records to be stored
-3:30PM GMT: Rating of call records restarts and bills are 
sent to customers

Root cause
Every morning the table spaces are manually checked to ensure that they have not exceeded 80%.
If they have exceeded the table spaces are freed to ensure usage falls below 80%. We are human and 
are prone to mistakes. Besides an early morming check means, drowsy eyes perusing information. An oversight was
made during this manual check that resulted in a table with usage over 80% being over looked and 
not reported for space freeing. The table spaces were freed to resume CDR rating.

Corrective and Preventive Measures
In order to prevent any further pauses in the billing process due to full table space, a cron job running
a script that checks for table usage of all tables essential to the billing process was started. In addition
checking table spaces it was considered important to also check disk spaces on servers. This script also sent
alerts to the Billing team to ensure nothing is overlooked. The team is working on other solutions like:
-Acquiring more space to store CDRs
-Automating the deletion of CDRs that have already been rated to make room for new CDRs

MyTelco is dedicated to providing good service to customers and appreciate their patient in times
of service delays.

Sincerely,

The MyTelco Billing Team.
