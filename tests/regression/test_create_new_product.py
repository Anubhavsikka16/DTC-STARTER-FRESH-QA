import pytest

class TestCreateNewProduct:

    @pytest.mark.regression
    def test_create_new_product(self,product_service):

        details_page=product_service.create_product("Bomber Jacket", 60)

        details_page.is_product_details_page_loaded()

        
        
    

    