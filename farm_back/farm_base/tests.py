from django.test import TestCase
from django.core.exceptions import ValidationError
from farm_base.models.farm import Farm
from farm_base.models.owner import Owner

# Create your tests here.

# Impedir a criacao de Farms sem os campos Owner, municipality, state e name

class FarmTestCase(TestCase):
    def test_nao_criar_farm_sem_state(self):
        Owner.objects.create(name='Owner teste', id=1)
        farm_sem_state = Farm(name='Farm', owner_id=Owner.objects.get(id=1), municipality='Florianopolis')

        self.assertRaises(ValidationError, farm_sem_state.full_clean)

    def test_nao_criar_farm_sem_municipality(self):
        Owner.objects.create(name='Owner teste', id=1)
        farm_sem_municipality = Farm(name='Farm', owner_id=Owner.objects.get(id=1), state='Santa Catarina')

        self.assertRaises(ValidationError, farm_sem_municipality.full_clean)

    def test_nao_criar_farm_sem_name(self):
        Owner.objects.create(name='Owner teste', id=1)
        farm_sem_name = Farm(owner_id=Owner.objects.get(id=1), municipality='Florianopolis', state='Santa Catarina')

        self.assertRaises(ValidationError, farm_sem_name.full_clean)

    def test_nao_criar_farm_sem_owner(self):
        farm_sem_owner = Farm(name='Farm', municipality='Florianopolis', state='Santa Catarina')

        self.assertRaises(ValidationError, farm_sem_owner.full_clean)
