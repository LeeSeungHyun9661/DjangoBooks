from django.db import models

class Book(models.Model):
    SEQ_NO = models.IntegerField(primary_key=True, null=False) # 일련번호
    ISBN_THIRTEEN_NO = models.CharField(max_length=13, blank=True) # ISBN13
    VLM_NM = models.CharField(max_length=20, blank=True, null=True) # 권명
    TITLE_NM = models.CharField(max_length=1200, blank=True, null=True) # 제목명
    AUTHR_NM = models.CharField(max_length=1000, blank=True, null=True) # 저작자명
    PUBLISHER_NM = models.CharField(max_length=1000, blank=True, null=True) # 출판사명
    PBLICTE_DE = models.CharField(max_length=10, blank=True, null=True) # 발행일자
    ADTION_SMBL_NM = models.CharField(max_length=5, blank=True, null=True) # 부가기호명
    PRC_VALUE = models.CharField(max_length=20, blank=True, null=True) # 가격값
    IMAGE_URL = models.CharField(max_length=1000, blank=True, null=True) # 이미지URL
    BOOK_INTRCN_CN = models.TextField(blank=True, null=True) # 서적소개내용
    KDC_NM = models.CharField(max_length=20, blank=True, null=True) # KDC명
    TITLE_SBST_NM = models.CharField(max_length=1200, blank=True, null=True) # 제목대체명
    AUTHR_SBST_NM = models.CharField(max_length=1000, blank=True, null=True) # 저작자대체명	
    TWO_PBLICTE_DE = models.CharField(max_length=10, blank=True, null=True) # 2발행일자
    INTNT_BOOKST_BOOK_EXST_AT = models.CharField(max_length=1, blank=True, null=True)
    PORTAL_SITE_BOOK_EXST_AT = models.CharField(max_length=1, blank=True, null=True)
    ISBN_NO = models.CharField(max_length=200, blank=True, null=True) # ISBN번호

    class Meta:
        db_table = u'books'
        ordering = ['-SEQ_NO']