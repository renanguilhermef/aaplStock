# Requirements
Script works on both OS (Linux / Windows). It's necessary to have:
  - Python3 and pip module 
  - Oracle instant client. Download according with your OS:
  	-  Windows: https://www.oracle.com/br/database/technologies/instant-client/downloads.html
  	-  Linux: https://docs.oracle.com/en/database/oracle/oracle-database/21/lacli/install-instant-client-using-rpm.html
  - Oracle database
 
 Install required modules
 
 	python3 -m pip install -r requirements.txt
# pre-execution
go to db/db_params.yml and fill up with desired database to connect

  - Username: user to connect on the database
  - Password: database user password
  - Client: Oracle Instant Client path
  - Connection: your oracle database connection string. Recommended: Set your TNS configuration to the Oracle instant client path.
	- Types: TNS alias, TNS string or Easy connection
	
	
		TNS alias:
				
				connection: <TNS_ALIAS>
	
		TNS string:
				
				connection: (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=<HOSTNAME>)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=<SERVICE_NAME>)))
				
		Easy connection:
		
				connection: <hostname>:<port>/<service_name>
# Execute
In your prefered command line, run :

	python3 aapl_stocks_report.py
