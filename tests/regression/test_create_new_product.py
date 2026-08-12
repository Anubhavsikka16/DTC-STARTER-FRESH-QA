import pytest
from framework.utils.testdata import generate_product_data
from framework.utils.testdata import generate_product_data

class TestCreateNewProduct:

    @pytest.mark.regression
    def test_create_new_product(self,authenticated_product_service, product_repository):
        product=generate_product_data()

        details_page=authenticated_product_service.create_product(product["title"],
                            product["usd_price"]
                        )

                    
                

        details_page.is_product_details_page_loaded()
        product_id = details_page.get_product_id()

        db_product = product_repository.get_product(
            product_id
        )
        assert db_product is not None
        assert db_product[0] == product_id
        assert db_product[1] == product["title"]
        

        
        
    

    