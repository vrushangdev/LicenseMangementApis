from django.db import models

import  time
# Create your models here.
class ContractDetails(models.Model):
    ethereum_address = models.CharField(max_length=50,primary_key=True)
    license_name = models.CharField(max_length=50)
    validity_date = models.DateField()
    hardware_id = models.CharField(max_length=200)
    license_type = models.CharField(max_length=50)
    contract_bytecode = models.TextField()
    contract_abi = models.TextField()
    tx_hash = models.TextField()


    def __str__(self):
        return "{}".format(self.ethereum_address)





class userdetail(models.Model):

    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    ethereum_address= models.ForeignKey(ContractDetails,on_delete=models.CASCADE)


    def __str__(self):
        return "%s | %s | %s | %s | %s" % (self.id, self.name,self.email_id,self.phone_number,self.ethereum_address)
