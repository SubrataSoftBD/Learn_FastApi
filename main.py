from fastapi import FastAPI
from scalar_fastapi import  get_scalar_api_reference

app = FastAPI()


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