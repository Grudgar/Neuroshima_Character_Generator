from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Origins(models.Model):
    origin_name = models.TextField
    origin_description = models.TextField
    origin_agility_bonus = models.BinaryField(default=0)
    origin_perception_bonus = models.BinaryField(default=0)
    origin_character_bonus = models.BinaryField(default=0)
    origin_guile_bonus = models.BinaryField(default=0)
    origin_build_bonus = models.BinaryField(default=0)


class OriginPerks(models.Model):
    origin_source_id = models.ForeignKey(Origins, on_delete=models.CASCADE)
    origin_perk_name = models.TextField
    origin_perk_description = models.TextField


class CharClass(models.Model):
    char_class_name = models.TextField
    char_class_description = models.TextField


class CharClassPerk(models.Model):
    char_class_source_id = models.ForeignKey(CharClass, on_delete=models.CASCADE)
    char_class_perk_name = models.TextField
    char_class_perk_description = models.TextField


class Specializations(models.Model):
    specialization_name = models.TextField
    specialization_description = models.TextField


class Skills(models.Model):
    specialization_source_id = models.ForeignKey(Specializations, on_delete=models.CASCADE)
    skill_name = models.TextField
    skill_description = models.TextField


class Tricks(models.Model):
    trick_name = models.TextField
    trick_description = models.TextField
    trick_req_build = models.IntegerField
    trick_req_agility = models.IntegerField
    trick_req_character = models.IntegerField
    trick_req_guile = models.IntegerField
    trick_req_perception = models.IntegerField


class TricksAdditional(models.Model):
    """ Model for adding skill requierments. """
    skill_source_id = models.ForeignKey(Skills, on_delete=models.CASCADE)
    trick_source_id = models.ForeignKey(Tricks, on_delete=models.CASCADE)
    trick_req_skill_lvl = models.IntegerField


class Characters(models.Model):
    char_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    char_name = models.TextField
    char_origin = models.ForeignKey(Origins, on_delete=models.CASCADE)
    char_origin_perk = models.ForeignKey(OriginPerks, on_delete=models.CASCADE)
    char_class = models.ForeignKey(CharClass, on_delete=models.CASCADE)
    char_class_perk = models.ForeignKey(CharClassPerk, on_delete=models.CASCADE)


class CharacterSkills(models.Model):
    """ Model for adding skill levels. """
    character_source_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    skill_source_id = models.ForeignKey(Skills, on_delete=models.CASCADE)
    skill_lvl = models.IntegerField


class CharacterTricks(models.Model):
    """ Model for listing tricks. """
    character_source_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    trick_source_id = models.ForeignKey(Tricks, on_delete=models.CASCADE)

