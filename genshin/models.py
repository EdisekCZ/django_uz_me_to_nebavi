from django.db import models


def poster_path(instance, filename):
    return "genshin/media/"+ str(instance.name) + "/poster/" + filename


class Region(models.Model):
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Region',
                            help_text='Enter Region')

    def __str__(self):
        return self.name


class Artifacts(models.Model):
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Artifacts',
                            help_text='Enter Artifact Name')

    def __str__(self):
        return self.name


class Character(models.Model):
    GEO = 'Geo'
    ELECTRO = 'Electro'
    PYRO = 'Pyro'
    CRYO = 'Cryo'
    ANEMO = 'Anemo'
    HYDRO = 'Hydro'
    DENDRO = 'Dendro'

    ELEMENTS = [
        (GEO, 'Geo'),
        (ELECTRO, 'Electro'),
        (PYRO, 'Pyro'),
        (CRYO, 'Cryo'),
        (ANEMO, 'Anemo'),
        (HYDRO, 'Hydro'),
        (DENDRO, 'Dendro'),
    ]

    SWORD = 'Sword'
    CLAYMORE = 'Claymore'
    CATALYST = 'Catalyst'
    BOW = 'Bow'
    SPEAR = 'Spear'

    WEAPON_TYPE = [
        (SWORD, 'Sword'),
        (CLAYMORE, 'Claymore'),
        (CATALYST, 'Catalyst'),
        (BOW, 'Bow'),
        (SPEAR, 'Spear'),
    ]

    DPS = 'Dps'
    SUB_DPS = 'Sub Dps'
    UTILITY = 'Utility'

    ROLE = [
        (DPS, 'Dps'),
        (SUB_DPS, 'Sub Dps'),
        (UTILITY, 'Utility'),
    ]

    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Character Name',
                            help_text='Enter Character\'s Name')
    img = models.ImageField(upload_to=poster_path,
                            blank=True,
                            null=True,
                            verbose_name='Character Image')
    elements = models.CharField(choices=ELEMENTS,
                                verbose_name='Element',
                                max_length=50)
    weapon_type = models.CharField(choices=WEAPON_TYPE,
                                   verbose_name='Weapon Type',
                                   max_length=50)
    role = models.CharField(choices=ROLE,
                            verbose_name='Role',
                            max_length=50)
    recomended_artifacts = models.ManyToManyField(Artifacts, verbose_name='Artifacts')
    region = models.ManyToManyField(Region, verbose_name='Region')

    def __str__(self):
        return self.name

