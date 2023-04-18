from django import forms
c=[['python','python'],('java','java'),('SQL','sql'),['webtechnology','webtechnology'],['DJANGO','DJANGO']]
g=[('MALE','male'),['Female','Female']]

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=100,widget=forms.Textarea)
    phone=forms.IntegerField()
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
