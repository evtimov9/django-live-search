import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Company
from django.db.models import Q


class LiveSearchConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        query_data = json.loads(text_data)
        query = query_data.get("query", "").strip()

        if len(query) < 3:
            self.send(text_data=json.dumps({"results": []}))
            return

        companies = Company.objects.filter(
            Q(name__icontains=query) |
            Q(country__icontains=query) |
            Q(industry__icontains=query) |
            Q(founded_year__icontains=query) |
            Q(details__company_type__icontains=query) |
            Q(details__size__icontains=query) |
            Q(details__ceo_name__icontains=query) |
            Q(details__headquarters__icontains=query) |
            Q(financials__year__icontains=query) |
            Q(financials__revenue__icontains=query) |
            Q(financials__net_income__icontains=query)
        ).distinct()

        results = []
        for company in companies:
            results.append({
                "name": company.name,
                "country": company.country,
                "industry": company.industry,
                "founded_year": company.founded_year,
                "ceo": company.details.ceo_name if hasattr(company, "details") else "N/A",
            })

        self.send(text_data=json.dumps({"results": results}))
