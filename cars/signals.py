from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from cars.models import Cars, CarInventory



def car_inventory_update():
    cars_count = Cars.objects.all().count()
    cars_value = Cars.objects.aggregate(
        total_value = Sum('value')
    )['total_value']

    CarInventory.objects.create(
        cars_count = cars_count,
        cars_value =cars_value
    )


@receiver(pre_save, sender=Cars)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'Bio gerada automáticamente.'


@receiver(post_save, sender=Cars)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Cars)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()