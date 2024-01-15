from fastapi import APIRouter

landing_router = APIRouter(prefix="/landing")


@landing_router.get("/text-sections")
async def text_sections():
    return {"section1": "Mock Text 1", "section2": "Mock Text 2"}


@landing_router.get("/revenue-chart")
async def revenue_chart():
    mock_data = [{"x": 1, "y": 100}, {"x": 2, "y": 200}, {"x": 3, "y": 300}]
    return {"data": mock_data}
