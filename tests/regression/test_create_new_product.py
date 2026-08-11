import pytest

class TestCreateNewProduct:

    @pytest.mark.regression
    def test_create_new_product(self,authenticated_product_service):

        details_page=authenticated_product_service.create_product("Bomber Jacket", 60)

        details_page.is_product_details_page_loaded()

        
        
    

    