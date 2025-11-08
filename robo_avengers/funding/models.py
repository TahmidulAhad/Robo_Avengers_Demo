from django.db import models

class Funding(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_received = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class FundingSource(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField(blank=True)

    def __str__(self):
        return self.name

class FundingEntry(models.Model):
    funding = models.ForeignKey(Funding, on_delete=models.CASCADE)
    source = models.ForeignKey(FundingSource, on_delete=models.CASCADE)
    date_entry = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.funding.title} from {self.source.name}"