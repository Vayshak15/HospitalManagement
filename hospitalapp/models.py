from django.db import models

# Create your models here.
class Deparments(models.Model):
    dep_name= models.CharField(max_length=100)
    dep_description=models.TextField()

    def __str__(self):
        return self.dep_name


class Doctors(models.Model):
    doct_name= models.CharField(max_length=200)
    doct_spec=models.CharField(max_length=200)
    dep_name=models.ForeignKey(Deparments,on_delete=models.CASCADE)
    doct_image=models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr' + self.doct_name + '-(' +self.doct_spec + ')'



class Booking(models.Model):
    p_name = models.CharField(max_length=200)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)


