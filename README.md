*# Retail ML Monitoring Project*



*## Project Overview*



*This project demonstrates an end-to-end Machine Learning Monitoring pipeline using SQL, Python, Scikit-learn, and Arize.*



*The application performs the following tasks:*



*- Reads retail data from MySQL.*

*- Uses a trained Machine Learning model to generate predictions.*

*- Uploads prediction data to Arize.*

*- Creates monitoring modules using Separation of Concerns (SoC).*

*- Exports monitor information into SQL.*



*---*



*## Technologies Used*



*- Python*

*- MySQL*

*- Pandas*

*- SQLAlchemy*

*- Scikit-learn*

*- Arize SDK*



*---*



*## Project Structure*



*```text*

*Retail\_ML\_Monitoring\_Project*

*│*

*├── config*

*├── database*

*├── data*

*├── ingestion*

*├── monitoring*

*├── arize\_to\_sql*

*├── models*

*├── docs*

*├── notebooks*

*```*



*---*



*## How to Run*



*### Activate Virtual Environment*



*```bash*

*.\\venv\\Scripts\\activate*

*```*



*### Run Model Ingestion*



*```bash*

*python -m ingestion.model\_ingestion*

*```*



*### Run Monitoring Script*



*```bash*

*python -m monitoring.create\_monitors*

*```*



*### Export Monitor Data*



*```bash*

*python -m arize\_to\_sql.monitor\_export*

*```*



*---*



*## SQL Verification*



*```sql*

*SELECT \* FROM retail\_view;*



*SELECT \* FROM arize\_monitor\_data;*

*```*



*---*



*## Project Status*



*- SQL Database Created*

*- Machine Learning Model Developed*

*- Data Ingested into Arize*

*- Monitoring Module Implemented*

*- Monitor Data Exported to SQL*



*---*



*## Author*



*\*\*Naina Kose\*\**

