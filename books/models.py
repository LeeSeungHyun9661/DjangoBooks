from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=20, primary_key=True, null=False) # 일련번호
    olid = models.CharField(max_length=20, blank=True) # ISBN13
    title = models.CharField(max_length=100, blank=True, null=True) # 권명
    subtitle = models.TextField(blank=True, null=True) # 제목명
    authors = models.CharField(max_length=100, blank=True, null=True) # 저작자명
    authors_id = models.CharField(max_length=100, blank=True, null=True) # 출판사명
    publishers = models.CharField(max_length=100, blank=True, null=True) # 발행일자
    publish_places = models.CharField(max_length=100, blank=True, null=True) # 부가기호명
    publish_date = models.CharField(max_length=100, blank=True, null=True) # 부가기호명
    languages = models.CharField(max_length=50, blank=True, null=True) # 가격값
    number_of_pages = models.IntegerField( blank=True, null=True) # 이미지URL
    physical_format = models.CharField(max_length=100, blank=True, null=True) # 서적소개내용
    physical_dimensions = models.CharField(max_length=100, blank=True, null=True) # KDC명
    subjects = models.TextField(blank=True, null=True) # 제목대체명
    description = models.TextField(blank=True, null=True) # 저작자대체명	
    preview_url = models.CharField(max_length=200, blank=True, null=True) # 2발행일자
    info_url = models.CharField(max_length=200, blank=True, null=True) # 2발행일자
    img_url_s = models.CharField(max_length=200, blank=True, null=True)
    img_url_m = models.CharField(max_length=200, blank=True, null=True)
    img_url_l = models.CharField(max_length=200, blank=True, null=True) # ISBN번호

    class Meta:
        db_table = u'books'

class Bestseller(models.Model):
    isbn = models.CharField(max_length=20, primary_key=True, null=False) # 일련번호
    comments = models.TextField(blank=True, null=True) # 저작자대체명
    
    class Meta:
        db_table = u'books_bestseller'

class NewRelease(models.Model):
    isbn = models.CharField(max_length=20, primary_key=True, null=False) # 일련번호
    comments = models.TextField(blank=True, null=True) # 저작자대체명
    
    class Meta:
        db_table = u'books_newrelease'

class Author(models.Model):
    authors_id = models.CharField(max_length=100, primary_key=True, null=False) # 출판사명
    name = models.CharField(max_length=100, blank=True, null=True) # 발행일자
    personal_name = models.CharField(max_length=100, blank=True, null=True) # 부가기호명
    location = models.CharField(max_length=100, blank=True, null=True) # 부가기호명
    bio = models.TextField(max_length=50, blank=True, null=True) # 가격값
    birth_date = models.CharField( max_length=100, null=True) # 이미지URL
    death_date = models.CharField(max_length=100, blank=True, null=True) # 서적소개내용
    img = models.CharField(max_length=200, blank=True, null=True) # KDC명

    class Meta:
        db_table = u'authors'