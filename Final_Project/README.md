✅ Project Title:
Multi-Country Data Pipeline with Conditional Child Triggering using Azure Data Factory

🔧 Tools Required:
Azure Data Factory

Azure Data Lake Storage Gen2

Azure SQL Database (for simulating DB data)

REST API (https://restcountries.com/v3.1/name/{name})

Postman (for initial testing of API)

Dataset Creation using mock data for Customer and Product tables (can be provided in CSV or SQL format)

🧾 Problem Statement Breakdown & Solution:
📌 1. Fetch Country Data from API and Save to JSON Files
✔ Steps:
Use Web activity in ADF to call the REST API:

bash
Copy
Edit
https://restcountries.com/v3.1/name/{Country}
Use ForEach activity to loop through countries: ["india", "us", "uk", "china", "russia"].

Inside the loop:

Use Web Activity to fetch API.

Use Copy Activity to save the output to ADLS in JSON format.

Filename should be like india.json, us.json, etc.

✔ Datasets:
Source: REST API (via Web activity)

Sink: ADLS Gen2 (Linked Service required)

📌 2. Add Trigger to Run Pipeline 2 Times a Day
✔ Steps:
Go to Triggers > New/Edit > Schedule Trigger

Set the Recurrence to Daily

Choose time:

12:00 AM IST

12:00 PM IST

Attach this trigger to the country data pipeline.

📌 3. Create Conditional Pipeline for Customer Data (>500 Records)
✔ Steps:
Create a Stored Procedure in Azure SQL to return Customer Count.

In ADF:

Use Lookup Activity or Stored Procedure Activity to get customer count.

Use If Condition Activity:

If count > 500:

Copy Customer data from DB to ADLS.

Also, check: if count > 600 → Trigger child pipeline.

✔ Child Pipeline:
Takes count as parameter.

If invoked → Copies product data to ADLS.

📌 4. Pass Count as Parameter to Child Pipeline
✔ Steps:
In parent pipeline:

Use Execute Pipeline activity to call child pipeline.

Pass parameter customerCount with value from lookup/stored procedure.

In child pipeline:

Use @pipeline().parameters.customerCount for any logic or naming.

📁 Datasets Needed:
1. Customer Table Dataset (Mock Data)
csv
Copy
Edit
CustomerID, Name, Email, Country
1, Alice, alice@mail.com, US
2, Bob, bob@mail.com, UK
...
2. Product Table Dataset
csv
Copy
Edit
ProductID, ProductName, Price
101, Laptop, 600
102, Phone, 200
...
You can simulate these using:

Azure SQL Database

Or upload CSV to Azure Blob/ADLS and use as source

🏗 Folder Structure on ADLS:
bash
Copy
Edit
/raw/
    /countries/
        india.json
        us.json
        ...
    /customers/
        customer_data_2025-07-23.json
    /products/
        product_data_2025-07-23.json
🔁 Summary Flow:
CountryPipeline
→ Loop 5 countries
→ Fetch via REST API
→ Save as JSON

CustomerPipeline
→ Check count > 500
→ Copy to ADLS
→ If count > 600 → call ProductChildPipeline

ProductChildPipeline
→ Takes customer count as parameter
→ Copies Product Data

