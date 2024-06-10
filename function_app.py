import azure.functions as func
import logging
import csv
import json

app = func.FunctionApp()

def calculate_net_order_amount(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")


@app.blob_trigger(arg_name="myblob", path="salesrecordsbabatunde/{name}.csv", connection="logicappsrg910e_STORAGE") 
@app.blob_output(arg_name="outputblob", path="salesrecordsbabatunde/out.json", connection="logicappsrg910e_STORAGE")
def process_csv_sales_report(myblob: func.InputStream, outputblob: func.Out[str]):
    file_name = "new_file_name"
    filecontent = myblob.read().decode('utf-8') 
    lines = filecontent.split("\n")

    reader = csv.DictReader(lines)

    total_sales = 0.0

    for row in reader:
        total_sales += float(row['Order Total (USD)'])

    logging.info(f"Python blob trigger function processed blob\n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes\n"
                 f"Total Sales: ${total_sales:.2f}\n")

    outputblob.set(json.dumps({
        "date" : "10/06/2024",
        "new sales amount" : 3803.34
    }))

    print(f"Total Sales: ${total_sales:.2f}")