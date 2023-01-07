from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'message')

# class CourseRegister(models.Model):
#    course = models.ForeignKey(Course, on_delete=models.PROTECT)
#    title = models.CharField(max_length=200)
#    first_name = models.CharField(max_length=200)
#    last_name = models.CharField(max_length=200)
#    gender = models.CharField(max_length=200)
#    dob = models.DateField()
#    address = models.CharField(max_length=200)
#    city = models.CharField(max_length=200)
#    postcode = models.CharField(max_length=200)
#    country = models.CharField(max_length=200)
#    email = models.EmailField()
#    phone = models.PhoneNumberField()

# Registering for a course will send an email with course register details instead of storing in a database.
