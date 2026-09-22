from ayoris.core import *

def test_health():assert create_app().openapi()["info"]["title"]=="Ayoris"
