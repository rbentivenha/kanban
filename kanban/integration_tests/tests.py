import json

from graphene_django.utils.testing import GraphQLTestCase

class QueriesTest(GraphQLTestCase):
    GRAPHQL_URL = '/graphql'
    GRAPHQL_SCHEMA = 'kanban.schema.schema'

    def test_some_query(self):
        response = self.query(
            '''
                query {
                    hello
                }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)