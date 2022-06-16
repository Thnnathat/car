from fastapi import FastAPI
import uvicorn
from activity import Activity

app = FastAPI()
activity = Activity()

@app.get("/car/values_gyro")
async def values_gyro():
    data = activity.select_all("x","y","z" ,table_name="values_gyro")
    return data

@app.get("/car/status_gyro")
async def status_gyro():
    data = activity.select_all("status",table_name="status_gyro")
    return data

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
    