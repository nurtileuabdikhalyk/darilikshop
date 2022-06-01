from django.db import models


class Tur(models.Model):
    name = models.CharField('Аты', max_length=255)

    class Meta:
        db_table = 'tur'
        verbose_name = "Дәрі шөп түрі"
        verbose_name_plural = "Дәрі шөп түрлері"

    def __str__(self):
        return self.name


class Scientists(models.Model):
    name = models.CharField('Аты', max_length=255)
    surname = models.CharField('Тегі', max_length=255)
    lauazym = models.CharField('Лауазымы', max_length=255)
    ainalasu_salasy = models.CharField('Айналысу саласы', max_length=255)
    slug = models.SlugField()
    dariler = models.ManyToManyField('DariShopter', verbose_name='Зерттеген дәрілер', related_name='dari', blank=True)
    image = models.ImageField('Сурет', upload_to='scientists/', null=True, blank=True)

    class Meta:
        db_table = 'scientists'
        verbose_name = "Ғалым"
        verbose_name_plural = "Ғалымдар"

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.lauazym}"


class Laboratory(models.Model):
    name = models.CharField('Аты', max_length=255)
    director = models.CharField('Директоры', max_length=255)
    mamandar_sany = models.IntegerField('Мамандар саны')
    created_at = models.DateField('Құрылған уақыты')
    slug = models.SlugField()
    image = models.ImageField('Сурет', upload_to='laboratory/', null=True, blank=True)

    class Meta:
        db_table = 'laboratory'
        verbose_name = "Зертхана"
        verbose_name_plural = "Зертханалар"

    def __str__(self):
        return f"{self.name} - {self.director} - {self.created_at}"


class Region(models.Model):
    name = models.CharField('Облыс', max_length=255)
    district = models.CharField('Аудан', max_length=255)
    tau_aty = models.CharField('Тау аты', max_length=255, null=True, blank=True)
    qoryq_aty = models.CharField('Қорық аты', max_length=255, null=True, blank=True)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE, verbose_name='Жауапты зертхана', null=True,
                                   blank=True)
    slug = models.SlugField()

    class Meta:
        db_table = 'region'
        verbose_name = "Аумақ"
        verbose_name_plural = "Аумақтар"

    def __str__(self):
        return f"{self.name} - {self.district} - {self.tau_aty} - {self.qoryq_aty}"


class DariShopter(models.Model):
    name = models.CharField('Аты', max_length=255)
    type = models.ForeignKey(Tur, on_delete=models.CASCADE, verbose_name='Түрі')
    anyqtama = models.TextField('Анықтама', null=True, blank=True)
    description = models.TextField('Сипаттамасы')
    qoldanui = models.TextField('Қолдануы')
    count = models.IntegerField('Саны')
    scientists = models.ManyToManyField(Scientists, verbose_name='Зерттеуші ғалымдар')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Таралуы')
    image = models.ImageField('Сурет', upload_to='darishopter/', blank=True, null=True)
    created_at = models.DateTimeField('Жарияланған күні', auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        db_table = 'darishopter'
        verbose_name = "Дәрі шөп"
        verbose_name_plural = "Дәрі шөптер"

    def __str__(self):
        return f"{self.name} - {self.type} - {self.count}"


class Reviews(models.Model):
    name = models.CharField("Есімі", max_length=100)
    title = models.CharField("Тақырыбы", max_length=100)
    email = models.EmailField()
    text = models.TextField("Хабарлама", max_length=5000)
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        db_table = 'reviews'
        verbose_name = "Пікір"
        verbose_name_plural = "Пікірлер"
