# Requirements
Script works on both OS (Linux / Windows). It's necessary to have:
  - Python3 and pip module 
  - Oracle instant client with oracle libraries. Download according with your OS:
  	-  https://www.oracle.com/br/database/technologies/instant-client/downloads.html
  - Oracle database
 
 Install required modules in your env
 
 	python3 -m pip install -r requirements.txt
# pre-execution
go to db/db_params.yml and fill up with desired database to connect

  - Username: user to connect on the database
  - Password: database user password
  - oracle_lib: set unarchived Oracle Instant Client path. In case of using your own Oracle Client, make sure to point to your Lib folder
  - Connection: your oracle database connection string
	- Types: TNS alias, TNS string or Easy connection
	
	
		TNS alias: Set your TNS configuration in the <oracle_lib>/network/admin
				
				connection: <TNS_ALIAS>
	
		TNS string:
				
				connection: (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=<HOSTNAME>)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=<SERVICE_NAME>)))
				
		Easy connection:
		
				connection: <hostname>:<port>/<service_name>
# Execute
On the script folder, in your prefered command line, run :

	python3 aapl_stocks_report.py
