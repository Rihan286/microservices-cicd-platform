import sys

sys.path.insert(0, "services/user-service")
from app import app as user_app

sys.path.pop(0)
sys.path.insert(0, "services/product-service")
from app import app as product_app

sys.path.pop(0)
sys.path.insert(0, "services/order-service")
from app import app as order_app

sys.path.pop(0)
sys.path.insert(0, "services/notification-service")
from app import app as notification_app


def test_user_service():
    client = user_app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_product_service():
    client = product_app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_order_service():
    client = order_app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_notification_service():
    client = notification_app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"