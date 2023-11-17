QUERY = '''
query Query {
    search(storeId: %s) {
            products(from: 0, size: 100, fieldFilters: [ {field: "category_id", value: "413620" }, {field: "stocks.eshop_availability", value: "true"}]) {  
              products {
                article
                name
                url
                stocks {
                    prices {
                        price
                        old_price
                        discount
                    }
                }
                manufacturer {
                    name
                }
              }
            }
          }
        }
'''
STORES = {
    'Санкт-Петербург, пр-т Косыгина, д.4, лит. А': 16,
    'Москва, Ленинградское ш., д.71Г': 10
}
