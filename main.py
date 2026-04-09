
from typing import Any
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import  get_scalar_api_reference

app = FastAPI()


profileData = {
    12701: {
        "name": "John",
        "age": 30,
        "status": "Alive"
    },
    12702: {
        "name": "Alice",
        "age": 25,
        "status": "Alive"
    },
    12703: {
        "name": "Robert",
        "age": 40,
        "status": "Deceased"
    },
    12704: {
        "name": "Emma",
        "age": 35,
        "status": "Alive"
    },
    12705: {
        "name": "David",
        "age": 28,
        "status": "Missing"
    },
    12706: {
        "name": "Sophia",
        "age": 22,
        "status": "Alive"
    },
    12707: {
        "name": "Michael",
        "age": 50,
        "status": "Deceased"
    }
}

@app.get("/details/latest")
async  def get_latest_data() -> dict[str, str | dict[str, str | int]]:
    id = max(profileData.keys())
    return {
        "status": "Success",
        "data": profileData[id]
    }
# @app.get("/details/{id}")
# async  def get_data(id: int) -> dict[str, str | dict[str, str | int]]:
#     if id not in profileData:
#         return {"status": "Error", "message": "Profile not found"}
#     return ({
#         "status": "Success",
#         "data": profileData[id]
#     }
#Query Params:
@app.get("/details")
async  def get_data_with_params(id: int) -> dict[str, str | dict[str, str | int]]:
    if id not in profileData:
        raise  HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    return {
        "status": "Success",
        "data": profileData[id]
    }
@app.post("/details")
# async  def post_data(name: str, age: int):
async  def post_data(data: dict)-> dict[str, Any]:
    return data
    if age < 18:
        raise  HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail="Age must be greater than 18"
        )
    new_id = max(profileData.keys()) + 1
    profileData[new_id] = {"name": name, "age": age, "status": "Alive"}
    return {
        "status": "Success",
        "data": profileData[new_id]
    }

@app.get("/details/{field}")
async  def get_data_by_field(field: str, id: int):
    return profileData[id][field]

@app.get("/new-shipment")
def get_shipment():
    return {
        "status": "Success",
        "data": "Nice to meet you"
    }


@app.get("/scalar", include_in_schema=False)
def get_scalar_doc():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API Reference",
    )

#Path Params:
@app.get("/path/{id}")
async  def get_data(id) -> dict[str, int]:
    return {
        "id": id
    }