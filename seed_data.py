from live_search_app.models import Company, CompanyDetails, FinancialData
import random

companies = [
    ("Apple Inc.", "USA", "Technology", 1976),
    ("Toyota", "Japan", "Automotive", 1937),
    ("Amazon", "USA", "E-commerce", 1994),
    ("BMW", "Germany", "Automotive", 1916),
    ("Sony", "Japan", "Electronics", 1946),
]

for name, country, industry, founded in companies:
    company = Company.objects.create(
        name=name,
        country=country,
        industry=industry,
        founded_year=founded
    )

    CompanyDetails.objects.create(
        company=company,
        company_type="Public" if random.choice([True, False]) else "Private",
        size=random.choice(["Small", "Medium", "Large"]),
        ceo_name=f"CEO {name.split()[0]}",
        headquarters=f"{country} HQ"
    )

    for year in range(2020, 2024):
        FinancialData.objects.create(
            company=company,
            year=year,
            revenue=random.uniform(1000, 100000),
            net_income=random.uniform(100, 10000)
        )

print("✅ Seeded sample company data.")