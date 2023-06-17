from rest_framework.response import Response
from rest_framework import viewsets



class SentimentAnalysisViewSet(viewsets.ViewSet):
    def create(self, request):
        # {
        #     'text': 'hello'
        # }
        response_data = {
            'sentiment': 'coming-soon',
        }

        return Response(response_data)
