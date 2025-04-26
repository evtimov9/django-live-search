from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    founded_year = models.IntegerField()

    def __str__(self):
        return self.name


class FinancialData(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='financials')
    year = models.IntegerField()
    revenue = models.DecimalField(max_digits=15, decimal_places=2)
    net_income = models.DecimalField(max_digits=15, decimal_places=2)


class CompanyDetails(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='details')
    company_type = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    ceo_name = models.CharField(max_length=255)
    headquarters = models.CharField(max_length=255)
